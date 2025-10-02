# utilities

"""
Package with various utilities depending on windows platform i. e. windows handling

Set of submodules contains:

- submodule with utilities specific for Win32 platform

Raises:
    ImportError: import error if implementation is not available for platform
"""


# ruff and mypy per file settings
#
# empty lines
# ruff: noqa: E302, E303
# naming conventions
# ruff: noqa: N801, N802, N803, N806, N812, N813, N815, N816, N818, N999
#
# disable mypy errors
# mypy: disable-error-code = "assignment"

# fmt: off


# version determination

# original Hatchlor version
# from importlib.metadata import PackageNotFoundError, version
# try:
#     __version__ = version('{{ cookiecutter.project_slug }}')
# except PackageNotFoundError:  # pragma: no cover
#     __version__ = 'unknown'
# finally:
#     del version, PackageNotFoundError

# latest import requirement for hatch-vcs-footgun-example
from utils_mystuff_windows.version import __version__


import sys
import os

# platform / OS dependent imports
# inspiration: https://stackoverflow.com/questions/3496592/conditional-import-of-modules-in-python
# general schema:
# if sys.platform == "cli":
#     <import>
# else:
#     if os.name == "nt" or sys.platform == "win32":
#         <import>
#     elif os.name == "posix":
#         <import>
#     elif os.name == "java":
#         <import>
#     elif os.name == "macos":
#         pass
#     else:
#         raise ImportError(f"No implementation for your platform ('{os.name}') available")

if os.name == "nt" or sys.platform == "win32":
    from utils_win32 import *
else:
    raise ImportError(f"No implementation of window utilities available for your platform ('{os.name}').")
