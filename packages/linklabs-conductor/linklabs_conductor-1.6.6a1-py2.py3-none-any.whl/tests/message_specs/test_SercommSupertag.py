import logging
import unittest

import coloredlogs

from conductor.airfinder import devices as af_devs

LOG = logging.getLogger(__name__)
LOG_LEVEL = logging.DEBUG


class SercommSupertagTests(unittest.TestCase):

    @unittest.skip("todo")
    def test_ConfigurationSercommV2(self):
        """ Verifies building a Sercomm V2 Configuration Message. """
        spec_v2 = af_devs.sercomm_supertag.SercommDownlinkMessageSpecV2_0()

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
        exp.append(0x00)  # 30: Transition Base Update Rate
        exp.append(0x00)  # 31: Transition Base Update Rate
        exp.append(0x00)  # 32: Transition Base Update Rate
        exp.append(0x0b)  # 33: Transition Base Update Rate
        exp.append(0x00)  # 34: Transition Increase Rate
        exp.append(0x04)  # 35: Scans per Fix
        exp.append(0x0a)  # 36: Max WIFI APs
        exp.append(0x00)  # 37: Max Cell IDs
        exp.append(0x1b)  # 38: Location Update Order
        exp.append(0x01)  # 39: Accel Enable
        exp.append(0x00)  # 40: Accel Duration
        exp.append(0x03)  # 41: Accel Duration
        exp.append(0x00)  # 42: Accel Threshold
        exp.append(0x50)  # 43: Accel Threshold
        exp.append(0x00)  # 44: Cache Enable
        exp.append(0x00)  # 45: Cache Length
        exp.append(0x00)  # 46: GPS Power Mode
        exp.append(0x00)  # 47: GPS Timeout
        exp.append(0xb4)  # 48: GPS Timeout
        exp.append(0x02)  # 49: Network Lost Timeout
        exp.append(0x58)  # 50: Network Lost Timeout
        exp.append(0x02)  # 51: Ref Lost Timeout
        exp.append(0x58)  # 52: Ref Lost Timeout
        exp.append(0x00)  # 53: Network Scan Interval
        exp.append(0xb4)  # 54: Network Scan Interval
        exp.append(0x05)  # 55: SymBLE Retries
        exp.append(0x4f)  # 56: Network Token
        exp.append(0x50)  # 57: Network Token
        exp.append(0x45)  # 58: Network Token
        exp.append(0x4e)  # 59: Network Token
        self.assertSequenceEqual(msg, exp)

        # Specified Values
        msg = spec_v2.build_message("Configuration",
                                    # Omit change mask.

                                    heartbeat=723,
                                    no_ap_heartbeat=7323,
                                    # Omit No Sym Heartbeat.
                                    location_update_rate=234,
                                    # Omit no ap loc upd
                                    no_sym_location_update_rate=9453,
                                    transition_base_update_rate=2124,
                                    transition_increasing_interval_enable=0x01,

                                    scans_per_fix=7,
                                    # Omit Max Wifi APs
                                    max_cell_ids=76,
                                    location_update_order=234,
                                    acc_enable=True,
                                    acc_duration=23445,
                                    # Omit acc_thresh
                                    cache_enable=True,

                                    cache_length=45,
                                    gps_power_mode=0,
                                    # omit gps_timeout
                                    network_lost_timeout=54321,
                                    # Omit ref lost timeout
                                    network_scan_interval=34,
                                    # Omit symble retries
                                    network_token=0xd37d2a78)

        exp = bytearray()
        exp.append(0x01)  # 00: Msg Type
        exp.append(0x02)  # 01: Message Spec Version
        exp.append(0b00000000)  # 02: Change Mask
        exp.append(0b10101011)  # 03: Change Mask
        exp.append(0b10111101)  # 04: Change Mask
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
        exp.append(0x00)  # 30: Transition Base Update Rate
        exp.append(0x00)  # 31: Transition Base Update Rate
        exp.append(0x08)  # 32: Transition Base Update Rate
        exp.append(0x4c)  # 33: Transition Base Update Rate
        exp.append(0x01)  # 34: Transition Update Increase
        exp.append(0x07)  # 35: Scans per Fix
        exp.append(0x0a)  # 36: Max WIFI APs
        exp.append(0x4c)  # 37: Max Cell IDs
        exp.append(0xea)  # 38: Location Update Order
        exp.append(0x01)  # 39: Accel Enable
        exp.append(0x5b)  # 40: Accel Duration
        exp.append(0x95)  # 41: Accel Duration
        exp.append(0x00)  # 42: Accel Threshold
        exp.append(0x50)  # 43: Accel Threshold
        exp.append(0x01)  # 44: Cache Enable
        exp.append(0x2d)  # 45: Cache Length
        exp.append(0x00)  # 46: GPS Power Mode
        exp.append(0x00)  # 47: GPS Timeout
        exp.append(0xb4)  # 48: GPS Timeout
        exp.append(0xd4)  # 49: Network Lost Timeout
        exp.append(0x31)  # 50: Network Lost Timeout
        exp.append(0x02)  # 51: Ref Lost Timeout
        exp.append(0x58)  # 52: Ref Lost Timeout
        exp.append(0x00)  # 53: Network Scan Interval
        exp.append(0x22)  # 54: Network Scan Interval
        exp.append(0x05)  # 55: SymBLE Retries
        exp.append(0xd3)  # 56: Network Token
        exp.append(0x7d)  # 57: Network Token
        exp.append(0x2a)  # 58: Network Token
        exp.append(0x78)  # 59: Network Token
        self.assertSequenceEqual(msg, exp)

    @unittest.skip("todo")
    def test_ConfigurationSercommV2_1(self):
        """ Verifies building a Sercomm V2 Configuration Message. """
        spec_v2 = af_devs.sercomm_supertag.SercommDownlinkMessageSpecV2_1()

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
        exp.append(0x00)  # 30: Transition Base Update Rate
        exp.append(0x00)  # 31: Transition Base Update Rate
        exp.append(0x00)  # 32: Transition Base Update Rate
        exp.append(0x0b)  # 33: Transition Base Update Rate
        exp.append(0x00)  # 34: Transition Increase Rate
        exp.append(0x04)  # 35: Scans per Fix
        exp.append(0x0a)  # 36: Max WIFI APs
        exp.append(0x00)  # 37: Max Cell IDs
        exp.append(0x1b)  # 38: Location Update Order
        exp.append(0x01)  # 39: Accel Enable
        exp.append(0x00)  # 40: Accel Duration
        exp.append(0x03)  # 41: Accel Duration
        exp.append(0x00)  # 42: Accel Threshold
        exp.append(0x50)  # 43: Accel Threshold
        exp.append(0x00)  # 44: Cache Enable
        exp.append(0x00)  # 45: Cache Length
        exp.append(0x00)  # 46: GPS Power Mode
        exp.append(0x00)  # 47: GPS Timeout
        exp.append(0xb4)  # 48: GPS Timeout
        exp.append(0x02)  # 49: Network Lost Timeout
        exp.append(0x58)  # 50: Network Lost Timeout
        exp.append(0x02)  # 51: Ref Lost Timeout
        exp.append(0x58)  # 52: Ref Lost Timeout
        exp.append(0x00)  # 53: Network Scan Interval
        exp.append(0xb4)  # 54: Network Scan Interval
        exp.append(0x05)  # 55: SymBLE Retries
        exp.append(0x4f)  # 56: Network Token
        exp.append(0x50)  # 57: Network Token
        exp.append(0x45)  # 58: Network Token
        exp.append(0x4e)  # 59: Network Token
        self.assertSequenceEqual(msg, exp)

        # Specified Values
        msg = spec_v2.build_message("Configuration",
                                    # Omit change mask.

                                    heartbeat=723,
                                    no_ap_heartbeat=7323,
                                    # Omit No Sym Heartbeat.
                                    location_update_rate=234,
                                    # Omit no ap loc upd
                                    no_sym_location_update_rate=9453,
                                    transition_base_update_rate=2124,
                                    transition_increasing_interval_enable=0x01,

                                    scans_per_fix=7,
                                    # Omit Max Wifi APs
                                    max_cell_ids=76,
                                    location_update_order=234,
                                    acc_enable=True,
                                    acc_duration=23445,
                                    # Omit acc_thresh
                                    cache_enable=True,

                                    cache_length=45,
                                    gps_power_mode=0,
                                    # omit gps_timeout
                                    network_lost_timeout=54321,
                                    # Omit ref lost timeout
                                    network_scan_interval=34,
                                    # Omit symble retries
                                    network_token=0xd37d2a78)

        exp = bytearray()
        exp.append(0x01)  # 00: Msg Type
        exp.append(0x02)  # 01: Message Spec Version
        exp.append(0b00000000)  # 02: Change Mask
        exp.append(0b10101011)  # 03: Change Mask
        exp.append(0b10111101)  # 04: Change Mask
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
        exp.append(0x00)  # 30: Transition Base Update Rate
        exp.append(0x00)  # 31: Transition Base Update Rate
        exp.append(0x08)  # 32: Transition Base Update Rate
        exp.append(0x4c)  # 33: Transition Base Update Rate
        exp.append(0x01)  # 34: Transition Update Increase
        exp.append(0x07)  # 35: Scans per Fix
        exp.append(0x0a)  # 36: Max WIFI APs
        exp.append(0x4c)  # 37: Max Cell IDs
        exp.append(0xea)  # 38: Location Update Order
        exp.append(0x01)  # 39: Accel Enable
        exp.append(0x5b)  # 40: Accel Duration
        exp.append(0x95)  # 41: Accel Duration
        exp.append(0x00)  # 42: Accel Threshold
        exp.append(0x50)  # 43: Accel Threshold
        exp.append(0x01)  # 44: Cache Enable
        exp.append(0x2d)  # 45: Cache Length
        exp.append(0x00)  # 46: GPS Power Mode
        exp.append(0x00)  # 47: GPS Timeout
        exp.append(0xb4)  # 48: GPS Timeout
        exp.append(0xd4)  # 49: Network Lost Timeout
        exp.append(0x31)  # 50: Network Lost Timeout
        exp.append(0x02)  # 51: Ref Lost Timeout
        exp.append(0x58)  # 52: Ref Lost Timeout
        exp.append(0x00)  # 53: Network Scan Interval
        exp.append(0x22)  # 54: Network Scan Interval
        exp.append(0x05)  # 55: SymBLE Retries
        exp.append(0xd3)  # 56: Network Token
        exp.append(0x7d)  # 57: Network Token
        exp.append(0x2a)  # 58: Network Token
        exp.append(0x78)  # 59: Network Token
        self.assertSequenceEqual(msg, exp)

    def test_BatteryConsumptionV2_1(self):
        """ Verifies building a V2 Battery Consumption Window Configuration Message. """
        spec_v2 = af_devs.sercomm_supertag.SercommDownlinkMessageSpecV2_1()

        # Default Values
        msg = spec_v2.build_message("BattConsumptionWindow",
                                    mask=0xffffffff,
                                    battery_capacity=0x100012,
                                    shipping_mode_power=0x19,
                                    start_up_power=0x56,
                                    alive_time_power=0x78,
                                    psm_sleep_power=0x34,
                                    location_update_power=0x90,
                                    network_scan_power=0x21,
                                    ble_connection_power=0x43,
                                    lte_success_power=0x65,
                                    lte_failed_power=0x87,
                                    lte_registration_power=0x22,
                                    gps_avg_power=0x09,
                                    wifi_avg_power=0x00,
                                    temp_read_power=0x11,
                                    battery_read_power=0x22,
                                    led_power=0x33,
                                    ftp_power=0x44)
        exp = bytearray()
        exp.append(0x03)  # 0: Msg Type
        exp.append(0x02)  # 1: Message Spec Version
        exp.append(0xff)  # 2: Change Mask
        exp.append(0xff)  # 3: Change Mask
        exp.append(0xff)  # 4: Change Mask
        exp.append(0xff)  # 5: Change Mask
        exp.append(0x00)  # 6: xx
        exp.append(0x10)  # 7: x
        exp.append(0x00)  # 8: x
        exp.append(0x12)  # 9: Battery Capacity
        exp.append(0x00)  # 10: xx
        exp.append(0x00)  # 11: x
        exp.append(0x00)  # 12: x
        exp.append(0x19)  # 13: Shipping mode power
        exp.append(0x00)  # 14: xx
        exp.append(0x00)  # 15: x
        exp.append(0x00)  # 16: x
        exp.append(0x56)  # 17: Startup event power
        exp.append(0x00)  # 18: xx
        exp.append(0x00)  # 19: x
        exp.append(0x00)  # 20: x
        exp.append(0x78)  # 21: Alive time event power
        exp.append(0x00)  # 22: xx
        exp.append(0x00)  # 23: x
        exp.append(0x00)  # 24: x
        exp.append(0x34)  # 25: PSM sleep power
        exp.append(0x00)  # 26: xx
        exp.append(0x90)  # 27: Location scan event power
        exp.append(0x00)  # 28: x
        exp.append(0x21)  # 29: Network scan event power
        exp.append(0x00)  # 30: x
        exp.append(0x43)  # 31: BLE connection event power
        exp.append(0x00)  # 32: xx
        exp.append(0x00)  # 33: x
        exp.append(0x00)  # 34: x
        exp.append(0x65)  # 35: LTE-m success event power
        exp.append(0x00)  # 36: xx
        exp.append(0x00)  # 37: x
        exp.append(0x00)  # 38: x
        exp.append(0x87)  # 39: LTE-m fail event power
        exp.append(0x00)  # 40: xx
        exp.append(0x00)  # 41: x
        exp.append(0x00)  # 42: x
        exp.append(0x22)  # 43: LTE-m registration event power
        exp.append(0x00)  # 44: xx
        exp.append(0x00)  # 45: x
        exp.append(0x00)  # 46: x
        exp.append(0x09)  # 47: GPS average power
        exp.append(0x00)  # 48: xx
        exp.append(0x00)  # 49: x
        exp.append(0x00)  # 50: x
        exp.append(0x00)  # 51: WiFi scan average power
        exp.append(0x00)  # 52: xx
        exp.append(0x11)  # 53: Temperature read event power
        exp.append(0x00)  # 54: xx
        exp.append(0x22)  # 55: Battery read event power
        exp.append(0x00)  # 56: xx
        exp.append(0x00)  # 57: x
        exp.append(0x00)  # 58: x
        exp.append(0x33)  # 59: LED event power
        exp.append(0x00)  # 60: xx
        exp.append(0x00)  # 61: x
        exp.append(0x00)  # 62: x
        exp.append(0x44)  # 63: FOTA event power
        self.assertSequenceEqual(msg, exp)

    def test_BatteryConsumptionV2_1(self):
        """ Verifies building a V2 Battery Consumption Window Configuration Message. """
        spec_v2 = af_devs.sercomm_supertag.SercommDownlinkMessageSpecV2_1()

        # Default Values
        msg = spec_v2.build_message("BattConsumptionWindow",
                                    mask=0xffffffff,
                                    battery_capacity=0x100012,
                                    shipping_mode_power=0x19,
                                    start_up_power=0x56,
                                    alive_time_power=0x78,
                                    psm_sleep_power=0x34,
                                    location_update_power=0x90,
                                    network_scan_power=0x21,
                                    ble_connection_power=0x43,
                                    lte_success_power=0x65,
                                    lte_failed_power=0x87,
                                    lte_registration_power=0x22,
                                    gps_avg_power=0x09,
                                    wifi_avg_power=0x00,
                                    temp_read_power=0x11,
                                    battery_read_power=0x22,
                                    led_power=0x33,
                                    ftp_power=0x44)
        exp = bytearray()
        exp.append(0x03)  # 0: Msg Type
        exp.append(0x02)  # 1: Message Spec Version
        exp.append(0xff)  # 2: Change Mask
        exp.append(0xff)  # 3: Change Mask
        exp.append(0xff)  # 4: Change Mask
        exp.append(0xff)  # 5: Change Mask
        exp.append(0x00)  # 6: xx
        exp.append(0x10)  # 7: x
        exp.append(0x00)  # 8: x
        exp.append(0x12)  # 9: Battery Capacity
        exp.append(0x00)  # 10: xx
        exp.append(0x00)  # 11: x
        exp.append(0x00)  # 12: x
        exp.append(0x19)  # 13: Shipping mode power
        exp.append(0x00)  # 14: xx
        exp.append(0x00)  # 15: x
        exp.append(0x00)  # 16: x
        exp.append(0x56)  # 17: Startup event power
        exp.append(0x00)  # 18: xx
        exp.append(0x00)  # 19: x
        exp.append(0x00)  # 20: x
        exp.append(0x78)  # 21: Alive time event power
        exp.append(0x00)  # 22: xx
        exp.append(0x00)  # 23: x
        exp.append(0x00)  # 24: x
        exp.append(0x34)  # 25: PSM sleep power
        exp.append(0x00)  # 26: xx
        exp.append(0x90)  # 27: Location scan event power
        exp.append(0x00)  # 28: x
        exp.append(0x21)  # 29: Network scan event power
        exp.append(0x00)  # 30: x
        exp.append(0x43)  # 31: BLE connection event power
        exp.append(0x00)  # 32: xx
        exp.append(0x00)  # 33: x
        exp.append(0x00)  # 34: x
        exp.append(0x65)  # 35: LTE-m success event power
        exp.append(0x00)  # 36: xx
        exp.append(0x00)  # 37: x
        exp.append(0x00)  # 38: x
        exp.append(0x87)  # 39: LTE-m fail event power
        exp.append(0x00)  # 40: xx
        exp.append(0x00)  # 41: x
        exp.append(0x00)  # 42: x
        exp.append(0x22)  # 43: LTE-m registration event power
        exp.append(0x00)  # 44: xx
        exp.append(0x00)  # 45: x
        exp.append(0x00)  # 46: x
        exp.append(0x09)  # 47: GPS average power
        exp.append(0x00)  # 48: xx
        exp.append(0x00)  # 49: x
        exp.append(0x00)  # 50: x
        exp.append(0x00)  # 51: WiFi scan average power
        exp.append(0x00)  # 52: xx
        exp.append(0x11)  # 53: Temperature read event power
        exp.append(0x00)  # 54: xx
        exp.append(0x22)  # 55: Battery read event power
        exp.append(0x00)  # 56: xx
        exp.append(0x00)  # 57: x
        exp.append(0x00)  # 58: x
        exp.append(0x33)  # 59: LED event power
        exp.append(0x00)  # 60: xx
        exp.append(0x00)  # 61: x
        exp.append(0x00)  # 62: x
        exp.append(0x44)  # 63: FOTA event power
        self.assertSequenceEqual(msg, exp)

    def test_BatteryConsumptionSercommV2(self):
        """ Test building a Sercomm V2 Battery Consumption. """
        spec_v2 = af_devs.sercomm_supertag.SercommDownlinkMessageSpecV2_0()

        # Default Values
        msg = spec_v2.build_message("BattConsumptionWindow")
        exp = bytearray()
        exp.append(0x03)  # 00: Msg Type
        exp.append(0x02)  # 01: Message Spec Version
        exp.append(0b00000000)  # 02: Change Mask
        exp.append(0b00000000)  # 03: Change Mask
        exp.append(0b00000000)  # 04: Change Mask
        exp.append(0b00000000)  # 05: Change Mask
        exp.append(0x00)  # 06: Battery Capacity
        exp.append(0x00)  # 07: Battery Capacity
        exp.append(0x00)  # 08: Battery Capacity
        exp.append(0x00)  # 09: Battery Capacity
        exp.append(0x00)  # 10: Shipping Mode Power
        exp.append(0x00)  # 11: x
        exp.append(0x00)  # 12: x
        exp.append(0x00)  # 13: xx
        exp.append(0x00)  # 10: Startup Event Power
        exp.append(0x00)  # 11: x
        exp.append(0x00)  # 12: x
        exp.append(0x00)  # 13: xx
        exp.append(0x00)  # 14: Alive Time Event Power
        exp.append(0x00)  # 15: Alive Time Event Power
        exp.append(0x00)  # 16: Alive Time Event Power
        exp.append(0x00)  # 17: Alive Time Event Power
        exp.append(0x00)  # 10: PSM Sleep Power
        exp.append(0x00)  # 11: x
        exp.append(0x00)  # 12: x
        exp.append(0x00)  # 13: xx
        exp.append(0x00)  # 18: Location Scan Event Power
        exp.append(0x00)  # 19: Location Scan Event Power
        exp.append(0x00)  # 20: Network Scan Event Power
        exp.append(0x00)  # 21: Network Scan Event Power
        exp.append(0x00)  # 22: BLE Connection Event Power
        exp.append(0x00)  # 23: BLE Connection Event Power
        exp.append(0x00)  # 24: LTEm Success Event Power
        exp.append(0x00)  # 25: LTEm Success Event Power
        exp.append(0x00)  # 26: LTEm Success Event Power
        exp.append(0x00)  # 27: LTEm Success Event Power
        exp.append(0x00)  # 28: LTEm Failure Event Power
        exp.append(0x00)  # 29: LTEm Failure Event Power
        exp.append(0x00)  # 30: LTEm Failure Event Power
        exp.append(0x00)  # 31: LTEm Failure Event Power
        exp.append(0x00)  # 28: LTEm Registration Event Power
        exp.append(0x00)  # 29: LTEm xx
        exp.append(0x00)  # 30: LTEm x
        exp.append(0x00)  # 31: LTEm xx
        exp.append(0x00)  # 32: GPS Average Power
        exp.append(0x00)  # 33: GPS Average Power
        exp.append(0x00)  # 34: GPS Average Power
        exp.append(0x00)  # 35: GPS Average Power
        exp.append(0x00)  # 36: WIFI Average Power
        exp.append(0x00)  # 37: WIFI Average Power
        exp.append(0x00)  # 38: WIFI Average Power
        exp.append(0x00)  # 39: WIFI Average Power
        exp.append(0x00)  # 40: Temperature Read Event Power
        exp.append(0x00)  # 41: Temperature Read Event Power
        exp.append(0x00)  # 42: Battery Read Event Power
        exp.append(0x00)  # 43: Battery Read Event Power
        exp.append(0x00)  # 44: LED Event Power
        exp.append(0x00)  # 45: LED Event Power
        exp.append(0x00)  # 46: LED Event Power
        exp.append(0x00)  # 47: LED Event Power
        exp.append(0x00)  # 48: FTP Event Power
        exp.append(0x00)  # 49: FTP Event Power
        exp.append(0x00)  # 50: FTP Event Power
        exp.append(0x00)  # 51: FTP Event Power
        self.assertSequenceEqual(msg, exp)

        # Specific Values
        msg = spec_v2.build_message("BattConsumptionWindow",
                                    # battery_capacity,
                                    # shipping_mode_power,
                                    start_up_power=72384,
                                    alive_time_power=59275,

                                    # location_update_power
                                    # psm_sleep_power,
                                    # location_update_power,
                                    network_scan_power=8371,

                                    ble_connection_power=56924,
                                    # lte_success_power,
                                    lte_failed_power=32784567,
                                    # lte_registration_power,

                                    gps_avg_power=48274,
                                    # wifi_avg_power,
                                    temp_read_power=34938,
                                    battery_read_power=48002,

                                    # led_power,
                                    ftp_power=0)

        exp = bytearray()
        exp.append(0x03)  # 00: Msg Type
        exp.append(0x02)  # 01: Message Spec Version
        exp.append(0b00000000)  # 02: Change Mask
        exp.append(0b00000001)  # 03: Change Mask
        exp.append(0b01101010)  # 04: Change Mask
        exp.append(0b11001100)  # 05: Change Mask
        exp.append(0x00)  # 06: Battery Capacity
        exp.append(0x00)  # 07: Battery Capacity
        exp.append(0x00)  # 08: Battery Capacity
        exp.append(0x00)  # 09: Battery Capacity
        exp.append(0x00)  # 10: Shipping Mode Power
        exp.append(0x00)  # 11: x
        exp.append(0x00)  # 12: x
        exp.append(0x00)  # 13: xx
        exp.append(0x00)  # 14: Startup Event Power
        exp.append(0x01)  # 15: Startup Event Power
        exp.append(0x1a)  # 16: Startup Event Power
        exp.append(0xc0)  # 17: Startup Event Power
        exp.append(0x00)  # 18: Alive Time Event Power
        exp.append(0x00)  # 19: Alive Time Event Power
        exp.append(0xe7)  # 20: Alive Time Event Power
        exp.append(0x8b)  # 21: Alive Time Event Power
        exp.append(0x00)  # 22: PSM Sleep Power
        exp.append(0x00)  # 23: x
        exp.append(0x00)  # 24: x
        exp.append(0x00)  # 25: xx
        exp.append(0x00)  # 26: Location Scan Event Power
        exp.append(0x00)  # 27: Location Scan Event Power
        exp.append(0x20)  # 28: Network Scan Event Power
        exp.append(0xb3)  # 29: Network Scan Event Power
        exp.append(0xde)  # 30: BLE Connection Event Power
        exp.append(0x5c)  # 31: BLE Connection Event Power
        exp.append(0x00)  # 32: LTEm Success Event Power
        exp.append(0x00)  # 33: LTEm Success Event Power
        exp.append(0x00)  # 34: LTEm Success Event Power
        exp.append(0x00)  # 35: LTEm Success Event Power
        exp.append(0x01)  # 36: LTEm Failure Event Power
        exp.append(0xf4)  # 37: LTEm Failure Event Power
        exp.append(0x40)  # 38: LTEm Failure Event Power
        exp.append(0xb7)  # 39: LTEm Failure Event Power
        exp.append(0x00)  # 40: LTEm Registration Event Power
        exp.append(0x00)  # 41: LTEm xx
        exp.append(0x00)  # 42: LTEm x
        exp.append(0x00)  # 43: LTEm xx
        exp.append(0x00)  # 44: GPS Average Power
        exp.append(0x00)  # 45: GPS Average Power
        exp.append(0xbc)  # 46: GPS Average Power
        exp.append(0x92)  # 47: GPS Average Power
        exp.append(0x00)  # 48: WIFI Average Power
        exp.append(0x00)  # 49: WIFI Average Power
        exp.append(0x00)  # 50: WIFI Average Power
        exp.append(0x00)  # 51: WIFI Average Power
        exp.append(0x88)  # 52: Temperature Read Event Power
        exp.append(0x7a)  # 53: Temperature Read Event Power
        exp.append(0xbb)  # 54: Battery Read Event Power
        exp.append(0x82)  # 55: Battery Read Event Power
        exp.append(0x00)  # 56: LED Event Power
        exp.append(0x00)  # 57: LED Event Power
        exp.append(0x00)  # 58: LED Event Power
        exp.append(0x00)  # 59: LED Event Power
        exp.append(0x00)  # 60: FTP Event Power
        exp.append(0x00)  # 61: FTP Event Power
        exp.append(0x00)  # 62: FTP Event Power
        exp.append(0x00)  # 63: FTP Event Power
        self.assertSequenceEqual(msg, exp)

    @unittest.skip("TODO: implement test")
    def test_BatteryConsumptionSercommV2_1(self):
        """ Test building a Sercomm V2 Battery Consumption. """
        spec_v2 = af_devs.sercomm_supertag.SercommDownlinkMessageSpecV2_1()

        # Default Values
        msg = spec_v2.build_message("BattConsumptionWindow")
        exp = bytearray()
        exp.append(0x03)  # 00: Msg Type
        exp.append(0x02)  # 01: Message Spec Version
        exp.append(0b00000000)  # 02: Change Mask
        exp.append(0b00000000)  # 03: Change Mask
        exp.append(0b00000000)  # 04: Change Mask
        exp.append(0b00000000)  # 05: Change Mask
        exp.append(0x00)  # 06: Battery Capacity
        exp.append(0x00)  # 07: Battery Capacity
        exp.append(0x00)  # 08: Battery Capacity
        exp.append(0x00)  # 09: Battery Capacity
        exp.append(0x00)  # 10: Shipping Mode Power
        exp.append(0x00)  # 11: x
        exp.append(0x00)  # 12: x
        exp.append(0x00)  # 13: xx
        exp.append(0x00)  # 10: Startup Event Power
        exp.append(0x00)  # 11: x
        exp.append(0x00)  # 12: x
        exp.append(0x00)  # 13: xx
        exp.append(0x00)  # 14: Alive Time Event Power
        exp.append(0x00)  # 15: Alive Time Event Power
        exp.append(0x00)  # 16: Alive Time Event Power
        exp.append(0x00)  # 17: Alive Time Event Power
        exp.append(0x00)  # 10: PSM Sleep Power
        exp.append(0x00)  # 11: x
        exp.append(0x00)  # 12: x
        exp.append(0x00)  # 13: xx
        exp.append(0x00)  # 18: Location Scan Event Power
        exp.append(0x00)  # 19: Location Scan Event Power
        exp.append(0x00)  # 20: Network Scan Event Power
        exp.append(0x00)  # 21: Network Scan Event Power
        exp.append(0x00)  # 22: BLE Connection Event Power
        exp.append(0x00)  # 23: BLE Connection Event Power
        exp.append(0x00)  # 24: LTEm Success Event Power
        exp.append(0x00)  # 25: LTEm Success Event Power
        exp.append(0x00)  # 26: LTEm Success Event Power
        exp.append(0x00)  # 27: LTEm Success Event Power
        exp.append(0x00)  # 28: LTEm Failure Event Power
        exp.append(0x00)  # 29: LTEm Failure Event Power
        exp.append(0x00)  # 30: LTEm Failure Event Power
        exp.append(0x00)  # 31: LTEm Failure Event Power
        exp.append(0x00)  # 28: LTEm Registration Event Power
        exp.append(0x00)  # 29: LTEm xx
        exp.append(0x00)  # 30: LTEm x
        exp.append(0x00)  # 31: LTEm xx
        exp.append(0x00)  # 32: GPS Average Power
        exp.append(0x00)  # 33: GPS Average Power
        exp.append(0x00)  # 34: GPS Average Power
        exp.append(0x00)  # 35: GPS Average Power
        exp.append(0x00)  # 36: WIFI Average Power
        exp.append(0x00)  # 37: WIFI Average Power
        exp.append(0x00)  # 38: WIFI Average Power
        exp.append(0x00)  # 39: WIFI Average Power
        exp.append(0x00)  # 40: Temperature Read Event Power
        exp.append(0x00)  # 41: Temperature Read Event Power
        exp.append(0x00)  # 42: Battery Read Event Power
        exp.append(0x00)  # 43: Battery Read Event Power
        exp.append(0x00)  # 44: LED Event Power
        exp.append(0x00)  # 45: LED Event Power
        exp.append(0x00)  # 46: LED Event Power
        exp.append(0x00)  # 47: LED Event Power
        exp.append(0x00)  # 48: FTP Event Power
        exp.append(0x00)  # 49: FTP Event Power
        exp.append(0x00)  # 50: FTP Event Power
        exp.append(0x00)  # 51: FTP Event Power
        self.assertSequenceEqual(msg, exp)

        # Specific Values
        msg = spec_v2.build_message("BattConsumptionWindow",
                                    # battery_capacity,
                                    # shipping_mode_power,
                                    start_up_power=72384,
                                    alive_time_power=59275,

                                    # location_update_power
                                    # psm_sleep_power,
                                    # location_update_power,
                                    network_scan_power=8371,

                                    ble_connection_power=56924,
                                    # lte_success_power,
                                    lte_failed_power=32784567,
                                    # lte_registration_power,

                                    gps_avg_power=48274,
                                    # wifi_avg_power,
                                    temp_read_power=34938,
                                    battery_read_power=48002,

                                    # led_power,
                                    ftp_power=0)

        exp = bytearray()
        exp.append(0x03)  # 00: Msg Type
        exp.append(0x02)  # 01: Message Spec Version
        exp.append(0b00000000)  # 02: Change Mask
        exp.append(0b00000001)  # 03: Change Mask
        exp.append(0b01101010)  # 04: Change Mask
        exp.append(0b11001100)  # 05: Change Mask
        exp.append(0x00)  # 06: Battery Capacity
        exp.append(0x00)  # 07: Battery Capacity
        exp.append(0x00)  # 08: Battery Capacity
        exp.append(0x00)  # 09: Battery Capacity
        exp.append(0x00)  # 10: Shipping Mode Power
        exp.append(0x00)  # 11: x
        exp.append(0x00)  # 12: x
        exp.append(0x00)  # 13: xx
        exp.append(0x00)  # 14: Startup Event Power
        exp.append(0x01)  # 15: Startup Event Power
        exp.append(0x1a)  # 16: Startup Event Power
        exp.append(0xc0)  # 17: Startup Event Power
        exp.append(0x00)  # 18: Alive Time Event Power
        exp.append(0x00)  # 19: Alive Time Event Power
        exp.append(0xe7)  # 20: Alive Time Event Power
        exp.append(0x8b)  # 21: Alive Time Event Power
        exp.append(0x00)  # 22: PSM Sleep Power
        exp.append(0x00)  # 23: x
        exp.append(0x00)  # 24: x
        exp.append(0x00)  # 25: xx
        exp.append(0x00)  # 26: Location Scan Event Power
        exp.append(0x00)  # 27: Location Scan Event Power
        exp.append(0x20)  # 28: Network Scan Event Power
        exp.append(0xb3)  # 29: Network Scan Event Power
        exp.append(0xde)  # 30: BLE Connection Event Power
        exp.append(0x5c)  # 31: BLE Connection Event Power
        exp.append(0x00)  # 32: LTEm Success Event Power
        exp.append(0x00)  # 33: LTEm Success Event Power
        exp.append(0x00)  # 34: LTEm Success Event Power
        exp.append(0x00)  # 35: LTEm Success Event Power
        exp.append(0x01)  # 36: LTEm Failure Event Power
        exp.append(0xf4)  # 37: LTEm Failure Event Power
        exp.append(0x40)  # 38: LTEm Failure Event Power
        exp.append(0xb7)  # 39: LTEm Failure Event Power
        exp.append(0x00)  # 40: LTEm Registration Event Power
        exp.append(0x00)  # 41: LTEm xx
        exp.append(0x00)  # 42: LTEm x
        exp.append(0x00)  # 43: LTEm xx
        exp.append(0x00)  # 44: GPS Average Power
        exp.append(0x00)  # 45: GPS Average Power
        exp.append(0xbc)  # 46: GPS Average Power
        exp.append(0x92)  # 47: GPS Average Power
        exp.append(0x00)  # 48: WIFI Average Power
        exp.append(0x00)  # 49: WIFI Average Power
        exp.append(0x00)  # 50: WIFI Average Power
        exp.append(0x00)  # 51: WIFI Average Power
        exp.append(0x88)  # 52: Temperature Read Event Power
        exp.append(0x7a)  # 53: Temperature Read Event Power
        exp.append(0xbb)  # 54: Battery Read Event Power
        exp.append(0x82)  # 55: Battery Read Event Power
        exp.append(0x00)  # 56: LED Event Power
        exp.append(0x00)  # 57: LED Event Power
        exp.append(0x00)  # 58: LED Event Power
        exp.append(0x00)  # 59: LED Event Power
        exp.append(0x00)  # 60: FTP Event Power
        exp.append(0x00)  # 61: FTP Event Power
        exp.append(0x00)  # 62: FTP Event Power
        exp.append(0x00)  # 63: FTP Event Power
        self.assertSequenceEqual(msg, exp)

    def test_SetDiagnosticModeSercommV2(self):
        """ Test building a Sercomm V2 Set Diagnostic Message. """
        spec_v2 = af_devs.sercomm_supertag.SercommDownlinkMessageSpecV2_0()

        # Default Values
        msg = spec_v2.build_message("SetDiagnosticMode")
        exp = bytearray()
        exp.append(0x04)  # 00: Msg Type
        exp.append(0x02)  # 01: Message Spec Version
        exp.append(0x00)  # 03: Enable
        self.assertSequenceEqual(msg, exp)

        # Specified Values
        msg = spec_v2.build_message("SetDiagnosticMode", enable=True)
        exp = bytearray()
        exp.append(0x04)  # 00: Msg Type
        exp.append(0x02)  # 01: Message Spec Version
        exp.append(0x01)  # 03: Enable
        self.assertSequenceEqual(msg, exp)

    def test_SetDiagnosticModeSercommV2_1(self):
        """ Test building a Sercomm V2 Set Diagnostic Message. """
        spec_v2 = af_devs.sercomm_supertag.SercommDownlinkMessageSpecV2_1()

        # Default Values
        msg = spec_v2.build_message("SetDiagnosticMode")
        exp = bytearray()
        exp.append(0x04)  # 00: Msg Type
        exp.append(0x02)  # 01: Message Spec Version
        exp.append(0x00)  # 03: Enable
        self.assertSequenceEqual(msg, exp)

        # Specified Values
        msg = spec_v2.build_message("SetDiagnosticMode", enable=True)
        exp = bytearray()
        exp.append(0x04)  # 00: Msg Type
        exp.append(0x02)  # 01: Message Spec Version
        exp.append(0x01)  # 03: Enable
        self.assertSequenceEqual(msg, exp)

    def test_ConsumptionRequestSercommV2(self):
        """ Test building a Consumption Request for Sercomm V2. """
        spec_v2 = af_devs.sercomm_supertag.SercommDownlinkMessageSpecV2_0()

        # Default Values
        msg = spec_v2.build_message("ConsumptionRequest")
        exp = bytearray()
        exp.append(0x05)  # 00: Msg Type
        exp.append(0x02)  # 01: Message Spec Version
        self.assertSequenceEqual(msg, exp)

    def test_ConsumptionRequestSercommV2_1(self):
        """ Test building a Consumption Request for Sercomm V2. """
        spec_v2 = af_devs.sercomm_supertag.SercommDownlinkMessageSpecV2_1()

        # Default Values
        msg = spec_v2.build_message("ConsumptionRequest")
        exp = bytearray()
        exp.append(0x05)  # 00: Msg Type
        exp.append(0x02)  # 01: Message Spec Version
        self.assertSequenceEqual(msg, exp)

    def test_SetThrottlingSercommV2(self):
        """ Test building a Sercomm V2 Set Throttling Message. """
        spec_v2 = af_devs.sercomm_supertag.SercommDownlinkMessageSpecV2_0()

        # Default Values
        msg = spec_v2.build_message("SetThrottling")
        exp = bytearray()
        exp.append(0x06)  # 00: Msg Type
        exp.append(0x02)  # 01: Message Spec Version
        exp.append(0x00)  # 02: Change Mask
        exp.append(0x00)  # 03: Change Mask
        exp.append(0x00)  # 04: Enable
        exp.append(0x01)  # 05: Mode
        exp.append(0x00)  # 06: Time Window Length
        exp.append(0x00)  # 07: Time Window Length
        exp.append(0x00)  # 08: Time Window Length
        exp.append(0x1e)  # 09: Time Window Length
        exp.append(0x00)  # 10: Minimum Battery Life
        exp.append(0x01)  # 11: Minimum Battery Life
        exp.append(0x19)  # 12: Minimum Battery Life
        exp.append(0x40)  # 13: Minimum Battery Life
        exp.append(0x5a)  # 14: Window Limit
        exp.append(0x01)  # 15: Battery Capacity
        exp.append(0x01)  # 16: Battery Capacity
        exp.append(0x01)  # 17: Battery Capacity
        exp.append(0x00)  # 18: Battery Capacity
        self.assertSequenceEqual(msg, exp)

        # Specified Values
        msg = spec_v2.build_message("SetThrottling",
                                    enable=True,
                                    mode=1,
                                    win_len=635233,
                                    min_batt=23643,
                                    # win_limit=0,
                                    batt_cap=5463453)
        exp = bytearray()
        exp.append(0x06)  # 00: Msg Type
        exp.append(0x02)  # 01: Message Spec Version
        exp.append(0b00000000)  # 02: Change Mask
        exp.append(0b00101111)  # 03: Change Mask
        exp.append(0x01)  # 04: Enable
        exp.append(0x01)  # 05: Mode
        exp.append(0x00)  # 06: Time Window Length
        exp.append(0x09)  # 07: Time Window Length
        exp.append(0xb1)  # 08: Time Window Length
        exp.append(0x61)  # 09: Time Window Length
        exp.append(0x00)  # 10: Minimum Battery Life
        exp.append(0x00)  # 11: Minimum Battery Life
        exp.append(0x5c)  # 12: Minimum Battery Life
        exp.append(0x5b)  # 13: Minimum Battery Life
        exp.append(0x5a)  # 14: Window Limit
        exp.append(0x00)  # 15: Battery Capacity
        exp.append(0x53)  # 16: Battery Capacity
        exp.append(0x5d)  # 17: Battery Capacity
        exp.append(0x9d)  # 18: Battery Capacity
        self.assertSequenceEqual(msg, exp)

    def test_SetThrottlingSercommV2_1(self):
        """ Test building a Sercomm V2 Set Throttling Message. """
        spec_v2 = af_devs.sercomm_supertag.SercommDownlinkMessageSpecV2_1()

        # Default Values
        msg = spec_v2.build_message("SetThrottling")
        exp = bytearray()
        exp.append(0x06)  # 00: Msg Type
        exp.append(0x02)  # 01: Message Spec Version
        exp.append(0x00)  # 02: Change Mask
        exp.append(0x00)  # 03: Change Mask
        exp.append(0x00)  # 04: Enable
        exp.append(0x01)  # 05: Mode
        exp.append(0x00)  # 06: Time Window Length
        exp.append(0x00)  # 07: Time Window Length
        exp.append(0x00)  # 08: Time Window Length
        exp.append(0x1e)  # 09: Time Window Length
        exp.append(0x00)  # 10: Minimum Battery Life
        exp.append(0x01)  # 11: Minimum Battery Life
        exp.append(0x19)  # 12: Minimum Battery Life
        exp.append(0x40)  # 13: Minimum Battery Life
        exp.append(0x5a)  # 14: Window Limit
        exp.append(0x01)  # 15: Battery Capacity
        exp.append(0x01)  # 16: Battery Capacity
        exp.append(0x01)  # 17: Battery Capacity
        exp.append(0x00)  # 18: Battery Capacity
        self.assertSequenceEqual(msg, exp)

        # Specified Values
        msg = spec_v2.build_message("SetThrottling",
                                    enable=True,
                                    mode=1,
                                    win_len=635233,
                                    min_batt=23643,
                                    # win_limit=0,
                                    batt_cap=5463453)
        exp = bytearray()
        exp.append(0x06)  # 00: Msg Type
        exp.append(0x02)  # 01: Message Spec Version
        exp.append(0b00000000)  # 02: Change Mask
        exp.append(0b00101111)  # 03: Change Mask
        exp.append(0x01)  # 04: Enable
        exp.append(0x01)  # 05: Mode
        exp.append(0x00)  # 06: Time Window Length
        exp.append(0x09)  # 07: Time Window Length
        exp.append(0xb1)  # 08: Time Window Length
        exp.append(0x61)  # 09: Time Window Length
        exp.append(0x00)  # 10: Minimum Battery Life
        exp.append(0x00)  # 11: Minimum Battery Life
        exp.append(0x5c)  # 12: Minimum Battery Life
        exp.append(0x5b)  # 13: Minimum Battery Life
        exp.append(0x5a)  # 14: Window Limit
        exp.append(0x00)  # 15: Battery Capacity
        exp.append(0x53)  # 16: Battery Capacity
        exp.append(0x5d)  # 17: Battery Capacity
        exp.append(0x9d)  # 18: Battery Capacity
        self.assertSequenceEqual(msg, exp)

    def test_FTPAvailableSercommV2(self):
        """ Test building a Sercomm V2 FTP Notification Message. """
        spec_v2 = af_devs.sercomm_supertag.SercommDownlinkMessageSpecV2_0()

        # Default Values
        msg = spec_v2.build_message("FtpAvailable")
        exp = bytearray()
        exp.append(0x07)  # 00: Msg Type
        exp.append(0x02)  # 01: Message Spec Version
        exp.append(0x00)  # 02: App Major
        exp.append(0x00)  # 03: App Minor
        exp.append(0x00)  # 04: App Tag
        exp.append(0x00)  # 05: App Tag
        exp.append(0x00)  # 06: LTEm Modem Major
        exp.append(0x00)  # 07: LTEm Modem Minor
        exp.append(0x00)  # 08: LTEm Modem Tag
        exp.append(0x00)  # 09: LTEm Modem Tag
        self.assertSequenceEqual(msg, exp)

        # Specified Values
        msg = spec_v2.build_message("FtpAvailable",
                                    app_vers_major=4,
                                    app_vers_minor=6,
                                    app_vers_tag=23,
                                    modem_vers_major=86,
                                    modem_vers_minor=12,
                                    modem_vers_tag=23452)
        exp = bytearray()
        exp.append(0x07)  # 00: Msg Type
        exp.append(0x02)  # 01: Message Spec Version
        exp.append(0x04)  # 02: App Major
        exp.append(0x06)  # 03: App Minor
        exp.append(0x00)  # 04: App Tag
        exp.append(0x17)  # 05: App Tag
        exp.append(0x56)  # 06: LTEm Modem Major
        exp.append(0x0c)  # 07: LTEm Modem Minor
        exp.append(0x5b)  # 08: LTEm Modem Tag
        exp.append(0x9c)  # 09: LTEm Modem Tag
        self.assertSequenceEqual(msg, exp)

    def test_FTPAvailableSercommV2_1(self):
        """ Test building a Sercomm V2 FTP Notification Message. """
        spec_v2 = af_devs.sercomm_supertag.SercommDownlinkMessageSpecV2_1()

        # Default Values
        msg = spec_v2.build_message("FtpAvailable")
        exp = bytearray()
        exp.append(0x07)  # 00: Msg Type
        exp.append(0x02)  # 01: Message Spec Version
        exp.append(0x00)  # 02: App Major
        exp.append(0x00)  # 03: App Minor
        exp.append(0x00)  # 04: App Tag
        exp.append(0x00)  # 05: App Tag
        exp.append(0x00)  # 06: LTEm Modem Major
        exp.append(0x00)  # 07: LTEm Modem Minor
        exp.append(0x00)  # 08: LTEm Modem Tag
        exp.append(0x00)  # 09: LTEm Modem Tag
        self.assertSequenceEqual(msg, exp)

        # Specified Values
        msg = spec_v2.build_message("FtpAvailable",
                                    app_vers_major=4,
                                    app_vers_minor=6,
                                    app_vers_tag=23,
                                    modem_vers_major=86,
                                    modem_vers_minor=12,
                                    modem_vers_tag=23452)
        exp = bytearray()
        exp.append(0x07)  # 00: Msg Type
        exp.append(0x02)  # 01: Message Spec Version
        exp.append(0x04)  # 02: App Major
        exp.append(0x06)  # 03: App Minor
        exp.append(0x00)  # 04: App Tag
        exp.append(0x17)  # 05: App Tag
        exp.append(0x56)  # 06: LTEm Modem Major
        exp.append(0x0c)  # 07: LTEm Modem Minor
        exp.append(0x5b)  # 08: LTEm Modem Tag
        exp.append(0x9c)  # 09: LTEm Modem Tag
        self.assertSequenceEqual(msg, exp)


if __name__ == '__main__':

    coloredlogs.install(level=LOG_LEVEL)

    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    suite.addTests(loader.loadTestsFromTestCase(SercommSupertagTests))
