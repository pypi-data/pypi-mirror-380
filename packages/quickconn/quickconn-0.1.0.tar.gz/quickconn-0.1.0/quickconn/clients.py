import asyncio
import ssl
import os
import random
import string
from collections import deque
from typing import Deque, Dict, Optional, Any
from urllib.parse import urlparse, urlencode
from aioquic.asyncio.client import connect
from aioquic.asyncio.protocol import QuicConnectionProtocol
from aioquic.h3.connection import H3Connection, H3_ALPN
from aioquic.h3.events import HeadersReceived, DataReceived
from aioquic.quic.configuration import QuicConfiguration
import httpx
import cloudscraper
import http.client
import json as js
import random
import string


def _R2(n=30):
    return "----" + "".join(random.choice(string.ascii_letters + string.digits) for _ in range(n))


class _Protocol(QuicConnectionProtocol):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._http = H3Connection(self._quic)
        self._request_events: Dict[int, Deque] = {}
        self._request_waiter: Dict[int, asyncio.Future] = {}

    async def perform_request(self, method: bytes, authority: str, path: str,
                              headers: list, body: bytes, timeout: float = 10.0):
        stream_id = self._quic.get_next_available_stream_id()

        hdrs = [
            (b":method", method),
            (b":scheme", b"https"),
            (b":authority", authority.encode("utf8")),
            (b":path", path.encode("utf8")),
        ] + headers
        self._http.send_headers(stream_id=stream_id, headers=hdrs)

        if body:
            self._http.send_data(stream_id=stream_id, data=body, end_stream=True)
        else:
            self._http.send_data(stream_id=stream_id, data=b"", end_stream=True)

        loop = asyncio.get_event_loop()
        waiter = loop.create_future()
        self._request_events[stream_id] = deque()
        self._request_waiter[stream_id] = waiter

        self.transmit()

        try:
            events = await asyncio.wait_for(waiter, timeout)
        except asyncio.TimeoutError:
            self._request_events.pop(stream_id, None)
            self._request_waiter.pop(stream_id, None)
            raise
        return events

    def H_R(self, event):
        if isinstance(event, (HeadersReceived, DataReceived)):
            stream_id = event.stream_id
            if stream_id in self._request_events:
                self._request_events[stream_id].append(event)
                if getattr(event, "stream_ended", False):
                    waiter = self._request_waiter.pop(stream_id, None)
                    events = self._request_events.pop(stream_id, deque())
                    if waiter and not waiter.done():
                        waiter.set_result(events)

    def quic_event_received(self, event):
        for http_event in self._http.handle_event(event):
            self.H_R(http_event)


class H3Response:
    def __init__(self, status: int, headers: Dict[str, str], content: bytes):
        self.status_code = status
        self.headers = headers
        self.content = content
        try:
            self.text = content.decode("utf-8", errors="ignore")
        except Exception:
            self.text = content.decode("latin1", errors="ignore")
        self.http_version = "HTTP/3"


