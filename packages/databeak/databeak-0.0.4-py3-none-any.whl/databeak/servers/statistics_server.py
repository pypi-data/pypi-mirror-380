"""Standalone Statistics server for DataBeak using FastMCP server composition.

This module provides a complete Statistics server implementation following DataBeak's modular server
architecture pattern. It focuses on core statistical analysis, numerical computations, and
correlation analysis with optimized mathematical processing.
"""

from __future__ import annotations

import logging
from typing import Annotated, Any, Literal

import numpy as np
import pandas as pd
from fastmcp import Context, FastMCP
from fastmcp.exceptions import ToolError
from pydantic import Field

from databeak.core.session import get_session_data
from databeak.core.settings import get_settings

# Import session management and data models from the main package
from databeak.exceptions import (
    ColumnNotFoundError,
    InvalidParameterError,
    NoDataLoadedError,
    SessionNotFoundError,
)

# Import response models - needed at runtime for FastMCP
from databeak.models.statistics_models import (
    ColumnStatisticsResult,
    CorrelationResult,
    StatisticsResult,
    ValueCountsResult,
)

logger = logging.getLogger(__name__)

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================


# ============================================================================
# STATISTICAL OPERATIONS LOGIC - DIRECT IMPLEMENTATIONS
# ============================================================================


async def get_statistics(
    ctx: Annotated[Context, Field(description="FastMCP context for session access")],
    *,
    columns: Annotated[
        list[str] | None,
        Field(description="List of specific columns to analyze (None = all numeric columns)"),
    ] = None,
) -> StatisticsResult:
    """Get comprehensive statistical summary of numerical columns.

    Computes descriptive statistics for all or specified numerical columns including
    count, mean, standard deviation, min/max values, and percentiles. Optimized for
    AI workflows with clear statistical insights and data understanding.

    Returns:
        Comprehensive statistical analysis with per-column summaries

    Statistical Metrics:
        📊 Count: Number of non-null values
        📈 Mean: Average value
        📉 Std: Standard deviation (measure of spread)
        🔢 Min/Max: Minimum and maximum values
        📊 Percentiles: 25th, 50th (median), 75th quartiles

    Examples:
        # Get statistics for all numeric columns
        stats = await get_statistics("session_123")

        # Analyze specific columns only
        stats = await get_statistics("session_123", columns=["price", "quantity"])

        # Analyze all numeric columns (percentiles always included)
        stats = await get_statistics("session_123")

    AI Workflow Integration:
        1. Essential for data understanding and quality assessment
        2. Identifies data distribution and potential issues
        3. Guides feature engineering and analysis decisions
        4. Provides context for outlier detection thresholds

    """
    try:
        # Get session_id from FastMCP context
        session_id = ctx.session_id
        _session, df = get_session_data(session_id)  # Only need df, not session

        # Select numeric columns
        if columns:
            missing_cols = [col for col in columns if col not in df.columns]
            if missing_cols:
                raise ColumnNotFoundError(missing_cols[0], df.columns.tolist())
            numeric_df = df[columns].select_dtypes(include=[np.number])
            # Return empty results if no numeric columns found when specific columns requested
            if numeric_df.empty:
                return StatisticsResult(
                    statistics={},
                    column_count=0,
                    numeric_columns=[],
                    total_rows=len(df),
                )
        else:
            numeric_df = df.select_dtypes(include=[np.number])
            # Return empty results if no numeric columns
            if numeric_df.empty:
                return StatisticsResult(
                    statistics={},
                    column_count=0,
                    numeric_columns=[],
                    total_rows=len(df),
                )

        # Calculate statistics
        stats_dict = {}
        for col in numeric_df.columns:
            col_data = numeric_df[col].dropna()

            # Create StatisticsSummary directly
            from databeak.models.statistics_models import (  # Avoids circular import
                StatisticsSummary,
            )

            # Calculate statistics, using 0.0 for undefined values
            col_stats = StatisticsSummary.model_validate(
                {
                    "count": int(col_data.count()),
                    "mean": float(col_data.mean())
                    if len(col_data) > 0 and not pd.isna(col_data.mean())
                    else 0.0,
                    "std": float(col_data.std())
                    if len(col_data) > 1 and not pd.isna(col_data.std())
                    else 0.0,
                    "min": float(col_data.min())
                    if len(col_data) > 0 and not pd.isna(col_data.min())
                    else 0.0,
                    "max": float(col_data.max())
                    if len(col_data) > 0 and not pd.isna(col_data.max())
                    else 0.0,
                    "25%": float(col_data.quantile(0.25)) if len(col_data) > 0 else 0.0,
                    "50%": float(col_data.quantile(0.50)) if len(col_data) > 0 else 0.0,
                    "75%": float(col_data.quantile(0.75)) if len(col_data) > 0 else 0.0,
                },
            )

            stats_dict[col] = col_stats

        # No longer recording operations (simplified MCP architecture)

        return StatisticsResult(
            statistics=stats_dict,
            column_count=len(stats_dict),
            numeric_columns=list(stats_dict.keys()),
            total_rows=len(df),
        )

    except (
        SessionNotFoundError,
        NoDataLoadedError,
        ColumnNotFoundError,
        InvalidParameterError,
    ) as e:
        logger.exception("Statistics calculation failed: %s", e.message)
        raise ToolError(e.message) from e
    except Exception as e:
        logger.exception("Error calculating statistics: %s", str(e))
        msg = f"Error calculating statistics: {e}"
        raise ToolError(msg) from e


