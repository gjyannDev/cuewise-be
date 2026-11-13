"""SSRF-safe fetch (Slice 8b). A fake resolver and a recording MockTransport stand in for DNS and the network, so each
test can assert not only the error but that a refused address was never contacted."""

import httpx
import pytest

from app.core.safe_fetch import (
    FetchedPage,
    ResponseUnreadableError,
    SafeFetcher,
    UrlUnreachableError,
    is_public_address,
)

PUBLIC_IP = "93.184.216.34"
HTML = {"content-type": "text/html; charset=utf-8"}


class FakeResolver:
    """Answers from a host -> addresses table; `then` gives a different answer on later calls (DNS rebinding)."""

    def __init__(self, table: dict[str, list[str]], then: dict[str, list[str]] | None = None):
        self.table, self.then, self.calls = table, then or {}, []

    def __call__(self, host: str, port: int) -> list[str]:
        self.calls.append(host)
        if host in self.then and self.calls.count(host) > 1:
            return self.then[host]
        if host not in self.table:
            raise OSError("name not resolved")
        return self.table[host]


class Recorder:
    """A MockTransport handler that records every request it receives and replies from `routes` (by Host header)."""

    def __init__(self, routes=None, default=None):
        self.routes, self.default, self.requests = routes or {}, default, []

    def __call__(self, request: httpx.Request) -> httpx.Response:
        self.requests.append(request)
        reply = self.routes.get(request.headers["host"], self.default)
        if callable(reply):
            return reply(request)
        return reply or httpx.Response(200, headers=HTML, content=b"<html><body>ok</body></html>")

    @property
    def contacted(self) -> list[str]:
        return [r.url.host for r in self.requests]


def fetcher(resolver, recorder, **overrides) -> SafeFetcher:
    limits = {
        "allowed_ports": frozenset({80, 443}),
        "max_bytes": 1000,
        "max_redirects": 3,
        "total_seconds": 5.0,
        "connect_seconds": 2.0,
    } | overrides
    return SafeFetcher(resolver=resolver, transport=httpx.MockTransport(recorder), **limits)


def public(*hosts: str) -> FakeResolver:
    return FakeResolver({h: [PUBLIC_IP] for h in hosts})


# --- slice 1: the address rule ------------------------------------------------------------------------------------


@pytest.mark.parametrize(
    "address",
    [
        "127.0.0.1",
        "10.0.0.5",
        "172.16.0.1",
        "192.168.1.1",
        "169.254.169.254",  # cloud metadata
        "100.64.0.1",  # carrier-grade NAT
        "0.0.0.0",
        "224.0.0.1",  # multicast
        "255.255.255.255",
        "::1",
        "::",
        "fc00::1",  # unique local
        "fe80::1",  # link local
        "fe80::1%eth0",  # with a zone id
        "::ffff:127.0.0.1",  # IPv4-mapped
        "::ffff:169.254.169.254",
        "64:ff9b::a00:1",  # NAT64 of 10.0.0.1: Python calls it global
        "2002:7f00:1::",  # 6to4 of 127.0.0.1
        "ff02::1",
        "not-an-ip",
    ],
)
def test_non_public_addresses_are_refused(address):  # EC2
    assert not is_public_address(address)


@pytest.mark.parametrize("address", [PUBLIC_IP, "8.8.8.8", "2606:4700::1", "64:ff9b::808:808"])
def test_public_addresses_pass(address):
    assert is_public_address(address)


# --- slice 2: URL and address checks before any connection -------------------------------------------------------


@pytest.mark.parametrize(
    "url",
    [
        "file:///etc/passwd",
        "ftp://example.com/x",
        "gopher://example.com/",
        "https://user:pass@example.com/",  # EC9
        "https://example.com:8080/",  # EC8
        "http://example.com:22/",
        "not a url",
        "https:///nohost",
    ],
)
def test_bad_urls_are_refused_without_contact(url):  # EC1, EC8, EC9
    recorder = Recorder()
    with pytest.raises(UrlUnreachableError):
        fetcher(public("example.com"), recorder).fetch(url)
    assert recorder.contacted == []


