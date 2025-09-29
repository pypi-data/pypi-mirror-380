#!/usr/bin/env python3

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="py-lite-edu",
    version="0.1.1",
    author="DekimDev",
    author_email="collins.vv.dev@gmail.com",
    description="Упрощённый Python для обучения детей программированию",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/QueenDekim/pylite",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Education",
        "Topic :: Software Development :: Interpreters",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "pylite=pylite.cli:main",
        ],
    },
    install_requires=[
        # Используем только стандартную библиотеку Python
    ],
)
