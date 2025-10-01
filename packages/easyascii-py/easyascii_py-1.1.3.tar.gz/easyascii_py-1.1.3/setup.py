from setuptools import setup

setup(
    name="easyascii-py",
    version="1.1.3",
    author="Matttz",
    author_email="proactivestudiocomercial@gmail.com",
    description="A simple, zero-dependency library for creating ASCII art and console UIs.",
    long_description="Easy ASCII - A comprehensive, single-file, zero-dependency Python library for creating beautiful and functional text-based user interfaces and ASCII art.  | Github Page for full documentation: https://github.com/Matt-The-Generico/easyascii  |  MIT License: https://opensource.org/licenses/MIT",
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