async def get_column_statistics(
    ctx: Annotated[Context, Field(description="FastMCP context for session access")],
    column: Annotated[str, Field(description="Name of the column to analyze in detail")],
) -> ColumnStatisticsResult:
    """Get detailed statistical analysis for a single column.

    Provides focused statistical analysis for a specific column including
    data type information, null value handling, and comprehensive numerical
    statistics when applicable.

    Returns:
        Detailed statistical analysis for the specified column

    Column Analysis:
        🔍 Data Type: Detected pandas data type
        📊 Statistics: Complete statistical summary for numeric columns
        🔢 Non-null Count: Number of valid (non-null) values
        📈 Distribution: Statistical distribution characteristics

    Examples:
        # Analyze a price column
        stats = await get_column_statistics(ctx, "price")

        # Analyze a categorical column
        stats = await get_column_statistics(ctx, "category")

    AI Workflow Integration:
        1. Deep dive analysis for specific columns of interest
        2. Data quality assessment for individual features
        3. Understanding column characteristics for modeling
        4. Validation of data transformations

    """
    try:
        # Get session_id from FastMCP context
        session_id = ctx.session_id
        _session, df = get_session_data(session_id)  # Only need df, not session

        if column not in df.columns:
            raise ColumnNotFoundError(column, df.columns.tolist())

        col_data = df[column]
        dtype = str(col_data.dtype)
        count = int(col_data.count())
        null_count = int(col_data.isna().sum())
        unique_count = int(col_data.nunique())

        # Initialize statistics dict using ColumnStatistics structure
        from databeak.models.typed_dicts import ColumnStatistics  # Avoids circular import

        statistics: ColumnStatistics = {
            "count": count,
            "null_count": null_count,
            "unique_count": unique_count,
            "dtype": str(col_data.dtype),
        }

        # Add numeric statistics if column is numeric (but not boolean)
        if pd.api.types.is_numeric_dtype(col_data) and not pd.api.types.is_bool_dtype(col_data):
            # Helper function to safely convert pandas scalars to float
            def safe_float(value: Any) -> float:
                """Safely convert pandas scalar to float."""
                try:
                    return float(value) if not pd.isna(value) else 0.0
                except (TypeError, ValueError):
                    return 0.0

            statistics.update(
                {
                    "mean": safe_float(col_data.mean()),
                    "std": safe_float(col_data.std()),
                    "min": safe_float(col_data.min()),
                    "max": safe_float(col_data.max()),
                    "sum": safe_float(col_data.sum()),
                    "variance": safe_float(col_data.var()),
                    "skewness": safe_float(col_data.skew()),
                    "kurtosis": safe_float(col_data.kurtosis()),
                },
            )
        # Create additional dict for non-standard fields
        additional_stats: dict[str, str | int] = {}
        if (
            not (
                pd.api.types.is_numeric_dtype(col_data) and not pd.api.types.is_bool_dtype(col_data)
            )
            and count > 0
        ):
            # For non-numeric columns, add most frequent value in additional dict
            mode_result = col_data.mode()
            most_frequent = mode_result.iloc[0] if len(mode_result) > 0 else None
            if most_frequent is not None and not pd.isna(most_frequent):
                additional_stats["most_frequent"] = str(most_frequent)
                additional_stats["most_frequent_count"] = int(col_data.value_counts().iloc[0])

        # No longer recording operations (simplified MCP architecture)

        # Convert statistics dict to StatisticsSummary
        from databeak.models.statistics_models import (  # Avoids circular import
            StatisticsSummary,
        )

        if pd.api.types.is_numeric_dtype(col_data) and not pd.api.types.is_bool_dtype(col_data):
            # Numeric columns - calculate percentiles for Pydantic model
            col_data_non_null = col_data.dropna()
            percentile_25 = (
                float(col_data_non_null.quantile(0.25)) if len(col_data_non_null) > 0 else None
            )
            percentile_50 = (
                float(col_data_non_null.quantile(0.50)) if len(col_data_non_null) > 0 else None
            )
            percentile_75 = (
                float(col_data_non_null.quantile(0.75)) if len(col_data_non_null) > 0 else None
            )

            stats_summary = StatisticsSummary(
                count=statistics["count"],
                mean=statistics.get("mean"),
                std=statistics.get("std"),
                min=statistics.get("min"),
                percentile_25=percentile_25,
                percentile_50=percentile_50,
                percentile_75=percentile_75,
                max=statistics.get("max"),
                unique=statistics["unique_count"],
            )
        else:
            # For non-numeric columns, populate categorical statistics
            stats_summary = StatisticsSummary(
                count=statistics["count"],
                mean=None,
                std=None,
                min=None,
                percentile_25=None,
                percentile_50=None,
                percentile_75=None,
                max=None,
                unique=statistics["unique_count"],
                top=str(additional_stats.get("most_frequent"))
                if additional_stats.get("most_frequent")
                else None,
                freq=int(freq_value)
                if (freq_value := additional_stats.get("most_frequent_count"))
                and isinstance(freq_value, int)
                else None,
            )

        # Map dtype to expected literal type
        dtype_map: dict[
            str,
            Literal["int64", "float64", "object", "bool", "datetime64", "category"],
        ] = {
            "int64": "int64",
            "float64": "float64",
            "object": "object",
            "bool": "bool",
            "datetime64[ns]": "datetime64",
            "category": "category",
        }
        data_type: Literal["int64", "float64", "object", "bool", "datetime64", "category"] = (
            dtype_map.get(dtype, "object")
        )

        return ColumnStatisticsResult(
            column=column,
            statistics=stats_summary,
            data_type=data_type,
            non_null_count=count,
        )

    except (SessionNotFoundError, NoDataLoadedError, ColumnNotFoundError) as e:
        await ctx.error(f"Column statistics failed: {e.message}")
        raise ToolError(e.message) from e
    except Exception as e:
        await ctx.error(f"Error calculating column statistics: {e}")
        msg = f"Error calculating column statistics: {e}"
        raise ToolError(msg) from e


