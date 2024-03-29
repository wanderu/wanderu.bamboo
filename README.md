# wanderu.bamboo

A reliable distributed redis-backed job queuing system with ack/fail semantics
and support for multiple languages.

## Client libraries:

    * Go version: https://bitbucket.org/offero/go-bamboo
    * Python version: https://bitbucket.org/wanderua/wanderu.bamboo
    * Javascript version: https://bitbucket.org/offero/jsbamboo
    * Lua Scripts: https://github.com/wanderu/bamboo-scripts.git

## Build

To build the package

    git clone --recursive https://bitbucket.org/wanderua/wanderu.bamboo.git
    python setup.py bdist_wheel
    ls dist/

## Test

To run the tests:

    pip install nose coverage
    python setup.py nosetests
    coverage report -m
