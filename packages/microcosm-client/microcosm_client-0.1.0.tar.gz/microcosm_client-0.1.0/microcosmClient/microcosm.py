import logging
from typing import Any, Dict, Optional, Union

import httpx
from atproto import NSID, AtUri

__all__ = ["AsyncMicrocosmClient", "NSID", "AtUri",
           "MicrocosmError", "MicrocosmHTTPError"]


logger = logging.getLogger(__name__)


BASE_URL = "https://constellation.microcosm.blue/"


def _coerce_aturi(value: Union[AtUri, str]) -> AtUri:
    """Coerce a value to AtUri. If it's already an AtUri return it, else parse from string."""
    if isinstance(value, AtUri):
        return value
    if isinstance(value, str):
        return AtUri.from_str(value)
    raise TypeError("target must be an AtUri or str")


def _coerce_nsid(value: Union[NSID, str]) -> NSID:
    """Coerce a value to NSID. If it's already an NSID return it, else parse from string."""
    if isinstance(value, NSID):
        return value
    if isinstance(value, str):
        return NSID.from_str(value)
    raise TypeError("collection must be an NSID or str")


class AsyncMicrocosmClient:
    """Asynchronous Microcosm client.

    Methods accept either typed objects (`AtUri`, `NSID`) or their string
    representations. Strings are coerced to the appropriate type before use.
    """

    def __init__(self, base_url: str = BASE_URL, timeout: float = 10.0):
        self.base_url = base_url
        self.client = httpx.AsyncClient(base_url=base_url, timeout=timeout)

    def aclose(self): return self.close()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.close()

    async def links(self, target: Union[AtUri, str], collection: Union[NSID, str], path: str) -> Dict[str, Any]:
        """List records linking to a target."""
        target = _coerce_aturi(target)
        collection = _coerce_nsid(collection)
        r = await self.client.get(
            "/links",
            params={"target": str(target), "collection": str(
                collection), "path": path},
        )
        try:
            r.raise_for_status()
        except httpx.HTTPStatusError as exc:
            logger.debug("links request failed: %s %s", r.status_code, r.text)
            raise MicrocosmHTTPError(r.status_code, r.text) from exc
        return r.json()

    async def links_distinct_dids(self, target: Union[AtUri, str], collection: Union[NSID, str], path: str) -> Dict[str, Any]:
        """List distinct DIDs with links to a target."""
        target = _coerce_aturi(target)
        collection = _coerce_nsid(collection)
        r = await self.client.get(
            "/links/distinct-dids",
            params={"target": str(target), "collection": str(
                collection), "path": path},
        )
        try:
            r.raise_for_status()
        except httpx.HTTPStatusError as exc:
            logger.debug("links_distinct_dids failed: %s %s",
                         r.status_code, r.text)
            raise MicrocosmHTTPError(r.status_code, r.text) from exc
        return r.json()

    async def links_count(self, target: Union[AtUri, str], collection: Union[NSID, str], path: str, cursor: Optional[str] = None) -> Dict[str, Any]:
        """Get total number of links pointing at a target."""
        target = _coerce_aturi(target)
        collection = _coerce_nsid(collection)
        params = {"target": str(target), "collection": str(
            collection), "path": path}
        if cursor:
            params["cursor"] = cursor
        r = await self.client.get("/links/count", params=params)
        try:
            r.raise_for_status()
        except httpx.HTTPStatusError as exc:
            logger.debug("links_count failed: %s %s", r.status_code, r.text)
            raise MicrocosmHTTPError(r.status_code, r.text) from exc
        return r.json()

    async def links_count_distinct_dids(self, target: Union[AtUri, str], collection: Union[NSID, str], path: str, cursor: Optional[str] = None) -> Dict[str, Any]:
        """Get total number of distinct DIDs linking to a target."""
        target = _coerce_aturi(target)
        collection = _coerce_nsid(collection)
        params = {"target": str(target), "collection": str(
            collection), "path": path}
        if cursor:
            params["cursor"] = cursor
        r = await self.client.get("/links/count/distinct-dids", params=params)
        try:
            r.raise_for_status()
        except httpx.HTTPStatusError as exc:
            logger.debug("links_count_distinct_dids failed: %s %s",
                         r.status_code, r.text)
            raise MicrocosmHTTPError(r.status_code, r.text) from exc
        return r.json()

    async def links_all(self, target: Union[AtUri, str]) -> Dict[str, Any]:
        """Show all sources with links to a target, including counts and distinct linking DIDs."""
        target = _coerce_aturi(target)
        r = await self.client.get("/links/all", params={"target": str(target)})
        try:
            r.raise_for_status()
        except httpx.HTTPStatusError as exc:
            logger.debug("links_all failed: %s %s", r.status_code, r.text)
            raise MicrocosmHTTPError(r.status_code, r.text) from exc
        return r.json()

    async def links_all_count(self, target: Union[AtUri, str]) -> Dict[str, Any]:
        """[Deprecated] Total counts of all links pointing at a target, grouped by collection and path."""
        target = _coerce_aturi(target)
        r = await self.client.get("/links/all/count", params={"target": str(target)})
        try:
            r.raise_for_status()
        except httpx.HTTPStatusError as exc:
            logger.debug("links_all_count failed: %s %s",
                         r.status_code, r.text)
            raise MicrocosmHTTPError(r.status_code, r.text) from exc
        return r.json()

    async def close(self):
        await self.client.aclose()


class MicrocosmError(Exception):
    """Base exception for Microcosm wrapper errors."""


class MicrocosmHTTPError(MicrocosmError):
    """Raised when Microcosm responds with an error status code.

    Attributes:
        status_code: HTTP status code returned by the server
        response_text: text content of the response
    """

    def __init__(self, status_code: int, response_text: str):
        super().__init__(f"Microcosm HTTP {status_code}: {response_text}")
        self.status_code = status_code
        self.response_text = response_text
