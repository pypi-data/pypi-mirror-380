from setuptools import setup, find_packages

setup(
    name="installer-ml",
    version="1.1.5",
    description="Auto install and import ML/DL libraries in Python",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Nguyen Tan Dat",
    author_email="tandatnguyen89@gmail.com",
    url="https://github.com/tandatnguyen89",
    license="MIT",
    packages=["installer_ml"],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