@pytest.mark.parametrize(
    ("host", "resolved"),
    [
        ("127.0.0.1", ["127.0.0.1"]),
        ("10.0.0.5", ["10.0.0.5"]),
        ("169.254.169.254", ["169.254.169.254"]),
        ("[::1]", ["::1"]),
        ("[::ffff:127.0.0.1]", ["::ffff:127.0.0.1"]),
        ("2130706433", ["127.0.0.1"]),  # numeric-host form of 127.0.0.1
        ("intranet.example.com", ["10.1.2.3"]),  # EC3: a public name pointing inside
    ],
)
def test_private_targets_are_refused_without_contact(host, resolved):  # EC2, EC3, AC2
    resolver = FakeResolver({host.strip("[]"): resolved})
    recorder = Recorder()
    with pytest.raises(UrlUnreachableError):
        fetcher(resolver, recorder).fetch(f"http://{host}/job")
    assert recorder.contacted == []


def test_one_private_address_among_several_refuses_the_host():  # EC4
    resolver = FakeResolver({"mixed.example.com": [PUBLIC_IP, "127.0.0.1"]})
    recorder = Recorder()
    with pytest.raises(UrlUnreachableError):
        fetcher(resolver, recorder).fetch("https://mixed.example.com/")
    assert recorder.contacted == []


def test_a_name_that_does_not_resolve_is_unreachable():  # EC24
    recorder = Recorder()
    with pytest.raises(UrlUnreachableError):
        fetcher(FakeResolver({}), recorder).fetch("https://nowhere.example.com/")
    assert recorder.contacted == []


# --- slice 3: the connection goes to the validated address -------------------------------------------------------


def test_the_connection_uses_the_validated_address_and_keeps_the_real_name():  # AC4
    recorder = Recorder()
    page = fetcher(public("jobs.example.com"), recorder).fetch("https://jobs.example.com/posting/1?ref=x")

    assert isinstance(page, FetchedPage)
    (request,) = recorder.requests
    assert request.url.host == PUBLIC_IP
    assert request.url.path == "/posting/1"
    assert request.headers["host"] == "jobs.example.com"
    # TLS checks the certificate against this name, not against the IP.
    assert request.extensions["sni_hostname"] == "jobs.example.com"


def test_dns_rebinding_cannot_swap_in_a_private_address():  # EC5
    resolver = FakeResolver({"rebind.example.com": [PUBLIC_IP]}, then={"rebind.example.com": ["127.0.0.1"]})
    recorder = Recorder()

    fetcher(resolver, recorder).fetch("http://rebind.example.com/")

    assert resolver.calls == ["rebind.example.com"]
    assert recorder.contacted == [PUBLIC_IP]


def test_proxy_environment_variables_are_ignored(monkeypatch):
    # A proxy would make the real connection go somewhere the address check never saw.
    monkeypatch.setenv("HTTPS_PROXY", "http://10.0.0.9:3128")
    monkeypatch.setenv("HTTP_PROXY", "http://10.0.0.9:3128")
    recorder = Recorder()
    fetcher(public("jobs.example.com"), recorder).fetch("https://jobs.example.com/")
    assert recorder.contacted == [PUBLIC_IP]


# --- slice 4: redirects -------------------------------------------------------------------------------------------


def redirect(to: str, status: int = 302) -> httpx.Response:
    return httpx.Response(status, headers={"location": to})


@pytest.mark.parametrize("status", [301, 302, 303, 307, 308])
def test_a_redirect_to_a_public_page_is_followed_with_the_same_checks(status):
    resolver = FakeResolver({"a.example.com": [PUBLIC_IP], "b.example.com": ["93.184.216.35"]})
    recorder = Recorder(routes={"a.example.com": redirect("https://b.example.com/job", status)})

    page = fetcher(resolver, recorder).fetch("https://a.example.com/")

    assert recorder.contacted == [PUBLIC_IP, "93.184.216.35"]
    assert recorder.requests[1].headers["host"] == "b.example.com"
    assert page.host == "b.example.com"


