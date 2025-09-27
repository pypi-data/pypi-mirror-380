from __future__ import annotations
from typing import Any, Dict, Iterable, Iterator, Literal, Mapping, MutableMapping, Optional, Tuple, Union, IO, List
from dataclasses import dataclass
from urllib.parse import urljoin, urlparse
from contextlib import contextmanager
from pathlib import Path

import requests
from requests import Response, Session
from requests.adapters import HTTPAdapter

try:
    # Retry is in urllib3 >=1.26 and requests.packages.urllib3 in some installs
    from urllib3.util.retry import Retry
except Exception:
    from requests.packages.urllib3.util.retry import Retry  # type: ignore

Json = Mapping[str, Any]
Params = Mapping[str, Any]
FileSpec = Union[str, Path, IO[bytes]]  # path or open binary file
FilesDict = Mapping[str, Tuple[str, FileSpec]]  # field -> (filename, file/path/handle)


class ApiError(RuntimeError):
    def __init__(self, response: Response, message: Optional[str] = None):
        self.response = response
        self.status_code = response.status_code
        self.url = response.request.url if response.request else None
        super().__init__(message or f"API error {self.status_code} for {self.url}: {response.text[:500]}")


@dataclass
class RetryConfig:
    total: int = 3
    backoff_factor: float = 0.4
    status_forcelist: Tuple[int, ...] = (429, 500, 502, 503, 504)
    allowed_methods: Tuple[str, ...] = ("HEAD", "GET", "PUT", "POST", "PATCH", "DELETE", "OPTIONS")


def _is_absolute(url: str) -> bool:
    try:
        return bool(urlparse(url).scheme)
    except Exception:
        return False


