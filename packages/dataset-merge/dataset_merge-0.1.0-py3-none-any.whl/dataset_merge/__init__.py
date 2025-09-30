# read version from installed package
from importlib.metadata import version
__version__ = version("dataset_merge")

from .fetch import merge_datasets
