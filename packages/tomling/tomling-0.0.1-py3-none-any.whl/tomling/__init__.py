"""Reads and writes toml by tomling!"""
from .reader import read_toml, _read_value, _set_key, _ensure_path
from .writer import write_toml, _write_dict, _write_value

__all__  = ["read_toml", "write_toml"]

__version__ = "0.0.1"
__author__ = "devs_des1re"
__license__ = "MIT"
__email__ = "arjunbrij8811@gmail.com"
