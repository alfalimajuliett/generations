# generations

A set of recursive population models for ecologists including:

- Nicholson Bailey host-parasitoid model
- Weed-herbivore coupled model for an annual seedbanking plant from [Buckley et al. 2005](http://onlinelibrary.wiley.com/doi/10.1111/j.1365-2664.2005.00991.x/epdf)
- Weed-herbivore model for a biennial seedbanking plant

## Running

    python -m generations.nicholson_bailey
    python -m generations.buckley
    python -m generations.biennial

## Testing

    ./test.sh

This will run the unit tests. If you have [pipenv](https://docs.pipenv.org/), it will also run a number of other checks:

- [`yapf`](https://github.com/google/yapf/): reformat the code automatically
- [`mypy`](http://mypy-lang.org): check for runtime errors like misnamed imports or variables, or incompatible types
- [`tox`](https://tox.readthedocs.io/en/latest/): run the unit tests against Python 2.7 and 3.7
- [`coverage`](https://github.com/nedbat/coveragepy): report on lines that are not covered by unit tests


## Uploading to PyPI

Install [pipenv](https://docs.pipenv.org/#install-pipenv-today) if you don't have it.

Run the tests one last time:

    ./test.sh

Build the distribution files:

    pipenv run python3 setup.py sdist bdist_wheel

Upload using [`twine`](https://github.com/pypa/twine). It will prompt for your PyPI password:

    pipenv run twine upload dist/*
