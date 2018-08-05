#!/usr/bin/env bash
set -e

if command -v pipenv >/dev/null 2>&1; then
    echo Pipenv detected.
    echo Running extended checks
    echo Installing dependencies using pipenv...
    pipenv install
    pipenv install -d

    echo Reformatting automatically...
    pipenv run yapf -i $(git ls-files | grep .py$)

    echo Checking types...
    pipenv run mypy generations tests

    echo Running unit tests against multiple python versions and reporting coverage...
    pipenv run tox

    echo Running programs as an integration test...
    python -m generations.nicholson_bailey
    python -m generations.buckley
    python -m generations.biennial

    echo Opening coverage report...
    open htmlcov/index.html # to browse coverage data in browser
else
    echo Pipenv not detected!
    echo For more information about pipenv: https://docs.pipenv.org
    echo Skipping some checks
    echo Running unit tests...
    python -m unittest discover
fi
