from typing import Any, Dict

import pyarrow as pa

from arize.logging import log_a_list


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
            f"There are conflicting keys: {
                log_a_list(conflicting_keys, join_word='and')
            }"
        )

    updated_metadata = metadata.copy()
    updated_metadata.update(new_metadata)
    return pa_schema.with_metadata(updated_metadata)


def write_arrow_file(
    path: str, pa_table: pa.Table, pa_schema: pa.Schema
) -> None:
    with pa.OSFile(path, mode="wb") as sink, pa.ipc.RecordBatchStreamWriter(
        sink, pa_schema
    ) as writer:
        writer.write_table(pa_table, max_chunksize=16384)
