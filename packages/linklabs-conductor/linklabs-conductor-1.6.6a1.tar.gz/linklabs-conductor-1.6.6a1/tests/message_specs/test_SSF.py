import logging
import unittest

import coloredlogs

from conductor.airfinder import devices as af_devs

LOG = logging.getLogger(__name__)
LOG_LEVEL = logging.DEBUG


class SSFTests(unittest.TestCase):

    def __init__(self, test_name):
        super().__init__(test_name)

    def test_ConfigurationV1(self):
        """ Verifies building the Configuration Message. """
        spec_v1 = af_devs.ssf.SSFDownlinkMessageSpecV1()

        # Default Values
        msg = spec_v1.build_message("Configuration")
        exp = bytearray()
        exp.append(0x01)  # 0: Msg Type
        exp.append(0x01)  # 1: Message Spec Version
        exp.append(0x05)  # 2: Max Retires
        exp.append(0x03)  # 3: Scans per Fix
        exp.append(0x00)  # 4: Sensor Data Interval
        exp.append(0x00)  # 5: Sensor Data Interval
        exp.append(0x50)  # 6: Sensor Data Interval
        exp.append(0x00)  # 7: Sensor Data Interval
        exp.append(0x00)  # 8: Heartbeat Interval
        exp.append(0x00)  # 9: Heartbeat Interval
        exp.append(0x00)  # 10: Heartbeat Interval
        exp.append(0x90)  # 11: Heartbeat Interval
        self.assertSequenceEqual(msg, exp)

        # Specific Values
        msg = spec_v1.build_message("Configuration",
                                    max_retries=0x55,
                                    scan_per_fix=0x12,
                                    sensor_data_interval=0x07906543,
                                    heartbeat=0x23446422)
        exp = bytearray()
        exp.append(0x01)  # 0: Msg Type
        exp.append(0x01)  # 1: Message Spec Version
        exp.append(0x55)  # 2: Max Retires
        exp.append(0x12)  # 3: Scans per Fix
        exp.append(0x07)  # 4: Sensor Data Interval
        exp.append(0x90)  # 5: Sensor Interval
        exp.append(0x65)  # 6: Sensor Interval
        exp.append(0x43)  # 7: Sensor Interval
        exp.append(0x23)  # 8: Heartbeat Interval
        exp.append(0x44)  # 9: Heartbeat Interval
        exp.append(0x64)  # 10: Heartbeat Interval
        exp.append(0x22)  # 11: Heartbeat Interval
        self.assertSequenceEqual(msg, exp)

    def test_ResetV1(self):
        """ Verifies building a V1 Reset Message. """
        spec_v1 = af_devs.ssf.SSFDownlinkMessageSpecV1()

        msg = spec_v1.build_message("Reset")
        exp = bytearray()
        exp.append(0x02)  # 0: Msg Type
        exp.append(0x01)  # 1: Message Spec Version
        exp.append(0xd5)  # 2: Reset Value
        exp.append(0x83)  # 3: Reset Value
        exp.append(0x7e)  # 4: Reset Value
        exp.append(0xd6)  # 5: Reset Value
        self.assertSequenceEqual(msg, exp)

    def test_AddFiltersV1(self):
        """ Verifies building a V1 Reset Message. """
        spec_v1 = af_devs.ssf.SSFDownlinkMessageSpecV1()

        msg = spec_v1.build_ctrl_message("ADD_FILTERS")
        exp = bytearray()
        exp.append(0x03)  # 00: Msg Type
        exp.append(0x01)  # 01: Message Spec Version
        exp.append(0x01)  # 02: Operation Code
        exp.append(0x00)  # 03: Filter ID
        exp.append(0x01)  # 04: Filter Priority
        exp.append(0x05)  # 05: Event Rate
        exp.append(0x30)  # 06: Min RSSI Level
        exp.append(0x05)  # 07: Advertisement Length
        exp.append(0x00)  # 08: Number of sub-filters.
        exp.append(0x01)  # 09: sub-filter 1 length
        exp.append(0xff)  # 10: sub-filter 1
        exp.append(0x01)  # 11: sub-filter 2 length
        exp.append(0xff)  # 12: sub-filter 2
        exp.append(0x01)  # 13: sub-filter 3 length
        exp.append(0xff)  # 14: sub-filter 3
        exp.append(0x01)  # 15: sub-filter 4 length
        exp.append(0xff)  # 16: sub-filter 4
        self.assertSequenceEqual(msg, exp)

        msg = spec_v1.build_ctrl_message("ADD_FILTERS",
                                         filter_id=0x95,
                                         filter_priority=0x23,
                                         event_rate=0x99,
                                         min_adv_rssi=0x12,
                                         adv_length=0x82,
                                         num_sub_filters=0x03,
                                         sub_filter1_len=0x06,
                                         data1=b'\xff\xab\xcd\xef\xff',
                                         sub_filter2_len=0x02,
                                         data2=b'\xff\xee',
                                         sub_filter3_len=0x03,
                                         data3=b'\xff\xaa\xbb')
        exp = bytearray()
        exp.append(0x03)  # 00: Msg Type
        exp.append(0x01)  # 01: Message Spec Version
        exp.append(0x01)  # 02: Operation Code
        exp.append(0x95)  # 03: Filter ID
        exp.append(0x23)  # 04: Filter Priority
        exp.append(0x99)  # 05: Event Rate
        exp.append(0x12)  # 06: Min RSSI Level
        exp.append(0x82)  # 07: Advertisement Length
        exp.append(0x03)  # 08: Number of sub-filters.
        exp.append(0x06)  # 09: sub-filter 1 length
        exp.append(0xff)  # 10: sub-filter 1
        exp.append(0xab)  # 11: sub-filter 1
        exp.append(0xcd)  # 12: sub-filter 1
        exp.append(0xef)  # 13: sub-filter 1
        exp.append(0xff)  # 14: sub-filter 1
        exp.append(0x02)  # 15: sub-filter 2 length
        exp.append(0xff)  # 16: sub-filter 2
        exp.append(0xee)  # 17: sub-filter 2
        exp.append(0x03)  # 18: sub-filter 3 length
        exp.append(0xff)  # 19: sub-filter 3
        exp.append(0xaa)  # 20: sub-filter 3
        exp.append(0xbb)  # 21: sub-filter 3
        exp.append(0x01)  # 22: sub-filter 4 length
        exp.append(0xff)  # 23: sub-filter 4
        self.assertSequenceEqual(msg, exp)

    def test_ModifyFiltersV1(self):
        """ Verifies building a V1 Reset Message. """
        spec_v1 = af_devs.ssf.SSFDownlinkMessageSpecV1()

        msg = spec_v1.build_ctrl_message("MODIFY_FILTERS")
        exp = bytearray()
        exp.append(0x03)  # 00: Msg Type
        exp.append(0x01)  # 01: Message Spec Version
        exp.append(0x02)  # 02: Operation Code
        exp.append(0x00)  # 03: Filter ID
        exp.append(0x01)  # 04: Filter Priority
        exp.append(0x05)  # 05: Event Rate
        exp.append(0x30)  # 06: Min RSSI Level
        exp.append(0x05)  # 07: Advertisement Length
        exp.append(0x00)  # 08: Number of sub-filters.
        exp.append(0x01)  # 09: sub-filter 1 length
        exp.append(0xff)  # 10: sub-filter 1
        exp.append(0x01)  # 11: sub-filter 2 length
        exp.append(0xff)  # 12: sub-filter 2
        exp.append(0x01)  # 13: sub-filter 3 length
        exp.append(0xff)  # 14: sub-filter 3
        exp.append(0x01)  # 15: sub-filter 4 length
        exp.append(0xff)  # 16: sub-filter 4
        self.assertSequenceEqual(msg, exp)

        msg = spec_v1.build_ctrl_message("MODIFY_FILTERS",
                                         filter_id=0x95,
                                         filter_priority=0x23,
                                         event_rate=0x99,
                                         min_adv_rssi=0x12,
                                         adv_length=0x82,
                                         num_sub_filters=0x03,
                                         sub_filter1_len=0x06,
                                         data1=b'\xff\xab\xcd\xef\xff',
                                         sub_filter2_len=0x02,
                                         data2=b'\xff\xee',
                                         sub_filter3_len=0x03,
                                         data3=b'\xff\xaa\xbb')
        exp = bytearray()
        exp.append(0x03)  # 00: Msg Type
        exp.append(0x01)  # 01: Message Spec Version
        exp.append(0x02)  # 02: Operation Code
        exp.append(0x95)  # 03: Filter ID
        exp.append(0x23)  # 04: Filter Priority
        exp.append(0x99)  # 05: Event Rate
        exp.append(0x12)  # 06: Min RSSI Level
        exp.append(0x82)  # 07: Advertisement Length
        exp.append(0x03)  # 08: Number of sub-filters.
        exp.append(0x06)  # 09: sub-filter 1 length
        exp.append(0xff)  # 10: sub-filter 1
        exp.append(0xab)  # 11: sub-filter 1
        exp.append(0xcd)  # 12: sub-filter 1
        exp.append(0xef)  # 13: sub-filter 1
        exp.append(0xff)  # 14: sub-filter 1
        exp.append(0x02)  # 15: sub-filter 2 length
        exp.append(0xff)  # 16: sub-filter 2
        exp.append(0xee)  # 17: sub-filter 2
        exp.append(0x03)  # 18: sub-filter 3 length
        exp.append(0xff)  # 19: sub-filter 3
        exp.append(0xaa)  # 20: sub-filter 3
        exp.append(0xbb)  # 21: sub-filter 3
        exp.append(0x01)  # 22: sub-filter 4 length
        exp.append(0xff)  # 23: sub-filter 4
        self.assertSequenceEqual(msg, exp)

    def test_DeleteFiltersV1(self):
        """ Verifies building a V1 Reset Message. """
        spec_v1 = af_devs.ssf.SSFDownlinkMessageSpecV1()

        msg = spec_v1.build_ctrl_message("DELETE_FILTERS")
        exp = bytearray()
        exp.append(0x03)  # Msg Type
        exp.append(0x01)  # Message Spec Version
        exp.append(0x03)  # Operation Code
        self.assertSequenceEqual(msg, exp)

    def test_FilterStatusV1(self):
        """ Verifies building a V1 Reset Message. """
        spec_v1 = af_devs.ssf.SSFDownlinkMessageSpecV1()

        msg = spec_v1.build_ctrl_message("FILTER_STATUS")
        exp = bytearray()
        exp.append(0x03)  # Msg Type
        exp.append(0x01)  # Message Spec Version
        exp.append(0x04)  # Operation Code
        self.assertSequenceEqual(msg, exp)


if __name__ == '__main__':
    coloredlogs.install(level=LOG_LEVEL)

    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    # Validate library before Authentication.
    suite.addTests(loader.loadTestsFromTestCase(SSFTests))
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)
    suite = unittest.TestSuite()
