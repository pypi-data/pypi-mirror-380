import logging
import unittest

import coloredlogs

from conductor.airfinder import devices as af_devs

LOG = logging.getLogger(__name__)
LOG_LEVEL = logging.DEBUG


class AlertTagTests(unittest.TestCase):

    def __init__(self, test_name):
        super().__init__(test_name)

    def test_ConfigurationV1(self):
        """ Verifies building a V1 Configuration Message. """
        spec_v1 = af_devs.alert_tag.AlertTagDownlinkMessageSpecV1()

        # Default Values
        msg = spec_v1.build_message("Configuration")
        exp = bytearray()
        exp.append(0x01)  # Msg Type
        exp.append(0x01)  # Message Spec Version
        exp.append(0x00)  # Change Mask
        exp.append(0x02)  # Idle Heartbeat
        exp.append(0x58)  # Idle Heartbeat
        exp.append(0x1e)  # Alert Heartbeat Interval
        exp.append(0x0f)  # Alert Location Update
        exp.append(0x03)  # Network Lost Scan Count
        exp.append(0x01)  # Network Lost Scan Interval
        exp.append(0x2c)  # Network Lost Scan Interval
        exp.append(0x03)  # Max SymBLE Retries
        exp.append(0x03)  # Button Hold Length
        exp.append(0x01)  # Audible Alarm Enable
        self.assertSequenceEqual(msg, exp)

        # Specific Values
        msg = spec_v1.build_message("Configuration",
                                    # Omit mask, autogen.
                                    heartbeat=3527,
                                    # Omit alert heartbeat, check mask.
                                    alert_loc_upd=7,
                                    net_lost_scan_count=12,
                                    net_lost_scan_int=1462,
                                    # Omit Max SymBLE Retries, check mask.
                                    # Omit Button Hold Len, check mask.
                                    audible_alarm_en=False)
        exp = bytearray()
        exp.append(0x01)  # Msg Type
        exp.append(0x01)  # Message Spec Version
        exp.append(0b10011101)  # Change Mask
        exp.append(0x0d)  # Idle Heartbeat
        exp.append(0xc7)  # Idle Heartbeat
        exp.append(0x1e)  # Alert Heartbeat Interval
        exp.append(0x07)  # Alert Location Update
        exp.append(0x0c)  # Network Lost Scan Count
        exp.append(0x05)  # Network Lost Scan Interval
        exp.append(0xb6)  # Network Lost Scan Interval
        exp.append(0x03)  # Max SymBLE Retries
        exp.append(0x03)  # Button Hold Length
        exp.append(0x00)  # Audible Alarm Enable
        self.assertSequenceEqual(msg, exp)

    def test_AckV1(self):
        """ Verifies building a V1 ACK Message. """
        spec_v1 = af_devs.alert_tag.AlertTagDownlinkMessageSpecV1()

        # Default Values
        msg = spec_v1.build_message("Ack")
        exp = bytearray()
        exp.append(0x06)  # Msg Type
        exp.append(0x01)  # Message Spec Version
        self.assertSequenceEqual(msg, exp)

    def test_CloseV1(self):
        """ Verifies building a V1 ACK Message. """
        spec_v1 = af_devs.alert_tag.AlertTagDownlinkMessageSpecV1()

        # Default Values
        msg = spec_v1.build_message("Close")
        exp = bytearray()
        exp.append(0x07)  # Msg Type
        exp.append(0x01)  # Message Spec Version
        self.assertSequenceEqual(msg, exp)

    def test_ConfigurationV2(self):
        """ Verifies building a V2 Configuration Message. """
        spec_v2 = af_devs.alert_tag.AlertTagDownlinkMessageSpecV2()

        # Default Values
        msg = spec_v2.build_message("Configuration")
        exp = bytearray()
        exp.append(0x01)  # Msg Type
        exp.append(0x02)  # Message Spec Version
        exp.append(0x00)  # Change Mask
        exp.append(0x00)  # Change Mask
        exp.append(0x02)  # Idle Heartbeat
        exp.append(0x58)  # Idle Heartbeat
        exp.append(0x1e)  # Alert Heartbeat Interval
        exp.append(0x0f)  # Alert Location Update
        exp.append(0x03)  # Network Lost Scan Count
        exp.append(0x01)  # Network Lost Scan Interval
        exp.append(0x2c)  # Network Lost Scan Interval
        exp.append(0x03)  # Max SymBLE Retries
        exp.append(0x03)  # Button Hold Length
        exp.append(0x01)  # Audible Alarm Enable
        exp.append(0x40)  # U Lite Flags
        self.assertSequenceEqual(msg, exp)

        # Specific Values
        msg = spec_v2.build_message("Configuration",
                                    # Omit mask, autogen.
                                    heartbeat=3527,
                                    alert_heartbeat=70,
                                    # Omit alert location update
                                    net_lost_scan_count=12,
                                    net_lost_scan_int=1462,
                                    max_symble_retries=43,
                                    button_hold_len=82,
                                    # Omit Audible Alarm Enable
                                    ulite_flags=0b11000000)
        exp = bytearray()
        exp.append(0x01)  # Msg Type
        exp.append(0x02)  # Message Spec Version
        exp.append(0b00000001)  # Change Mask
        exp.append(0b01111011)  # Change Mask
        exp.append(0x0d)  # Idle Heartbeat
        exp.append(0xc7)  # Idle Heartbeat
        exp.append(0x46)  # Alert Heartbeat Interval
        exp.append(0x0f)  # Alert Location Update
        exp.append(0x0c)  # Network Lost Scan Count
        exp.append(0x05)  # Network Lost Scan Interval
        exp.append(0xb6)  # Network Lost Scan Interval
        exp.append(0x2b)  # Max SymBLE Retries
        exp.append(0x52)  # Button Hold Length
        exp.append(0x01)  # Audible Alarm Enable
        exp.append(0xc0)  # U Lite Flags
        self.assertSequenceEqual(msg, exp)

    def test_AckV2(self):
        """ Verifies building a V2 ACK Message. """
        spec_v2 = af_devs.alert_tag.AlertTagDownlinkMessageSpecV2()

        # Default Values
        msg = spec_v2.build_message("Ack")
        exp = bytearray()
        exp.append(0x06)  # Msg Type
        exp.append(0x02)  # Message Spec Version
        self.assertSequenceEqual(msg, exp)

    def test_CloseV2(self):
        """ Verifies building a V2 ACK Message. """
        spec_v2 = af_devs.alert_tag.AlertTagDownlinkMessageSpecV2()

        # Default Values
        msg = spec_v2.build_message("Close")
        exp = bytearray()
        exp.append(0x07)  # Msg Type
        exp.append(0x02)  # Message Spec Version
        self.assertSequenceEqual(msg, exp)


if __name__ == '__main__':

    coloredlogs.install(level=LOG_LEVEL)

    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    suite.addTests(loader.loadTestsFromTestCase(AlertTagTests))
