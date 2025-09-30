from setuptools import setup, find_packages
import os

# Read the contents of README file for long description
this_directory = os.path.abspath(os.path.dirname(__file__))
try:
    with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = "GDD - Data Science and Machine Learning Package"

setup(
    name="gdd-package",
    version="0.1.3",
    author="gdd02",
    author_email="gdd02@example.com",
    description="GDD - A comprehensive data science and machine learning package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gdd02/gdd-package",
    packages=find_packages(),
    install_requires=[
        "pandas>=1.3.0,<2.1.0",
        "numpy>=1.21.0,<2.0.0",
        "matplotlib>=3.3.0",
        "scikit-learn>=1.0.0",
        "mlxtend>=0.19.0",
        "scipy>=1.7.0"
    ],
    include_package_data=True,
    package_data={
        "gdd": ["../datasets/*.csv"]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    keywords="data science, machine learning, analytics, clustering, classification",
    project_urls={
        "Bug Reports": "https://github.com/gdd02/gdd-package/issues",
        "Source": "https://github.com/gdd02/gdd-package",
    },
)