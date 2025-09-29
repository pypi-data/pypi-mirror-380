# Installation

There are several methods of installing `tcx2gpx` depending and which depends on whether you wish to simply use a stable
version that (hopefully) "Just Works(tm)" out of the box, try out the latest development version or get the development
version and perhaps contribute.

| Usage          | Install Method             |
|:---------------|:---------------------------|
| Convert Files  | PyPI install using `pip`   |
| Latest Version | GitLab install using `pip` |
| Contribute     | Fork and clone repository  |

## PyPI

`tcx2gpx` is available on [PyPI](https://pypi.org/project/tcx2gpx/), the Python Package Index. To install, ideally under
a virtual environment simply use the following to get the latest stable release.

``` bash
pip install tcx2gpx
```

GitLab using `pip`, replace `<branch>` with the branch you wish to clone.

``` bash
pip install tcx2gpx@git+https://gitlab.com/nshephard/tcx2gpx.git@main
```

## Contributing

Fork the repository and clone locally to work on it. Assuming you do not rename the repository when you fork it replace
`<username>` in the following with your GitLab username. Then install in editable mode.

``` bash
git clone git@gitlab.com:<username>/tcx2gpx.git
pip install -e .[dev,docs,pypi,test]
```

[pre-commit](https://pre-commit.com) is used to lint and check the code base conforms to PEP8 standards, to install the
hooks and ensure they are run before making commits you should install `pre-commit`.

``` bash
cd tcx2gpx
pre-commit install
```
