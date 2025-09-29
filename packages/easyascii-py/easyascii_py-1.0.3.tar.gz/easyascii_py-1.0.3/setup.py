from setuptools import setup

setup(
    name="easyascii-py",
    version="1.0.3",
    author="Matttz",
    author_email="proactivestudiocomercial@gmail.com",
    description="A simple, zero-dependency library for creating ASCII art and console UIs.",
    long_description="Easy ASCII - A comprehensive, single-file, zero-dependency Python library for creating beautiful and functional text-based user interfaces and ASCII art.  | Github Page for full documentation: https://github.com/Matt-The-Generico/easyascii  |  License: MIT: https://opensource.org/licenses/MIT  |  Easy ASCII is designed to be incredibly simple to use while providing a powerful set of tools for command-line applications. Whether you need to display data in a clean table, create an eye-catching banner, or show progress for a long-running task, this library has you covered.",
    long_description_content_type="text/markdown",
    url="https://github.com/Matt-The-Generico/easyascii",
    
    py_modules=["easyascii"],
    
    # Metadata for PyPI
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Terminals",
        "Topic :: Text Processing :: General",
    ],
    python_requires='>=3.6',
)