import os
import re
from setuptools import setup, find_packages

# Read version from __init__.py
with open(os.path.join("acronym_expander", "__init__.py"), "r", encoding="utf-8") as f:
    version_match = re.search(r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read())
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")

setup(
    name="acronym_expander",
    version=version,
    packages=find_packages(),
    install_requires=[],
    python_requires='>=3.6',
)
