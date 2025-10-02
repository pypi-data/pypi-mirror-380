import asyncio

import ibis
from ibis.backends.duckdb import Backend as DuckDBBackend

from planar.config import PlanarConfig
from planar.data.config import (
    DuckDBCatalogConfig,
    PostgresCatalogConfig,
    SQLiteCatalogConfig,
)
from planar.data.exceptions import DataError
from planar.files.storage.config import LocalDirectoryConfig, S3Config
from planar.logging import get_logger
from planar.session import get_config

logger = get_logger(__name__)


async def _create_connection(config: PlanarConfig) -> DuckDBBackend:
    """Create Ibis DuckDB connection with Ducklake."""
    data_config = config.data
    if not data_config:
        raise DataError("Data configuration not found")

    # Connect to DuckDB with Ducklake extension
    con = await asyncio.to_thread(ibis.duckdb.connect, extensions=["ducklake"])

    # Build Ducklake connection string based on catalog type
    catalog_config = data_config.catalog

    match catalog_config:
        case DuckDBCatalogConfig():
            metadata_path = catalog_config.path
        case PostgresCatalogConfig():
            # Use connection components to build postgres connection string
            metadata_path = f"postgres:dbname={catalog_config.db}"
            if catalog_config.host:
                metadata_path += f" host={catalog_config.host}"
            if catalog_config.port:
                metadata_path += f" port={catalog_config.port}"
            if catalog_config.user:
                metadata_path += f" user={catalog_config.user}"
            if catalog_config.password:
                metadata_path += f" password={catalog_config.password}"
        case SQLiteCatalogConfig():
            metadata_path = f"sqlite:{catalog_config.path}"
        case _:
            raise ValueError(f"Unsupported catalog type: {catalog_config.type}")

    try:
        await asyncio.to_thread(con.raw_sql, "INSTALL ducklake")
        match catalog_config.type:
            case "sqlite":
                await asyncio.to_thread(con.raw_sql, "INSTALL sqlite;")
            case "postgres":
                await asyncio.to_thread(con.raw_sql, "INSTALL postgres;")
        logger.debug("installed Ducklake extensions", catalog_type=catalog_config.type)
    except Exception as e:
        raise DataError(f"Failed to install Ducklake extensions: {e}") from e

    # Build ATTACH statement
    attach_sql = f"ATTACH 'ducklake:{metadata_path}' AS planar_ducklake"

    # Add data path from storage config
    storage = data_config.storage
    if isinstance(storage, LocalDirectoryConfig):
        data_path = storage.directory
    elif isinstance(storage, S3Config):
        data_path = f"s3://{storage.bucket_name}/"
    else:
        # Generic fallback
        data_path = getattr(storage, "path", None) or getattr(storage, "directory", ".")

    ducklake_catalog = data_config.catalog_name
    attach_sql += f" (DATA_PATH '{data_path}'"
    if catalog_config.type != "sqlite":
        attach_sql += f", METADATA_SCHEMA '{ducklake_catalog}'"
    attach_sql += ");"

    # Attach to Ducklake
    try:
        await asyncio.to_thread(con.raw_sql, attach_sql)
    except Exception as e:
        raise DataError(f"Failed to attach to Ducklake: {e}") from e

    await asyncio.to_thread(con.raw_sql, "USE planar_ducklake;")
    logger.debug(
        "connection created",
        catalog=ducklake_catalog,
        catalog_type=catalog_config.type,
        attach_sql=attach_sql,
    )

    return con


async def _get_connection() -> DuckDBBackend:
    """Get Ibis connection to Ducklake."""
    config = get_config()

    if not config.data:
        raise DataError(
            "Data configuration not found. Please configure 'data' in your planar.yaml"
        )

    # TODO: Add cached connection pooling or memoize the connection
    return await _create_connection(config)
