# SPDX-License-Identifier: MIT
# Copyright (c) 2025 Hammerheads Engineers sp. z o.o.
# Author: Aleksander Stanik
"""
SPX Python Client

Dictionary-like interface to SPX Server API v3.
Supports GET and PUT for components and attributes under a named system.
"""
import requests
import re
import json
import os
import threading
import contextlib
import logging
from collections.abc import MutableMapping
from typing import Optional, List, Any

log = logging.getLogger("spx.client")

# ---------------------------------------------------------------------------
# Global / thread-local transparent mode controls
# ---------------------------------------------------------------------------
_GLOBAL_TRANSPARENT = False
_thread_local = threading.local()


def set_global_transparent(enabled: bool) -> None:
    """
    Set process-wide transparent mode for newly constructed SpxClient instances.
    Explicit SpxClient(transparent=...) always takes precedence.
    """
    global _GLOBAL_TRANSPARENT
    _GLOBAL_TRANSPARENT = bool(enabled)


def get_global_transparent() -> bool:
    """
    Return effective transparent mode from (in order of precedence):
      1) thread-local override set by `transparent_mode` context manager
      2) environment variable SPX_TRANSPARENT (1/true/yes/on)
      3) process-global flag set via set_global_transparent()
    """
    tl = getattr(_thread_local, "transparent", None)
    if tl is not None:
        return bool(tl)
    env = os.getenv("SPX_TRANSPARENT")
    if env is not None:
        return env.strip().lower() in {"1", "true", "yes", "on"}
    return _GLOBAL_TRANSPARENT


def get_global_pretty_errors() -> bool:
    """Return default pretty-errors setting from env (SPX_PRETTY_ERRORS). Defaults to True."""
    env = os.getenv("SPX_PRETTY_ERRORS")
    if env is None:
        return True
    return env.strip().lower() in {"1", "true", "yes", "on"}


def get_global_fault_verbose() -> bool:
    """Return whether client should log full fault JSON to console (SPX_CLIENT_FAULT_VERBOSE). Defaults to False."""
    env = os.getenv("SPX_CLIENT_FAULT_VERBOSE")
    if env is None:
        return False
    return env.strip().lower() in {"1", "true", "yes", "on"}


@contextlib.contextmanager
def transparent_mode(enabled: bool):
    """
    Temporarily set transparent mode for the current thread.
    Usage:
        with transparent_mode(True):
            # all new SpxClient() created here default to transparent=True
            ...
    """
    prev = getattr(_thread_local, "transparent", None)
    _thread_local.transparent = bool(enabled)
    try:
        yield
    finally:
        if prev is None:
            try:
                delattr(_thread_local, "transparent")
            except AttributeError:
                pass
        else:
            _thread_local.transparent = prev


class _TransparentSentinel:
    """
    No-op placeholder used when SpxClient runs in transparent mode.

    Behaves as:
    - callable: returns {"result": True}
    - attribute access: returns itself again (chaining-friendly)
    - setting attributes: ignored
    - numeric cast: 0 / 0.0
    - iteration: empty
    - truthiness: False
    """
    def __call__(self, *args, **kwargs):
        return {"result": True}

    def __getattr__(self, name: str):
        return self

    def __setattr__(self, name: str, value: Any):
        # ignore writes
        pass

    def __repr__(self):
        return "<transparent>"

    def __str__(self):
        return "<transparent>"

    def __bool__(self):
        return False

    def __int__(self):
        return 0

    def __float__(self):
        return 0.0

    def __iter__(self):
        return iter(())


class SpxApiError(requests.HTTPError):
    """HTTP error raised by SpxClient with parsed fault payload attached.

    Attributes:
        fault: dict with fault projection (may be compact/full) or fallback info
        correlation_id: correlation id extracted from response headers if present
    """
    def __init__(self, message: str, response=None, fault: Optional[dict] = None):
        super().__init__(message, response=response)
        self.fault = fault or {}
        try:
            self.correlation_id = (response.headers.get("x-correlation-id") if response is not None else None)
        except Exception:
            self.correlation_id = None


