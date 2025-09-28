"""DDPC package initialization."""

import polars as pl

# Configure Polars display options globally
pl.Config.set_tbl_hide_column_data_types(True)  # Hide data type headers
pl.Config.set_float_precision(3)  # Set float precision for display