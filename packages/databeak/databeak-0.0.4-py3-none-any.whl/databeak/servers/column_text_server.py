"""FastMCP server for text and string column operations.

This server provides specialized text manipulation operations for column data following DataBeak's
server composition architecture with direct implementations.
"""

from __future__ import annotations

import logging
import re
from typing import Annotated, Any, Literal

import pandas as pd
from fastmcp import Context, FastMCP
from fastmcp.exceptions import ToolError
from pydantic import BaseModel, Field

# Removed: OperationType (no longer tracking operations)
from databeak.core.session import DatabeakSession, get_session_data
from databeak.exceptions import (
    ColumnNotFoundError,
    InvalidParameterError,
    NoDataLoadedError,
    SessionNotFoundError,
)
from databeak.models.tool_responses import ColumnOperationResult

logger = logging.getLogger(__name__)

# Type aliases
CellValue = str | int | float | bool | None

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================


# Use defensive session access pattern with validation
def _get_session_data(session_id: str) -> tuple[DatabeakSession, pd.DataFrame]:
    """Get session and DataFrame with comprehensive validation."""
    return get_session_data(session_id)


# =============================================================================
# PYDANTIC MODELS FOR REQUEST PARAMETERS
# =============================================================================


class RegexPattern(BaseModel):
    """Regex pattern specification."""

    pattern: str = Field(description="Regular expression pattern")
    flags: list[Literal["IGNORECASE", "MULTILINE", "DOTALL"]] = Field(
        default_factory=list,
        description="Regex flags to apply",
    )


class SplitConfig(BaseModel):
    """Configuration for column splitting."""

    delimiter: str = Field(default=" ", description="String to split on")
    max_splits: int | None = Field(default=None, description="Maximum number of splits")
    expand: bool = Field(default=False, description="Expand into multiple columns")


# =============================================================================
# TOOL DEFINITIONS (Direct implementations for testing)
# =============================================================================


async def replace_in_column(
    ctx: Annotated[Context, Field(description="FastMCP context for session access")],
    column: Annotated[str, Field(description="Column name to apply pattern replacement in")],
    pattern: Annotated[str, Field(description="Pattern to search for (regex or literal string)")],
    replacement: Annotated[str, Field(description="Replacement text to use for matches")],
    *,
    regex: Annotated[
        bool,
        Field(description="Whether to treat pattern as regex (True) or literal string (False)"),
    ] = True,
) -> ColumnOperationResult:
    r"""Replace patterns in a column with replacement text.

    Returns:
        ColumnOperationResult with replacement details

    Examples:
        # Replace with regex
        replace_in_column(ctx, "name", r"Mr\.", "Mister")

        # Remove non-digits from phone numbers
        replace_in_column(ctx, "phone", r"\D", "", regex=True)

        # Simple string replacement
        replace_in_column(ctx, "status", "N/A", "Unknown", regex=False)

        # Replace multiple spaces with single space
        replace_in_column(ctx, "description", r"\s+", " ")

    """
    try:
        # Get session_id from FastMCP context
        session_id = ctx.session_id
        _session, df = get_session_data(session_id)

        if column not in df.columns:
            raise ColumnNotFoundError(column, df.columns.tolist())

        # Validate regex pattern if using regex mode
        if regex:
            try:
                re.compile(pattern)
            except re.error as e:
                msg = "pattern"
                raise InvalidParameterError(
                    msg,
                    pattern,
                    f"Invalid regex pattern: {e}",
                ) from e

        # Count replacements made
        original_data = df[column].copy()

        # Apply replacements
        if regex:
            df[column] = df[column].astype(str).str.replace(pattern, replacement, regex=True)
        else:
            df[column] = df[column].astype(str).str.replace(pattern, replacement, regex=False)

        # Count changes
        changed_mask = original_data.astype(str) != df[column].astype(str)
        changes_made = int(changed_mask.sum())

        return ColumnOperationResult(
            operation="replace_pattern",
            rows_affected=changes_made,
            columns_affected=[column],
        )

    except (
        SessionNotFoundError,
        NoDataLoadedError,
        ColumnNotFoundError,
        InvalidParameterError,
    ) as e:
        logger.exception("Replace in column failed: %s", e.message)
        raise ToolError(e.message) from e
    except Exception as e:
        logger.exception("Error replacing in column: %s", str(e))
        msg = f"Error replacing in column: {e}"
        raise ToolError(msg) from e


