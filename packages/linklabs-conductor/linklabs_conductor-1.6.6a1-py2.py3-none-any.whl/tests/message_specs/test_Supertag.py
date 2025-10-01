import logging
import unittest

import coloredlogs

from conductor.airfinder import devices as af_devs

LOG = logging.getLogger(__name__)
LOG_LEVEL = logging.DEBUG


class SupertagTests(unittest.TestCase):

    def __init__(self, test_name):
        super().__init__(test_name)

    @unittest.skip("todo")
    def test_ConfigurationV1(self):
        """ Verifies building a V1 Configuration Message. """
        spec_v1 = af_devs.supertag.SupertagDownlinkMessageSpecV1()

        # Default Values
        msg = spec_v1.build_message("Configuration")
        exp = bytearray()
        exp.append(0x01)  # 00: Msg Type
        exp.append(0x01)  # 01: Message Spec Version
        exp.append(0b00000000)  # 02: Change Mask
        exp.append(0b00000000)  # 03: Change Mask
        exp.append(0x00)  # 04: Heartbeat Interval
        exp.append(0x00)  # 05: Heartbeat Interval
        exp.append(0x00)  # 06: Heartbeat Interval
        exp.append(0x3c)  # 07: Heartbeat Interval
        exp.append(0x00)  # 08: No AP Heartbeat Interval
        exp.append(0x01)  # 09: No AP Heartbeat Interval
        exp.append(0x51)  # 10: No AP Heartbeat Interval
        exp.append(0x80)  # 11: No AP Heartbeat Interval
        exp.append(0x00)  # 12: No Sym Heartbeat Interval
        exp.append(0x01)  # 13: No Sym Heartbeat Interval
        exp.append(0x51)  # 14: No Sym Heartbeat Interval
        exp.append(0x80)  # 15: No Sym Heartbeat Interval
        exp.append(0x00)  # 16: Location Update Rate
        exp.append(0x00)  # 17: Location Update Rate
        exp.append(0x00)  # 18: Location Update Rate
        exp.append(0x0b)  # 19: Location Update Rate
        exp.append(0x00)  # 20: No AP Location Update Rate
        exp.append(0x00)  # 21: No AP Location Update Rate
        exp.append(0x54)  # 22: No AP Location Update Rate
        exp.append(0x60)  # 23: No AP Location Update Rate
        exp.append(0x00)  # 24: No Sym Location Update Rate
        exp.append(0x00)  # 25: No Sym Location Update Rate
        exp.append(0x54)  # 26: No Sym Location Update Rate
        exp.append(0x60)  # 27: No Sym Location Update Rate
        exp.append(0x04)  # 28: Scans per Fix
        exp.append(0x0a)  # 29: Max WIFI APs
        exp.append(0x00)  # 30: Max Cell IDs
        exp.append(0x1b)  # 31: Location Update Order
        exp.append(0x02)  # 32: Network Lost Timeout
        exp.append(0x58)  # 33: Network Lost Timeout
        exp.append(0x02)  # 34: Ref Lost Timeout
        exp.append(0x58)  # 35: Ref Lost Timeout
        exp.append(0x00)  # 36: Network Scan Interval
        exp.append(0xb4)  # 37: Network Scan Interval
        self.assertSequenceEqual(msg, exp)

        # Specified Values
        msg = spec_v1.build_message("Configuration",
                                    # Omit change mask.
                                    sym_heartbeat=0x02d3,
                                    # Omit No AP Heartbeat.
                                    lb_only_heartbeat=7323,
                                    location_update_rate=234,
                                    st_mode_heartbeat=9453,
                                    # Omit no sym loc upd
                                    scans_per_fix=7,
                                    # Omit no sym loc update

                                    max_wifi_aps=76,
                                    # Omit Max Cell IDs
                                    location_update_order=234,
                                    network_lost_timeout=54321,
                                    # Omit ref lost timeout
                                    network_scan_interval=34)

        exp = bytearray()
        exp.append(0x01)  # Msg Type
        exp.append(0x01)  # Message Spec Version
        exp.append(0b00010110)  # Change Mask 02
        exp.append(0b11001111)  # Change Mask 03
        exp.append(0x00)  # Heartbeat Interval 04
        exp.append(0x00)  # Heartbeat Interval 05
        exp.append(0x02)  # Heartbeat Interval 06
        exp.append(0xd3)  # Heartbeat Interval 07
        exp.append(0x00)  # No AP Heartbeat Interval 08
        exp.append(0x00)  # No AP Heartbeat Interval 09
        exp.append(0x51)  # No AP Heartbeat Interval
        exp.append(0x80)  # No AP Heartbeat Interval
        exp.append(0x00)  # No Sym Heartbeat Interval
        exp.append(0x00)  # No Sym Heartbeat Interval
        exp.append(0x1c)  # No Sym Heartbeat Interval
        exp.append(0x9b)  # No Sym Heartbeat Interval
        exp.append(0x00)  # Location Update Rate
        exp.append(0x00)  # Location Update Rate
        exp.append(0x00)  # Location Update Rate
        exp.append(0xea)  # Location Update Rate
        exp.append(0x00)  # No AP Location Update Rate
        exp.append(0x00)  # No AP Location Update Rate
        exp.append(0x24)  # No AP Location Update Rate
        exp.append(0xed)  # No AP Location Update Rate
        exp.append(0x00)  # No Sym Location Update Rate
        exp.append(0x00)  # No Sym Location Update Rate
        exp.append(0x54)  # No Sym Location Update Rate
        exp.append(0x60)  # No Sym Location Update Rate
        exp.append(0x07)  # Scans per Fix
        exp.append(0x4c)  # Max WIFI APs
        exp.append(0x00)  # Max Cell IDs
        exp.append(0xea)  # Location Update Order
        exp.append(0xd4)  # Network Lost Timeout
        exp.append(0x31)  # Network Lost Timeout
        exp.append(0x02)  # Ref Lost Timeout
        exp.append(0x58)  # Ref Lost Timeout
        exp.append(0x00)  # Network Scan Interval
        exp.append(0x22)  # Network Scan Interval
        self.assertSequenceEqual(msg, exp)

    @unittest.skip("todo")
    def test_ConfigurationV2(self):
        """ Verifies building a V2 Configuration Message. """
        spec_v2 = af_devs.supertag.SupertagDownlinkMessageSpecV2()

        # Default Values
        msg = spec_v2.build_message("Configuration")
        exp = bytearray()
        exp.append(0x01)  # 00: Msg Type
        exp.append(0x02)  # 01: Message Spec Version
        exp.append(0b00000000)  # 02: Change Mask
        exp.append(0b00000000)  # 03: Change Mask
        exp.append(0b00000000)  # 04: Change Mask
        exp.append(0b00000000)  # 05: Change Mask
        exp.append(0x00)  # 06: Heartbeat Interval
        exp.append(0x00)  # 07: Heartbeat Interval
        exp.append(0x00)  # 08: Heartbeat Interval
        exp.append(0x3c)  # 09: Heartbeat Interval
        exp.append(0x00)  # 10: No AP Heartbeat Interval
        exp.append(0x01)  # 11: No AP Heartbeat Interval
        exp.append(0x51)  # 12: No AP Heartbeat Interval
        exp.append(0x80)  # 13: No AP Heartbeat Interval
        exp.append(0x00)  # 14: No Sym Heartbeat Interval
        exp.append(0x01)  # 15: No Sym Heartbeat Interval
        exp.append(0x51)  # 16: No Sym Heartbeat Interval
        exp.append(0x80)  # 17: No Sym Heartbeat Interval
        exp.append(0x00)  # 18: Location Update Rate
        exp.append(0x00)  # 19: Location Update Rate
        exp.append(0x00)  # 20: Location Update Rate
        exp.append(0x0b)  # 21: Location Update Rate
        exp.append(0x00)  # 22: No AP Location Update Rate
        exp.append(0x00)  # 23: No AP Location Update Rate
        exp.append(0x00)  # 24: No AP Location Update Rate
        exp.append(0x3c)  # 25: No AP Location Update Rate
        exp.append(0x00)  # 26: No Sym Location Update Rate
        exp.append(0x00)  # 27: No Sym Location Update Rate
        exp.append(0x54)  # 28: No Sym Location Update Rate
        exp.append(0x60)  # 29: No Sym Location Update Rate
        exp.append(0x00)  # 30: Help Location Update Rate
        exp.append(0x00)  # 31: Help Location Update Rate
        exp.append(0x00)  # 32: Help Location Update Rate
        exp.append(0x0b)  # 33: Help Location Update Rate
        exp.append(0x04)  # 34: Scans per Fix
        exp.append(0x0a)  # 35: Max WIFI APs
        exp.append(0x00)  # 36: Max Cell IDs
        exp.append(0x1b)  # 37: Location Update Order
        exp.append(0x01)  # 38: Accel Enable
        exp.append(0x00)  # 39: Accel Duration
        exp.append(0x03)  # 40: Accel Duration
        exp.append(0x00)  # 41: Accel Threshold
        exp.append(0x50)  # 42: Accel Threshold
        exp.append(0x00)  # 43: Shock Threshold
        exp.append(0xa0)  # 44: Shock Threshold
        exp.append(0x00)  # 45: Cache Enable
        exp.append(0x00)  # 46: Cache Length
        exp.append(0x00)  # 47: GPS Power Mode
        exp.append(0x00)  # 48: GPS Timeout
        exp.append(0xb4)  # 49: GPS Timeout
        exp.append(0x02)  # 50: Network Lost Timeout
        exp.append(0x58)  # 51: Network Lost Timeout
        exp.append(0x02)  # 52: Ref Lost Timeout
        exp.append(0x58)  # 53: Ref Lost Timeout
        exp.append(0x00)  # 54: Network Scan Interval
        exp.append(0xb4)  # 55: Network Scan Interval
        self.assertSequenceEqual(msg, exp)

        # Specified Values
        msg = spec_v2.build_message("Configuration",
                                    # Omit change mask.

                                    sym_heartbeat=723,
                                    no_ap_heartbeat=7323,
                                    # Omit No Sym Heartbeat.
                                    location_update_rate=234,
                                    # Omit no ap loc upd
                                    no_sym_location_update_rate=9453,
                                    help_location_update_rate=2124,
                                    scans_per_fix=7,

                                    # Omit Max Wifi APs
                                    max_cell_ids=76,
                                    location_update_order=234,
                                    acc_enable=True,
                                    acc_duration=23445,
                                    # Omit acc_thresh
                                    shock_threshold=23523,
                                    cache_enable=True,

                                    cache_length=45,
                                    gps_power_mode=0,
                                    # omit gps_timeout
                                    net_lost_timeout=54321,
                                    # Omit ref lost timeout
                                    network_scan_interval=34)

        exp = bytearray()
        exp.append(0x01)  # 00: Msg Type
        exp.append(0x02)  # 01: Message Spec Version
        exp.append(0b00000000)  # 02: Change Mask
        exp.append(0b00101011)  # 03: Change Mask
        exp.append(0b11011110)  # 04: Change Mask
        exp.append(0b11101011)  # 05: Change Mask
        exp.append(0x00)  # 06: Heartbeat Interval
        exp.append(0x00)  # 07: Heartbeat Interval
        exp.append(0x02)  # 08: Heartbeat Interval
        exp.append(0xd3)  # 09: Heartbeat Interval
        exp.append(0x00)  # 10: No AP Heartbeat Interval
        exp.append(0x00)  # 11: No AP Heartbeat Interval
        exp.append(0x1c)  # 12: No AP Heartbeat Interval
        exp.append(0x9b)  # 13: No AP Heartbeat Interval
        exp.append(0x00)  # 14: No Sym Heartbeat Interval
        exp.append(0x01)  # 15: No Sym Heartbeat Interval
        exp.append(0x51)  # 16: No Sym Heartbeat Interval
        exp.append(0x80)  # 17: No Sym Heartbeat Interval
        exp.append(0x00)  # 18: Location Update Rate
        exp.append(0x00)  # 19: Location Update Rate
        exp.append(0x00)  # 20: Location Update Rate
        exp.append(0xea)  # 21: Location Update Rate
        exp.append(0x00)  # 22: No AP Location Update Rate
        exp.append(0x00)  # 23: No AP Location Update Rate
        exp.append(0x00)  # 24: No AP Location Update Rate
        exp.append(0x3c)  # 25: No AP Location Update Rate
        exp.append(0x00)  # 26: No Sym Location Update Rate
        exp.append(0x00)  # 27: No Sym Location Update Rate
        exp.append(0x24)  # 28: No Sym Location Update Rate
        exp.append(0xed)  # 29: No Sym Location Update Rate
        exp.append(0x00)  # 30: Help Location Update Rate
        exp.append(0x00)  # 31: Help Location Update Rate
        exp.append(0x08)  # 32: Help Location Update Rate
        exp.append(0x4c)  # 33: Help Location Update Rate
        exp.append(0x07)  # 34: Scans per Fix
        exp.append(0x0a)  # 35: Max WIFI APs
        exp.append(0x4c)  # 36: Max Cell IDs
        exp.append(0xea)  # 37: Location Update Order
        exp.append(0x01)  # 38: Accel Enable
        exp.append(0x5b)  # 39: Accel Duration
        exp.append(0x95)  # 40: Accel Duration
        exp.append(0x00)  # 41: Accel Threshold
        exp.append(0x50)  # 42: Accel Threshold
        exp.append(0x5b)  # 43: Shock Threshold
        exp.append(0xe3)  # 44: Shock Threshold
        exp.append(0x01)  # 45: Cache Enable
        exp.append(0x2d)  # 46: Cache Length
        exp.append(0x00)  # 47: GPS Power Mode
        exp.append(0x00)  # 48: GPS Timeout
        exp.append(0xb4)  # 49: GPS Timeout
        exp.append(0xd4)  # 50: Network Lost Timeout
        exp.append(0x31)  # 51: Network Lost Timeout
        exp.append(0x02)  # 52: Ref Lost Timeout
        exp.append(0x58)  # 53: Ref Lost Timeout
        exp.append(0x00)  # 54: Network Scan Interval
        exp.append(0x22)  # 55: Network Scan Interval
        self.assertSequenceEqual(msg, exp)

    def test_EnableTestModeV2(self):
        """ Verifies building a V2 Test Enable Message. """
        spec_v2 = af_devs.supertag.SupertagDownlinkMessageSpecV2()

        # Default Values
        msg = spec_v2.build_message("EnableTestMode")
        exp = bytearray()
        exp.append(0x02)  # 00: Msg Type
        exp.append(0x02)  # 01: Message Spec Version
        self.assertSequenceEqual(msg, exp)

    def test_AckV2(self):
        """ Verified building a V2 Ack Message. """
        spec_v2 = af_devs.supertag.SupertagDownlinkMessageSpecV2()

        # Default Values
        msg = spec_v2.build_message("Ack")
        exp = bytearray()
        exp.append(0x03)  # 00: Msg Type
        exp.append(0x02)  # 01: Message Spec Version
        exp.append(0x11)  # 02: Help RXed
        exp.append(0x05)  # 03: Help TXed
        self.assertSequenceEqual(msg, exp)


if __name__ == '__main__':

    coloredlogs.install(level=LOG_LEVEL)

    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    suite.addTests(loader.loadTestsFromTestCase(SupertagTests))
