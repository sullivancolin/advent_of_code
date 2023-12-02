<p align="center">
  <a href="https://sullivancolin.github.io/advent_of_code/"><img src="https://sullivancolin.github.io/advent_of_code/images/IMG_5796.JPG" width="300", height="300"  alt="aoc"></a>
</p>

[![CI](https://github.com/sullivancolin/advent_of_code/actions/workflows/CI.yml/badge.svg)](https://github.com/sullivancolin/advent_of_code/actions)

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/sullivancolin/advent_of_code)

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)

[![Open in Dev Containers](https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/sullivancolin/advent-of-code)

My record of current and past attempts at Advent of Code in Python.  (I usually peter out around the second week as they take more time and I'm spending more time with family.)
## Installation

### Using the `devcontainter`
Click the button above to launch into Codespaces, or clone the repo and open in [VScode](https://code.visualstudio.com/).  VScode will recognize the presence of devcontainer configuration and prompt you reopen the repository inside the container after building the Docker Image.

### Manually
Before installing dependencies please make sure you have an accessible distribution of python 3.11 available and installed [poetry](https://python-poetry.org/).  To create a new virtual environment and install all dependencies run
```sh
$ poetry install
```

## Running the solutions
The solutions for each day will be in its own sub package of the top level `aoc` package with one module for each part.  All input data will be in the `data` directory labeled by day. The `tests` directory contains one module for each day with tests for both parts.  The solution for each part can be printed by runing the include command line interface `aoc` with each day and part as subcommands. For example to get the solution to Day 1, Part 1, run
```sh
$ poetry run aoc day1 part1 data/day1.txt
```

To get more information on how to use the CLI just append `--help` to the command for example:
```sh
$ poetry run aoc --help
```

## Runing the tests
Each day has its own tests using the provided example input data.  To run the tests for all days run `pytest` from the root directory.

To run tests for a single day run `pytest tests/test_day1.py`


## Documentation
Documentation is provided via `mkdocs-material` and `mkdocstrings` and are generated from the source code, and host on github pages.
