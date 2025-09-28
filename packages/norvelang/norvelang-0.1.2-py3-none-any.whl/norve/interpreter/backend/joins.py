"""
Join operations for the backend.

This module provides optimized join operations including cross joins, natural joins,
and explicit key joins with performance optimizations.
"""

from dataclasses import dataclass
from typing import List, Optional
import pandas as pd
from .column_utils import resolve_column_fast, get_join_var_fast


@dataclass
class JoinKeys:
    """Join key configuration."""
    left_key: Optional[str] = None
    right_key: Optional[str] = None


@dataclass
class JoinAliases:
    """Join alias configuration."""
    left_alias: Optional[str] = None
    right_alias: Optional[str] = None
    right_source: Optional[str] = None


@dataclass
class JoinConfig:
    """Configuration for join operations."""
    left_df: pd.DataFrame
    right_df: pd.DataFrame
    join_type: str
    keys: JoinKeys
    aliases: JoinAliases

# Performance constants
_SMALL_DATASET_THRESHOLD = 100  # Threshold for algorithm selection


def perform_cross_join(left_df: pd.DataFrame, right_df: pd.DataFrame) -> pd.DataFrame:
    """Perform a cross join between two DataFrames with size-based optimization."""
    # For small datasets, avoid temporary column creation
    if len(left_df) * len(right_df) < _SMALL_DATASET_THRESHOLD * 10:
        # Use more efficient approach for small cross joins
        left_df = left_df.assign(_tmp=1)
        right_df = right_df.assign(_tmp=1)
        merged = pd.merge(left_df, right_df, on="_tmp", how="inner").drop(
            "_tmp", axis=1
        )
        return merged
    # Original approach for larger datasets
    left_df["_tmp"] = 1
    right_df["_tmp"] = 1
    merged = pd.merge(left_df, right_df, on="_tmp").drop("_tmp", axis=1)
    return merged


def find_natural_join_columns(
    left_df: pd.DataFrame, right_df: pd.DataFrame
) -> List[str]:
    """Find common columns for natural join using optimized set operations."""
    # Use set intersection for O(1) lookup performance
    left_cols = set(left_df.columns)
    right_cols = set(right_df.columns)
    common_cols = list(left_cols & right_cols)

    if common_cols:
        return common_cols

    # Case-insensitive matches using dict comprehension for speed
    left_lower = {col.lower(): col for col in left_cols}
    right_lower_keys = {col.lower() for col in right_cols}
    common_lower = set(left_lower.keys()) & right_lower_keys

    return [left_lower[k] for k in common_lower] if common_lower else []


def perform_join(config: JoinConfig) -> pd.DataFrame:
    """
    Perform a join operation between two DataFrames.

    Args:
        config: JoinConfig object containing all join parameters

    Returns:
        Merged DataFrame
    """
    # Handle cross join
    if config.join_type == "cross":
        return perform_cross_join(config.left_df, config.right_df)

    # Handle natural join
    if config.join_type == "natural":
        return _perform_natural_join(config.left_df, config.right_df)

    # Handle explicit key joins - optimized
    return _perform_explicit_key_join(config)


def _perform_natural_join(left_df: pd.DataFrame, right_df: pd.DataFrame) -> pd.DataFrame:
    """Perform a natural join between two DataFrames."""
    common_cols = find_natural_join_columns(left_df, right_df)
    if not common_cols:
        raise RuntimeError(
            f"No common columns for NATURAL JOIN.\n"
            f"Left columns: {list(left_df.columns)}\n"
            f"Right columns: {list(right_df.columns)}\n"
            f"Consider using an explicit join key "
            f"(e.g., ... left ... on country=code) or rename columns."
        )
    merged = pd.merge(
        left_df, right_df, on=common_cols, how="inner", suffixes=("", "_right")
    )
    return merged


def _perform_explicit_key_join(config: JoinConfig) -> pd.DataFrame:
    """Perform an explicit key join between two DataFrames."""
    if config.keys.left_key is None or config.keys.right_key is None:
        raise RuntimeError(
            f"Join type '{config.join_type}' requires join keys, but none were provided."
        )

    # Fast column resolution using optimized method
    left_cols = list(config.left_df.columns)
    right_cols = list(config.right_df.columns)
    left_key_full = resolve_column_fast(left_cols, config.keys.left_key)
    right_key_full = resolve_column_fast(right_cols, config.keys.right_key)

    # Perform the join
    how = config.join_type if config.join_type in ["outer", "inner", "left", "right"] else "left"

    # Optimized join variable determination
    join_var = get_join_var_fast(config.aliases.right_alias, config.aliases.right_source)

    # Efficient column prefixing using dict comprehension
    right_cols_to_rename = {
        col: f"{join_var}.{col}" for col in config.right_df.columns if col != right_key_full
    }

    # Only rename if there are columns to rename
    if right_cols_to_rename:
        right_df_renamed = config.right_df.rename(columns=right_cols_to_rename)
    else:
        right_df_renamed = config.right_df

    # Perform the merge
    merged = config.left_df.merge(
        right_df_renamed,
        left_on=left_key_full,
        right_on=right_key_full,
        how=how,
        suffixes=("", "_right"),
    )

    # Apply left alias if specified - optimized
    if config.aliases.left_alias:
        left_alias = config.aliases.left_alias
        left_rename_cols = {
            col: col if col.startswith(f"{left_alias}.") else f"{left_alias}.{col}"
            for col in left_cols
            if col in merged.columns
        }
        if left_rename_cols:
            merged = merged.rename(columns=left_rename_cols)

    return merged
