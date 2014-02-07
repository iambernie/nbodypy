#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

""" 
Timers
"""

class Timer(object):
    """
    Context Manager Class to time functions.

    Example
    -------
 
    def myfunction():
        for i in range(100000):
            math.sin(i)**2*math.cos(i)**3

    with Timer(verbose=True) as timer:
        myfunction()

    print(timer.secs)

    """
    def __init__(self, verbose=False):
        self.verbose = verbose

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.secs = self.end - self.start
        self.msecs = self.secs * 1000  # millisecs
        if self.verbose:
            print('Elapsed Time: %f ms'%self.msecs)

def example_usage_timer():
    import math

    def myfunction():
        for i in range(100000):
            math.sin(i)**2*math.cos(i)**3

    with Timer(verbose=True) as timer:
        myfunction()
 
    print(timer.secs)


if __name__ == "__main__":
    example_usage_timer()