class Http3Client:
    _verify = True
    _timeout = 15.0
    _alpn = list(H3_ALPN)

    @classmethod
    def _B2H(cls, headers: Optional[Dict[str, str]], data, json, files):
        headers = headers.copy() if headers else {}
        body = b""

        if json is not None:
            body = js.dumps(json).encode("utf-8")
            headers.setdefault("Content-Type", "application/json")
            return headers, body

        if files:
            if isinstance(files, str):
                files = {"file": files}
            boundary = _R2()
            parts = []
            for fieldname, path in files.items():
                filename = os.path.basename(path)
                with open(path, "rb") as f:
                    data_bytes = f.read()
                part_headers = (
                    f'--{boundary}\r\n'
                    f'Content-Disposition: form-data; name="{fieldname}"; filename="{filename}"\r\n'
                    f'Content-Type: application/octet-stream\r\n\r\n'
                ).encode("utf-8")
                parts.append(part_headers + data_bytes + b"\r\n")
            parts.append(f'--{boundary}--\r\n'.encode("utf-8"))
            body = b"".join(parts)
            headers.setdefault("Content-Type", f"multipart/form-data; boundary={boundary}")
            return headers, body
            
        

        if data is not None:
            if isinstance(data, (bytes, bytearray)):
                body = bytes(data)
            elif isinstance(data, str):
                body = data.encode("utf-8")
            elif isinstance(data, dict):
                body = urlencode(data).encode("utf-8")
                headers.setdefault("Content-Type", "application/x-www-form-urlencoded")
            else:
                body = str(data).encode("utf-8")

        return headers, body

    @classmethod
    async def _async_request(cls, method: str, url: str,
                             headers: Optional[Dict[str, str]] = None,
                             params: Optional[Dict[str, Any]] = None,
                             data: Any = None, json: Any = None,
                             files: Optional[Any] = None, timeout: Optional[float] = None,
                             verify: Optional[bool] = None):

        verify = cls._verify if verify is None else bool(verify)
        timeout = timeout or cls._timeout

        parsed = urlparse(url)
        if not parsed.scheme.startswith("http"):
            raise ValueError("URL must be http/https")

        host = parsed.hostname
        port = parsed.port or 443
        path = parsed.path or "/"

        if parsed.query:
            path += "?" + parsed.query
        if params:
            q = urlencode(params)
            path += ("&" if "?" in path else "?") + q

        hdrs, body = cls._B2H(headers or {}, data, json, files)

        config = QuicConfiguration(is_client=True, alpn_protocols=cls._alpn)
        if not verify:
            config.verify_mode = ssl.CERT_NONE

        async with connect(host, port, configuration=config, create_protocol=_Protocol) as protocol:
            protocol: _Protocol
            events = await protocol.perform_request(method.encode("utf-8"), parsed.netloc, path,
                                                    [(k.encode("utf-8"), str(v).encode("utf-8")) for k, v in hdrs.items()],
                                                    body, timeout=timeout)

            status = 0
            resp_headers: Dict[str, str] = {}
            content = b""
            for ev in events:
                if isinstance(ev, HeadersReceived):
                    for k, v in ev.headers:
                        if k == b":status":
                            status = int(v.decode())
                        else:
                            resp_headers[k.decode()] = v.decode()
                elif isinstance(ev, DataReceived):
                    content += ev.data

            return H3Response(status, resp_headers, content)

    @classmethod
    def request(cls, method: str, url: str, **kwargs):
        
        return asyncio.run(cls._async_request(method, url, **kwargs))

    @classmethod
    def get(cls, url: str, **kwargs):
        return cls.request("GET", url, **kwargs)

    @classmethod
    def post(cls, url: str, **kwargs):
        return cls.request("POST", url, **kwargs)

    @classmethod
    def put(cls, url: str, **kwargs):
        return cls.request("PUT", url, **kwargs)

    @classmethod
    def delete(cls, url: str, **kwargs):
        return cls.request("DELETE", url, **kwargs)


class CloudFlareSolver:
    @staticmethod
    def request(method, url, **kwargs):
        scraper = cloudscraper.create_scraper()
        return scraper.request(method, url, **kwargs)

    @staticmethod
    def get(url, **kwargs):
        return CloudFlareSolver.request("GET", url, **kwargs)

    @staticmethod
    def post(url, **kwargs):
        return CloudFlareSolver.request("POST", url, **kwargs)

    @staticmethod
    def put(url, **kwargs):
        return CloudFlareSolver.request("PUT", url, **kwargs)

    @staticmethod
    def delete(url, **kwargs):
        return CloudFlareSolver.request("DELETE", url, **kwargs)

    @staticmethod
    def head(url, **kwargs):
        return CloudFlareSolver.request("HEAD", url, **kwargs)

    @staticmethod
    def options(url, **kwargs):
        return CloudFlareSolver.request("OPTIONS", url, **kwargs)

    @staticmethod
    def patch(url, **kwargs):
        return CloudFlareSolver.request("PATCH", url, **kwargs)


