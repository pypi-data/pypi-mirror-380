# -*- coding: utf-8 -*-
from . import api as hk
from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions

__all__ = ["hk"]
