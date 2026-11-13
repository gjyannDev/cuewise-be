"""Fetch a web page whose address a user chose, without letting that user reach anything inside our network (SSRF).

Server-side request forgery: the server makes the request, so a URL like http://169.254.169.254/ (the cloud metadata
service) or http://localhost:5432 reaches places only the server can. The defences, each one closing a known bypass:

- only http and https, only the allowed ports, no credentials in the URL
- resolve the name once and refuse it if *any* address is not public; IPv4-mapped, NAT64 and 6to4 IPv6 forms are
  unwrapped first, so they can't smuggle a private IPv4 address past the check
- connect to the exact address that was checked (DNS rebinding: a second lookup could answer differently); the real
  name still goes in the Host header and the TLS server name, so virtual hosting and certificate checks keep working
- follow redirects by hand, re-running every check on every hop (a public page can redirect inside)
- ignore proxy environment variables (a proxy would make the real connection somewhere unchecked)
- one time budget for the whole fetch, a byte cap read as a stream, HTML only

Errors carry a short machine `reason` for logs; callers turn them into one generic message so the response can't be
used to map which internal hosts or ports exist.
"""

import codecs
import ipaddress
import re
import socket
import time
from collections.abc import Callable
from dataclasses import dataclass

import httpx

Resolver = Callable[[str, int], list[str]]

_DEFAULT_PORTS = {"http": 80, "https": 443}
_NAT64 = ipaddress.ip_network("64:ff9b::/96")
_META_CHARSET = re.compile(rb"""<meta[^>]+charset\s*=\s*["']?([A-Za-z0-9_.:\-]+)""", re.IGNORECASE)
_HTML_TYPES = {"text/html"}


class FetchError(Exception):
    def __init__(self, reason: str):
        super().__init__(reason)
        self.reason = reason


class UrlUnreachableError(FetchError):
    """Refused before connecting, or the network side failed (DNS, timeout, connection, status, redirects)."""


class ResponseUnreadableError(FetchError):
    """The server answered, but not with an HTML page we are willing to read."""


@dataclass(frozen=True)
class FetchedPage:
    host: str  # the final host, after redirects
    html: str
    size: int  # bytes read


def system_resolver(host: str, port: int) -> list[str]:
    return [str(info[4][0]) for info in socket.getaddrinfo(host, port, type=socket.SOCK_STREAM)]


def is_public_address(value: str) -> bool:
    """True only for a globally routable unicast address."""
    try:
        address = ipaddress.ip_address(value.split("%", 1)[0])  # drop an IPv6 zone id
    except ValueError:
        return False
    if isinstance(address, ipaddress.IPv6Address):
        if address.ipv4_mapped is not None:
            address = address.ipv4_mapped
        elif address in _NAT64:
            address = ipaddress.IPv4Address(int(address) & 0xFFFFFFFF)
        elif address.sixtofour is not None:
            address = address.sixtofour
        elif address.teredo is not None:
            return False
    return address.is_global and not address.is_multicast


