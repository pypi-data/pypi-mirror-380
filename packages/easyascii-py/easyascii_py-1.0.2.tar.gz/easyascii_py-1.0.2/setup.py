from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="easyascii-py",
    version="1.0.2",
    author="Matttz",
    author_email="proactivestudiocomercial@gmail.com",
    description="A simple, zero-dependency library for creating ASCII art and console UIs.",
    long_description=long_description,
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