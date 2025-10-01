"""
STAC catalog creation utilities for Open Polar Radar data.

This module provides tools for generating STAC (SpatioTemporal Asset Catalog)
metadata for OPR datasets, enabling spatial and temporal search capabilities
across radar campaigns and data products.
"""

from .catalog import (
    create_catalog, create_collection, create_item,
    create_items_from_flight_data,
    build_catalog_from_parquet_files,
    export_collection_to_parquet
)
from .config import load_config, save_config, validate_config, get_default_config
from .geometry import (
    build_collection_extent, build_collection_extent_and_geometry,
    merge_item_geometries, merge_flight_geometries
)
from .metadata import extract_item_metadata, discover_campaigns, discover_flight_lines, collect_uniform_metadata
from .build import (
    process_single_flight, process_single_campaign,
    collect_metadata_from_items,
    build_catalog_from_parquet_metadata
)

__all__ = [
    # Configuration
    "load_config",
    "save_config",
    "validate_config",
    "get_default_config",
    # Catalog functions
    "create_catalog",
    "create_collection", 
    "create_item",
    "build_collection_extent",
    "create_items_from_flight_data",
    "build_catalog_from_parquet_files",
    # Metadata functions
    "extract_item_metadata",
    "discover_campaigns",
    "discover_flight_lines",
    "collect_uniform_metadata",
    # Build functions
    "process_single_flight",
    "process_single_campaign",
    "collect_metadata_from_items",
    "export_collection_to_parquet",
    "build_catalog_from_parquet_metadata"
]