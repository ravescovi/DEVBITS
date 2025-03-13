# -*- coding: iso-8859-1 -*-

"""Model Bluesky Data Acquisition Instrument."""

import bits.demo_instrument  # noqa: F401
from bits.utils.logging_setup import configure_logging

configure_logging()

__package__ = "bits"
try:
    from setuptools_scm import get_version

    __version__ = get_version(root="..", relative_to=__file__)
    del get_version
except (LookupError, ModuleNotFoundError):
    from importlib.metadata import version

    __version__ = version(__package__)
