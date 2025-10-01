#!/usr/bin/env python3

from setuptools import setup, find_packages
import pathlib

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="desmos-studio",
    version="1.2.3",
    description="Convert images and videos to mathematical curves for Desmos or matplotlib",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/yusuff-bot/desmos-studio",
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
        "opencv-python>=4.5.0",
        "numpy>=1.19.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black",
            "flake8",
            "twine",
            "build",
        ],
        "video": [
            "yt-dlp>=2023.1.0",  # For YouTube downloads
        ],
    },
    entry_points={
        "console_scripts": [
            "desmos-studio=desmos_studio.cli:main",
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