async def extract_from_column(
    ctx: Annotated[Context, Field(description="FastMCP context for session access")],
    column: Annotated[str, Field(description="Column name to extract patterns from")],
    pattern: Annotated[str, Field(description="Regex pattern with capturing groups to extract")],
    *,
    expand: Annotated[
        bool,
        Field(description="Whether to expand multiple groups into separate columns"),
    ] = False,
) -> ColumnOperationResult:
    r"""Extract patterns from a column using regex with capturing groups.

    Returns:
        ColumnOperationResult with extraction details

    Examples:
        # Extract email parts
        extract_from_column(ctx, "email", r"(.+)@(.+)")

        # Extract code components
        extract_from_column(ctx, "product_code", r"([A-Z]{2})-(\d+)")

        # Extract and expand into multiple columns
        extract_from_column(ctx, "full_name", r"(\w+)\s+(\w+)", expand=True)

        # Extract year from date string
        extract_from_column(ctx, "date", r"\d{4}")

    """
    try:
        # Get session_id from FastMCP context
        session_id = ctx.session_id
        session, df = get_session_data(session_id)

        if column not in df.columns:
            raise ColumnNotFoundError(column, df.columns.tolist())

        # Validate regex pattern
        try:
            re.compile(pattern)
        except re.error as e:
            msg = "pattern"
            raise InvalidParameterError(msg, pattern, f"Invalid regex pattern: {e}") from e

        # Apply extraction
        # Note: mypy has issues with overloaded extract method, but this is valid
        extracted = df[column].astype(str).str.extract(pattern, expand=expand)  # type: ignore[call-overload]

        if expand and isinstance(extracted, pd.DataFrame):
            # Multiple capturing groups - create new columns
            columns_created = []
            for i in range(len(extracted.columns)):
                new_col_name = f"{column}_extracted_{i}"
                if session.df is None:
                    msg = "Session data not available"
                    raise ToolError(msg)
                session.df[new_col_name] = extracted.iloc[:, i]
                columns_created.append(new_col_name)

            affected_columns = columns_created
            operation_desc = f"extract_expand_{len(columns_created)}_groups"
        else:
            # Single group or no expand - replace original column
            if isinstance(extracted, pd.DataFrame):
                # Multiple groups but not expanding - take first group
                if session.df is None:
                    msg = "Session data not available"
                    raise ToolError(msg)
                session.df[column] = extracted.iloc[:, 0]
            else:
                # Single series result
                if session.df is None:
                    msg = "Session data not available"
                    raise ToolError(msg)
                session.df[column] = extracted

            affected_columns = [column]
            operation_desc = "extract_pattern"

        # Count successful extractions (non-null results)
        if expand and isinstance(extracted, pd.DataFrame):
            successful_extractions = int((~extracted.isna()).any(axis=1).sum())
        else:
            successful_extractions = (
                int(extracted.notna().sum()) if hasattr(extracted, "notna") else len(extracted)
            )

        return ColumnOperationResult(
            operation=operation_desc,
            rows_affected=successful_extractions,
            columns_affected=affected_columns,
        )

    except (
        SessionNotFoundError,
        NoDataLoadedError,
        ColumnNotFoundError,
        InvalidParameterError,
    ) as e:
        logger.exception("Extract from column failed: %s", e.message)
        raise ToolError(e.message) from e
    except Exception as e:
        logger.exception("Error extracting from column: %s", str(e))
        msg = f"Error extracting from column: {e}"
        raise ToolError(msg) from e


