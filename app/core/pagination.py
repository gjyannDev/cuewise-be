"""Offset pagination shared by every list endpoint, so clients see one query contract and one response envelope.

Composition, not a base repository: a route takes `PageDep`, the repository applies `limit`/`offset` to its own query,
and the response is a feature's subclass of `Page[...]` (the subclass keeps a readable name in the OpenAPI schema).
"""

from typing import Annotated, NamedTuple

from fastapi import Depends, Query
from pydantic import BaseModel

DEFAULT_PAGE_SIZE = 20
MAX_PAGE_SIZE = 100


class PageParams(NamedTuple):
    limit: int
    offset: int


def page_params(
    limit: Annotated[int, Query(ge=1, le=MAX_PAGE_SIZE)] = DEFAULT_PAGE_SIZE,
    offset: Annotated[int, Query(ge=0)] = 0,
) -> PageParams:
    return PageParams(limit, offset)


PageDep = Annotated[PageParams, Depends(page_params)]


class Page[T](BaseModel):
    items: list[T]
    # Every row matching the request's filters, whatever limit and offset are.
    total: int
    limit: int
    offset: int
