import sys
from setuptools import setup

INSTRUCTIONS = """
Mypyc compiler is distributed as part of `mypy`. To install mypyc compiler use
`pip install mypy`. To install mypyc runtime library use `pip install librt`.
"""

if "egg_info" not in sys.argv and "sdist" not in sys.argv:
    raise ValueError(INSTRUCTIONS)

setup()