def test_a_relative_redirect_stays_on_the_same_host():
    recorder = Recorder(
        routes={"a.example.com": lambda r: redirect("/job") if r.url.path == "/" else httpx.Response(200, headers=HTML)}
    )
    fetcher(public("a.example.com"), recorder).fetch("https://a.example.com/")
    assert [r.url.path for r in recorder.requests] == ["/", "/job"]


@pytest.mark.parametrize(
    "location",
    [
        "http://127.0.0.1/admin",
        "http://169.254.169.254/latest/meta-data/",
        "http://[::1]/",
        "http://inside.example.com/",  # resolves private
        "file:///etc/passwd",
        "https://b.example.com:6379/",  # EC8 on a redirect
        "https://user:pw@b.example.com/",
    ],
)
def test_a_redirect_into_a_refused_target_is_never_followed(location):  # EC6, EC8, AC3
    resolver = FakeResolver(
        {"a.example.com": [PUBLIC_IP], "inside.example.com": ["10.0.0.7"], "b.example.com": ["93.184.216.35"]}
    )
    recorder = Recorder(routes={"a.example.com": redirect(location)})

    with pytest.raises(UrlUnreachableError):
        fetcher(resolver, recorder).fetch("https://a.example.com/")
    assert recorder.contacted == [PUBLIC_IP]


def test_too_many_redirects_are_refused():  # EC7
    recorder = Recorder(routes={"a.example.com": lambda r: redirect(f"/hop{len(recorder.requests)}")})
    with pytest.raises(UrlUnreachableError):
        fetcher(public("a.example.com"), recorder, max_redirects=3).fetch("https://a.example.com/")
    assert len(recorder.requests) == 4  # the first request and three redirects, never a fifth


def test_a_redirect_loop_ends_at_the_limit():  # EC7
    recorder = Recorder(routes={"a.example.com": redirect("https://a.example.com/")})
    with pytest.raises(UrlUnreachableError):
        fetcher(public("a.example.com"), recorder).fetch("https://a.example.com/")
    assert len(recorder.requests) == 4


def test_a_redirect_without_a_location_is_unreachable():
    recorder = Recorder(default=httpx.Response(302))
    with pytest.raises(UrlUnreachableError):
        fetcher(public("a.example.com"), recorder).fetch("https://a.example.com/")


# --- slice 5: network failures and status codes ------------------------------------------------------------------


@pytest.mark.parametrize("status", [400, 401, 403, 404, 429, 500, 503])
def test_a_non_success_status_is_unreachable(status):  # EC10
    recorder = Recorder(default=httpx.Response(status, headers=HTML, content=b"<html>blocked</html>"))
    with pytest.raises(UrlUnreachableError):
        fetcher(public("a.example.com"), recorder).fetch("https://a.example.com/")


@pytest.mark.parametrize("error", [httpx.ConnectTimeout, httpx.ReadTimeout, httpx.ConnectError, httpx.RemoteProtocolError])
def test_transport_failures_are_unreachable(error):  # EC11
    def fail(request):
        raise error("boom", request=request)

    with pytest.raises(UrlUnreachableError):
        fetcher(public("a.example.com"), Recorder(default=fail)).fetch("https://a.example.com/")


def test_the_whole_fetch_has_one_time_budget():  # EC11: a slow trickle can't outlast the total cap
    now = [0.0]

    def slow_body():
        while True:
            now[0] += 1.0
            yield b"x" * 10

    recorder = Recorder(default=httpx.Response(200, headers=HTML, content=slow_body()))
    slow = SafeFetcher(
        resolver=public("a.example.com"),
        transport=httpx.MockTransport(recorder),
        allowed_ports=frozenset({443}),
        max_bytes=10_000,
        max_redirects=3,
        total_seconds=5.0,
        connect_seconds=2.0,
        clock=lambda: now[0],
    )
    with pytest.raises(UrlUnreachableError):
        slow.fetch("https://a.example.com/")
    assert now[0] <= 7.0


# --- slice 6: what the body may be --------------------------------------------------------------------------------


