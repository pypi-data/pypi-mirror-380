from setuptools import setup, find_packages
from pathlib import Path

# Read README.md for long description
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="pyimage_scaler",
    version="1.1.2",
    description="A Python package to resize images (JPEG, PNG, BMP, GIF)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="codingmaster24",
    packages=find_packages(),
    python_requires=">=3.7",
)
