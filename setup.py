import io
import re

from setuptools import setup

with io.open("src/flask_sqlalchemy/__init__.py", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="Flask-SQLAlchemy",
    version=version,
    install_requires=[
        "backports.time_perf_counter==0.0.4",
        "Flask>=1.0.4",
        "future_fstrings>=1.2",
        "SQLAlchemy>=1.2",
    ]
)
