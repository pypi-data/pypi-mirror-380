# src/arize/client.py
from __future__ import annotations

from typing import TYPE_CHECKING

from arize._lazy import LazySubclientsMixin
from arize.config import SDKConfiguration

if TYPE_CHECKING:
    from arize.datasets.client import DatasetsClient
    from arize.experiments.client import ExperimentsClient
    from arize.spans.client import SpansClient


# TODO(Kiko): ArizeFlightClient options
# TODO(Kiko): Go over docstrings
# TODO(Kiko): Missing a __repr__ method
class ArizeClient(LazySubclientsMixin):
    _SUBCLIENTS = {
        "datasets": ("arize.datasets.client", "DatasetsClient"),
        "experiments": ("arize.experiments.client", "ExperimentsClient"),
        "spans": ("arize.spans.client", "SpansClient"),
    }
    _EXTRAS = {
        # Gate only the generated-backed ones
        "datasets": (
            "datasets-experiments",
            ("pydantic",),
        ),
        "experiments": (
            "datasets-experiments",
            ("pydantic",),
        ),
        "spans": (
            "spans",
            (
                "numpy",
                "pyarrow",
                "pandas",
                "google.protobuf",
                "openinference.semconv",
                "opentelemetry",
            ),
        ),
    }

    def __init__(self, server_url: str = "", api_key: str = ""):
        cfg_kwargs = {}
        if server_url:
            cfg_kwargs["server_url"] = server_url
        if api_key:
            cfg_kwargs["api_key"] = api_key
        super().__init__(SDKConfiguration(**cfg_kwargs))

    # typed properties for IDE completion
    @property
    def datasets(self) -> DatasetsClient:
        return self.__getattr__("datasets")

    @property
    def experiments(self) -> ExperimentsClient:
        return self.__getattr__("experiments")

    @property
    def spans(self) -> SpansClient:
        return self.__getattr__("spans")
