# generations

A set of recursive population models for ecologists including:

- Nicholson Bailey host-parasitoid model
- Weed-herbivore coupled model for an annual plant that forms a seed bank from [Buckley et al. 2005](http://onlinelibrary.wiley.com/doi/10.1111/j.1365-2664.2005.00991.x/epdf)
- Weed-herbivore model for a biennial plant that forms a seed bank


## Installation

Generations is available from the [Python Package Index](https://pypi.org/project/generations/). It can be installed using `pip`:

    pip install generations


## Running

Once installed, the user can run the various models in `generations` by entering the following commands. Python's `-m` flag imports and runs the specified module. Each population model in `generations` is in it's own module:

    python -m generations.nicholson_bailey

    python -m generations.buckley

    python -m generations.biennial

### Visualization

Generations requires the [Bokeh](https://pypi.org/project/bokeh/) Python package to generate interactive plots of the simulation outputs in the browser. This functionality is attached to each modeling module. When the module runs, it automatically generates a .csv of the population densities for each organism at each time step Bokeh uses that .csv to automatically generate an html page with an interactive plot of the results in the user's browser. 


### Custom parameters

The user can also create a copy of the default configuration file for the population model modules in their working directory. The file will be named `model_parameters.cfg`.

    python -m generations.create_config

The user can then edit parameters to fit their desired ecological system. Model parameters will be loaded from the working directory into the population models at runtime.


## Development

Generations source code is available on [GitHub](https://github.com/alfalimajuliett/generations).

    git clone https://github.com/alfalimajuliett/generations.git


### Testing

    ./test.sh

This will run the unit tests. If you have [pipenv](https://docs.pipenv.org/), it will also run a number of other checks:

- [`yapf`](https://github.com/google/yapf/): reformat the code automatically
- [`mypy`](http://mypy-lang.org): check for runtime errors like misnamed imports or variables, or incompatible types
- [`tox`](https://tox.readthedocs.io/en/latest/): run the unit tests against Python 2.7 and 3.7
- [`coverage`](https://github.com/nedbat/coveragepy): report on lines that are not covered by unit tests


### Uploading to PyPI

Install [pipenv](https://docs.pipenv.org/#install-pipenv-today) if you don't have it.

Increment the version in `setup.py`.

Run the tests one last time:

    ./test.sh

Build the distribution files:

    pipenv run python3 setup.py sdist bdist_wheel

Upload using [`twine`](https://github.com/pypa/twine). It will prompt for your PyPI password:

    pipenv run twine upload dist/*

Commit the version, create a tag, and push tags:

    git commit -am "$version"
    git tag $version
    git push --tags
    git push