@pytest.mark.parametrize("content_type", ["application/pdf", "image/png", "application/json", "text/plain", ""])
def test_a_non_html_response_is_unreadable(content_type):  # EC12
    headers = {"content-type": content_type} if content_type else {}
    recorder = Recorder(default=httpx.Response(200, headers=headers, content=b"%PDF-1.7"))
    with pytest.raises(ResponseUnreadableError):
        fetcher(public("a.example.com"), recorder).fetch("https://a.example.com/")


def test_a_body_over_the_cap_stops_the_read_early():  # EC13, AC7
    pulled = [0]

    def endless():
        while True:
            pulled[0] += 1
            yield b"<p>" + b"x" * 97

    recorder = Recorder(default=httpx.Response(200, headers=HTML, content=endless()))
    with pytest.raises(ResponseUnreadableError):
        fetcher(public("a.example.com"), recorder, max_bytes=1000).fetch("https://a.example.com/")
    assert pulled[0] <= 11  # 1000 bytes in 100-byte chunks: the eleventh crosses the cap, nothing more is read


def test_a_declared_length_over_the_cap_is_refused_before_reading():  # EC13
    pulled = [0]

    def body():
        pulled[0] += 1
        yield b"x"

    recorder = Recorder(
        default=httpx.Response(200, headers={**HTML, "content-length": "5000000"}, content=body())
    )
    with pytest.raises(ResponseUnreadableError):
        fetcher(public("a.example.com"), recorder).fetch("https://a.example.com/")
    assert pulled[0] == 0


def test_identity_encoding_is_requested():
    # A compressed body could expand far past the cap inside one chunk; asking for none keeps the cap meaningful.
    recorder = Recorder()
    fetcher(public("a.example.com"), recorder).fetch("https://a.example.com/")
    assert recorder.requests[0].headers["accept-encoding"] == "identity"


# --- slice 7: decoding and the happy path -------------------------------------------------------------------------


def test_the_page_is_returned_decoded_with_its_final_host():
    body = b"<html><body><h1>Backend engineer</h1></body></html>"
    recorder = Recorder(default=httpx.Response(200, headers=HTML, content=body))

    page = fetcher(public("jobs.example.com"), recorder).fetch("https://jobs.example.com/")

    assert page == FetchedPage(host="jobs.example.com", html=body.decode(), size=len(body))


def test_an_uppercase_content_type_is_html():
    recorder = Recorder(default=httpx.Response(200, headers={"content-type": "TEXT/HTML"}, content=b"<p>hi</p>"))
    assert fetcher(public("a.example.com"), recorder).fetch("https://a.example.com/").html == "<p>hi</p>"


def test_a_charset_from_the_header_is_used():  # EC20
    body = "<p>Développeur à Zürich</p>".encode("latin-1")
    recorder = Recorder(default=httpx.Response(200, headers={"content-type": "text/html; charset=ISO-8859-1"}, content=body))
    assert "Développeur à Zürich" in fetcher(public("a.example.com"), recorder).fetch("https://a.example.com/").html


def test_a_charset_from_a_meta_tag_is_used():  # EC20
    body = '<html><head><meta charset="windows-1252"></head><body>Café “senior”</body></html>'.encode("cp1252")
    recorder = Recorder(default=httpx.Response(200, headers={"content-type": "text/html"}, content=body))
    assert "Café “senior”" in fetcher(public("a.example.com"), recorder).fetch("https://a.example.com/").html


def test_an_unknown_charset_falls_back_without_crashing():  # EC20
    body = b"<p>caf\xe9</p>"
    recorder = Recorder(default=httpx.Response(200, headers={"content-type": "text/html; charset=bogus-9"}, content=body))
    html = fetcher(public("a.example.com"), recorder).fetch("https://a.example.com/").html
    assert html.startswith("<p>caf")


def test_the_default_ports_are_allowed_when_written_out():
    recorder = Recorder()
    fetcher(public("a.example.com"), recorder).fetch("https://a.example.com:443/")
    fetcher(public("a.example.com"), recorder).fetch("http://a.example.com:80/")
    assert len(recorder.requests) == 2
