from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="datacleanerx",
    version="0.2.0",
    author="Satyam Singh",
    author_email="satyamsingh7734@example.com",
    description="Automated dataset cleaner for machine learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SatyamSingh8306/datacleanerx",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "pandas>=1.3.0",
        "numpy>=1.20.0",
        "scikit-learn>=1.0.0",
    ],
)