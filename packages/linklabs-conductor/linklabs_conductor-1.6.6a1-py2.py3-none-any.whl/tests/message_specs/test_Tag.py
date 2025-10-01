import logging
import unittest

import coloredlogs

from conductor.airfinder import devices as af_devs

LOG_LEVEL = "DEBUG"  # Log Level tests and of all submodules.
LOG = logging.getLogger(__name__)


class TagTests(unittest.TestCase):

    def __init__(self, test_name):
        super().__init__(test_name)

    def setUp(self):
        """ TODO """
        pass

    def tearDown(self):
        """ TODO """
        pass

    def test_TODO(self):
        """ Verifies nothing. """
        pass


if __name__ == '__main__':

    coloredlogs.install(level=LOG_LEVEL)

    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    suite.addTests(loader.loadTestsFromTestCase(TagTests))
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)
    suite = unittest.TestSuite()