class Http2Client:
    @staticmethod
    def _prepare_proxy(proxy):
        if isinstance(proxy, dict):
            return next(iter(proxy.values()))
        return proxy

    @staticmethod
    def request(method, url, **kwargs):
        proxy = kwargs.pop("proxy", None)
        proxy = Http2Client._prepare_proxy(proxy)

        files = None
        file_path = kwargs.pop("file", None)
        if file_path:
            if os.path.exists(file_path):
                files = {"file": open(file_path, "rb")}

        with httpx.Client(http2=True, proxy=proxy, timeout=20.0, trust_env=False) as client:
            resp = client.request(
                method,
                url,
                headers=kwargs.pop("headers", None),
                params=kwargs.pop("params", None),
                data=kwargs.pop("data", None),
                json=kwargs.pop("json", None),
                files=files
            )
        return resp

    @staticmethod
    def get(url, **kwargs):
        return Http2Client.request("GET", url, **kwargs)

    @staticmethod
    def post(url, **kwargs):
        return Http2Client.request("POST", url, **kwargs)

    @staticmethod
    def put(url, **kwargs):
        return Http2Client.request("PUT", url, **kwargs)
        
        
    @staticmethod
    def head(url: str, **kwargs) -> httpx.Response:
        return Http2Client.request("HEAD", url, **kwargs)
        
   
    @staticmethod
    def patch(url: str, **kwargs) -> httpx.Response:
        return Http2Client.request("PATCH", url, **kwargs)
        
        
    @staticmethod
    def delete(url, **kwargs):
        return Http2Client.request("DELETE", url, **kwargs)


class Http1Client:
    @staticmethod
    def _prepare_proxy(proxy):
        if isinstance(proxy, dict):
            return next(iter(proxy.values()))
        return proxy

    @staticmethod
    def request(method, url, **kwargs):
        proxy = kwargs.pop("proxy", None)
        proxy = Http1Client._prepare_proxy(proxy)

        files = None
        file_path = kwargs.pop("file", None)
        if file_path:
            if os.path.exists(file_path):
                files = {"file": open(file_path, "rb")}

        with httpx.Client(http1=True, proxy=proxy, timeout=20.0, trust_env=False) as client:
            resp = client.request(
                method,
                url,
                headers=kwargs.pop("headers", None),
                params=kwargs.pop("params", None),
                data=kwargs.pop("data", None),
                json=kwargs.pop("json", None),
                files=files
            )
        return resp

    @staticmethod
    def get(url, **kwargs):
        return Http1Client.request("GET", url, **kwargs)

    @staticmethod
    def post(url, **kwargs):
        return Http1Client.request("POST", url, **kwargs)

    @staticmethod
    def put(url, **kwargs):
        return Http1Client.request("PUT", url, **kwargs)
        
        
    @staticmethod
    def head(url: str, **kwargs) -> httpx.Response:
        return Http1Client.request("HEAD", url, **kwargs)
        
   
    @staticmethod
    def patch(url: str, **kwargs) -> httpx.Response:
        return Http1Client.request("PATCH", url, **kwargs)
        
        
    @staticmethod
    def delete(url, **kwargs):
        return Http1Client.request("DELETE", url, **kwargs)
        
        

class Http10Response:
    def __init__(self, status, headers, content):
        self.status_code = status
        self.headers = headers
        self.content = content
        self.cookies = self._parse_cookies()
        try:
            self.text = content.decode("utf-8", errors="ignore")
        except:
            self.text = content.decode("latin1", errors="ignore")

    def json(self):
        try:
            return js.loads(self.text)
        except:
            return None

    def _parse_cookies(self):
        cookies = {}
        for k, v in self.headers.items():
            if k.lower() == "set-cookie":
                parts = v.split(";")
                for part in parts:
                    if "=" in part:
                        key, val = part.strip().split("=", 1)
                        cookies[key] = val
        return cookies

