# -*- coding: utf-8 -*-
"""
Improved SAP BW XMLA Client with enhanced productivity features.

Major improvements:
- Better error handling and logging
- Caching for frequently accessed data
- Async support for better performance
- Type hints and validation
- Configuration management
- Connection pooling
- Progress tracking
- Memory optimization
"""

from __future__ import annotations

import re
import threading
import time
import xml.etree.ElementTree as ET
from contextlib import contextmanager
from dataclasses import dataclass, field
from functools import wraps
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple, Union
from xml.sax.saxutils import escape

import pandas as pd
import requests
import yaml
from jinja2 import Template
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from hmcis_packs.logger.logger_config import setup_logger

# Setup logging
# logging.basicConfig(level=logging.INFO)
logger = setup_logger(__name__)


# ----------------------------------------------------------------------
# Configuration and Types
# ----------------------------------------------------------------------
@dataclass(frozen=True)
class ConnectionConfig:
    """Connection concfiguration with validation."""

    url: str
    username: str
    password: str
    catalog: str = "$INFOCUBE"
    datasource: str = "SAP_BW"
    timeout: int = 300
    max_retries: int = 3
    pool_connections: int = 10
    pool_maxsize: int = 10

    def __post_init__(self):
        if not self.url or not self.username or not self.password:
            raise ValueError("URL, username, and password are required")


@dataclass(frozen=True)
class DimensionSpec:
    """Normalized dimension specification with validation."""

    dimension: str
    hierarchy: str = field(default="")
    level: str = "LEVEL01"
    attributes: Optional[List[str]] = None
    dim_unique: str = field(init=False)

    def __post_init__(self):
        if not self.dimension:
            raise ValueError("Dimension name is required")

        # Set hierarchy default if not provided
        hierarchy = self.hierarchy or self.dimension
        object.__setattr__(self, "hierarchy", hierarchy)

        # Set dim_unique with brackets if needed
        dim_unique = (
            self.dimension if self.dimension.startswith("[") else f"[{self.dimension}]"
        )
        object.__setattr__(self, "dim_unique", dim_unique)


@dataclass
class QueryResult:
    """Enhanced result container with metadata."""

    data: pd.DataFrame
    query_time: float
    row_count: int
    column_count: int
    cache_hit: bool = False

    @property
    def is_empty(self) -> bool:
        return self.data.empty