class SpxClient(MutableMapping):
    """
    A client for SPX Server API v3 with dict-like access.

    Usage:
        client = SpxClient(
            base_url='http://127.0.0.1:8000',
            product_key='YOUR_PRODUCT_KEY',
            system_name='your_system'
        )
        # Read an attribute:
        temp = client['timer'].time
        # Set an attribute:
        client['timer'].time = 5.0
        # Get full component or root JSON:
        data = client ['timer'] # returns JSON at current path

        # Transparent mode (process-wide / thread-local / env):
        #   set_global_transparent(True)
        #   with transparent_mode(True):
        #       ...
        #   export SPX_TRANSPARENT=1
        # Or per-instance:
        #   SpxClient(..., transparent=True)
    """
    def __init__(self,
                 base_url: str,
                 product_key: str,
                 http_client=None,
                 path: Optional[List[str]] = None,
                 transparent: Optional[bool] = None,
                 on_fault: Optional[Any] = None,
                 pretty_errors: Optional[bool] = True,
                 client_fault_verbose: Optional[bool] = None,
                 ):
        self.base_url = base_url.rstrip('/')
        self.product_key = product_key
        self.path = path or []
        self.headers = {
            'Authorization': f'Bearer {self.product_key}',
            'Content-Type': 'application/json'
        }
        # allow injection of a custom HTTP client (e.g. FastAPI TestClient)
        self.http = http_client or requests
        # Determine effective transparent mode:
        # explicit arg > thread-local ctx > env var > module-global default
        effective_transparent = get_global_transparent() if transparent is None else bool(transparent)
        # set transparently via __dict__ to avoid __setattr__ side-effects during init
        self.__dict__["transparent"] = bool(effective_transparent)
        self.__dict__["_t"] = _TransparentSentinel() if self.__dict__["transparent"] else None
        self.__dict__["on_fault"] = on_fault
        eff_pretty = get_global_pretty_errors() if pretty_errors is None else bool(pretty_errors)
        self.__dict__["pretty_errors"] = eff_pretty
        eff_verbose = get_global_fault_verbose() if client_fault_verbose is None else bool(client_fault_verbose)
        self.__dict__["client_fault_verbose"] = eff_verbose

    def _build_url(self) -> str:
        if getattr(self, "transparent", False):
            # URL is irrelevant in transparent mode; return a stable pseudo-url
            return "transparent://"
        segments = [self.base_url, 'api', 'v3', 'system'] + self.path
        return '/'.join(segments)

    def _extract_fault_from_response(self, resp) -> dict:
        # Correlation id from headers (best-effort)
        corr = None
        try:
            corr = resp.headers.get("x-correlation-id") or resp.headers.get("X-Correlation-Id")
        except Exception:
            corr = None

        # Normalize status code once
        try:
            status = int(getattr(resp, "status_code", None))
        except Exception:
            status = None

        # Try to parse JSON body
        data = None
        try:
            data = resp.json()
        except Exception:
            data = None

        # 1) Already our diagnostics fault format
        if isinstance(data, dict) and data.get("type") == "fault":
            fault = dict(data)  # shallow copy to avoid mutating caller
            if fault.get("http_status") is None:
                fault["http_status"] = status
            if not fault.get("correlation_id") and corr:
                fault["correlation_id"] = corr
            return fault

        # 2) RFC7807 (+ optional extensions)
        if isinstance(data, dict) and ("title" in data or "status" in data or "type" in data):
            # Some servers omit status in body; prefer HTTP status
            body_status = data.get("status")
            try:
                body_status = int(body_status) if body_status is not None else status
            except Exception:
                body_status = status

            # Prefer problem+json extensions when present
            extensions = data.get("extensions") if isinstance(data.get("extensions"), dict) else {}
            if extensions.get("type") == "fault":
                fault = dict(extensions)
                if fault.get("http_status") is None:
                    fault["http_status"] = body_status
                if not fault.get("correlation_id") and corr:
                    fault["correlation_id"] = corr
                return fault

            # Generic problem normalization
            return {
                "type": "fault",
                "event": data.get("type", "problem"),
                "http_status": body_status,
                "action": extensions.get("action"),
                "component": extensions.get("component"),
                "correlation_id": extensions.get("correlation_id") or corr,
                "error": {
                    "type": data.get("title", "HTTPError"),
                    "message": data.get("detail") or data.get("description") or "",
                },
                "breadcrumbs": extensions.get("breadcrumbs"),
                "extra": extensions.get("extra"),
            }

        # 3) FastAPI/Starlette default shape {"detail": ...} or unknown JSON
        if isinstance(data, dict):
            message = data.get("detail") if "detail" in data else json.dumps(data, ensure_ascii=False)
            return {
                "type": "fault",
                "event": "http_error",
                "http_status": status,
                "action": None,
                "component": None,
                "correlation_id": corr,
                "error": {
                    "type": "HTTPError",
                    "message": message,
                },
            }

        # 4) Non-JSON / no body
        try:
            text = resp.text
        except Exception:
            text = ""
        return {
            "type": "fault",
            "event": "http_error",
            "http_status": status,
            "action": None,
            "component": None,
            "correlation_id": corr,
            "error": {
                "type": "HTTPError",
                "message": text,
            },
        }

    def _emit_fault_event(self, resp, where: str) -> dict:
        """Emit a structured client-side fault event via logging and optional callback."""
        fault = self._extract_fault_from_response(resp)
        payload = {
            "where": where,
            "method": getattr(getattr(resp, "request", None), "method", None),
            "url": getattr(getattr(resp, "request", None), "url", None),
            "http_status": getattr(resp, "status_code", None),
            "correlation_id": fault.get("correlation_id") or (resp.headers.get("x-correlation-id") if hasattr(resp, "headers") else None),
            "fault": fault,
        }
        # user hook first (non-fatal)
        try:
            cb = getattr(self, "on_fault", None)
            if cb:
                cb(payload)
        except Exception:
            pass
        try:
            if getattr(self, "pretty_errors", True) and not getattr(self, "client_fault_verbose", False):
                summary = self._format_pretty_fault(fault, where=where)
                # concise console message
                log.error("CLIENT_FAULT %s", summary)
                # full payload for deeper diagnostics at debug level
                try:
                    log.debug("CLIENT_FAULT_FULL %s", json.dumps(payload, ensure_ascii=False))
                except Exception:
                    log.debug("CLIENT_FAULT_FULL %r", payload)
            else:
                # verbose mode: keep previous behavior
                log.error("CLIENT_FAULT %s", json.dumps(payload, ensure_ascii=False))
        except Exception:
            # last resort plain repr
            log.error("CLIENT_FAULT %r", payload)
        return fault

    def _summarize_validator_message(self, msg: str) -> str:
        if not isinstance(msg, str) or not msg:
            return "validation failed"
        m = re.search(r"Template '([^']+)'\s+schema validation failed:\s*(\d+) errors?:\s*(.*)", msg)
        if m:
            name = m.group(1)
            tail = m.group(3)
            # Split by commas, keep readable ' at ' delimiter instead of '@'
            raw_parts = [p.strip() for p in tail.split(',') if p.strip()]
            norm_parts = list(raw_parts)  # keep readable ' at ' delimiter instead of '@'
            from collections import OrderedDict
            counts = OrderedDict()
            for p in norm_parts:
                counts[p] = counts.get(p, 0) + 1
            if counts:
                # Show up to 3 unique entries; aggregate duplicates with ×N suffix
                items = list(counts.items())
                head_items = items[:3]
                rest_unique = max(0, len(items) - len(head_items))
                head = [f"{text} ×{n}" if n > 1 else text for text, n in head_items]
                suffix = f"; +{rest_unique} more" if rest_unique > 0 else ""
                return f"Template '{name}': " + "; ".join(head) + suffix
            return f"Template '{name}': validation failed"
        first = msg.splitlines()[0]
        return (first[:300] + "…") if len(first) > 300 else first

    def _format_pretty_fault(self, fault: dict, where: str) -> str:
        status = fault.get("http_status")
        event = fault.get("event") or "error"
        cid = fault.get("correlation_id") or ""
        comp = fault.get("component") or {}
        comp_path = comp.get("path") or comp.get("name") or ""
        action = fault.get("action") or ""
        err = (fault.get("error") or {}).get("message") or ""
        core = self._summarize_validator_message(err)
        bits = []
        if status is not None:
            bits.append(str(status))
        if event:
            bits.append(event)
        if core:
            bits.append(core)
        summary = ": ".join(bits)
        meta = []
        if comp_path:
            meta.append(f"component={comp_path}")
        if action:
            meta.append(f"action={action}")
        if cid:
            meta.append(f"cid={cid}")
        if meta:
            summary += " (" + ", ".join(meta) + ")"
        return summary

    def _request(self, method: str, url: str, where: str, **kwargs):
        """Centralized HTTP request with fault capture and raising SpxApiError on 4xx/5xx."""
        if getattr(self, "transparent", False):
            class _Dummy:
                status_code = 200
                headers = {}

                def json(self):
                    return {}
            return _Dummy()
        # merge headers if caller provided extras
        headers = dict(self.headers)
        if "headers" in kwargs and isinstance(kwargs["headers"], dict):
            headers.update(kwargs.pop("headers"))
        resp = self.http.request(method, url, headers=headers, **kwargs)
        if 400 <= getattr(resp, "status_code", 0):
            fault = self._emit_fault_event(resp, where=where)
            if getattr(self, "pretty_errors", True):
                msg = self._format_pretty_fault(fault, where=where)
            else:
                msg = f"{method} {url} -> {getattr(resp, 'status_code', None)}"
            raise SpxApiError(msg, response=resp, fault=fault)
        return resp

    def __getitem__(self, key: str):
        if self.transparent:
            new_path = self.path + [key]
            return SpxClient(self.base_url, self.product_key, http_client=self.http, path=new_path, transparent=True, pretty_errors=self.pretty_errors, client_fault_verbose=self.client_fault_verbose)
        # Extend path and perform GET
        new_path = self.path + [key]
        url = '/'.join([self.base_url, 'api', 'v3', 'system'] + new_path)
        resp = self._request("GET", url, where="client.__getitem__")
        data = resp.json()
        # Leaf attribute returns {'value': ...}
        if isinstance(data, dict) and 'value' in data:
            return data['value']
        # Otherwise return a new client focused on the deeper path
        return SpxClient(self.base_url,
                         self.product_key,
                         http_client=self.http,
                         path=new_path,
                         transparent=self.transparent,
                         pretty_errors=self.pretty_errors,
                         client_fault_verbose=self.client_fault_verbose)

    def __setitem__(self, key: str, value):
        # Extend path and perform PUT
        url = '/'.join([self.base_url, 'api', 'v3', 'system'] + self.path)
        payload = {key: value}
        return self.put_item(url, payload)

    def put_item(self, path: str, payload: dict) -> Any:
        """
        Set a value at an arbitrary path under the current path.
        Example:
            client.put_item('sensor1/threshold', 42)
        """
        if self.transparent:
            return {}
        resp = self._request("PUT", path, where="client.put_item", json=payload)
        try:
            return resp.json()
        except ValueError:
            return {}

    def __delitem__(self, key: str):
        if self.transparent:
            return None
        # Extend path and perform DELETE
        new_path = self.path + [key]
        url = '/'.join([self.base_url, 'api', 'v3', 'system'] + new_path)
        self._request("DELETE", url, where="client.__delitem__")
        return None

    def __contains__(self, key: str) -> bool:
        """
        Dictionary-like membership test at the current path.
        Returns True if `key` exists in the JSON data returned by GET.
        """
        if self.transparent:
            return False
        data = self.get()
        children = data.get('children', [])
        return any(child.get('name') == key for child in children)

    def get(self):
        """
        GET the full JSON at current path.
        """
        if self.transparent:
            return {}
        url = self._build_url()
        resp = self._request("GET", url, where="client.get")
        return resp.json()

    def to_dict(self) -> dict:
        """
        Return the current path's JSON as a pure Python dict.
        """
        return self.get()

    def __call__(self, *args, **kwargs):
        """Allow calling any SpxClient in transparent mode as a no-op.
        This keeps attribute-access chains usable for RPC-like calls
        (e.g., client.instances.sensor.reset()).
        """
        if getattr(self, "transparent", False):
            return {"result": True}
        raise TypeError(
            "SpxClient is not callable in non-transparent mode; "
            "use attribute access to obtain a method stub (e.g. client.reset(...))."
        )

    def __repr__(self):
        return f"<SpxClient path={'/'.join(self.path) or '<root>'}>"

    def __eq__(self, other):
        """
        Compare this client's data to another client or dict by comparing
        their JSON structures.
        """
        if isinstance(other, SpxClient):
            return self.to_dict() == other.to_dict()
        if isinstance(other, dict):
            return self.to_dict() == other
        return False

    def __ne__(self, other):
        """
        Inverse of __eq__ for inequality comparison.
        """
        return not (self == other)

    def __str__(self):
        """
        Return the full system structure from the current path
        as formatted JSON.
        """

        data = self.get()
        return json.dumps(data, indent=2)

    def _child_names(self, data: dict) -> list[str]:
        """Return child component names from a system JSON dict."""
        return [child.get('name') for child in data.get('children', []) if isinstance(child, dict) and 'name' in child]

    def _call_method(self, method_name, **kwargs):
        if self.transparent:
            return {"result": True}
        url = f"{self._build_url()}/method/{method_name}"
        resp = self._request("POST", url, where="client._call_method", json={"kwargs": kwargs})
        try:
            return resp.json()
        except ValueError:
            return None

    def __getattr__(self, key: str) -> Any:
        # never intercept private/special names
        if key.startswith("_"):
            error_msg = (
                f"{type(self).__name__!r} has no attribute "
                f"{key!r}"
            )
            raise AttributeError(error_msg)
        # In transparent mode, attribute-style traversal should return a new
        # SpxClient focused on the extended path, without performing any HTTP.
        if getattr(self, "transparent", False):
            new_path = self.path + [key]
            return SpxClient(
                self.base_url,
                self.product_key,
                http_client=self.http,
                path=new_path,
                transparent=True,
                client_fault_verbose=self.client_fault_verbose,
            )
        data = object.__getattribute__(self, "get")()
        # top-level simple values
        if key in data and not isinstance(data[key], dict):
            return data[key]

        # attributes under 'attr'
        attr_sec = data.get("attr", {})
        if key in attr_sec:
            return attr_sec[key].get("value")

        # child components -> return a deeper SpxClient wrapper
        if any(child_name == key for child_name in self._child_names(data)):
            new_path = self.path + [key]
            return SpxClient(
                self.base_url,
                self.product_key,
                http_client=self.http,
                path=new_path,
                transparent=self.transparent,
                pretty_errors=self.pretty_errors,
                client_fault_verbose=self.client_fault_verbose
            )

        # fallback: treat as RPC method
        return lambda **kwargs: self._call_method(key, **kwargs)

    def __setattr__(self, key: str, value) -> Any:
        if key == "transparent":
            self.__dict__["transparent"] = bool(value)
            # keep sentinel in sync
            if self.__dict__["transparent"]:
                self.__dict__["_t"] = _TransparentSentinel()
            else:
                # remove sentinel when leaving transparent mode
                self.__dict__["_t"] = None
            return {}

        # Attributes that belong to the client object itself and must never trigger HTTP calls
        internal_keys = ('base_url', 'product_key', 'http', 'path', 'headers', '_t')

        # If we are setting any internal attribute, store it directly
        if key in internal_keys:
            return super().__setattr__(key, value)

        # In transparent mode, ignore any mutations to remote attributes
        try:
            is_transparent = object.__getattribute__(self, "transparent")
        except AttributeError:
            is_transparent = False

        if is_transparent:
            # no-op in transparent mode
            return {}

        # Delegate to put_attr so path handling is uniform
        return self.put_attr(key, value)

    def put_attr(self, path: str, value) -> dict:
        """
        Set an attribute value at an arbitrary path under the current path.
        Example:
            client.put_attr('sensor1/threshold', 42)
        """
        if self.transparent:
            return {}
        # Interpret `path` as relative to current node; the **last** segment is the attribute name.
        segments = [seg for seg in path.strip('/').split('/') if seg]
        if not segments:
            raise ValueError("path must contain at least an attribute name")
        parent_segments = segments[:-1]
        attr_name = segments[-1]
        new_path = self.path + parent_segments + ['attr', attr_name]
        url = '/'.join([self.base_url, 'api', 'v3', 'system'] + new_path)
        payload = {'value': value}
        resp = self._request("PUT", url, where="client.put_attr", json=payload)
        try:
            return resp.json()
        except ValueError:
            return {}

    def __iter__(self):
        """
        Iterate over keys in the current mapping:
        attribute names and child component names.
        """
        if self.transparent:
            return iter([])
        data = self.get()
        # Only child component names from 'children' list
        child_keys = [child.get('name') for child in data.get('children', [])]
        for key in child_keys:
            yield key

    def __len__(self):
        """
        Return the total number of keys in the mapping.
        """
        if self.transparent:
            return 0
        data = self.get()
        return len(data.get('attr', {})) + len(data.get('children', []))

    def keys(self):
        if self.transparent:
            return []
        return list(self.__iter__())

    def items(self):
        if self.transparent:
            return []
        return [(key, self[key]) for key in self]

    def values(self):
        if self.transparent:
            return []
        return [self[key] for key in self]
