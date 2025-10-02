
import gc
from os.path import dirname, join
import multiprocessing
import sys
import time
import unittest
import warnings
import os

from unittest.suite import TestSuite
from numba.testing import load_testsuite


try:
    import faulthandler
except ImportError:
    faulthandler = None
else:
    try:
        # May fail in IPython Notebook with UnsupportedOperation
        faulthandler.enable()
    except Exception as e:
        msg = "Failed to enable faulthandler due to:\n{err}"
        warnings.warn(msg.format(err=e))

def load_tests(loader, tests, pattern):
    suite = TestSuite()
    suite.addTests(load_testsuite(loader, dirname(__file__)))
    # Numba CUDA tests are located in a separate directory:
    cuda_dir = join(dirname(dirname(__file__)), 'cuda/tests')
    if os.path.isdir(cuda_dir):
        suite.addTests(loader.discover(cuda_dir))
    else:
        warnings.warn(f"CUDA test directory not found: {cuda_dir}, skipping CUDA tests.")
    return suite

