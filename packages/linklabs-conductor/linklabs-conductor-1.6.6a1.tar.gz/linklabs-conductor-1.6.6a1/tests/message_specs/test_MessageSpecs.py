import logging
import unittest

import coloredlogs

from conductor.airfinder.messages import DownlinkMessageSpec, \
    InvalidDownlinkMessageType

LOG_LEVEL = "DEBUG"  # Log Level tests and of all submodules.
LOG = logging.getLogger(__name__)


class BaseTests(unittest.TestCase):

    def __init__(self, test_name):
        super().__init__(test_name)

    def test_BaseMessage(self):
        """ Verifies the base message. """
        spec = DownlinkMessageSpec()
        spec.msg_types = {
            "Example": {
                'def': None,
                'struct': None,
                'defaults': None
            }
        }
        msg = spec.build_message('Example')
        expected = bytearray(b'\x01')
        self.assertSequenceEqual(msg, expected)

    def test_BaseMessageExplicitType(self):
        """ Verifies the base message. """
        spec = DownlinkMessageSpec()
        spec.msg_types = {
            "Example": {
                'type': 0x74,
                'def': None,
                'struct': None,
                'defaults': None
            }
        }
        msg = spec.build_message('Example')
        expected = bytearray(b'\x74')
        self.assertSequenceEqual(msg, expected)

    def test_NoAssertArgument(self):
        """ Verifies Unknown Argument doesn't Raise an Exception. """
        spec = DownlinkMessageSpec()
        spec.msg_types = {
            "Example": {
                'def': None,
                'struct': None,
                'defaults': None
            }
        }
        spec.build_message('Example', spec=5)

    def test_AssertMessageType(self):
        """ Verifies Unknown Messages Raise an Exception. """
        spec = DownlinkMessageSpec()
        with self.assertRaises(InvalidDownlinkMessageType):
            spec.build_message(msg_type=1)


if __name__ == '__main__':

    coloredlogs.install(level=LOG_LEVEL)

    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    # Validate library before Authentication.
    suite.addTests(loader.loadTestsFromTestCase(BaseTests))
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)
    suite = unittest.TestSuite()
