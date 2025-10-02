import asyncio
from typing import TypedDict

import ibis.expr.datatypes as dt
from ibis.common.exceptions import TableNotFound

from planar.data.connection import _get_connection
from planar.data.dataset import PlanarDataset
from planar.data.exceptions import DatasetNotFoundError
from planar.logging import get_logger

logger = get_logger(__name__)


# TODO: consider connection pooling or memoize the connection


async def list_datasets(limit: int = 100, offset: int = 0) -> list[PlanarDataset]:
    conn = await _get_connection()
    tables = await asyncio.to_thread(conn.list_tables)
    return [PlanarDataset(name=table) for table in tables]


async def list_schemas() -> list[str]:
    METADATA_SCHEMAS = [
        "information_schema",
        # FIXME: why is list_databases returning pg_catalog
        # if the ducklake catalog is sqlite?
        "pg_catalog",
    ]

    conn = await _get_connection()

    # in ibis, "databases" are schemas in the traditional sense
    # e.g. psql: schema == ibis: database
    # https://ibis-project.org/concepts/backend-table-hierarchy
    schemas = await asyncio.to_thread(conn.list_databases)

    return [schema for schema in schemas if schema not in METADATA_SCHEMAS]


async def get_dataset(dataset_name: str, schema_name: str = "main") -> PlanarDataset:
    # TODO: add schema_name as a parameter

    dataset = PlanarDataset(name=dataset_name)

    if not await dataset.exists():
        raise DatasetNotFoundError(f"Dataset {dataset_name} not found")

    return dataset


async def get_dataset_row_count(dataset_name: str) -> int:
    conn = await _get_connection()

    try:
        value = await asyncio.to_thread(
            lambda conn, dataset_name: conn.table(dataset_name).count().to_polars(),
            conn,
            dataset_name,
        )

        assert isinstance(value, int), "Scalar must be an integer"

        return value
    except TableNotFound:
        raise  # re-raise the exception and allow the caller to handle it


class DatasetMetadata(TypedDict):
    schema: dict[str, dt.DataType]
    row_count: int


async def get_dataset_metadata(
    dataset_name: str, schema_name: str
) -> DatasetMetadata | None:
    conn = await _get_connection()

    try:
        schema, row_count = await asyncio.gather(
            asyncio.to_thread(conn.get_schema, dataset_name, database=schema_name),
            get_dataset_row_count(dataset_name),
        )

        return DatasetMetadata(schema=schema.fields, row_count=row_count)

    except TableNotFound:
        return None
