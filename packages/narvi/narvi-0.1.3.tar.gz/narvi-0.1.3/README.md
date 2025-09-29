# narvi

A lightweight Python Web Application Server based on a threading model (each web service instance runs in its own thread)

## Installation Options

Narvi supports python versions >= 3.11 and is tested on linux

Installation with tornado is recommended:

```
pip install narvi[tornado]
```

Installation without dependencies (using slower built-in webserver):

```
pip install narvi
```

## Documentation

For documentation please see the user guide: https://www.visualtopology.org/docs/narvi/index.html

## Building Documentation

Documentation is built using mkdocs which can be installed using:

```
pip install mkdocs
python -m pip install "mkdocstrings[python]"
python -m pip install mkdocs-material
```

To build documentation:

```
cd docs
./build.sh
```

