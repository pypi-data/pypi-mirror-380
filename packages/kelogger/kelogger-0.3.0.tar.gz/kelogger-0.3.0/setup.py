from setuptools import setup, find_packages

setup(
    name="kelogger",
    version="0.3.0",
    description="Automatic error logging for Kaggle kernels",
    author="Brij Patel",
    packages=find_packages(),
    python_requires=">=3.6",
)
