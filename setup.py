#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name="silver",
    version="0.0.1",
    description="PyTorch Lightning Project Setup",
    author="",
    author_email="",
    url="https://github.com/user/project",
    install_requires=["lightning", "hydra-core"],
    packages=find_packages(),

    entry_points={
        "console_scripts": [
            "silver_train = silver.train:main",
            "silver_eval = silver.eval:main",
        ]
    },
)