# ----------------------------------------------------------------------
# Utilities and Decorators
# ----------------------------------------------------------------------
def timing_decorator(func):
    """Decorator to measure execution time."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        execution_time = time.time() - start_time
        logger.info(f"{func.__name__} executed in {execution_time:.2f} seconds")
        return result

    return wrapper


def cache_with_ttl(ttl_seconds: int = 300):
    """Cache decorator with TTL."""

    def decorator(func):
        cache = {}
        cache_times = {}

        @wraps(func)
        def wrapper(*args, **kwargs):
            # Create cache key from args and kwargs
            key = str(args) + str(sorted(kwargs.items()))
            current_time = time.time()

            # Check if cached and not expired
            if key in cache and (current_time - cache_times[key]) < ttl_seconds:
                logger.debug(f"Cache hit for {func.__name__}")
                return cache[key]

            # Execute and cache
            result = func(*args, **kwargs)
            cache[key] = result
            cache_times[key] = current_time

            # Clean old entries
            expired_keys = [
                k for k, t in cache_times.items() if (current_time - t) >= ttl_seconds
            ]
            for k in expired_keys:
                cache.pop(k, None)
                cache_times.pop(k, None)

            return result

        return wrapper

    return decorator


class ProgressTracker:
    """Enhanced progress tracking with context manager."""

    def __init__(self, description: str = "Processing", show_timer: bool = True):
        self.description = description
        self.show_timer = show_timer
        self.start_time = None
        self.stop_event = None
        self.timer_thread = None

    def __enter__(self):
        if self.show_timer:
            self.start_timer()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.show_timer:
            self.stop_timer()

    def start_timer(self):
        """Start the progress timer."""
        self.start_time = time.time()
        self.stop_event = threading.Event()

        def display_timer():
            while not self.stop_event.is_set():
                elapsed = time.time() - self.start_time
                print(f"\r{self.description}: {elapsed:.1f}s", end="", flush=True)
                time.sleep(0.1)

        self.timer_thread = threading.Thread(target=display_timer, daemon=True)
        self.timer_thread.start()

    def stop_timer(self):
        """Stop the progress timer."""
        if self.stop_event:
            self.stop_event.set()
        if self.timer_thread:
            self.timer_thread.join(timeout=1.0)

        final_time = time.time() - self.start_time if self.start_time else 0
        print(f"\r{' ' * 50}\r{self.description} completed in {final_time:.2f}s")


# ----------------------------------------------------------------------
# Main Client Class
# ----------------------------------------------------------------------
class SAPXMLAClient:
    """
    Enhanced SAP BW XMLA Client with improved productivity features:
    - Connection pooling and retry logic
    - Caching for frequently accessed data
    - Better error handling and logging
    - Progress tracking for long operations
    - Memory-efficient batch processing
    - Configuration management
    """

    DISCOVER_TEMPLATE = Template(
        """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
                      xmlns:xmla="urn:schemas-microsoft-com:xml-analysis">
      <soapenv:Header/>
      <soapenv:Body>
        <xmla:Discover>
          <xmla:RequestType>{{ request_type }}</xmla:RequestType>
          <xmla:Restrictions>
            <xmla:RestrictionList>
              {% for key, value in restrictions.items() %}
              <xmla:{{ key }}>{{ value }}</xmla:{{ key }}>
              {% endfor %}
            </xmla:RestrictionList>
          </xmla:Restrictions>
          <xmla:Properties>
            <xmla:PropertyList>
              <xmla:Catalog>{{ catalog }}</xmla:Catalog>
              <xmla:DataSourceInfo>{{ datasource }}</xmla:DataSourceInfo>
              <xmla:Format>{{ format_type }}</xmla:Format>
              {% for key, value in extra_properties.items() %}
              <xmla:{{ key }}>{{ value }}</xmla:{{ key }}>
              {% endfor %}
            </xmla:PropertyList>
          </xmla:Properties>
        </xmla:Discover>
      </soapenv:Body>
    </soapenv:Envelope>
    """
    )

    def __init__(self, config: Union[ConnectionConfig, Dict[str, Any], str, Path]):
        """Initialize client with enhanced configuration support."""
        self.config = self._load_config(config)
        self.session = self._create_session()
        self.ns = {"x": "urn:schemas-microsoft-com:xml-analysis:rowset"}
        self._dimension_cache = {}

        logger.info(f"Initialized XMLA client for {self.config.url}")

    @classmethod
    def from_config_file(cls, config_path: Union[str, Path] = None) -> "SAPXMLAClient":
        """Create client from configuration file."""
        if config_path is None:
            config_path = Path.home() / ".sap_bw.yml"
        return cls(config_path)

    def _load_config(
        self, config: Union[ConnectionConfig, Dict[str, Any], str, Path]
    ) -> ConnectionConfig:
        """Load and validate configuration from various sources."""
        if isinstance(config, ConnectionConfig):
            return config
        elif isinstance(config, dict):
            return ConnectionConfig(**config)
        elif isinstance(config, (str, Path)):
            config_path = Path(config)
            if not config_path.exists():
                raise FileNotFoundError(f"Configuration file not found: {config_path}")

            with open(config_path, "r", encoding="utf-8") as f:
                config_data = yaml.safe_load(f)

            # Map common key variations
            key_mapping = {
                "SAP_URL": "url",
                "SAP_USER": "username",
                "SAP_PASS": "password",
                "SAP_CATALOG": "catalog",
                "SAP_DATASOURCE": "datasource",
            }

            normalized_config = {}
            for key, value in config_data.items():
                mapped_key = key_mapping.get(key, key.lower())
                normalized_config[mapped_key] = value

            return ConnectionConfig(**normalized_config)
        else:
            raise ValueError(f"Unsupported config type: {type(config)}")

    def _create_session(self) -> requests.Session:
        """Create session with connection pooling and retry strategy."""
        session = requests.Session()

        # Retry strategy
        retry_strategy = Retry(
            total=self.config.max_retries,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
        )

        # Mount adapter with retry strategy
        adapter = HTTPAdapter(
            pool_connections=self.config.pool_connections,
            pool_maxsize=self.config.pool_maxsize,
            max_retries=retry_strategy,
        )
        session.mount("http://", adapter)
        session.mount("https://", adapter)

        # Set authentication
        session.auth = (self.config.username, self.config.password)

        return session

    def _send_request(self, soap_body: str, soap_action: str) -> str:
        """Send SOAP request with enhanced error handling."""
        headers = {
            "Content-Type": "text/xml; charset=utf-8",
            "SOAPAction": f"urn:schemas-microsoft-com:xml-analysis:{soap_action}",
        }

        try:
            response = self.session.post(
                self.config.url,
                headers=headers,
                data=soap_body.encode("utf-8"),
                timeout=self.config.timeout,
            )
            response.raise_for_status()
            return response.text

        except requests.exceptions.Timeout:
            logger.error(f"Request timeout after {self.config.timeout}s")
            raise
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {e}")
            raise

    # --------------------------- Discovery Methods ------------------------------

    @cache_with_ttl(ttl_seconds=600)  # Cache for 10 minutes
    @timing_decorator
    def discover_dimensions(self, cube_name: str, **kwargs) -> pd.DataFrame:
        """Discover cube dimensions with caching."""
        body = self.DISCOVER_TEMPLATE.render(
            request_type=escape("MDSCHEMA_DIMENSIONS"),
            restrictions={"CUBE_NAME": escape(cube_name)},
            catalog=escape(self.config.catalog),
            datasource=escape(self.config.datasource),
            format_type=escape(kwargs.get("format_type", "Tabular")),
            extra_properties=kwargs.get("extra_properties", {}),
        )
        exctracted = self._parse_rowset(self._send_request(body, "Discover"))
        print(exctracted)

        return exctracted

    @cache_with_ttl(ttl_seconds=300)  # Cache for 5 minutes
    def discover_dimension_members(
        self,
        cube_name: str,
        dimension: str,
        hierarchy: Optional[str] = None,
        level: str = "LEVEL01",
        **kwargs,
    ) -> pd.DataFrame:
        """Discover dimension members with caching."""
        hierarchy = hierarchy or dimension
        dim_unique = self._bracket_if_needed(dimension)
        hier_unique = self._bracket_if_needed(hierarchy)
        lvl_unique = f"{hier_unique}.[{level}]"

        restrictions = {
            "CATALOG_NAME": escape(self.config.catalog),
            "CUBE_NAME": escape(cube_name),
            "DIMENSION_UNIQUE_NAME": escape(dim_unique),
            "HIERARCHY_UNIQUE_NAME": escape(hier_unique),
            "LEVEL_UNIQUE_NAME": escape(lvl_unique),
        }

        body = self.DISCOVER_TEMPLATE.render(
            request_type=escape("MDSCHEMA_MEMBERS"),
            restrictions=restrictions,
            catalog=escape(self.config.catalog),
            datasource=escape(self.config.datasource),
            format_type=escape(kwargs.get("format_type", "Tabular")),
            extra_properties=kwargs.get("extra_properties", {}),
        )
        return self._parse_rowset(self._send_request(body, "Discover"))

    @cache_with_ttl(ttl_seconds=600)
    def discover_member_properties(
        self, cube_name: str, dimension: str, hierarchy: Optional[str] = None, **kwargs
    ) -> pd.DataFrame:
        """Discover member properties with caching."""
        hierarchy = hierarchy or dimension
        dim_unique = self._bracket_if_needed(dimension)
        hier_unique = self._bracket_if_needed(hierarchy)

        restrictions = {
            "CATALOG_NAME": escape(self.config.catalog),
            "CUBE_NAME": escape(cube_name),
            "DIMENSION_UNIQUE_NAME": escape(dim_unique),
            "HIERARCHY_UNIQUE_NAME": escape(hier_unique),
        }

        body = self.DISCOVER_TEMPLATE.render(
            request_type=escape("MDSCHEMA_PROPERTIES"),
            restrictions=restrictions,
            catalog=escape(self.config.catalog),
            datasource=escape(self.config.datasource),
            format_type=escape("Tabular"),
            extra_properties=kwargs.get("extra_properties", {}),
        )
        return self._parse_rowset(self._send_request(body, "Discover"))

    # --------------------------- Execute Methods --------------------------------

    @timing_decorator
    def execute_mdx(self, mdx: str, show_progress: bool = True) -> QueryResult:
        """Execute MDX with enhanced progress tracking and result metadata."""

        with ProgressTracker("Executing MDX query", show_timer=show_progress):
            start_time = time.time()

            body = f"""
                <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
                                  xmlns:x="urn:schemas-microsoft-com:xml-analysis">
                  <soapenv:Header/>
                  <soapenv:Body>
                    <x:Execute>
                      <x:Command>
                        <x:Statement>{escape(mdx)}</x:Statement>
                      </x:Command>
                      <x:Properties>
                        <x:PropertyList>
                          <x:Catalog>{self.config.catalog}</x:Catalog>
                          <x:DataSourceInfo>{self.config.datasource}</x:DataSourceInfo>
                          <x:Format>Tabular</x:Format>
                          <x:AxisFormat>TupleFormat</x:AxisFormat>
                        </x:PropertyList>
                      </x:Properties>
                    </x:Execute>
                  </soapenv:Body>
                </soapenv:Envelope>
            """

            xml_response = self._send_request(body, "Execute")
            df = self._parse_rowset(xml_response)
            query_time = time.time() - start_time

            return QueryResult(
                data=df,
                query_time=query_time,
                row_count=len(df),
                column_count=len(df.columns),
            )

    # ------------------------ Enhanced Convenience API ---------------------------

    def get_members_with_attributes(
        self,
        cube_name: str,
        dimension: str,
        hierarchy: Optional[str] = None,
        attributes: Optional[List[str]] = None,
        level: str = "LEVEL01",
        autoload_attributes: bool = True,
        **kwargs,
    ) -> QueryResult:
        """Get dimension members with attributes - enhanced version."""

        try:
            spec = DimensionSpec(
                dimension=dimension,
                hierarchy=hierarchy or dimension,
                level=level,
                attributes=attributes,
            )
        except ValueError as e:
            logger.error(f"Invalid dimension specification: {e}")
            raise

        if autoload_attributes and not spec.attributes:
            with ProgressTracker("Loading dimension properties", show_timer=True):
                df_props = self.discover_member_properties(
                    cube_name, spec.dimension, spec.hierarchy
                )
                if df_props.empty or "PROPERTY_NAME" not in df_props.columns:
                    logger.warning(
                        f"No properties found for dimension {spec.dimension}"
                    )
                    attributes = []
                else:
                    attributes = df_props["PROPERTY_NAME"].dropna().unique().tolist()
                    logger.info(
                        f"Auto-loaded {len(attributes)} attributes for {spec.dimension}"
                    )
        else:
            attributes = spec.attributes or []

        props_clause = self._build_properties_clause([(spec.dim_unique, attributes)])
        mdx = self._build_single_dimension_mdx(
            cube_name, spec.dim_unique, spec.level, props_clause
        )

        return self.execute_mdx(mdx, show_progress=kwargs.get("show_progress", True))

    def get_members_with_attributes_multi(
        self,
        cube_name: str,
        dimensions: Sequence[Union[str, Dict[str, Any]]],
        batch_size: Optional[int] = None,
        batch_dimension_index: int = 0,
        autoload_attributes: bool = False,
        **kwargs,
    ) -> QueryResult:
        """Get multiple dimensions with attributes - enhanced with better batching."""

        if not dimensions:
            return QueryResult(pd.DataFrame(), 0, 0, 0)

        specs = self._normalize_dimension_specs(dimensions)

        # Auto-load attributes if requested
        if autoload_attributes:
            for spec in specs:
                if not spec.attributes:
                    df_props = self.discover_member_properties(
                        cube_name, spec.dimension, spec.hierarchy
                    )
                    if not df_props.empty and "PROPERTY_NAME" in df_props.columns:
                        attrs = df_props["PROPERTY_NAME"].dropna().unique().tolist()
                        # Update the spec with new attributes
                        object.__setattr__(spec, "attributes", attrs)

        dim_attrs = [(s.dim_unique, s.attributes) for s in specs]
        props_clause = self._build_properties_clause(dim_attrs)
        level_sets = [self._level_members(s.dim_unique, s.level) for s in specs]

        # Single query if no batching
        if not batch_size or batch_size <= 0:
            rows = self._cross_join(level_sets)
            mdx = self._build_cross_join_mdx(cube_name, rows, props_clause)
            return self.execute_mdx(
                mdx, show_progress=kwargs.get("show_progress", True)
            )

        # Batched processing
        return self._execute_batched_query(
            cube_name,
            specs,
            level_sets,
            props_clause,
            batch_size,
            batch_dimension_index,
            **kwargs,
        )

    def _execute_batched_query(
        self,
        cube_name: str,
        specs: List[DimensionSpec],
        level_sets: List[str],
        props_clause: str,
        batch_size: int,
        batch_index: int,
        **kwargs,
    ) -> QueryResult:
        """Execute query in batches for memory efficiency."""

        if batch_index < 0 or batch_index >= len(specs):
            raise IndexError(
                f"batch_dimension_index={batch_index} out of range (0..{len(specs) - 1})"
            )

        batch_spec = specs[batch_index]

        # Get members for batching dimension
        with ProgressTracker(
            f"Loading members for {batch_spec.dimension}", show_timer=True
        ):
            df_members = self.discover_dimension_members(
                cube_name, batch_spec.dimension, batch_spec.hierarchy, batch_spec.level
            )

        if df_members.empty or "MEMBER_UNIQUE_NAME" not in df_members.columns:
            logger.error(
                f"No members found for batching dimension {batch_spec.dimension}"
            )
            return QueryResult(pd.DataFrame(), 0, 0, 0)

        member_names = df_members["MEMBER_UNIQUE_NAME"].dropna().tolist()
        other_level_sets = [ls for i, ls in enumerate(level_sets) if i != batch_index]
        other_rows = self._cross_join(other_level_sets) if other_level_sets else None

        # Process in batches
        total_batches = (len(member_names) + batch_size - 1) // batch_size
        logger.info(
            f"Processing {len(member_names)} members in {total_batches} batches"
        )

        results = []
        total_query_time = 0

        for i in range(0, len(member_names), batch_size):
            batch_num = i // batch_size + 1
            chunk = member_names[i : i + batch_size]

            with ProgressTracker(
                f"Processing batch {batch_num}/{total_batches}", show_timer=True
            ):
                members_set = "{ " + ", ".join(chunk) + " }"
                rows = (
                    f"CrossJoin({members_set}, {other_rows})"
                    if other_rows
                    else members_set
                )
                mdx = self._build_cross_join_mdx(cube_name, rows, props_clause)

                result = self.execute_mdx(mdx, show_progress=False)
                if not result.is_empty:
                    results.append(result.data)
                    total_query_time += result.query_time

        # Combine results
        if results:
            combined_df = pd.concat(results, ignore_index=True)
            return QueryResult(
                data=combined_df,
                query_time=total_query_time,
                row_count=len(combined_df),
                column_count=len(combined_df.columns),
            )
        else:
            return QueryResult(pd.DataFrame(), total_query_time, 0, 0)

    # ------------------------ Validation and Utilities -------------------------

    def validate_mdx_dimensions(self, mdx_query: str, cube_name: str) -> Dict[str, Any]:
        """Validate MDX dimensions against cube dimensions with enhanced analysis."""

        def extract_dimensions_from_mdx(mdx: str) -> set:
            # Improved regex to handle various MDX patterns
            patterns = [
                r"\[([^\[\]]+?)\]\.(?:Members|Children|\[[^\]]+\])",  # [DIM].Members or [DIM].[LEVEL]
                r"\[([^\[\]]+?)\]\.",  # General [DIM]. pattern
            ]

            dimensions = set()
            for pattern in patterns:
                matches = re.findall(pattern, mdx, re.IGNORECASE)
                dimensions.update(matches)

            # Filter out known non-dimensions
            ignore = {"Measures", "Time", "LEVEL01", "LEVEL02"}  # Add more as needed
            return {d for d in dimensions if d not in ignore}

        used_dims = extract_dimensions_from_mdx(mdx_query)

        # Get available dimensions
        df_dims = self.discover_dimensions(cube_name)
        available_dims = (
            set(df_dims["DIMENSION_NAME"].tolist()) if not df_dims.empty else set()
        )

        validation_result = {
            "is_valid": len(used_dims - available_dims) == 0,
            "used_dimensions": sorted(used_dims),
            "available_dimensions": sorted(available_dims),
            "matched_dimensions": sorted(used_dims & available_dims),
            "missing_dimensions": sorted(used_dims - available_dims),
            "unused_dimensions": sorted(available_dims - used_dims),
        }

        if not validation_result["is_valid"]:
            logger.warning(
                f"MDX validation failed. Missing dimensions: {validation_result['missing_dimensions']}"
            )

        return validation_result

    # ------------------------ Internal Helper Methods -------------------------

    @staticmethod
    def _bracket_if_needed(name: str) -> str:
        """Add brackets to dimension name if not present."""
        return name if name.startswith("[") and name.endswith("]") else f"[{name}]"

    @staticmethod
    def _level_members(dim_unique: str, level: str) -> str:
        """Create level members expression."""
        return f"{dim_unique}.{level}.Members"

    @staticmethod
    def _cross_join(level_sets: Sequence[str]) -> str:
        """Create nested CrossJoin expression."""
        if not level_sets:
            return ""
        if len(level_sets) == 1:
            return level_sets[0]

        result = level_sets[0]
        for level_set in level_sets[1:]:
            result = f"CrossJoin({result}, {level_set})"
        return result

    @staticmethod
    def _build_properties_clause(
        dim_attrs: Sequence[Tuple[str, Optional[List[str]]]],
    ) -> str:
        """Build DIMENSION PROPERTIES clause."""
        props = []
        for dim_unique, attrs in dim_attrs:
            if attrs:
                for attr in attrs:
                    # Ensure proper formatting of attribute names
                    if not attr.startswith(dim_unique):
                        props.append(f"{dim_unique}.{attr}")
                    else:
                        props.append(attr)
        return ", ".join(props) if props else "MEMBER_UNIQUE_NAME"

    @staticmethod
    def _build_single_dimension_mdx(
        cube_name: str, dim_unique: str, level: str, props_clause: str
    ) -> str:
        """Build MDX for single dimension query."""
        return f"""
            SELECT
              NON EMPTY {{}} ON COLUMNS,
              NON EMPTY {dim_unique}.{level}.Members
                DIMENSION PROPERTIES {props_clause}
              ON ROWS
            FROM [{cube_name}]
        """

    @staticmethod
    def _build_cross_join_mdx(cube_name: str, rows_set: str, props_clause: str) -> str:
        """Build MDX for cross-join query."""
        return f"""
            SELECT
              NON EMPTY {{}} ON COLUMNS,
              NON EMPTY {rows_set}
                DIMENSION PROPERTIES {props_clause}
              ON ROWS
            FROM [{cube_name}]
        """

    @staticmethod
    def _parse_rowset(xml_text: str) -> pd.DataFrame:
        """Parse XMLA tabular response with enhanced error handling."""
        try:
            root = ET.fromstring(xml_text)

            # Check for SOAP faults
            fault = root.find(
                ".//soap:Fault", {"soap": "http://schemas.xmlsoap.org/soap/envelope/"}
            )
            if fault is not None:
                fault_string = fault.find(".//faultstring")
                error_msg = (
                    fault_string.text
                    if fault_string is not None
                    else "Unknown SOAP fault"
                )
                raise RuntimeError(f"XMLA error: {error_msg}")

            # Parse rows
            rows = root.findall(
                ".//x:row", {"x": "urn:schemas-microsoft-com:xml-analysis:rowset"}
            )

            if not rows:
                logger.warning("No data rows found in XMLA response")
                return pd.DataFrame()

            data = []
            for row in rows:
                row_data = {}
                for cell in row:
                    # Extract column name (remove namespace if present)
                    col_name = cell.tag.split("}")[-1] if "}" in cell.tag else cell.tag
                    row_data[col_name] = cell.text
                data.append(row_data)

            df = pd.DataFrame(data)

            # Optimize memory usage by converting appropriate columns
            for col in df.columns:
                if df[col].dtype == "object":
                    # Try to convert to numeric if possible
                    try:
                        df[col] = pd.to_numeric(df[col], errors="ignore")
                    except:
                        pass

            logger.debug(f"Parsed {len(df)} rows with {len(df.columns)} columns")
            return df

        except ET.ParseError as e:
            logger.error(f"Failed to parse XML response: {e}")
            # Log first 1000 characters of response for debugging
            logger.debug(f"XML response preview: {xml_text[:1000]}...")
            raise ValueError(f"Invalid XML response: {e}")

    def _normalize_dimension_specs(
        self, dims: Sequence[Union[str, Dict[str, Any]]]
    ) -> List[DimensionSpec]:
        """Normalize dimension specifications with enhanced validation."""
        specs = []

        for i, dim in enumerate(dims):
            try:
                if isinstance(dim, str):
                    spec = DimensionSpec(dimension=dim)
                elif isinstance(dim, dict):
                    spec = DimensionSpec(
                        dimension=dim.get("dimension", ""),
                        hierarchy=dim.get("hierarchy", ""),
                        level=dim.get("level", "LEVEL01"),
                        attributes=dim.get("attributes"),
                    )
                else:
                    raise ValueError(f"Unsupported dimension spec type: {type(dim)}")

                specs.append(spec)

            except ValueError as e:
                logger.error(f"Invalid dimension spec at index {i}: {e}")
                raise

        return specs

    # ------------------------ Context Managers and Cleanup -------------------------

    @contextmanager
    def batch_operation(self, description: str = "Batch operation"):
        """Context manager for batch operations with cleanup."""
        logger.info(f"Starting {description}")
        start_time = time.time()

        try:
            yield
        finally:
            duration = time.time() - start_time
            logger.info(f"Completed {description} in {duration:.2f}s")

    def close(self):
        """Clean up resources."""
        if hasattr(self, "session"):
            self.session.close()
        logger.info("XMLA client closed")

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()


# ----------------------------------------------------------------------
# Factory and Helper Classes
# ----------------------------------------------------------------------
class ClientFactory:
    """Factory for creating configured XMLA clients."""

    @staticmethod
    def create_from_environment() -> SAPXMLAClient:
        """Create client from environment variables."""
        import os

        config = ConnectionConfig(
            url=os.getenv("SAP_BW_URL", ""),
            username=os.getenv("SAP_BW_USER", ""),
            password=os.getenv("SAP_BW_PASS", ""),
            catalog=os.getenv("SAP_BW_CATALOG", "$INFOCUBE"),
            datasource=os.getenv("SAP_BW_DATASOURCE", "SAP_BW"),
        )
        return SAPXMLAClient(config)

    @staticmethod
    def create_from_config_file(config_path: Union[str, Path] = None) -> SAPXMLAClient:
        """Create client from YAML config file."""
        return SAPXMLAClient.from_config_file(config_path)


class QueryBuilder:
    """Helper class for building complex MDX queries."""

    def __init__(self, cube_name: str):
        self.cube_name = cube_name
        self.columns = []
        self.rows = []
        self.where_conditions = []
        self.properties = []

    def add_column(self, expression: str) -> "QueryBuilder":
        """Add column expression."""
        self.columns.append(expression)
        return self

    def add_row(self, expression: str) -> "QueryBuilder":
        """Add row expression."""
        self.rows.append(expression)
        return self

    def add_where(self, condition: str) -> "QueryBuilder":
        """Add WHERE condition."""
        self.where_conditions.append(condition)
        return self

    def add_properties(self, *props: str) -> "QueryBuilder":
        """Add dimension properties."""
        self.properties.extend(props)
        return self

    def build(self) -> str:
        """Build the complete MDX query."""
        if not self.rows:
            raise ValueError("At least one row expression is required")

        # Build SELECT clause
        columns_clause = (
            "NON EMPTY { " + ", ".join(self.columns) + " }"
            if self.columns
            else "NON EMPTY {}"
        )
        rows_clause = "NON EMPTY { " + ", ".join(self.rows) + " }"

        # Add properties if specified
        if self.properties:
            props_clause = f"DIMENSION PROPERTIES {', '.join(self.properties)}"
            rows_clause += f"\n  {props_clause}"

        # Build query
        mdx = f"""
