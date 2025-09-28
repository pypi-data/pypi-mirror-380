from __future__ import annotations

"""
Diagnostics context utilities.

This module provides a single global ContextVar `CORRELATION_ID` and helpers to
get/set/propagate it across threads, tasks and framework boundaries.

It intentionally has **no hard dependencies** on FastAPI/Starlette/etc.
Where integration is useful, we expose tiny adapters that import lazily.
"""

from contextlib import contextmanager
from contextvars import ContextVar, copy_context
from typing import Any, Callable, Generator, Optional, TypeVar
import functools
import uuid
import logging

T = TypeVar("T")

# ---------------------------------------------------------------------------
# Global correlation id (string or None). Frameworks may set it per-request.
# ---------------------------------------------------------------------------
CORRELATION_ID: ContextVar[Optional[str]] = ContextVar("CORRELATION_ID", default=None)


# ---------------------------------------------------------------------------
# Basic API
# ---------------------------------------------------------------------------
def get_correlation_id() -> Optional[str]:
    """Return current correlation id (or None)."""
    return CORRELATION_ID.get()


def set_correlation_id(value: Optional[str]) -> Optional[str]:
    """
    Set correlation id explicitly. Returns the value set for convenience.
    Prefer using `use_correlation_id(...)` context manager in most cases.
    """
    CORRELATION_ID.set(value)
    return value


def new_correlation_id(prefix: str = "") -> str:
    """
    Generate and set a fresh correlation id. Returns the new id.
    """
    cid = f"{prefix}{uuid.uuid4()}" if prefix else str(uuid.uuid4())
    CORRELATION_ID.set(cid)
    return cid


def clear_correlation_id() -> None:
    """Clear correlation id (sets to None)."""
    CORRELATION_ID.set(None)


@contextmanager
def use_correlation_id(
    value: Optional[str] = None,
    *,
    generate_if_missing: bool = True,
    prefix: str = ""
) -> Generator[str, None, None]:
    """
    Context manager that sets correlation id for the duration of the block
    and restores the previous value afterwards.

    If `value` is None and there is no current id, a new one is generated
    when `generate_if_missing=True`.
    """
    current = CORRELATION_ID.get()
    if value is None:
        if current is None and generate_if_missing:
            value = f"{prefix}{uuid.uuid4()}" if prefix else str(uuid.uuid4())
        else:
            value = current
    token = CORRELATION_ID.set(value)
    try:
        yield value  # type: ignore[misc]
    finally:
        CORRELATION_ID.reset(token)


# ---------------------------------------------------------------------------
# Call / thread helpers
# ---------------------------------------------------------------------------
def wrap_with_correlation(fn: Callable[..., T], correlation_id: Optional[str] = None) -> Callable[..., T]:
    """
    Capture current (or given) correlation id and return a wrapper that
    restores it before calling `fn`. Useful for threading/async executors.
    """
    corr = correlation_id if correlation_id is not None else CORRELATION_ID.get()

    @functools.wraps(fn)
    def _wrapped(*args, **kwargs) -> T:
        token = CORRELATION_ID.set(corr)
        try:
            return fn(*args, **kwargs)
        finally:
            CORRELATION_ID.reset(token)

    return _wrapped


def copy_context_with_correlation() -> Any:
    """
    Return a contextvars copy of the current context (including correlation id).
    You can run callables inside it via `ctx.run(callable, *args)`.
    """
    return copy_context()


# ---------------------------------------------------------------------------
# Logging integration
# ---------------------------------------------------------------------------
class CorrelationFilter(logging.Filter):
    """
    Logging filter that injects the correlation id into LogRecord as
    `record.correlation_id`. Add to your handlers and use in formatter as
    `%(correlation_id)s`.
    """
    def filter(self, record: logging.LogRecord) -> bool:  # type: ignore[override]
        try:
            record.correlation_id = CORRELATION_ID.get()
        except Exception:
            record.correlation_id = None
        return True


def fastapi_dependency(header_name: str = "x-correlation-id", generate_if_missing: bool = True):
    """
    Tiny dependency function factory for FastAPI/Starlette that:
        - reads correlation id from `request.headers[header_name]` if present,
        - otherwise (optionally) generates a new id,
        - sets the ContextVar for the request scope,
        - returns the correlation id (string).

    Usage:
        from fastapi import Depends, Request
        from spx_sdk.diagnostics.context import fastapi_dependency

        get_cid = fastapi_dependency()

        @app.get("/ping")
        def ping(cid: str = Depends(get_cid)):
            return {"ok": True, "cid": cid}
    """
    def _dep(request: Any) -> str:
        # Lazy import only if really used
        try:
            hdrs = request.headers  # type: ignore[attr-defined]
        except Exception:
            hdrs = {}
        raw = None
        if hasattr(hdrs, "get"):
            raw = hdrs.get(header_name)  # type: ignore[call-arg]
        if raw is None and generate_if_missing:
            raw = str(uuid.uuid4())
        set_correlation_id(raw)
        return raw
    return _dep


def attach_response_header(response: Any, header_name: str = "x-correlation-id") -> None:
    """
    Try to attach the current correlation id to a response-like object that
    supports `headers` mapping or `__setitem__` on headers.
    Safe to call even if `response` is not a Starlette/fastapi Response.
    """
    cid = CORRELATION_ID.get()
    if cid is None:
        return
    try:
        # Starlette/FastAPI Response
        if hasattr(response, "headers") and hasattr(response.headers, "__setitem__"):
            response.headers[header_name] = cid  # type: ignore[index]
            return
        # Generic mapping-like
        if hasattr(response, "__setitem__"):
            response[header_name] = cid  # type: ignore[index]
    except Exception:
        pass
