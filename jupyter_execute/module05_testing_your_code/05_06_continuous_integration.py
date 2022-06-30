#!/usr/bin/env python
# coding: utf-8

# # Continuous Integration
# 
# ## Test servers
# 
# Goal: 
# 
# 1. run tests nightly
# 2. run tests after each commit to github (or other)
# 3. run tests on different platforms
# 
# Various groups run servers that can be used to do this automatically.

# ## Memory and profiling
# 
# For compiled languages (C, C++, Fortran):
# * Checking for memory leaks with [valgrind](http://valgrind.org/):
#   `valgrind --leak-check=full program`
# * Checking cache hits and cache misses with
#   [cachegrind](http://valgrind.org/docs/manual/cg-manual.html):
#   `valgrind --tool=cachegrind program`
# * Profiling the code with [callgrind](http://valgrind.org/docs/manual/cl-manual.html):
#   `valgrind --tool=callgrind program`

# * Python: [profile](http://docs.python.org/2/library/profile.html) with [runsnake](http://www.vrplumber.com/programming/runsnakerun/)
# * R: [Rprof](http://stat.ethz.ch/R-manual/R-devel/library/utils/html/Rprof.html)
