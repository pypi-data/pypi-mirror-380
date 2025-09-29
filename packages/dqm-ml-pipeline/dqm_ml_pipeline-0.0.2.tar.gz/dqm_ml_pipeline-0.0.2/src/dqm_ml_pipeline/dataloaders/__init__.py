"""
Data processors module.

This module contains classes for processing data and computing metrics.
"""

from dqm_ml_pipeline.dataloaders.parquet import ParquetDataLoader

# Registry of supported data loaders
dqml_dataloaders_registry = {"parquet": ParquetDataLoader}

__all__ = ["ParquetDataLoader", "dqml_dataloaders_registry"]
