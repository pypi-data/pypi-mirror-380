#!/usr/bin/env python3

from setuptools import setup, find_packages
import pathlib

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="desmos-studio",
    version="1.0.0",
    description="Convert images to mathematical curves for Desmos or matplotlib",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/image2curves",
    author="Yusuf Sabuwala",
    author_email="yusuff.0279@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Multimedia :: Graphics :: Graphics Conversion",
    ],
    keywords="image tracing, desmos, matplotlib, svg, potrace, bezier curves",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "matplotlib>=3.0.0",
        "svgpathtools>=1.4.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black",
            "flake8",
            "twine",
            "build",
        ],
    },
    entry_points={
        "console_scripts": [
            "desmos-art=desmos_art.cli:main",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/yourusername/image2curves/issues",
        "Source": "https://github.com/yourusername/image2curves",
        "Documentation": "https://github.com/yourusername/image2curves#readme",
    },
    include_package_data=True,
    zip_safe=False,
)