async def get_correlation_matrix(
    ctx: Annotated[Context, Field(description="FastMCP context for session access")],
    method: Annotated[
        Literal["pearson", "spearman", "kendall"],
        Field(description="Correlation method: pearson (linear), spearman (rank), kendall (rank)"),
    ] = "pearson",
    columns: Annotated[
        list[str] | None,
        Field(description="List of columns to include (None = all numeric columns)"),
    ] = None,
    min_correlation: Annotated[
        float | None,
        Field(description="Minimum correlation threshold to include in results"),
    ] = None,
) -> CorrelationResult:
    """Calculate correlation matrix for numerical columns.

    Computes pairwise correlations between numerical columns using various
    correlation methods. Essential for understanding relationships between
    variables and feature selection in analytical workflows.

    Returns:
        Correlation matrix with pairwise correlation coefficients

    Correlation Methods:
        📊 Pearson: Linear relationships (default, assumes normality)
        📈 Spearman: Monotonic relationships (rank-based, non-parametric)
        🔄 Kendall: Concordant/discordant pairs (robust, small samples)

    Examples:
        # Basic correlation analysis
        corr = await get_correlation_matrix(ctx)

        # Analyze specific columns with Spearman correlation
        corr = await get_correlation_matrix(ctx,
                                          columns=["price", "rating", "sales"],
                                          method="spearman")

        # Filter correlations above threshold
        corr = await get_correlation_matrix(ctx, min_correlation=0.5)

    AI Workflow Integration:
        1. Feature selection and dimensionality reduction
        2. Multicollinearity detection before modeling
        3. Understanding variable relationships
        4. Data validation and quality assessment

    """
    try:
        # Get session_id from FastMCP context
        session_id = ctx.session_id
        _session, df = get_session_data(session_id)  # Only need df, not session

        # Select numeric columns
        if columns:
            missing_cols = [col for col in columns if col not in df.columns]
            if missing_cols:
                raise ColumnNotFoundError(missing_cols[0], df.columns.tolist())
            numeric_df = df[columns].select_dtypes(include=[np.number])
        else:
            numeric_df = df.select_dtypes(include=[np.number])

        if numeric_df.empty:
            msg = "No numeric columns found for correlation analysis"
            raise ToolError(msg)

        settings = get_settings()
        if len(numeric_df.columns) < settings.min_statistical_sample_size:
            msg = "Correlation analysis requires at least two numeric columns"
            raise ToolError(msg)

        # Calculate correlation matrix
        corr_matrix = numeric_df.corr(method=method)

        # Convert to dict format
        correlation_dict: dict[str, dict[str, float]] = {}
        for col1 in corr_matrix.columns:
            correlation_dict[col1] = {}
            for col2 in corr_matrix.columns:
                corr_val = corr_matrix.loc[col1, col2]
                if not pd.isna(corr_val):
                    # Ensure we have a numeric value for conversion
                    correlation_dict[col1][col2] = (
                        float(corr_val) if isinstance(corr_val, int | float) else 0.0
                    )
                else:
                    correlation_dict[col1][col2] = 0.0

        # Filter by minimum correlation if specified
        if min_correlation is not None:
            filtered_dict = {}
            for col1, col_corrs in correlation_dict.items():
                filtered_col = {
                    col2: corr_val
                    for col2, corr_val in col_corrs.items()
                    if abs(corr_val) >= abs(min_correlation) or col1 == col2
                }
                if filtered_col:
                    filtered_dict[col1] = filtered_col
            correlation_dict = filtered_dict

        # No longer recording operations (simplified MCP architecture)

        return CorrelationResult(
            method=method,
            correlation_matrix=correlation_dict,
            columns_analyzed=list(numeric_df.columns),
        )

    except (
        SessionNotFoundError,
        NoDataLoadedError,
        ColumnNotFoundError,
        InvalidParameterError,
    ) as e:
        logger.exception("Correlation calculation failed: %s", e.message)
        raise ToolError(e.message) from e
    except ToolError:
        # Re-raise ToolErrors as-is to preserve the exact error message
        raise
    except Exception as e:
        logger.exception("Error calculating correlation matrix: %s", str(e))
        msg = f"Error calculating correlation matrix: {e}"
        raise ToolError(msg) from e


