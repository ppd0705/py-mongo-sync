# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

version = "0.0.1"


def read_file(file):
    with open(file, "rt") as f:
        return f.read()

setup(
    name="mongo_sync_tool",
    version=version,
    description="mongo sync tool",
    author="Ricequant",
    author_email="public@ricequant.com",
    url="https://www.ricequant.com/",
    include_package_data=True,
    packages=find_packages(exclude=["example"]),
    install_requires=read_file("requirements.txt").strip(),
    python_requires=">=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
    entry_points={
        "console_scripts": [
            "mongo_sync = mongosync.__main__:main",
        ]
    },
    zip_safe=False,
)
