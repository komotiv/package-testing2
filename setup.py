import sys
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="komotiv_package_testing",
    version="0.1.0",
    author="Komotiv Inc.",
    author_email="contact@komotiv.com",
    description="Komotiv package test",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(exclude=["tests", "docs"]),
    install_requires=[
        "openai",
        "git+https://github.com/komotiv/package-testing2",
    ],
)