async def split_column(
    ctx: Annotated[Context, Field(description="FastMCP context for session access")],
    column: Annotated[str, Field(description="Column name to split values in")],
    delimiter: Annotated[str, Field(description="String delimiter to split on")] = " ",
    *,
    part_index: Annotated[
        int | None,
        Field(description="Which part to keep (0-based index, None for first part)"),
    ] = None,
    expand_to_columns: Annotated[
        bool,
        Field(description="Whether to expand splits into multiple columns"),
    ] = False,
    new_columns: Annotated[
        list[str] | None,
        Field(description="Names for new columns when expanding"),
    ] = None,
) -> ColumnOperationResult:
    """Split column values by delimiter.

    Returns:
        ColumnOperationResult with split details

    Examples:
        # Keep first part of split
        split_column(ctx, "full_name", " ", part_index=0)

        # Keep last part
        split_column(ctx, "email", "@", part_index=1)

        # Expand into multiple columns
        split_column(ctx, "address", ",", expand_to_columns=True)

        # Expand with custom column names
        split_column(ctx, "name", " ", expand_to_columns=True,
                    new_columns=["first_name", "last_name"])

    """
    try:
        # Get session_id from FastMCP context
        session_id = ctx.session_id
        session, df = get_session_data(session_id)

        if column not in df.columns:
            raise ColumnNotFoundError(column, df.columns.tolist())

        if not delimiter:
            msg = "delimiter"
            raise InvalidParameterError(msg, delimiter, "Delimiter cannot be empty")

        # Apply split operation
        # Note: mypy has issues with overloaded split method, but this is valid
        split_data = df[column].astype(str).str.split(delimiter, expand=expand_to_columns)  # type: ignore[call-overload]

        if expand_to_columns:
            # Expanding to multiple columns
            if isinstance(split_data, pd.DataFrame):
                num_parts = len(split_data.columns)
                columns_created = []

                # Use custom column names if provided
                if new_columns:
                    if len(new_columns) > num_parts:
                        # Truncate to actual number of parts
                        new_columns = new_columns[:num_parts]
                    elif len(new_columns) < num_parts:
                        # Extend with default names
                        for i in range(len(new_columns), num_parts):
                            new_columns.append(f"{column}_part_{i}")
                    column_names = new_columns
                else:
                    # Generate default column names
                    column_names = [f"{column}_part_{i}" for i in range(num_parts)]

                # Create new columns
                for i, col_name in enumerate(column_names):
                    if i < len(split_data.columns):
                        if session.df is None:
                            msg = "Session data not available"
                            raise ToolError(msg)
                        session.df[col_name] = split_data.iloc[:, i]
                        columns_created.append(col_name)

                affected_columns = columns_created
                operation_desc = f"split_expand_{len(columns_created)}_parts"
                rows_affected = len(df)
            else:
                # Shouldn't happen with expand=True, but handle gracefully
                msg = "expand_to_columns"
                raise InvalidParameterError(
                    msg,
                    str(expand_to_columns),
                    "Split with expand=True did not produce DataFrame",
                )
        else:
            # Not expanding - keep specific part or first part
            if part_index is None:
                part_index = 0

            if isinstance(split_data, pd.DataFrame):
                # This shouldn't happen with expand=False, but handle it
                if session.df is None:
                    msg = "Session data not available"
                    raise ToolError(msg)
                if part_index < len(split_data.columns):
                    session.df[column] = split_data.iloc[:, part_index]
                else:
                    # Index out of range - fill with NaN
                    session.df[column] = pd.NA
            else:
                # Series of lists - extract specified part
                def get_part(split_list: Any) -> Any:
                    if isinstance(split_list, list) and len(split_list) > part_index:
                        return split_list[part_index]
                    return pd.NA

                if session.df is None:
                    msg = "Session data not available"
                    raise ToolError(msg)
                session.df[column] = split_data.apply(get_part)

            affected_columns = [column]
            operation_desc = f"split_keep_part_{part_index}"

            # Count successful splits (non-null results)
            if session.df is None:
                msg = "Session data not available"
                raise ToolError(msg)
            rows_affected = int(session.df[column].notna().sum())

        return ColumnOperationResult(
            operation=operation_desc,
            rows_affected=rows_affected,
            columns_affected=affected_columns,
        )

    except (
        SessionNotFoundError,
        NoDataLoadedError,
        ColumnNotFoundError,
        InvalidParameterError,
    ) as e:
        logger.exception("Split column failed: %s", e.message)
        raise ToolError(e.message) from e
    except Exception as e:
        logger.exception("Error splitting column: %s", str(e))
        msg = f"Error splitting column: {e}"
        raise ToolError(msg) from e


