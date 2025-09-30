# type: ignore[pb2]
from __future__ import annotations

import base64
from dataclasses import dataclass, field
from typing import Any, Dict, List, Tuple

import pyarrow as pa
from google.protobuf import json_format
from pyarrow import flight

from arize._flight.types import FlightRequestType
from arize._generated.protocol.flight.ingest_pb2 import (
    WriteSpanAnnotationResponse,
    WriteSpanAttributesMetadataResponse,
    WriteSpanEvaluationResponse,
)
from arize.config import get_python_version
from arize.constants.config import (
    DEFAULT_FLIGHT_HOST,
    DEFAULT_FLIGHT_PORT,
    DEFAULT_FLIGHT_TRANSPORT_SCHEME,
)
from arize.logging import log_a_list
from arize.utils.proto import get_pb_flight_doput_request, get_pb_schema_tracing
from arize.version import __version__

BytesPair = Tuple[bytes, bytes]
Headers = List[BytesPair]
WriteSpanResponse = (
    WriteSpanEvaluationResponse
    | WriteSpanAnnotationResponse
    | WriteSpanAttributesMetadataResponse
)


@dataclass(frozen=True)
class ArizeFlightClient:
    api_key: str = field(repr=False)
    host: str = DEFAULT_FLIGHT_HOST
    port: int = DEFAULT_FLIGHT_PORT
    scheme: str = DEFAULT_FLIGHT_TRANSPORT_SCHEME
    # otlp_endpoint: str = DEFAULT_ARIZE_OTLP_ENDPOINT
    # insecure: bool = False
    # developer_key: Optional[str] = None

    # internal cache for the underlying FlightClient
    _client: flight.FlightClient | None = field(
        default=None, init=False, repr=False
    )

    # ---------- Properties ----------

    @property
    def headers(self) -> Headers:
        # Keep the typing simple: (bytes, bytes)
        return [
            (b"origin", b"arize-logging-client"),
            (b"auth-token-bin", str(self.api_key).encode("utf-8")),
            (b"sdk-language", b"python"),
            (b"language-version", get_python_version().encode("utf-8")),
            (b"sdk-version", __version__.encode("utf-8")),
        ]

    @property
    def call_options(self) -> flight.FlightCallOptions:
        return flight.FlightCallOptions(headers=self.headers)

    # ---------- Connection management ----------

    def _ensure_client(self) -> flight.FlightClient:
        client = object.__getattribute__(self, "_client")
        if client is not None:
            return client

        # disable TLS verification for local dev on localhost
        disable_cert = self.host.lower() == "localhost"

        new_client = flight.FlightClient(
            location=f"{self.scheme}://{self.host}:{self.port}",
            disable_server_verification=disable_cert,
        )
        object.__setattr__(self, "_client", new_client)
        return new_client

    def close(self) -> None:
        client = object.__getattribute__(self, "_client")
        if client is not None:
            client.close()
            object.__setattr__(self, "_client", None)

    # ---------- Context manager ----------

    def __enter__(self) -> ArizeFlightClient:
        self._ensure_client()
        return self

    def __exit__(self, exc_type, exc_val, _) -> None:
        # if exc_type:
        #     logger.error(f"An exception occurred: {exc_val}")
        self.close()

    # ---------- do_put & do_action simple passthrough wrappers ----------

    def do_put(self, *args: Any, **kwargs: Any):
        client = self._ensure_client()
        kwargs.setdefault("options", self.call_options)
        return client.do_put(*args, **kwargs)

    def do_action(self, *args: Any, **kwargs: Any):
        client = self._ensure_client()
        kwargs.setdefault("options", self.call_options)
        return client.do_action(*args, **kwargs)

    # ---------- logging methods ----------

    def log_arrow_table(
        self,
        space_id: str,
        project_name: str,
        request_type: FlightRequestType,
        pa_table: pa.Table,
        verbose: bool = False,
    ) -> WriteSpanResponse:
        # print("Opening Flight client")
        # print(f"Flight server: {self.host}")
        # print(f"Flight port: {self.port}")
        # print(f"Flight scheme: {self.scheme}")
        # print(f"Space ID: {space_id}")
        # print(f"Project name: {project_name}")
        # print(" ")
        # print("Arrow table info:")
        # print("Num rows:", pa_table.num_rows)
        # print("Num columns:", pa_table.num_columns)
        # print("Schema:", pa_table.schema)
        # if pa_table.schema.metadata:
        #     print("Schema metadata:")
        #     for k, v in pa_table.schema.metadata.items():
        #         print(f"  {k!r}: {v!r}")
        # else:
        #     print("No schema metadata")
        # print("Columns:", pa_table.column_names)
        # for f in pa_table.schema:
        #     print(f"  {f.name}: {f.type}")
        # print("Preview:")
        # print(pa_table.to_pandas().head())  # Safe for small tables
        # print("Logging evaluations via Flight")
        # print(" ")
        # if verbose:
        #     logger.debug("Serializing schema.")

        proto_schema = get_pb_schema_tracing(project_name=project_name)
        # print(f"proto_schema={proto_schema}")
        base64_schema = base64.b64encode(proto_schema.SerializeToString())
        # print(f"base64_schema: {base64_schema}")
        pa_schema = append_to_pyarrow_metadata(
            pa_table.schema, {"arize-schema": base64_schema}
        )
        # # print("After appending metadata:")
        # if pa_schema.metadata:
        #     print("Schema metadata:")
        #     for k, v in pa_schema.metadata.items():
        #         print(f"  {k!r}: {v!r}")
        # else:
        #     print("No schema metadata")
        # # print(f"pa_schema={pa_schema}")

        doput_request = get_pb_flight_doput_request(
            space_id=space_id,
            model_id=project_name,
            request_type=request_type,
        )
        # print(f"doput_request={doput_request}")

        descriptor = flight.FlightDescriptor.for_command(
            json_format.MessageToJson(doput_request).encode("utf-8")
        )
        # print(" ")
        # print(f"Descriptor: {descriptor}")
        try:
            # print("CHECK 1")
            flight_writer, flight_metadata_reader = self.do_put(
                descriptor, pa_schema, options=self.call_options
            )
            # print(f"self._client: {self._client}")
            # print(f"call_options={self.call_options}")
            with flight_writer:
                # print("CHECK 2")
                # write table as stream to flight server
                flight_writer.write_table(pa_table)
                # indicate that client has flushed all contents to stream
                flight_writer.done_writing()
                # read response from flight server
                flight_response = flight_metadata_reader.read()
                if flight_response is None:
                    # print("CHECK RETURN NONE")
                    return None

                # print("CHECK 3")
                # print(f"flight_response: {flight_response}")
                res = None
                match request_type:
                    case FlightRequestType.EVALUATION:
                        # print("CHECK EVAL")
                        res = WriteSpanEvaluationResponse()
                        res.ParseFromString(flight_response.to_pybytes())
                    case FlightRequestType.ANNOTATION:
                        # print("CHECK ANNOT")
                        res = WriteSpanAnnotationResponse()
                        res.ParseFromString(flight_response.to_pybytes())
                    case FlightRequestType.METADATA:
                        # print("CHECK META")
                        res = WriteSpanAttributesMetadataResponse()
                        res.ParseFromString(flight_response.to_pybytes())
                        # print(f"Parsed response: {res}")
                    case _:
                        raise ValueError(
                            f"Unsupported request_type: {request_type}"
                        )
                # print("CHECK 4")
                # print(f"records_updated: {records_updated}")
                # print(f"res: {res}")

                return res
        except Exception as e:
            # logger.exception(f"Error logging {log_context} data to Arize")
            raise


def append_to_pyarrow_metadata(
    pa_schema: pa.Schema, new_metadata: Dict[str, Any]
):
    # Ensure metadata is handled correctly, even if initially None.
    metadata = pa_schema.metadata
    if metadata is None:
        # Initialize an empty dict if schema metadata was None
        metadata = {}

    conflicting_keys = metadata.keys() & new_metadata.keys()
    if conflicting_keys:
        raise KeyError(
            "Cannot append metadata to pyarrow schema. "
            f"There are conflicting keys: {log_a_list(conflicting_keys, join_word='and')}"
        )

    updated_metadata = metadata.copy()
    updated_metadata.update(new_metadata)
    return pa_schema.with_metadata(updated_metadata)
