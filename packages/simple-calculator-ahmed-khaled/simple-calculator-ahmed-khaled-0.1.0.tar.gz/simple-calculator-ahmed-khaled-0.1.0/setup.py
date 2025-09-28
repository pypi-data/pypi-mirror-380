'''Setup script for the simple_calculator_ahmed_khaled package.'''

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="simple-calculator-ahmed-khaled",
    version="0.1.0",
    author="Ahmed Khaled",
    author_email="ahmed.khaled@example.com",
    description="A simple calculator package for basic math operations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/example/simple-calculator-ahmed-khaled",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