async def transform_column_case(
    ctx: Annotated[Context, Field(description="FastMCP context for session access")],
    column: Annotated[str, Field(description="Column name to transform text case in")],
    transform: Annotated[
        Literal["upper", "lower", "title", "capitalize"],
        Field(description="Case transformation: upper, lower, title, or capitalize"),
    ],
) -> ColumnOperationResult:
    """Transform the case of text in a column.

    Returns:
        ColumnOperationResult with transformation details

    Examples:
        # Convert to uppercase
        transform_column_case(ctx, "code", "upper")

        # Convert names to title case
        transform_column_case(ctx, "name", "title")

        # Convert to lowercase for comparison
        transform_column_case(ctx, "email", "lower")

        # Capitalize sentences
        transform_column_case(ctx, "description", "capitalize")

    """
    try:
        # Get session_id from FastMCP context
        session_id = ctx.session_id
        session, df = get_session_data(session_id)

        if column not in df.columns:
            raise ColumnNotFoundError(column, df.columns.tolist())

        # Store original for comparison
        original_data = df[column].copy()

        # Apply case transformation
        str_col = df[column].astype(str)

        if session.df is None:
            msg = "Session data not available"
            raise ToolError(msg)
        if transform == "upper":
            session.df[column] = str_col.str.upper()
        elif transform == "lower":
            session.df[column] = str_col.str.lower()
        elif transform == "title":
            session.df[column] = str_col.str.title()
        elif transform == "capitalize":
            session.df[column] = str_col.str.capitalize()
        else:
            msg = "transform"
            raise InvalidParameterError(
                msg,
                transform,
                "Supported transforms: upper, lower, title, capitalize",
            )

        # Count changes made (ignore null values)
        if session.df is None:
            msg = "Session data not available"
            raise ToolError(msg)
        changed_mask = original_data.astype(str).fillna("") != session.df[column].astype(
            str,
        ).fillna("")
        changes_made = int(changed_mask.sum())

        return ColumnOperationResult(
            operation=f"case_{transform}",
            rows_affected=changes_made,
            columns_affected=[column],
        )

    except (
        SessionNotFoundError,
        NoDataLoadedError,
        ColumnNotFoundError,
        InvalidParameterError,
    ) as e:
        logger.exception("Transform column case failed: %s", e.message)
        raise ToolError(e.message) from e
    except Exception as e:
        logger.exception("Error transforming column case: %s", str(e))
        msg = f"Error transforming column case: {e}"
        raise ToolError(msg) from e


async def strip_column(
    ctx: Annotated[Context, Field(description="FastMCP context for session access")],
    column: Annotated[str, Field(description="Column name to strip characters from")],
    chars: Annotated[
        str | None,
        Field(description="Characters to strip (None for whitespace, string for specific chars)"),
    ] = None,
) -> ColumnOperationResult:
    r"""Strip whitespace or specified characters from column values.

    Returns:
        ColumnOperationResult with strip details

    Examples:
        # Remove leading/trailing whitespace
        strip_column(ctx, "name")

        # Remove specific characters
        strip_column(ctx, "phone", "()")

        # Clean currency values
        strip_column(ctx, "price", "$,")

        # Remove quotes
        strip_column(ctx, "quoted_text", "'\"")

    """
    try:
        # Get session_id from FastMCP context
        session_id = ctx.session_id
        session, df = get_session_data(session_id)

        if column not in df.columns:
            raise ColumnNotFoundError(column, df.columns.tolist())

        # Store original for comparison
        original_data = df[column].copy()

        # Apply strip operation
        if session.df is None:
            msg = "Session data not available"
            raise ToolError(msg)
        if chars is None:
            # Strip whitespace
            session.df[column] = df[column].astype(str).str.strip()
        else:
            # Strip specified characters
            session.df[column] = df[column].astype(str).str.strip(chars)

        # Count changes made
        if session.df is None:
            msg = "Session data not available"
            raise ToolError(msg)
        changed_mask = original_data.astype(str).fillna("") != session.df[column].astype(
            str,
        ).fillna("")
        changes_made = int(changed_mask.sum())

        return ColumnOperationResult(
            operation=f"strip_{'whitespace' if chars is None else 'chars'}",
            rows_affected=changes_made,
            columns_affected=[column],
        )

    except (SessionNotFoundError, NoDataLoadedError, ColumnNotFoundError) as e:
        logger.exception("Strip column failed: %s", e.message)
        raise ToolError(e.message) from e
    except Exception as e:
        logger.exception("Error stripping column: %s", str(e))
        msg = f"Error stripping column: {e}"
        raise ToolError(msg) from e


