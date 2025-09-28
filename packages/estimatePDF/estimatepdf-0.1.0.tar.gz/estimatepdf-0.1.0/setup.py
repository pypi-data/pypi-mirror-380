# %%
import sys
from setuptools import setup, find_packages


# %%

setup(
    name="estimatePDF",  # the PyPI package name
    version="0.1.0",
    description="Probability Density Function Estimation Library",
    author="Shantanu Sarkar",
    author_email="shantanu75@gmail.com",
    url="https://github.com/ShanSarkar75/estimatePDF",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "scipy",
        "pandas",
        "matplotlib",
        "tensorflow"  # if used
    ],
    python_requires=">=3.8",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
)
