import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="generations",
    version="1.3.0",
    author="M. Marek-Spartz",
    author_email="patt0335@umn.edu",
    description="A set of recursive population models for ecologists",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alfalimajuliett/generations",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=(
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities", "Environment :: Console"),
)