async def fill_column_nulls(
    ctx: Annotated[Context, Field(description="FastMCP context for session access")],
    column: Annotated[str, Field(description="Column name to fill null values in")],
    value: Annotated[Any, Field(description="Value to use for filling null/NaN values")],
) -> ColumnOperationResult:
    """Fill null/NaN values in a specific column with a specified value.

    Returns:
        ColumnOperationResult with fill details

    Examples:
        # Fill missing names with "Unknown"
        fill_column_nulls(ctx, "name", "Unknown")

        # Fill missing ages with 0
        fill_column_nulls(ctx, "age", 0)

        # Fill missing status with default
        fill_column_nulls(ctx, "status", "pending")

        # Fill missing scores with -1
        fill_column_nulls(ctx, "score", -1)

    """
    try:
        # Get session_id from FastMCP context
        session_id = ctx.session_id
        session, df = get_session_data(session_id)

        if column not in df.columns:
            raise ColumnNotFoundError(column, df.columns.tolist())

        # Count nulls before filling
        nulls_before = int(df[column].isna().sum())

        if nulls_before == 0:
            # No nulls to fill
            return ColumnOperationResult(
                operation="fill_nulls",
                rows_affected=0,
                columns_affected=[column],
            )

        # Fill null values
        if session.df is None:
            msg = "Session data not available"
            raise ToolError(msg)
        # Use explicit assignment to avoid downcasting warnings
        with pd.option_context("future.no_silent_downcasting", True):  # noqa: FBT003
            filled_series = df[column].fillna(value)
            if hasattr(filled_series, "infer_objects"):
                filled_series = filled_series.infer_objects(copy=False)
            session.df[column] = filled_series

        # Verify fills worked
        nulls_after = int(session.df[column].isna().sum())
        filled_count = nulls_before - nulls_after

        return ColumnOperationResult(
            operation="fill_nulls",
            rows_affected=filled_count,
            columns_affected=[column],
        )

    except (SessionNotFoundError, NoDataLoadedError, ColumnNotFoundError) as e:
        logger.exception("Fill column nulls failed: %s", e.message)
        raise ToolError(e.message) from e
    except Exception as e:
        logger.exception("Error filling column nulls: %s", str(e))
        msg = f"Error filling column nulls: {e}"
        raise ToolError(msg) from e


# =============================================================================
# SERVER INITIALIZATION
# =============================================================================

column_text_server = FastMCP(
    "DataBeak Text Column Operations Server",
    instructions="Text and string column operations server providing pattern matching, extraction, case transformation, and text cleaning",
)

# Register the functions as MCP tools
column_text_server.tool(name="replace_in_column")(replace_in_column)
column_text_server.tool(name="extract_from_column")(extract_from_column)
column_text_server.tool(name="split_column")(split_column)
column_text_server.tool(name="transform_column_case")(transform_column_case)
column_text_server.tool(name="strip_column")(strip_column)
column_text_server.tool(name="fill_column_nulls")(fill_column_nulls)