class SafeFetcher:
    def __init__(
        self,
        *,
        allowed_ports: frozenset[int],
        max_bytes: int,
        max_redirects: int,
        total_seconds: float,
        connect_seconds: float,
        resolver: Resolver = system_resolver,
        transport: httpx.BaseTransport | None = None,
        clock: Callable[[], float] = time.monotonic,
    ):
        self._allowed_ports = allowed_ports
        self._max_bytes = max_bytes
        self._max_redirects = max_redirects
        self._total_seconds = total_seconds
        self._connect_seconds = connect_seconds
        self._resolver = resolver
        self._transport = transport
        self._clock = clock

    def fetch(self, url: str) -> FetchedPage:
        deadline = self._clock() + self._total_seconds
        try:
            current = httpx.URL(url)
        except (httpx.InvalidURL, TypeError) as exc:
            raise UrlUnreachableError("invalid_url") from exc
        # trust_env=False: no proxy from the environment, no .netrc credentials.
        with httpx.Client(transport=self._transport, follow_redirects=False, trust_env=False) as client:
            for _ in range(self._max_redirects + 1):
                host, port, address = self._check(current)
                location = self._get(client, current, host, port, address, deadline)
                if isinstance(location, FetchedPage):
                    return location
                try:
                    current = current.join(location)
                except httpx.InvalidURL as exc:
                    raise UrlUnreachableError("invalid_redirect") from exc
        raise UrlUnreachableError("too_many_redirects")

    def _check(self, url: httpx.URL) -> tuple[str, int, str]:
        """Scheme, credentials, port and every resolved address. Returns the address to connect to."""
        if url.scheme not in _DEFAULT_PORTS:
            raise UrlUnreachableError("scheme")
        if url.userinfo:
            raise UrlUnreachableError("credentials")
        host = url.raw_host.decode("ascii")
        if not host:
            raise UrlUnreachableError("no_host")
        port = url.port or _DEFAULT_PORTS[url.scheme]
        if port not in self._allowed_ports:
            raise UrlUnreachableError("port")
        try:
            addresses = self._resolver(host, port)
        except (OSError, UnicodeError) as exc:
            raise UrlUnreachableError("dns") from exc
        if not addresses:
            raise UrlUnreachableError("dns")
        if not all(is_public_address(a) for a in addresses):
            raise UrlUnreachableError("non_public_address")
        return host, port, addresses[0]

    def _get(
        self, client: httpx.Client, url: httpx.URL, host: str, port: int, address: str, deadline: float
    ) -> FetchedPage | str:
        """One hop: a page, or the redirect's Location to check next."""
        remaining = deadline - self._clock()
        if remaining <= 0:
            raise UrlUnreachableError("timeout")
        pinned = url.copy_with(host=address.split("%", 1)[0], fragment=None)
        netloc = host if port == _DEFAULT_PORTS[url.scheme] else f"{host}:{port}"
        headers = {"Host": netloc, "Accept": "text/html", "Accept-Encoding": "identity"}
        extensions = {"sni_hostname": host} if url.scheme == "https" else {}
        timeout = httpx.Timeout(remaining, connect=min(self._connect_seconds, remaining))
        try:
            with client.stream("GET", pinned, headers=headers, extensions=extensions, timeout=timeout) as response:
                if response.is_redirect:
                    if "location" not in response.headers:
                        raise UrlUnreachableError("redirect_without_location")
                    return response.headers["location"]
                if not response.is_success:
                    raise UrlUnreachableError(f"status_{response.status_code}")
                return self._read(response, host, deadline)
        except httpx.TimeoutException as exc:
            raise UrlUnreachableError("timeout") from exc
        except httpx.HTTPError as exc:
            raise UrlUnreachableError(type(exc).__name__) from exc

    def _read(self, response: httpx.Response, host: str, deadline: float) -> FetchedPage:
        media_type = response.headers.get("content-type", "").split(";", 1)[0].strip().lower()
        if media_type not in _HTML_TYPES:
            raise ResponseUnreadableError("content_type")
        declared = response.headers.get("content-length", "")
        if declared.isdigit() and int(declared) > self._max_bytes:
            raise ResponseUnreadableError("too_large")
        body = bytearray()
        for chunk in response.iter_bytes():
            body += chunk
            if len(body) > self._max_bytes:
                raise ResponseUnreadableError("too_large")
            if self._clock() > deadline:
                raise UrlUnreachableError("timeout")
        return FetchedPage(host=host, html=_decode(bytes(body), response.charset_encoding), size=len(body))


def _decode(body: bytes, declared: str | None) -> str:
    """Header charset, else a <meta> charset, else UTF-8; never raises (bad bytes become U+FFFD)."""
    match = _META_CHARSET.search(body[:4096])
    for candidate in (declared, match and match.group(1).decode("ascii"), "utf-8"):
        if not candidate:
            continue
        try:
            codecs.lookup(candidate)
        except LookupError:
            continue
        return body.decode(candidate, errors="replace")
    return body.decode("utf-8", errors="replace")