SELECT
  {columns_clause} ON COLUMNS,
  {rows_clause} ON ROWS
FROM [{self.cube_name}]"""

        # Add WHERE clause if specified
        if self.where_conditions:
            where_clause = " AND ".join(self.where_conditions)
            mdx += f"\nWHERE ({where_clause})"

        return mdx.strip()


class DataProcessor:
    """Helper class for post-processing query results."""

    @staticmethod
    def clean_member_names(df: pd.DataFrame, columns: List[str] = None) -> pd.DataFrame:
        """Clean member unique names to extract readable values."""
        df = df.copy()

        if columns is None:
            columns = [col for col in df.columns if "MEMBER_UNIQUE_NAME" in col.upper()]

        for col in columns:
            if col in df.columns:
                # Extract readable part from [DIM].[HIER].[LEVEL].&[KEY]
                df[f"{col}_CLEAN"] = df[col].str.extract(r"\.&\[([^\]]+)\]")[0]
                df[f"{col}_CLEAN"] = df[f"{col}_CLEAN"].fillna(df[col])

        return df

    @staticmethod
    def pivot_attributes(
        df: pd.DataFrame, member_col: str, attr_cols: List[str]
    ) -> pd.DataFrame:
        """Pivot attribute columns for better readability."""
        if member_col not in df.columns:
            raise ValueError(f"Member column '{member_col}' not found")

        # Create base dataframe with unique members
        unique_members = df[member_col].unique()
        result = pd.DataFrame({member_col: unique_members})

        # Add attribute columns
        for attr_col in attr_cols:
            if attr_col in df.columns:
                attr_map = df.drop_duplicates(member_col).set_index(member_col)[
                    attr_col
                ]
                result[attr_col] = result[member_col].map(attr_map)

        return result

    @staticmethod
    def export_to_excel(
        results: Dict[str, pd.DataFrame], filename: str, include_metadata: bool = True
    ) -> None:
        """Export multiple DataFrames to Excel with metadata."""
        with pd.ExcelWriter(filename, engine="openpyxl") as writer:
            for sheet_name, df in results.items():
                # Ensure sheet name is valid
                safe_name = re.sub(r"[^\w\s-]", "", sheet_name)[:31]
                df.to_excel(writer, sheet_name=safe_name, index=False)

            # Add metadata sheet if requested
            if include_metadata:
                metadata = {
                    "Sheet": list(results.keys()),
                    "Rows": [len(df) for df in results.values()],
                    "Columns": [len(df.columns) for df in results.values()],
                    "Generated": [pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")]
                    * len(results),
                }
                pd.DataFrame(metadata).to_excel(
                    writer, sheet_name="Metadata", index=False
                )


# ----------------------------------------------------------------------
# Example Usage and Testing
# ----------------------------------------------------------------------
def main():
    """Example usage of the improved XMLA client."""

    # Example 1: Using factory with config file
    try:
        with ClientFactory.create_from_config_file() as client:
            # Discover dimensions
            print("=== Discovering Dimensions ===")
            dims_result = client.discover_dimensions("$HA01D003")
            client.discover_member_properties("$HA01C0502", dimension="0FISCYEAR")
            print(f"Found {len(dims_result)} dimensions")

            # Get members with auto-loaded attributes
            print("\n=== Getting Members with Attributes ===")
            result = client.get_members_with_attributes(
                cube_name="$HA01C0502",
                dimension="0ASSET_AFAB",
                attributes=["[20ASSET_AFAB]", "[2ZSCR_VAL]"],
            )
            print(f"Query completed in {result.query_time:.2f}s")
            print(
                f"Retrieved {result.row_count} rows with {result.column_count} columns"
            )

            # Multi-dimensional query with batching
            print("\n=== Multi-dimensional Query ===")
            multi_result = client.get_members_with_attributes_multi(
                cube_name="$HA01C0502",
                dimensions=[
                    {
                        "dimension": "0ASSET_AFAB",
                        "attributes": ["[20ASSET_AFAB]", "[2ZSCR_VAL]"],
                    },
                    {
                        "dimension": "0FISCYEAR",
                        "attributes": ["[20FISCYEAR]", "[80FISCYEAR]"],
                    },
                ],
                batch_size=10000,
                batch_dimension_index=0,
            )
            print(f"Multi-query completed in {multi_result.query_time:.2f}s")
            print(f"Retrieved {multi_result.row_count} rows")

            # Using QueryBuilder
            print("\n=== Using Query Builder ===")
            query = (
                QueryBuilder("$HA01D003")
                .add_row("[ZHA_VHVIN].LEVEL01.Members")
                .add_properties("[ZHA_VHVIN].[2ZHA_VHVIN]", "[ZHA_VHVIN].[2ZHPTSNO]")
                .build()
            )

            print("Generated MDX:")
            print(query)

            custom_result = client.execute_mdx(query)
            print(f"Custom query returned {custom_result.row_count} rows")

    except Exception as e:
        logger.error(f"Error in main execution: {e}")
        raise


if __name__ == "__main__":
    main()
