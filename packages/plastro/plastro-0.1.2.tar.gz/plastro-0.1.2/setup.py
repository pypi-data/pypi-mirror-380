"""Setup script for PLASTRO package."""

from setuptools import setup, find_packages
import os

# Read long description from README
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements from requirements.txt
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="plastro",
    version="0.1.0",
    author="Sitara Persad",
    author_email="sitara.persad@example.com",
    description="A Python package for simulating cellular plasticity in single-cell data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/username/plastro",
    project_urls={
        "Bug Tracker": "https://github.com/username/plastro/issues",
        "Documentation": "https://plastro.readthedocs.io/",
        "Source": "https://github.com/username/plastro",
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.8",
            "pre-commit>=2.0",
        ],
        "docs": [
            "sphinx>=4.0",
            "sphinx-rtd-theme>=1.0",
            "nbsphinx>=0.8",
            "pandoc>=1.0",
        ],
        "notebooks": [
            "jupyter>=1.0",
            "ipykernel>=6.0",
            "matplotlib>=3.0",
            "seaborn>=0.11",
        ],
        "phylo": [
            "scikit-bio>=0.5.6",
        ],
    },
    include_package_data=True,
    package_data={
        "plastro": ["data/*.csv", "data/*.h5ad"],
    },
    entry_points={
        "console_scripts": [
            "plastro=plastro.cli:main",
        ],
    },
    keywords=[
        "single-cell",
        "plasticity", 
        "lineage-tracing",
        "phylogeny",
        "bioinformatics",
        "computational-biology",
        "cellular-plasticity",
        "CRISPR",
    ],
    zip_safe=False,
)