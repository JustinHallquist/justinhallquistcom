#!/bin/bash
ulimit -t 2
exec ~/pypy/bin/pypy3.9 -m cProfile $@
