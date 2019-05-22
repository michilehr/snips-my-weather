import unittest

from tests.DataProviderTest import OpenWeatherMapTest
from tests import MyWeatherTest
from tests import TextGeneratorTest

loader = unittest.TestLoader()

suite = loader.loadTestsFromModule(MyWeatherTest)
suite.addTests(loader.loadTestsFromModule(OpenWeatherMapTest))
suite.addTests(loader.loadTestsFromModule(TextGeneratorTest))

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)
