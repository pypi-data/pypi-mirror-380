#!/usr/bin/env python

from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="binigogeo",
    version="0.0.5",
    license="MIT",
    description="2D and 3D geometry in Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Benjamin D. Killeen with contributions from Blanca",
    author_email="binigo1@jhu.edu",
    python_requires=">=3.10",
    install_requires=[
        "numpy",
        "scipy",
        "typing_extensions",
    ],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
