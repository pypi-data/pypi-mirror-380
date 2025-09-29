from setuptools import setup
from setuptools.config.expand import find_packages

setup(
    name="asset-model-data-storage",
    version="1.0.0",
    description="Data storage library for asset model apps",
    author="Manoel Silva",
    packages=find_packages(),
    install_requires=["boto3", "botocore"],
    python_requires=">=3.7",
)