class BappFrameworkApiClient:
    def __init__(
            self,
            base_url: Optional[str] = None,
            token: Optional[str] = None,
            bearer: Optional[str] = None,
            app: str = "erp",
            tenant: Optional[str] = None,
            timeout: float = 30.0,
            retry: Optional[RetryConfig] = RetryConfig(),
            session: Optional[Session] = None,
    ):
        self.base_url: str = (base_url or "https://panel.bapp.ro/api/").rstrip("/") + "/"
        self.timeout = timeout
        self.session: Session = session or requests.Session()

        # Session headers (carried across requests)
        self.session.headers.update({
            "User-Agent": "BappFrameworkApiClient/1.0 (+python-requests)",
            "X-App-Slug": app,
        })
        if token:
            self.set_token(token)
        elif bearer:
            self.set_bearer(bearer)
        if tenant:
            self.set_tenant(tenant)

        # Retries
        if retry:
            adapter = HTTPAdapter(
                max_retries=Retry(
                    total=retry.total,
                    backoff_factor=retry.backoff_factor,
                    status_forcelist=retry.status_forcelist,
                    allowed_methods=retry.allowed_methods,
                    raise_on_status=False,
                )
            )
            self.session.mount("https://", adapter)
            self.session.mount("http://", adapter)

    # ---------- auth / tenant ----------
    def set_token(self, token: str) -> None:
        self.session.headers["Authorization"] = f"Token {token}"

    def set_bearer(self, bearer: str) -> None:
        self.session.headers["Authorization"] = f"Bearer {bearer}"

    def clear_auth(self) -> None:
        self.session.headers.pop("Authorization", None)

    def set_tenant(self, tenant: Optional[str] = None) -> None:
        if tenant is None:
            self.session.headers.pop("x-tenant-id", None)
        else:
            self.session.headers["x-tenant-id"] = tenant

    @contextmanager
    def tenant_context(self, tenant: Optional[str]) -> Iterator[None]:
        """Temporarily set tenant for a block."""
        prev = self.session.headers.get("x-tenant-id")
        try:
            self.set_tenant(tenant)
            yield
        finally:
            if prev is None:
                self.session.headers.pop("x-tenant-id", None)
            else:
                self.session.headers["x-tenant-id"] = prev

    # ---------- low-level ----------
    def _url(self, path: str) -> str:
        return urljoin(self.base_url, path.lstrip("/"))

    def _handle_response(self, resp: Response) -> Any:
        if resp.status_code == 204:
            return {}
        if 200 <= resp.status_code < 300:
            ctype = resp.headers.get("Content-Type", "")
            if "application/json" in ctype:
                try:
                    return resp.json()
                except ValueError as e:
                    raise ApiError(resp, f"Invalid JSON response: {resp.text[:500]}") from e
            # Return text by default (or bytes if non-text)
            if ctype.startswith("text/") or "charset=" in ctype:
                return resp.text
            return resp.content
        # error
        raise ApiError(resp)

    def _request(
            self,
            method: Literal["GET", "POST", "PUT", "PATCH", "DELETE"],
            path: str,
            *,
            params: Optional[Params] = None,
            json: Optional[Json] = None,
            files: Optional[FilesDict] = None,
            data: Optional[Mapping[str, Any]] = None,
            stream: bool = False,
            timeout: Optional[float] = None,
    ) -> Response:
        url = self._url(path)
        resp = self.session.request(
            method=method.upper(),
            url=url,
            params=params,
            json=json,
            data=data,
            files=files,
            timeout=timeout or self.timeout,
            stream=stream,
        )
        return resp

    # ---------- file handling ----------
    @contextmanager
    def _opened_files(self, files: Optional[FilesDict]) -> Iterator[Optional[Mapping[str, Tuple[str, IO[bytes]]]]]:
        """
        Accepts files dict where each value is (filename, FileSpec).
        If FileSpec is a path/str, opens it and closes on exit.
        If it's already a file-like, passes through.
        """
        if not files:
            yield None
            return

        opened: Dict[str, Tuple[str, IO[bytes]]] = {}
        auto_close: list[IO[bytes]] = []
        try:
            for field, (fname, spec) in files.items():
                if hasattr(spec, "read"):
                    fh = spec  # type: ignore
                else:
                    fh = open(Path(spec), "rb")  # type: ignore[arg-type]
                    auto_close.append(fh)
                opened[field] = (fname, fh)  # requests expects (filename, fileobj)
            yield opened
        finally:
            for fh in auto_close:
                try:
                    fh.close()
                except Exception:
                    pass

    # ---------- high-level helpers ----------
    def api_call(
            self,
            method: Literal["GET", "POST", "PUT", "PATCH", "DELETE"],
            path: str,
            params: Optional[Params] = None,
            *,
            json: Optional[Json] = None,
            files: Optional[FilesDict] = None,
            data: Optional[Mapping[str, Any]] = None,
            stream: bool = False,
            timeout: Optional[float] = None,
    ) -> Any:
        with self._opened_files(files) as opened:
            resp = self._request(method, path, params=params, json=json, files=opened, data=data, stream=stream, timeout=timeout)
        if stream:
            return resp  # caller handles streaming/closing
        return self._handle_response(resp)

    # ---------- convenience methods for your API ----------
    # Tasks
    def get_available_tasks(self) -> Any:
        return self.api_call("GET", "tasks")

    def get_task_options(self, task_code: str) -> Any:
        return self.api_call("GET", f"tasks/{task_code}")

    def call_task(self, task_code: str, data: Optional[Dict[str, Any]] = None, files: Optional[FilesDict] = None, use_get: bool = False) -> Any:
        """
        Prefer POST for tasks with payload.
        Set use_get=True only for tasks explicitly designed for GET with query params.
        """
        data = data or {}
        if files:
            return self.api_call("POST", f"tasks/{task_code}", data=data, files=files)
        if use_get:
            return self.api_call("GET", f"tasks/{task_code}", params=data)
        return self.api_call("POST", f"tasks/{task_code}", json=data)

    # Introspect
    def introspect_content_type(self, content_type: str) -> Any:
        return self.api_call("GET", f"introspect/{content_type}/")

    # Actions
    def get_available_actions(self) -> Any:
        return self.api_call("GET", "actions")

    def get_action_options(self, action_code: str) -> Any:
        return self.api_call("GET", "actions", params={"code": action_code})

    def call_action(self, action_code: str, data: Optional[Dict[str, Any]] = None) -> Any:
        payload: Dict[str, Any] = {"code": action_code}
        if data:
            payload["payload"] = data
        return self.api_call("POST", "actions", json=payload)

    # Widgets
    def get_available_widgets(self) -> Any:
        return self.api_call("GET", "widgets")

    def get_widget_options(self, widget_code: str) -> Any:
        return self.api_call("GET", "widgets", params={"code": widget_code})

    def call_widget(self, widget_code: str, data: Optional[Dict[str, Any]] = None) -> Any:
        return self.api_call("POST", "widgets", json={"code": widget_code, "payload": data or {}})

    # Generic CRUD
    def list(self, content_type: str, params: Optional[Params] = None) -> Any:
        return self.api_call("GET", f"content-type/{content_type}/", params=params)

    def retrieve(self, content_type: str, pk: str, params: Optional[Params] = None) -> Any:
        return self.api_call("GET", f"content-type/{content_type}/{pk}/", params=params)

    def create(self, content_type: str, data: Dict[str, Any], files: Optional[FilesDict] = None) -> Any:
        if files:
            return self.api_call("POST", f"content-type/{content_type}/", data=data, files=files)
        return self.api_call("POST", f"content-type/{content_type}/", json=data)

    def update(self, content_type: str, pk: str, data: Dict[str, Any], files: Optional[FilesDict] = None) -> Any:
        if files:
            # Use PATCH or PUT semantics with correct endpoint when uploading files.
            return self.api_call("PUT", f"content-type/{content_type}/{pk}/", data=data, files=files)
        return self.api_call("PUT", f"content-type/{content_type}/{pk}/", json=data)

    def patch(self, content_type: str, pk: str, data: Dict[str, Any], files: Optional[FilesDict] = None) -> Any:
        if files:
            return self.api_call("PATCH", f"content-type/{content_type}/{pk}/", data=data, files=files)
        return self.api_call("PATCH", f"content-type/{content_type}/{pk}/", json=data)

    def delete(self, content_type: str, pk: str) -> Any:
        return self.api_call("DELETE", f"content-type/{content_type}/{pk}/")

    # Me
    def me(self) -> Any:
        # Using GET with explicit query params.
        return self.api_call("GET", "tasks/bapp_framework.me", params={"with_ua": "true"})

    # Utilities
    def list_paginated(self, content_type: str, params: Optional[Params] = None, page_param: str = "page", start: int = 1) -> Iterable[Any]:
        """
        Simple generator that paginates assuming `?page=N`. Adjust to your API's pagination scheme.
        """
        page = start
        while True:
            p = dict(params or {})
            p[page_param] = page
            data = self.list(content_type, p)
            yield data
            # Stop condition—customize if your API returns pagination metadata
            if not data or (isinstance(data, list) and not data):
                break
            page += 1

    def download(self, path: str, *, params: Optional[Params] = None, chunk_size: int = 8192) -> Iterator[bytes]:
        """
        Stream-download an endpoint.
        """
        resp = self._request("GET", path, params=params, stream=True)
        try:
            resp.raise_for_status()
            for chunk in resp.iter_content(chunk_size=chunk_size):
                if chunk:
                    yield chunk
        finally:
            resp.close()

    def list_pages(
            self,
            content_type: str,
            params: Optional[Dict[str, Any]] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        Yields full page payloads:
        {'count': int, 'next': str|None, 'previous': str|None, 'results': [...]}
        """
        # first page
        page: Dict[str, Any] = self.api_call("GET", f"content-type/{content_type}/", params=params)
        yield page

        # follow absolute 'next' URLs (DRF gives absolute)
        next_url = page.get("next")
        while next_url:
            # api_call/_url already handles absolute URLs; passing as 'path' is fine
            page = self.api_call("GET", next_url)
            yield page
            next_url = page.get("next")

    def iter_results(
            self,
            content_type: str,
            params: Optional[Dict[str, Any]] = None,
            limit: Optional[int] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        Streams individual items across all pages. Optional `limit` to stop early.
        """
        yielded = 0
        for page in self.list_pages(content_type, params=params):
            for item in page.get("results", []):
                yield item
                yielded += 1
                if limit is not None and yielded >= limit:
                    return

    def list_all(
            self,
            content_type: str,
            params: Optional[Dict[str, Any]] = None,
    ) -> Tuple[List[Dict[str, Any]], int]:
        """
        Collects all items into memory and returns (items, total_count).
        Prefer `iter_results` for large datasets.
        """
        items: List[Dict[str, Any]] = []
        total_count: Optional[int] = None
        for i, page in enumerate(self.list_pages(content_type, params=params)):
            if i == 0:
                total_count = int(page.get("count", 0))
            items.extend(page.get("results", []))
        return items, (total_count or len(items))

    # Context manager for auto-closing the session if you want it
    def close(self) -> None:
        self.session.close()

    def __enter__(self) -> "BappFrameworkApiClient":
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.close()
