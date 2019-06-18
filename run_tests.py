import unittest
import sys

from tests.DataProviderTest import OpenWeatherMapTest
from tests import MyWeatherTest
from tests import TextGeneratorTest

loader = unittest.TestLoader()

suite = loader.loadTestsFromModule(MyWeatherTest)
suite.addTests(loader.loadTestsFromModule(OpenWeatherMapTest))
suite.addTests(loader.loadTestsFromModule(TextGeneratorTest))

runner = unittest.TextTestRunner(verbosity=2)
hasFailedTests = not runner.run(suite).wasSuccessful()

if hasFailedTests:
    sys.exit(1)