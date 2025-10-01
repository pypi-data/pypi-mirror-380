import logging
import unittest

import coloredlogs

from conductor.airfinder import devices as af_devs
from conductor.airfinder.messages import DownlinkMessageSpec, \
    MissingDownlinkArgument, \
    ControlMessageNotSupported, \
    InvalidDownlinkMessageType

LOG_LEVEL = "DEBUG"  # Log Level tests and of all submodules.
LOG = logging.getLogger(__name__)


class LocationTests(unittest.TestCase):

    def __init__(self, test_name):
        super().__init__(test_name)

    def test_ConfigurationV1(self):
        """ Verifies building the Configuration Message. """
        spec_v1 = af_devs.location.LocationDownlinkMessageSpecV1()

        # Default Values
        msg = spec_v1.build_message("Configuration")
        exp = bytearray()
        exp.append(0x01)  # Msg Type
        exp.append(0x01)  # Message Spec Version
        exp.append(0x00)  # Change Mask
        exp.append(0x01)  # Advertising Enable
        for i in range(21):
            exp.append(0xff)  # Schedule
        exp.append(0x00)  # Heartbeat Interval
        exp.append(0x00)  # Heartbeat Interval
        exp.append(0x00)  # Heartbeat Interval
        exp.append(0x78)  # Heartbeat Interval
        exp.append(0x00)  # RSSI Adjustment
        exp.append(0x00)  # Location Weight
        exp.append(0x00)  # Location Group
        exp.append(0x00)  # TX Power
        self.assertSequenceEqual(msg, exp)

        # Specific Values
        msg = spec_v1.build_message("Configuration",
                                    # Omitting mask, auto gen.
                                    adv_en=True,
                                    # Omitted sched, checking mask gen.
                                    heartbeat=3434,
                                    rssi_adj=5,
                                    # Omitted loc_weight, checking mask gen.
                                    loc_group=54,
                                    tx_pwr=121)
        exp = bytearray()
        exp.append(0x01)  # Msg Type
        exp.append(0x01)  # Message Spec Version
        exp.append(0b01101101)  # Change Mask
        exp.append(0x01)  # Advertising Enable
        for i in range(21):
            exp.append(0xff)    # Schedule
        exp.append(0x00)  # Heartbeat Interval
        exp.append(0x00)  # Heartbeat Interval
        exp.append(0x0d)  # Heartbeat Interval
        exp.append(0x6a)  # Heartbeat Interval
        exp.append(0x05)  # RSSI Adjustment
        exp.append(0x00)  # Location Weight
        exp.append(0x36)  # Location Group
        exp.append(0x79)  # TX Power
        self.assertSequenceEqual(msg, exp)

    def test_ResetV1(self):
        """ Verifies building a V1 Reset Message. """
        spec_v1 = af_devs.location.LocationDownlinkMessageSpecV1()

        msg = spec_v1.build_message("Reset")
        exp = bytearray()
        exp.append(0x02)  # Msg Type
        exp.append(0x01)  # Message Spec Version
        exp.append(0xd5)  # Reset Value
        exp.append(0x83)  # Reset Value
        exp.append(0x7e)  # Reset Value
        exp.append(0xd6)  # Reset Value
        self.assertSequenceEqual(msg, exp)

    def test_ConfigurationV2(self):
        """ Verifies building a V2 Configuration Message. """
        spec_v2 = af_devs.location.LocationDownlinkMessageSpecV2()

        # Default Values
        msg = spec_v2.build_message("Configuration")
        exp = bytearray()
        exp.append(0x01)  # Msg Type
        exp.append(0x02)  # Message Spec Version
        exp.append(0x00)  # Change Mask
        exp.append(0x01)  # Advertising Enable
        for i in range(21):
            exp.append(0xff)  # Schedule
        exp.append(0x00)  # Heartbeat Interval
        exp.append(0x00)  # Heartbeat Interval
        exp.append(0x00)  # Heartbeat Interval
        exp.append(0x78)  # Heartbeat Interval
        exp.append(0x00)  # RSSI Adjustment
        exp.append(0x00)  # Location Weight
        exp.append(0x00)  # Location Group
        exp.append(0x00)  # TX Power
        self.assertSequenceEqual(msg, exp)

        # Specific Values
        msg = spec_v2.build_message("Configuration",
                                    # Omitting mask, auto gen.
                                    adv_en=True,
                                    # Omitted sched, checking mask gen.
                                    heartbeat=3434,
                                    rssi_adj=5,
                                    # Omitted loc_weight, checking mask gen.
                                    loc_group=54,
                                    tx_pwr=121)
        exp = bytearray()
        exp.append(0x01)  # Msg Type
        exp.append(0x02)  # Message Spec Version
        exp.append(0b01101101)  # Change Mask
        exp.append(0x01)  # Advertising Enable
        for i in range(21):
            exp.append(0xff)    # Schedule
        exp.append(0x00)  # Heartbeat Interval
        exp.append(0x00)  # Heartbeat Interval
        exp.append(0x0d)  # Heartbeat Interval
        exp.append(0x6a)  # Heartbeat Interval
        exp.append(0x05)  # RSSI Adjustment
        exp.append(0x00)  # Location Weight
        exp.append(0x36)  # Location Group
        exp.append(0x79)  # TX Power
        self.assertSequenceEqual(msg, exp)

    def test_ResetV2(self):
        """ Verifies building a V2 Reset Message. """
        spec_v2 = af_devs.location.LocationDownlinkMessageSpecV2()

        msg = spec_v2.build_message("Reset")
        exp = bytearray()
        exp.append(0x02)  # Msg Type
        exp.append(0x02)  # Message Spec Version
        exp.append(0xd5)  # Reset Value
        exp.append(0x83)  # Reset Value
        exp.append(0x7e)  # Reset Value
        exp.append(0xd6)  # Reset Value
        self.assertSequenceEqual(msg, exp)

    def test_ConfigurationV3(self):
        """ Verifies building a V3 Configuration Message. """
        spec_v3 = af_devs.location.LocationDownlinkMessageSpecV3()

        # Default Values
        msg = spec_v3.build_message("Configuration")
        exp = bytearray()
        exp.append(0x01)  # Msg Type
        exp.append(0x03)  # Message Spec Version
        exp.append(0x00)  # Change Mask
        exp.append(0x01)  # Advertising Enable
        for i in range(21):
            exp.append(0xff)  # Schedule
        exp.append(0x00)  # Heartbeat Interval
        exp.append(0x00)  # Heartbeat Interval
        exp.append(0x00)  # Heartbeat Interval
        exp.append(0x78)  # Heartbeat Interval
        exp.append(0x00)  # RSSI Adjustment
        exp.append(0x00)  # Location Weight
        exp.append(0x00)  # Location Group
        exp.append(0x00)  # TX Power
        self.assertSequenceEqual(msg, exp)

        # Specific Values
        msg = spec_v3.build_message("Configuration",
                                    # Omitting mask, auto gen.
                                    adv_en=True,
                                    # Omitted sched, checking mask gen.
                                    heartbeat=3434,
                                    rssi_adj=5,
                                    # Omitted loc_weight, checking mask gen.
                                    loc_group=54,
                                    tx_pwr=121)
        exp = bytearray()
        exp.append(0x01)  # Msg Type
        exp.append(0x03)  # Message Spec Version
        exp.append(0b01101101)  # Change Mask
        exp.append(0x01)  # Advertising Enable
        for i in range(21):
            exp.append(0xff)    # Schedule
        exp.append(0x00)  # Heartbeat Interval
        exp.append(0x00)  # Heartbeat Interval
        exp.append(0x0d)  # Heartbeat Interval
        exp.append(0x6a)  # Heartbeat Interval
        exp.append(0x05)  # RSSI Adjustment
        exp.append(0x00)  # Location Weight
        exp.append(0x36)  # Location Group
        exp.append(0x79)  # TX Power
        self.assertSequenceEqual(msg, exp)

    def test_ResetV3(self):
        """ Verifies building a V3 Reset Message. """
        spec_v3 = af_devs.location.LocationDownlinkMessageSpecV3()

        msg = spec_v3.build_message("Reset")
        exp = bytearray()
        exp.append(0x02)  # Msg Type
        exp.append(0x03)  # Message Spec Version
        exp.append(0xd5)  # Reset Value
        exp.append(0x83)  # Reset Value
        exp.append(0x7e)  # Reset Value
        exp.append(0xd6)  # Reset Value
        self.assertSequenceEqual(msg, exp)

    def test_UltrasoundChangeV3(self):
        """ Verifies building a V3 UltrasoundChange Message. """
        spec_v3 = af_devs.location.LocationDownlinkMessageSpecV3()

        # Default Values
        msg = spec_v3.build_message("UltrasoundChange")
        exp = bytearray()
        exp.append(0x03)  # Msg Type
        exp.append(0x03)  # Message Spec Version
        exp.append(0x00)  # Change Mask
        exp.append(0x00)  # Frequency
        exp.append(0x28)  # Frequency
        exp.append(0x07)  # Code Length
        exp.append(0x02)  # BPS Idx
        exp.append(0x04)  # Deviation
        exp.append(0x00)  # Code Type
        exp.append(0x04)  # Num Repeat
        self.assertSequenceEqual(msg, exp)

        # Specific Values
        msg = spec_v3.build_message("UltrasoundChange",
                                    # Omitting mask, auto gen.
                                    freq=23542,
                                    code_len=41,
                                    # Omitted bps, checking mask gen.
                                    deviation=34,
                                    code_type=5,
                                    num_repeat=21)
        exp = bytearray()
        exp.append(0x03)  # Msg Type
        exp.append(0x03)  # Message Spec Version
        exp.append(0b00111011)  # Change Mask
        exp.append(0x5b)  # Frequency
        exp.append(0xf6)  # Frequency
        exp.append(0x29)  # Code Length
        exp.append(0x02)  # BPS Idx
        exp.append(0x22)  # Deviation
        exp.append(0x05)  # Code Type
        exp.append(0x15)  # Num Repeat
        self.assertSequenceEqual(msg, exp)

    def test_ConfigurationV4(self):
        """ Verifies building a V3 Configuration Message. """
        spec_v4 = af_devs.location.LocationDownlinkMessageSpecV4()

        # Default Values
        msg = spec_v4.build_message("Configuration")
        exp = bytearray()
        exp.append(0x01)  # Msg Type
        exp.append(0x04)  # Message Spec Version
        exp.append(0x00)  # Change Mask
        exp.append(0x01)  # Advertising Enable
        for i in range(21):
            exp.append(0xff)  # Schedule
        exp.append(0x00)  # Heartbeat Interval
        exp.append(0x00)  # Heartbeat Interval
        exp.append(0x00)  # Heartbeat Interval
        exp.append(0x78)  # Heartbeat Interval
        exp.append(0x00)  # RSSI Adjustment
        exp.append(0x00)  # Location Weight
        exp.append(0x00)  # Location Group
        exp.append(0x00)  # TX Power
        self.assertSequenceEqual(msg, exp)

        # Specific Values
        msg = spec_v4.build_message("Configuration",
                                    # Omitting mask, auto gen.
                                    adv_en=True,
                                    # Omitted sched, checking mask gen.
                                    heartbeat=3434,
                                    rssi_adj=5,
                                    # Omitted loc_weight, checking mask gen.
                                    loc_group=54,
                                    tx_pwr=121)
        exp = bytearray()
        exp.append(0x01)  # Msg Type
        exp.append(0x04)  # Message Spec Version
        exp.append(0b01101101)  # Change Mask
        exp.append(0x01)  # Advertising Enable
        for i in range(21):
            exp.append(0xff)    # Schedule
        exp.append(0x00)  # Heartbeat Interval
        exp.append(0x00)  # Heartbeat Interval
        exp.append(0x0d)  # Heartbeat Interval
        exp.append(0x6a)  # Heartbeat Interval
        exp.append(0x05)  # RSSI Adjustment
        exp.append(0x00)  # Location Weight
        exp.append(0x36)  # Location Group
        exp.append(0x79)  # TX Power
        self.assertSequenceEqual(msg, exp)

    def test_ResetV4(self):
        """ Verifies building a V3 Reset Message. """
        spec_v4 = af_devs.location.LocationDownlinkMessageSpecV4()

        msg = spec_v4.build_message("Reset")
        exp = bytearray()
        exp.append(0x02)  # Msg Type
        exp.append(0x04)  # Message Spec Version
        exp.append(0xd5)  # Reset Value
        exp.append(0x83)  # Reset Value
        exp.append(0x7e)  # Reset Value
        exp.append(0xd6)  # Reset Value
        self.assertSequenceEqual(msg, exp)

    def test_UltrasoundChangeV4(self):
        """ Verifies building a V3 UltrasoundChange Message. """
        spec_v4 = af_devs.location.LocationDownlinkMessageSpecV4()

        # Default Values
        msg = spec_v4.build_message("UltrasoundChange")
        exp = bytearray()
        exp.append(0x03)  # Msg Type
        exp.append(0x04)  # Message Spec Version
        exp.append(0x00)  # Change Mask
        exp.append(0x00)  # Frequency
        exp.append(0x28)  # Frequency
        exp.append(0x07)  # Code Length
        exp.append(0x02)  # BPS Idx
        exp.append(0x04)  # Deviation
        exp.append(0x00)  # Code Type
        exp.append(0x04)  # Num Repeat
        self.assertSequenceEqual(msg, exp)

        # Specific Values
        msg = spec_v4.build_message("UltrasoundChange",
                                    # Omitting mask, auto gen.
                                    freq=23542,
                                    code_len=41,
                                    # Omitted bps, checking mask gen.
                                    deviation=34,
                                    code_type=5,
                                    num_repeat=21)
        exp = bytearray()
        exp.append(0x03)  # Msg Type
        exp.append(0x04)  # Message Spec Version
        exp.append(0b00111011)  # Change Mask
        exp.append(0x5b)  # Frequency
        exp.append(0xf6)  # Frequency
        exp.append(0x29)  # Code Length
        exp.append(0x02)  # BPS Idx
        exp.append(0x22)  # Deviation
        exp.append(0x05)  # Code Type
        exp.append(0x15)  # Num Repeat
        self.assertSequenceEqual(msg, exp)

    def test_MakeTestTagV4(self):
        """ Verifies building a V3 Reset Message. """
        spec_v4 = af_devs.location.LocationDownlinkMessageSpecV4()

        msg = spec_v4.build_message("MakeTestTag")
        exp = bytearray()
        exp.append(0x04)  # Msg Type
        exp.append(0x04)  # Message Spec Version
        exp.append(0x66)  # SLA Value
        exp.append(0x36)  # SLA Value
        exp.append(0x35)  # SLA Value
        exp.append(0x38)  # SLA Value
        self.assertSequenceEqual(msg, exp)

    def test_ChangeNetTokenV4(self):
        """ Verifies building a V3 Reset Message. """
        spec_v4 = af_devs.location.LocationDownlinkMessageSpecV4()

        msg = spec_v4.build_message("ChangeNetToken",
                                    network_token=0xaabbccdd)
        exp = bytearray()
        exp.append(0x05)  # Msg Type
        exp.append(0x04)  # Message Spec Version
        exp.append(0x54)  # Net token code
        exp.append(0x4f)  # Net token code
        exp.append(0x4b)  # Net token code
        exp.append(0x45)  # Net token code
        exp.append(0x4e)  # Net token code
        exp.append(0xaa)  # Network Token
        exp.append(0xbb)  # Network Token
        exp.append(0xcc)  # Network Token
        exp.append(0xdd)  # Network Token
        self.assertSequenceEqual(msg, exp)


if __name__ == '__main__':

    coloredlogs.install(level=LOG_LEVEL)

    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    suite.addTests(loader.loadTestsFromTestCase(LocationTests))
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)
    suite = unittest.TestSuite()
