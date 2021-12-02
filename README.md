# Repo for Advent of Code 2021

## Installation

### Using the `devcontainter`
Clone the repo and open in [VScode](https://code.visualstudio.com/).  VScode will recognize the presence of devcontainer configuration and prompt you reopen the repository inside the container after building the Docker Image.   Afterwards simply install dependencies with `poetry install`

### Using Binder
Click the button below to build an image with all the dependencies installed with a jupyter environment in the browser.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sullivancolin/advent_of_code.git/HEAD)

### Manually
Before installing dependencies please make sure you have a distribution of
[python 3.10](https://www.python.org/downloads/release/python-3100/) available and installed [poetry](https://python-poetry.org/).  To install dependencies create a new virtual environment and install with `poetry install`

## Running the solutions
The solutions for each day will be in its own package with one module for each part.  All input data will be in the `data` directory labeled by day. The `tests` directory contains one module for each day with tests for both parts.  The solution for each part can be printed by run each module as a script. For example to get the solution to Day 1, Part 1, run
```shell
$ python -m advent_of_code.day1.part1
```

## Running the tests
To run all tests from the root directory simply run `pytest`, or run tests individually from VScode from the testing pane, once they have been automatically discovered.

## Runing the tests
Each day has it's own tests using the provided example input data.  To run the test for a single day run
```shell
advent_of_code/day1 $ pytest
```
or to run the tests for all days you can run `pytest` from the root directory.