class Http10Client:
    @staticmethod
    def _prepare_body_and_headers(data=None, json=None, files=None, headers=None):
        headers = headers.copy() if headers else {}
        body = None

        if json is not None:
            body = js.dumps(json).encode("utf-8")
            headers.setdefault("Content-Type", "application/json")
            return headers, body

        if files:
            if isinstance(files, str):
                files = {"file": files}
            boundary = _R2()
            parts = []
            if data is None:
                data = {}
            for key, value in data.items():
                part = (
                    f"--{boundary}\r\n"
                    f'Content-Disposition: form-data; name="{key}"\r\n\r\n'
                    f"{value}\r\n"
                ).encode("utf-8")
                parts.append(part)
            for fieldname, filepath in files.items():
                filename = os.path.basename(filepath)
                with open(filepath, "rb") as f:
                    file_content = f.read()
                part = (
                    f"--{boundary}\r\n"
                    f'Content-Disposition: form-data; name="{fieldname}"; filename="{filename}"\r\n'
                    f"Content-Type: application/octet-stream\r\n\r\n"
                ).encode("utf-8") + file_content + b"\r\n"
                parts.append(part)
            parts.append(f"--{boundary}--\r\n".encode("utf-8"))
            body = b"".join(parts)
            headers["Content-Type"] = f"multipart/form-data; boundary={boundary}"
            return headers, body

        if data is not None:
            if isinstance(data, dict):
                body = urlencode(data).encode("utf-8")
                headers.setdefault("Content-Type", "application/x-www-form-urlencoded")
            elif isinstance(data, str):
                body = data.encode("utf-8")
            elif isinstance(data, bytes):
                body = data
            else:
                body = str(data).encode("utf-8")

        return headers, body

    @staticmethod
    def request(method, url, headers=None, params=None, data=None, json=None, files=None,
                timeout=15, proxy=None, verify=True):
        parsed = urlparse(url)
        path = parsed.path or "/"
        if parsed.query:
            path += "?" + parsed.query
        if params:
            q = urlencode(params)
            path += ("&" if "?" in path else "?") + q

        headers, body = Http10Client._prepare_body_and_headers(data, json, files, headers)

        port = parsed.port or (443 if parsed.scheme == "https" else 80)
        conn_class = http.client.HTTPSConnection if parsed.scheme == "https" else http.client.HTTPConnection

        ssl_context = None
        if parsed.scheme == "https":
            if verify:
                ssl_context = ssl.create_default_context()
            else:
                ssl_context = ssl._create_unverified_context()

        
        if proxy:
            if isinstance(proxy, dict):
                proxy_url = proxy.get("http") or proxy.get("https")
            else:
                proxy_url = proxy
            proxy_parsed = urlparse(proxy_url)
            conn = conn_class(proxy_parsed.hostname, proxy_parsed.port, timeout=timeout, context=ssl_context)            
            full_path = url if parsed.scheme == "http" else url
            conn.request(method.upper(), full_path, body=body, headers=headers)
        else:
            conn = conn_class(parsed.hostname, port, timeout=timeout, context=ssl_context)
            conn.request(method.upper(), path, body=body, headers=headers)

        resp = conn.getresponse()
        content = resp.read()
        response_headers = dict(resp.getheaders())
        conn.close()

        return Http10Response(resp.status, response_headers, content)

    @staticmethod
    def get(url, **kwargs):
        return Http10Client.request("GET", url, **kwargs)

    @staticmethod
    def post(url, **kwargs):
        return Http10Client.request("POST", url, **kwargs)

    @staticmethod
    def put(url, **kwargs):
        return Http10Client.request("PUT", url, **kwargs)

    @staticmethod
    def delete(url, **kwargs):
        return Http10Client.request("DELETE", url, **kwargs)


