import os
import sys
import threading
from dataclasses import dataclass, field, fields
from typing import Any, Dict

from arize.constants.config import (
    DEFAULT_API_HOST,
    DEFAULT_API_INSECURE,
    DEFAULT_FLIGHT_HOST,
    DEFAULT_FLIGHT_PORT,
    DEFAULT_FLIGHT_TRANSPORT_SCHEME,
    ENV_API_HOST,
    ENV_API_INSECURE,
    ENV_API_KEY,
    ENV_FLIGHT_HOST,
    ENV_FLIGHT_PORT,
    ENV_FLIGHT_TRANSPORT_SCHEME,
)
from arize.exceptions.auth import MissingAPIKeyError
from arize.version import __version__


def _api_key_factory() -> str:
    return os.getenv(ENV_API_KEY, "")


def _api_host_factory() -> str:
    return os.getenv(ENV_API_HOST, DEFAULT_API_HOST)


def _api_scheme_factory() -> str:
    insecure = os.getenv(ENV_API_INSECURE, DEFAULT_API_INSECURE)
    if insecure:
        return "http"
    return "https"


def _flight_host_factory() -> str:
    return os.getenv(ENV_FLIGHT_HOST, DEFAULT_FLIGHT_HOST)


def _flight_port_factory() -> int:
    return int(os.getenv(ENV_FLIGHT_PORT, DEFAULT_FLIGHT_PORT))


def _flight_scheme_factory() -> str:
    return os.getenv(
        ENV_FLIGHT_TRANSPORT_SCHEME, DEFAULT_FLIGHT_TRANSPORT_SCHEME
    )


def _mask_secret(secret: str, N: int = 4) -> str:
    """Show first N chars then '***'; empty string if empty."""
    return f"{secret[:N]}***"


def _endpoint(scheme: str, base: str, path: str) -> str:
    return scheme + "://" + base.rstrip("/") + "/" + path.lstrip("/")


@dataclass(frozen=True)
class SDKConfiguration:
    api_key: str = field(default_factory=_api_key_factory)
    api_host: str = field(default_factory=_api_host_factory)
    api_scheme: str = field(default_factory=_api_scheme_factory)
    flight_server_host: str = field(default_factory=_flight_host_factory)
    flight_server_port: int = field(default_factory=_flight_port_factory)
    flight_scheme: str = field(default_factory=_flight_scheme_factory)
    request_verify: bool | str = True

    # Private, excluded from comparisons & repr
    _headers: Dict[str, str] = field(init=False, repr=False, compare=False)
    _gen_client: Any = field(default=None, repr=False, compare=False)
    _gen_lock: threading.Lock = field(
        default_factory=threading.Lock, repr=False, compare=False
    )

    def __post_init__(self):
        # Validate Configuration
        if not self.api_key:
            raise MissingAPIKeyError()

    @property
    def files_url(self) -> str:
        return _endpoint(self.api_scheme, self.api_host, "/v1/pandas_arrow")

    @property
    def headers(self) -> Dict[str, str]:
        # Create base headers
        return {
            "authorization": self.api_key,
            "sdk-language": "python",
            "language-version": get_python_version(),
            "sdk-version": __version__,
            # "arize-space-id": self._space_id,
            # "arize-interface": "batch",
            # "sync": "0",  # Defaults to async logging
        }

    def __repr__(self) -> str:
        # Dynamically build repr for all fields
        parts = []
        for f in fields(self):
            if not f.repr:
                continue
            val = getattr(self, f.name)
            if f.name == "api_key":
                val = _mask_secret(val, 6)
            parts.append(f"{f.name}={val!r}")
        return f"{self.__class__.__name__}({', '.join(parts)})"

    # TODO(Kiko): This may not be well placed in this class
    def get_generated_client(self):
        # If already cached, return immediately
        if self._gen_client is not None:
            return self._gen_client

        # Thread-safe initialization
        with self._gen_lock:
            if self._gen_client is not None:
                return self._gen_client

            # Import lazily so extras can be enforced outside
            from arize._generated import api_client as gen

            cfg = gen.Configuration(host=self.api_host)
            if self.api_key:
                cfg.api_key["ApiKeyAuth"] = self.api_key
            client = gen.ApiClient(cfg)

            # Bypass frozen to set the cache once
            object.__setattr__(self, "_gen_client", client)
            return client


def get_python_version():
    return (
        f"{sys.version_info.major}.{sys.version_info.minor}."
        f"{sys.version_info.micro}"
    )
