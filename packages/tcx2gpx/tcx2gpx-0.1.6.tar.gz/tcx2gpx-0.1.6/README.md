[![PyPI version](https://badge.fury.io/py/tcx2gpx.svg)](https://badge.fury.io/py/tcx2gpx)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/tcx2gpx)
[![Code style: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json))](https://github.com/astral-sh/ruff)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Code style: flake8](https://img.shields.io/badge/code%20style-flake8-456789.svg)](https://github.com/psf/flake8)
[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier)
[![Downloads](https://static.pepy.tech/badge/tcx2gpx)](https://pepy.tech/project/tcx2gpx)
[![Downloads](https://static.pepy.tech/badge/tcx2gpx/month)](https://pepy.tech/project/tcx2gpx)
[![Downloads](https://static.pepy.tech/badge/tcx2gpx/week)](https://pepy.tech/project/tcx2gpx)
[![Donate](https://liberapay.com/assets/widgets/donate.svg)](https://liberapay.com/slackline/donate)

# tcx2gpx

This module converts the Garmin [tcx](https://en.wikipedia.org/wiki/Training_Center_XML) GPS file format
to the more commonly used [gpx](https://en.wikipedia.org/wiki/GPS_Exchange_Format) file format.
Both formats are a form of [XML](https://en.wikipedia.org/wiki/XML) but there are some fields in the former that are not
present in the later.
It uses two packages to do the grunt work [tcxparser](https://github.com/vkurup/python-tcxparser/) and
[gpxpy](https://github.com/tkrajina/gpxpy).

## Installation

Install from [PyPi.org](https://pypi.org/project/tcx2gpx) using...

```bash
pip install tcx2gpx
```

For more information on installing please refer to the [documentation][tcx2gpx-docs].

## Usage

The easiest way to use `tcx2gpx` is the command line version included. It will by default search the current directory
path for files with the `.tcx` extension and convert them to `.gpx`. There are various options available that change
where output is written or the directory that is searched. For details on usage see...

``` bash
tcx2gpx --help
```

For more information on usage please refer to the [documentation][tcx2gpx-docs].

## License

`tcx2gpx` is licensed under GNU GPL-3.0-only, please refer to the `COPYING` file for further details.

[tcx2gpx-docs]: https://tcx2gpx.readthedocs.io/en/latest/