async def get_value_counts(
    ctx: Annotated[Context, Field(description="FastMCP context for session access")],
    column: Annotated[str, Field(description="Name of the column to analyze value distribution")],
    *,
    normalize: Annotated[
        bool,
        Field(description="Return percentages instead of raw counts"),
    ] = False,
    sort: Annotated[bool, Field(description="Sort results by frequency")] = True,
    ascending: Annotated[
        bool,
        Field(description="Sort in ascending order (False = descending)"),
    ] = False,
    top_n: Annotated[
        int | None,
        Field(description="Maximum number of values to return (None = all values)"),
    ] = None,
) -> ValueCountsResult:
    """Get frequency distribution of values in a column.

    Analyzes the distribution of values in a specified column, providing
    counts and optionally percentages for each unique value. Essential for
    understanding categorical data and identifying common patterns.

    Returns:
        Frequency distribution with counts/percentages for each unique value

    Analysis Features:
        🔢 Frequency Counts: Raw counts for each unique value
        📊 Percentage Mode: Normalized frequencies as percentages
        🎯 Top Values: Configurable limit for most frequent values
        📈 Summary Stats: Total values, unique count, distribution insights

    Examples:
        # Basic value counts
        counts = await get_value_counts(ctx, "category")

        # Get percentages for top 10 values
        counts = await get_value_counts(ctx, "status",
                                      normalize=True, top_n=10)

        # Sort in ascending order
        counts = await get_value_counts(ctx, "grade", ascending=True)

    AI Workflow Integration:
        1. Categorical data analysis and encoding decisions
        2. Data quality assessment (identifying rare values)
        3. Understanding distribution for sampling strategies
        4. Feature engineering insights for categorical variables

    """
    try:
        # Get session_id from FastMCP context
        session_id = ctx.session_id
        _session, df = get_session_data(session_id)  # Only need df, not session

        if column not in df.columns:
            raise ColumnNotFoundError(column, df.columns.tolist())

        # Get value counts
        # Note: mypy has issues with value_counts overloads when normalize is a bool variable
        value_counts = df[column].value_counts(
            normalize=normalize,
            sort=sort,
            ascending=ascending,
            dropna=True,
        )  # type: ignore[call-overload]

        # Limit to top_n if specified
        if top_n is not None and top_n > 0:
            value_counts = value_counts.head(top_n)

        # Convert to dict, handling various data types
        counts_dict = {}
        for value, count in value_counts.items():
            # Handle NaN and None values
            if pd.isna(value):
                key = "<null>"
            elif isinstance(value, str | int | float | bool):
                key = str(value)
            else:
                key = str(value)

            counts_dict[key] = float(count) if normalize else int(count)

        # Calculate summary statistics
        total_count = int(df[column].count())  # Non-null count
        unique_count = int(df[column].nunique())

        # No longer recording operations (simplified MCP architecture)

        return ValueCountsResult(
            column=column,
            value_counts=counts_dict,
            total_values=total_count,
            unique_values=unique_count,
            normalize=normalize,
        )

    except (SessionNotFoundError, NoDataLoadedError, ColumnNotFoundError) as e:
        logger.exception("Value counts calculation failed: %s", e.message)
        raise ToolError(e.message) from e
    except Exception as e:
        logger.exception("Error calculating value counts: %s", str(e))
        msg = f"Error calculating value counts: {e}"
        raise ToolError(msg) from e


# ============================================================================
# FASTMCP SERVER SETUP
# ============================================================================


# Create Statistics server
statistics_server = FastMCP(
    "DataBeak-Statistics",
    instructions="Statistics and correlation analysis server for DataBeak with comprehensive numerical analysis capabilities",
)


# Register the statistical analysis functions directly as MCP tools
statistics_server.tool(name="get_statistics")(get_statistics)
statistics_server.tool(name="get_column_statistics")(get_column_statistics)
statistics_server.tool(name="get_correlation_matrix")(get_correlation_matrix)
statistics_server.tool(name="get_value_counts")(get_value_counts)
