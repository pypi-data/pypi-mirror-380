from .theme import *
from typing import Any

_config = {
    "theme": dark_theme(),
    "font": "Roboto"
}

def set_config(attr: str, v: Any):
    _config[attr] = v

def get_config(attr: str) -> Any:
    return _config[attr]
