# `aoc`

CLI interface for `aoc` package.

**Usage**:

```console
$ aoc [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `-v, --version`: Print the current version.
* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `day1`: Command for running day1 stars
* `debug-version-info`: Print debug information to terminal.

## `aoc day1`

Command for running day1 stars

**Usage**:

```console
$ aoc day1 [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `part1`: Calculate the sum of all the first and...
* `part2`: Calculate the sum of all the first and...

### `aoc day1 part1`

Calculate the sum of all the first and last digits on each line concatenated together.

**Usage**:

```console
$ aoc day1 part1 [OPTIONS] [INPUT_PATH]
```

**Arguments**:

* `[INPUT_PATH]`: Path to file containing the input  [default: data/day1.txt]

**Options**:

* `--help`: Show this message and exit.

### `aoc day1 part2`

Calculate the sum of all the first and last number words or digits on each line concatenated together.

**Usage**:

```console
$ aoc day1 part2 [OPTIONS] [INPUT_PATH]
```

**Arguments**:

* `[INPUT_PATH]`: Path to file containing the input  [default: data/day1.txt]

**Options**:

* `--help`: Show this message and exit.

## `aoc debug-version-info`

Print debug information to terminal.

**Usage**:

```console
$ aoc debug-version-info [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.
