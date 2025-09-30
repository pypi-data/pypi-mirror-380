#!/usr/bin/env python
import unittest
import sys
import os

# Add the parent directory to sys.path to ensure imports work correctly
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

# Discover and run all tests
loader = unittest.TestLoader()
start_dir = os.path.dirname(__file__)
suite = loader.discover(start_dir, pattern="*_test.py")

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)

# Return non-zero exit code if tests failed
sys.exit(not result.wasSuccessful())
