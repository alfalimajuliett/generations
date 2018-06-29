import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="generations",
    version="0.0.1",
    author="M. Marek-Spartz",
    author_email="patt0335@umn.edu",
    description="A set of recursive population models for ecologists",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alfalimajuliett/generations",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
