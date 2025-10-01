import logging
import unittest

import coloredlogs

from conductor.airfinder import devices as af_devs
from conductor.airfinder.messages import DownlinkMessageSpec, \
    MissingDownlinkArgument, \
    ControlMessageNotSupported, \
    InvalidDownlinkMessageType

LOG = logging.getLogger(__name__)
LOG_LEVEL = logging.DEBUG


class AccessPointTests(unittest.TestCase):

    def __init__(self, test_name):
        super().__init__(test_name)

    def test_UnicastV100(self):
        """ Verifies v1.0.0 Unicast Construction. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_0()

        # Mac Address is required.
        with self.assertRaises(MissingDownlinkArgument):
            spec.build_message('Unicast')

        # Normal Message
        msg = spec.build_message('Unicast',
                                 endnode_addr=b'\xaa\xbb\xcc\xdd\xee\xff',
                                 time_to_live_s=30,
                                 uuid=0x1234,
                                 data=bytearray(b'\x12\x12\x23'))
        exp = bytearray()
        exp.append(0x01)  # 00: Msg Type
        exp.append(0x0f)  # 01: Msg Len
        exp.append(0xaa)  # 02: Endnode Address
        exp.append(0xbb)  # 03: Endnode Address
        exp.append(0xcc)  # 04: Endnode Address
        exp.append(0xdd)  # 05: Endnode Address
        exp.append(0xee)  # 06: Endnode Address
        exp.append(0xff)  # 07: Endnode Address
        exp.append(0x00)  # 08: Time to Live
        exp.append(0x1e)  # 09: Time to Live
        exp.append(0x00)  # 10: UUID
        exp.append(0x00)  # 11: UUID
        exp.append(0x12)  # 12: UUID
        exp.append(0x34)  # 13: UUID
        exp.append(0x12)  # 14: Data
        exp.append(0x12)  # 15: Data
        exp.append(0x23)  # 16: Data
        self.assertSequenceEqual(msg, exp)

        # Message with Unused Keys
        msg = spec.build_message('Unicast',
                                 msg_spec_vers_major=1,
                                 msg_spec_vers_minor=0,
                                 msg_spec_vers_tag=0,
                                 endnode_addr=b'\xaa\xbb\xcc\xdd\xee\xff',
                                 time_to_live_s=30,
                                 uuid=0x1234,
                                 data=bytearray(b'\x12\x12\x23'))
        exp = bytearray()
        exp.append(0x01)  # 00: Msg Type
        exp.append(0x0f)  # 01: Msg Len
        exp.append(0xaa)  # 02: Endnode Address
        exp.append(0xbb)  # 03: Endnode Address
        exp.append(0xcc)  # 04: Endnode Address
        exp.append(0xdd)  # 05: Endnode Address
        exp.append(0xee)  # 06: Endnode Address
        exp.append(0xff)  # 07: Endnode Address
        exp.append(0x00)  # 08: Time to Live
        exp.append(0x1e)  # 09: Time to Live
        exp.append(0x00)  # 10: UUID
        exp.append(0x00)  # 11: UUID
        exp.append(0x12)  # 12: UUID
        exp.append(0x34)  # 13: UUID
        exp.append(0x12)  # 14: Data
        exp.append(0x12)  # 15: Data
        exp.append(0x23)  # 16: Data
        self.assertSequenceEqual(msg, exp)

    def test_MulticastV100(self):
        """ Verifies v1.0.0 Multicast Construction. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_0()

        # App Token is required.
        with self.assertRaises(MissingDownlinkArgument):
            spec.build_message('Multicast')

        # Normal Message
        msg = spec.build_message('Multicast',
                                 app_tok=b'\xaa\xbb\xcc\xdd\xee\xff\xaa\xbb'
                                 b'\xcc\xdd',
                                 time_to_live_s=30,
                                 uuid=0x1234,
                                 data=bytearray(b'\x12\x12\x23'))
        exp = bytearray()
        exp.append(0x02)  # 00: Msg Type
        exp.append(0x13)  # 01: Msg Len
        exp.append(0xaa)  # 02: Application Token
        exp.append(0xbb)  # 03: Application Token
        exp.append(0xcc)  # 04: Application Token
        exp.append(0xdd)  # 05: Application Token
        exp.append(0xee)  # 06: Application Token
        exp.append(0xff)  # 07: Application Token
        exp.append(0xaa)  # 08: Application Token
        exp.append(0xbb)  # 09: Application Token
        exp.append(0xcc)  # 10: Application Token
        exp.append(0xdd)  # 11: Application Token
        exp.append(0x00)  # 12: Time to Live
        exp.append(0x1e)  # 13: Time to Live
        exp.append(0x00)  # 14: UUID
        exp.append(0x00)  # 15: UUID
        exp.append(0x12)  # 16: UUID
        exp.append(0x34)  # 17: UUID
        exp.append(0x12)  # 18: Data
        exp.append(0x12)  # 19: Data
        exp.append(0x23)  # 20: Data
        self.assertSequenceEqual(msg, exp)

        # Message with Unused Keys
        msg = spec.build_message('Multicast',
                                 msg_spec_vers_major=1,
                                 msg_spec_vers_minor=0,
                                 msg_spec_vers_tag=0,
                                 app_tok=b'\xaa\xbb\xcc\xdd\xee\xff\xaa\xbb'
                                         b'\xcc\xdd',
                                 time_to_live_s=30,
                                 uuid=0x1234,
                                 data=bytearray(b'\x12\x12\x23'))
        exp = bytearray()
        exp.append(0x02)  # 00: Msg Type
        exp.append(0x13)  # 01: Msg Len
        exp.append(0xaa)  # 02: Application Token
        exp.append(0xbb)  # 03: Application Token
        exp.append(0xcc)  # 04: Application Token
        exp.append(0xdd)  # 05: Application Token
        exp.append(0xee)  # 06: Application Token
        exp.append(0xff)  # 07: Application Token
        exp.append(0xaa)  # 08: Application Token
        exp.append(0xbb)  # 09: Application Token
        exp.append(0xcc)  # 10: Application Token
        exp.append(0xdd)  # 11: Application Token
        exp.append(0x00)  # 12: Time to Live
        exp.append(0x1e)  # 13: Time to Live
        exp.append(0x00)  # 14: UUID
        exp.append(0x00)  # 15: UUID
        exp.append(0x12)  # 16: UUID
        exp.append(0x34)  # 17: UUID
        exp.append(0x12)  # 18: Data
        exp.append(0x12)  # 19: Data
        exp.append(0x23)  # 20: Data
        self.assertSequenceEqual(msg, exp)

    def test_ControlV100_SetAPType(self):
        """ Verifies v1.0.0 Set AP Type Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_0()

        msg = spec.build_ctrl_message('SET_AP_TYPE', ap_type=0x01)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x02)  # 3: Ctrl Cmd
        exp.append(0x01)  # 4: AP Type
        self.assertSequenceEqual(msg, exp)

    def test_ControlV100_SetLocGroup(self):
        """ Verifies v1.0.0 Set Location Group Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_0()

        msg = spec.build_ctrl_message('SET_LOCATION_GROUP', loc_group=0x14)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x03)  # 3: Ctrl Cmd
        exp.append(0x14)  # 4: Loc Group
        self.assertSequenceEqual(msg, exp)

    def test_ControlV100_SetLocWeight(self):
        """ Verifies v1.0.0 Set Location Weight Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_0()

        msg = spec.build_ctrl_message('SET_LOCATION_WEIGHT', loc_weight=0x79)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x04)  # 3: Ctrl Cmd
        exp.append(0x79)  # 4: Loc Weight
        self.assertSequenceEqual(msg, exp)

    def test_ControlV100_SetRssiAdjust(self):
        """ Verifies v1.0.0 Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_0()

        msg = spec.build_ctrl_message('SET_RSSI_ADJ', rssi_adj=0x54)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x05)  # 3: Ctrl Cmd
        exp.append(0x54)  # 4: Rssi Adj
        self.assertSequenceEqual(msg, exp)

    def test_ControlV100_SetAdvRate(self):
        """ Verifies v1.0.0 Set Advertising Rate Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_0()

        msg = spec.build_ctrl_message('SET_ADV_RATE', adv_rate=0xaa)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x04)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x06)  # 3: Ctrl Cmd
        exp.append(0x00)  # 4: Advertising Rate
        exp.append(0xaa)  # 5: Advertising Rate
        self.assertSequenceEqual(msg, exp)

    def test_ControlV100_SetAdvRefresh(self):
        """ Verifies v1.0.0 Advertising Refresh Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_0()

        msg = spec.build_ctrl_message('SET_ADV_REFRESH', adv_refresh=0x2398)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x04)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x07)  # 3: Ctrl Cmd
        exp.append(0x23)  # 4: Advertising Refresh
        exp.append(0x98)  # 4: Advertising Refresh
        self.assertSequenceEqual(msg, exp)

    def test_ControlV100_SetTimeSyncRate(self):
        """ Verifies v1.0.0 Set Time Sync Rate Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_0()

        msg = spec.build_ctrl_message('SET_TIME_SYNC_RATE',
                                      sync_time_rate=0x64a8b2ee)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x06)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x08)  # 3: Ctrl Cmd
        exp.append(0x64)  # 4: Sync Time Rate
        exp.append(0xa8)  # 5: Sync Time Rate
        exp.append(0xb2)  # 6: Sync Time Rate
        exp.append(0xee)  # 7: Sync Time Rate
        self.assertSequenceEqual(msg, exp)

    def test_ControlV100_SetConnTimeout(self):
        """ Verifies v1.0.0 Set Connection Timeout Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_0()

        msg = spec.build_ctrl_message('SET_CONN_TIMEOUT',
                                      conn_timeout=0x1b92c23d)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x06)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x09)  # 3: Ctrl Cmd
        exp.append(0x1b)  # 4: Connection Timeout
        exp.append(0x92)  # 5: Connection Timeout
        exp.append(0xc2)  # 6: Connection Timeout
        exp.append(0x3d)  # 7: Connection Timeout
        self.assertSequenceEqual(msg, exp)

    def test_ControlV100_SetStatusRate(self):
        """ Verifies v1.0.0 Set Status Rate Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_0()

        msg = spec.build_ctrl_message('SET_STATUS_RATE',
                                      status_rate=0x5b2acc32)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x06)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x0a)  # 3: Ctrl Cmd
        exp.append(0x5b)  # 4: Status Rate
        exp.append(0x2a)  # 5: Status Rate
        exp.append(0xcc)  # 6: Status Rate
        exp.append(0x32)  # 7: Status Rate
        self.assertSequenceEqual(msg, exp)

    def test_ControlV100_SetMailboxRate(self):
        """ Verifies v1.0.0 Set Mailbox Rate Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_0()

        msg = spec.build_ctrl_message('SET_MAILBOX_RATE',
                                      mailbox_int=0x79b18dc2)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x06)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x0B)  # 3: Ctrl Cmd
        exp.append(0x79)  # 4: Mailbox Rate
        exp.append(0xb1)  # 5: Mailbox Rate
        exp.append(0x8d)  # 6: Mailbox Rate
        exp.append(0xc2)  # 7: Mailbox Rate
        self.assertSequenceEqual(msg, exp)

    def test_ControlV100_SetQueueRate(self):
        """ Verifies v1.0.0 Set Queue Rate Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_0()

        msg = spec.build_ctrl_message('SET_QUEUE_SEND_RATE',
                                      send_rate=0x11bb2233)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x06)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x0C)  # 3: Ctrl Cmd
        exp.append(0x11)  # 4: Send Rate
        exp.append(0xbb)  # 5: Send Rate
        exp.append(0x22)  # 6: Send Rate
        exp.append(0x33)  # 7: Send Rate
        self.assertSequenceEqual(msg, exp)

    def test_ControlV100_SetQueueThresh(self):
        """ Verifies v1.0.0 Set Queue Thresh Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_0()

        msg = spec.build_ctrl_message('SET_QUEUE_THRESH', send_threshold=0x23)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x0D)  # 3: Ctrl Cmd
        exp.append(0x23)  # 4: Send Threshold
        self.assertSequenceEqual(msg, exp)

    def test_ControlV100_SetEnableBLE(self):
        """ Verifies v1.0.0 Set Enable BLE Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_0()

        msg = spec.build_ctrl_message('SET_ENABLE_BLE', enable=True)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x01)  # 2: Ctrl Cmd
        exp.append(0x00)  # 3: Ctrl Cmd
        exp.append(0x01)  # 4: Enable BLe
        self.assertSequenceEqual(msg, exp)

    def test_ControlV100_GetStatus(self):
        """ Verifies v1.0.0 Get Status Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_0()

        msg = spec.build_ctrl_message('GET_STATUS')
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 1: Msg Len
        exp.append(0x01)  # 2: Ctrl Cmd
        exp.append(0x06)  # 3: Ctrl Cmd
        self.assertSequenceEqual(msg, exp)

    def test_ControlV100_SetEnableLocation(self):
        """ Verifies v1.0.0 Set Enable Location Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_0()

        msg = spec.build_ctrl_message('SET_ENABLE_LOCATION', enable=True)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x01)  # 2: Ctrl Cmd
        exp.append(0x07)  # 3: Ctrl Cmd
        exp.append(0x01)  # 4: Enable
        self.assertSequenceEqual(msg, exp)

    def test_ControlV100_TriggerAssert(self):
        """ Verifies v1.0.0 Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_0()

        msg = spec.build_ctrl_message('TRIGGER_ASSERT')
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 1: Msg Len
        exp.append(0x05)  # 2: Ctrl Cmd
        exp.append(0x00)  # 3: Ctrl Cmd
        self.assertSequenceEqual(msg, exp)

    def test_ControlV100_SetSyncDC(self):
        """ Verifies v1.0.0 Set Sync DC Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_0()

        with self.assertRaises(ControlMessageNotSupported):
            spec.build_ctrl_message('SET_SYNC_DC', sync=0x99)

    def test_ControlV100_SetSchedule(self):
        """ Verifies v1.0.0 Set Schedule Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_0()

        with self.assertRaises(ControlMessageNotSupported):
            spec.build_ctrl_message('SET_SCHEDULE',
                                    sched=b'\x00\x00\x00\x00\x00\x00\x00\x00'
                                          b'\x00\x00\x00\x00\x00\x00\x00\x00'
                                          b'\x00\x00\x00\x00\x00')

    def test_ControlV100_SetAckMode(self):
        """ Verifies v1.0.0 Set Ack Mode Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_0()

        with self.assertRaises(ControlMessageNotSupported):
            spec.build_ctrl_message('SET_ACK_MODE', mode=0x00)

    def test_ControlV100_SetTXPower(self):
        """ Verifies v1.0.0 Set TX Power Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_0()

        with self.assertRaises(ControlMessageNotSupported):
            spec.build_ctrl_message('SET_TX_POWER', tx_pwr=0x55)

    def test_ControlV100_ConfigBLEFrontEnd(self):
        """ Verifies v1.0.0 Config BLE Frontend Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_0()
        with self.assertRaises(ControlMessageNotSupported):
            spec.build_ctrl_message('CONFIG_BLE_FRONT_END', config=0x27)

    def test_ControlV100_SampleBatt(self):
        """ Verifies v1.0.0 Sample Battery Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_0()
        with self.assertRaises(ControlMessageNotSupported):
            spec.build_ctrl_message('SAMPLE_BATT')

    def test_ControlV100_SetDST(self):
        """ Verifies v1.0.0 Set DST Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_0()
        with self.assertRaises(ControlMessageNotSupported):
            spec.build_ctrl_message('SET_DST', enable=True)

    def test_ControlV100_SetDutyCycle(self):
        """ Verifies v1.0.0 Set Duty Cycle Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_0()
        with self.assertRaises(ControlMessageNotSupported):
            spec.build_ctrl_message('SET_DUTY_CYCLE', window=0x55)

    def test_ControlV100_SetGWRssi(self):
        """ Verifies v1.0.0 Set GW RSSI Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_0()
        with self.assertRaises(ControlMessageNotSupported):
            spec.build_ctrl_message('SET_SYM_GW_RSSI', rssi=0x95)

    def test_ControlV100_SetScanMode(self):
        """ Verifies v1.0.0 Set Scan Mode Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_0()
        with self.assertRaises(ControlMessageNotSupported):
            spec.build_ctrl_message('SET_SYM_SCAN_MODE', mode=0x00)

    def test_ControlV100_SetScanAttempts(self):
        """ Verifies v1.0.0 Set Scan Attempts Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_0()
        with self.assertRaises(ControlMessageNotSupported):
            spec.build_ctrl_message('SET_SYM_SCAN_ATTEMPTS', attempts=0x55)

    def test_ControlV100_SetScanHopInterval(self):
        """ Verifies v1.0.0 Set Scan Hop Interval Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_0()
        with self.assertRaises(ControlMessageNotSupported):
            spec.build_ctrl_message('SET_SYM_HOP_INT', interval=0x11223344)

    def test_ControlV100_SetMaxGWError(self):
        """ Verifies v1.0.0 Set Duty Cycle Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_0()
        with self.assertRaises(ControlMessageNotSupported):
            spec.build_ctrl_message('SET_MAX_GW_ERROR', max_err=0x90)

    def test_ControlV100_SetInfoScanInterval(self):
        """ Verifies v1.0.0 Set Info Scan Interval Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_0()

        with self.assertRaises(ControlMessageNotSupported):
            spec.build_ctrl_message('SET_SYM_INFO_SCAN_INT',
                                    interval=0xaabb4433)

    def test_SetConfigModeV100(self):
        """ Verifies v1.0.0 Config Mode Construction. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_0()

        msg = spec.build_message("SetConfigMode",
                                 timeout=2348,
                                 net_tok=0x3a2d1d4c,
                                 app_tok=b'\xa8\xa2\x1c\xa1\x3b\xc8\x32\xd1'
                                         b'\xaa\x39',
                                 key=b'\x11\x1a\x9c\xad\xbd\x9b\x0e\x1a\xc7'
                                         b'\xc4\xa8\xb2\xe2\xd9\xe4\xc5')
        exp = bytearray()
        exp.append(0xb0)  # 00: Msg Type
        exp.append(0x22)  # 01: Msg Len
        exp.append(0x00)  # 02: Timeout
        exp.append(0x00)  # 03: Timeout
        exp.append(0x09)  # 04: Timeout
        exp.append(0x2c)  # 05: Timeout
        exp.append(0x3a)  # 06: Network Token
        exp.append(0x2d)  # 07: Network Token
        exp.append(0x1d)  # 08: Network Token
        exp.append(0x4c)  # 09: Network Token
        exp.append(0xa8)  # 10: Application Token
        exp.append(0xa2)  # 11: Application Token
        exp.append(0x1c)  # 12: Application Token
        exp.append(0xa1)  # 13: Application Token
        exp.append(0x3b)  # 14: Application Token
        exp.append(0xc8)  # 15: Application Token
        exp.append(0x32)  # 16: Application Token
        exp.append(0xd1)  # 17: Application Token
        exp.append(0xaa)  # 18: Application Token
        exp.append(0x39)  # 19: Application Token
        exp.append(0x11)  # 20: Key
        exp.append(0x1a)  # 21: Key
        exp.append(0x9c)  # 22: Key
        exp.append(0xad)  # 23: Key
        exp.append(0xbd)  # 24: Key
        exp.append(0x9b)  # 25: Key
        exp.append(0x0e)  # 26: Key
        exp.append(0x1a)  # 27: Key
        exp.append(0xc7)  # 28: Key
        exp.append(0xc4)  # 29: Key
        exp.append(0xa8)  # 30: Key
        exp.append(0xb2)  # 31: Key
        exp.append(0xe2)  # 32: Key
        exp.append(0xd9)  # 33: Key
        exp.append(0xe4)  # 34: Key
        exp.append(0xc5)  # 35: Key
        self.assertSequenceEqual(msg, exp)

    def test_UnicastV101(self):
        """ Verifies v1.0.1 Unicast Construction. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_1()

        # Mac Address is required.
        with self.assertRaises(MissingDownlinkArgument):
            spec.build_message('Unicast')

        # Normal Message
        msg = spec.build_message('Unicast',
                                 endnode_addr=b'\xaa\xbb\xcc\xdd\xee\xff',
                                 time_to_live_s=30,
                                 uuid=0x1234,
                                 data=bytearray(b'\x12\x12\x23'))
        exp = bytearray()
        exp.append(0x01)  # 00: Msg Type
        exp.append(0x0f)  # 01: Msg Len
        exp.append(0xaa)  # 02: Endnode Address
        exp.append(0xbb)  # 03: Endnode Address
        exp.append(0xcc)  # 04: Endnode Address
        exp.append(0xdd)  # 05: Endnode Address
        exp.append(0xee)  # 06: Endnode Address
        exp.append(0xff)  # 07: Endnode Address
        exp.append(0x00)  # 08: Time to Live
        exp.append(0x1e)  # 09: Time to Live
        exp.append(0x00)  # 10: UUID
        exp.append(0x00)  # 11: UUID
        exp.append(0x12)  # 12: UUID
        exp.append(0x34)  # 13: UUID
        exp.append(0x12)  # 14: Data
        exp.append(0x12)  # 15: Data
        exp.append(0x23)  # 16: Data
        self.assertSequenceEqual(msg, exp)

        # Message with Unused Keys
        msg = spec.build_message('Unicast',
                                 msg_spec_vers_major=1,
                                 msg_spec_vers_minor=0,
                                 msg_spec_vers_tag=1,
                                 endnode_addr=b'\xaa\xbb\xcc\xdd\xee\xff',
                                 time_to_live_s=30,
                                 uuid=0x1234,
                                 data=bytearray(b'\x12\x12\x23'))
        exp = bytearray()
        exp.append(0x01)  # 00: Msg Type
        exp.append(0x0f)  # 01: Msg Len
        exp.append(0xaa)  # 02: Endnode Address
        exp.append(0xbb)  # 03: Endnode Address
        exp.append(0xcc)  # 04: Endnode Address
        exp.append(0xdd)  # 05: Endnode Address
        exp.append(0xee)  # 06: Endnode Address
        exp.append(0xff)  # 07: Endnode Address
        exp.append(0x00)  # 08: Time to Live
        exp.append(0x1e)  # 09: Time to Live
        exp.append(0x00)  # 10: UUID
        exp.append(0x00)  # 11: UUID
        exp.append(0x12)  # 12: UUID
        exp.append(0x34)  # 13: UUID
        exp.append(0x12)  # 14: Data
        exp.append(0x12)  # 15: Data
        exp.append(0x23)  # 16: Data
        self.assertSequenceEqual(msg, exp)

    def test_MulticastV101(self):
        """ Verifies v1.0.1 Multicast Construction. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_1()

        # App Token is required.
        with self.assertRaises(MissingDownlinkArgument):
            spec.build_message('Multicast')

        # Normal Message
        msg = spec.build_message('Multicast',
                                 app_tok=b'\xaa\xbb\xcc\xdd\xee\xff\xaa\xbb'
                                 b'\xcc\xdd',
                                 time_to_live_s=30,
                                 uuid=0x1234,
                                 data=bytearray(b'\x12\x12\x23'))
        exp = bytearray()
        exp.append(0x02)  # 00: Msg Type
        exp.append(0x13)  # 01: Msg Len
        exp.append(0xaa)  # 02: Application Token
        exp.append(0xbb)  # 03: Application Token
        exp.append(0xcc)  # 04: Application Token
        exp.append(0xdd)  # 05: Application Token
        exp.append(0xee)  # 06: Application Token
        exp.append(0xff)  # 07: Application Token
        exp.append(0xaa)  # 08: Application Token
        exp.append(0xbb)  # 09: Application Token
        exp.append(0xcc)  # 10: Application Token
        exp.append(0xdd)  # 11: Application Token
        exp.append(0x00)  # 12: Time to Live
        exp.append(0x1e)  # 13: Time to Live
        exp.append(0x00)  # 14: UUID
        exp.append(0x00)  # 15: UUID
        exp.append(0x12)  # 16: UUID
        exp.append(0x34)  # 17: UUID
        exp.append(0x12)  # 18: Data
        exp.append(0x12)  # 19: Data
        exp.append(0x23)  # 20: Data
        self.assertSequenceEqual(msg, exp)

        # Message with Unused Keys
        msg = spec.build_message('Multicast',
                                 msg_spec_vers_major=1,
                                 msg_spec_vers_minor=0,
                                 msg_spec_vers_tag=1,
                                 app_tok=b'\xaa\xbb\xcc\xdd\xee\xff\xaa\xbb'
                                 b'\xcc\xdd',
                                 time_to_live_s=30,
                                 uuid=0x1234,
                                 data=bytearray(b'\x12\x12\x23'))
        exp = bytearray()
        exp.append(0x02)  # 00: Msg Type
        exp.append(0x13)  # 01: Msg Len
        exp.append(0xaa)  # 02: Application Token
        exp.append(0xbb)  # 03: Application Token
        exp.append(0xcc)  # 04: Application Token
        exp.append(0xdd)  # 05: Application Token
        exp.append(0xee)  # 06: Application Token
        exp.append(0xff)  # 07: Application Token
        exp.append(0xaa)  # 08: Application Token
        exp.append(0xbb)  # 09: Application Token
        exp.append(0xcc)  # 10: Application Token
        exp.append(0xdd)  # 11: Application Token
        exp.append(0x00)  # 12: Time to Live
        exp.append(0x1e)  # 13: Time to Live
        exp.append(0x00)  # 14: UUID
        exp.append(0x00)  # 15: UUID
        exp.append(0x12)  # 16: UUID
        exp.append(0x34)  # 17: UUID
        exp.append(0x12)  # 18: Data
        exp.append(0x12)  # 19: Data
        exp.append(0x23)  # 20: Data
        self.assertSequenceEqual(msg, exp)

    def test_ControlV101_SetAPType(self):
        """ Verifies v1.0.1 Set AP Type Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_1()

        msg = spec.build_ctrl_message('SET_AP_TYPE', ap_type=0x01)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x02)  # 3: Ctrl Cmd
        exp.append(0x01)  # 4: AP Type
        self.assertSequenceEqual(msg, exp)

    def test_ControlV101_SetLocGroup(self):
        """ Verifies v1.0.1 Set Location Group Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_1()

        msg = spec.build_ctrl_message('SET_LOCATION_GROUP', loc_group=0x14)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x03)  # 3: Ctrl Cmd
        exp.append(0x14)  # 4: Loc Group
        self.assertSequenceEqual(msg, exp)

    def test_ControlV101_SetLocWeight(self):
        """ Verifies v1.0.1 Set Location Weight Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_1()

        msg = spec.build_ctrl_message('SET_LOCATION_WEIGHT', loc_weight=0x79)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x04)  # 3: Ctrl Cmd
        exp.append(0x79)  # 4: Loc Weight
        self.assertSequenceEqual(msg, exp)

    def test_ControlV101_SetRssiAdjust(self):
        """ Verifies v1.0.1 Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_1()

        msg = spec.build_ctrl_message('SET_RSSI_ADJ', rssi_adj=0x54)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x05)  # 3: Ctrl Cmd
        exp.append(0x54)  # 4: Rssi Adj
        self.assertSequenceEqual(msg, exp)

    def test_ControlV101_SetAdvRate(self):
        """ Verifies v1.0.1 Set Advertising Rate Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_1()

        msg = spec.build_ctrl_message('SET_ADV_RATE', adv_rate=0xaa)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x04)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x06)  # 3: Ctrl Cmd
        exp.append(0x00)  # 4: Advertising Rate
        exp.append(0xaa)  # 5: Advertising Rate
        self.assertSequenceEqual(msg, exp)

    def test_ControlV101_SetAdvRefresh(self):
        """ Verifies v1.0.1 Advertising Refresh Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_1()

        msg = spec.build_ctrl_message('SET_ADV_REFRESH', adv_refresh=0x2398)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x04)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x07)  # 3: Ctrl Cmd
        exp.append(0x23)  # 4: Advertising Refresh
        exp.append(0x98)  # 4: Advertising Refresh
        self.assertSequenceEqual(msg, exp)

    def test_ControlV101_SetTimeSyncRate(self):
        """ Verifies v1.0.1 Set Time Sync Rate Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_1()

        msg = spec.build_ctrl_message('SET_TIME_SYNC_RATE',
                                      sync_time_rate=0x64a8b2ee)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x06)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x08)  # 3: Ctrl Cmd
        exp.append(0x64)  # 4: Sync Time Rate
        exp.append(0xa8)  # 5: Sync Time Rate
        exp.append(0xb2)  # 6: Sync Time Rate
        exp.append(0xee)  # 7: Sync Time Rate
        self.assertSequenceEqual(msg, exp)

    def test_ControlV101_SetConnTimeout(self):
        """ Verifies v1.0.1 Set Connection Timeout Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_1()

        msg = spec.build_ctrl_message('SET_CONN_TIMEOUT',
                                      conn_timeout=0x1b92c23d)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x06)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x09)  # 3: Ctrl Cmd
        exp.append(0x1b)  # 4: Connection Timeout
        exp.append(0x92)  # 5: Connection Timeout
        exp.append(0xc2)  # 6: Connection Timeout
        exp.append(0x3d)  # 7: Connection Timeout
        self.assertSequenceEqual(msg, exp)

    def test_ControlV101_SetStatusRate(self):
        """ Verifies v1.0.1 Set Status Rate Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_1()

        msg = spec.build_ctrl_message('SET_STATUS_RATE',
                                      status_rate=0x5b2acc32)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x06)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x0a)  # 3: Ctrl Cmd
        exp.append(0x5b)  # 4: Status Rate
        exp.append(0x2a)  # 5: Status Rate
        exp.append(0xcc)  # 6: Status Rate
        exp.append(0x32)  # 7: Status Rate
        self.assertSequenceEqual(msg, exp)

    def test_ControlV101_SetMailboxRate(self):
        """ Verifies v1.0.1 Set Mailbox Rate Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_1()

        msg = spec.build_ctrl_message('SET_MAILBOX_RATE',
                                      mailbox_int=0x79b18dc2)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x06)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x0B)  # 3: Ctrl Cmd
        exp.append(0x79)  # 4: Mailbox Rate
        exp.append(0xb1)  # 5: Mailbox Rate
        exp.append(0x8d)  # 6: Mailbox Rate
        exp.append(0xc2)  # 7: Mailbox Rate
        self.assertSequenceEqual(msg, exp)

    def test_ControlV101_SetQueueRate(self):
        """ Verifies v1.0.1 Set Queue Rate Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_1()

        msg = spec.build_ctrl_message('SET_QUEUE_SEND_RATE',
                                      send_rate=0x11bb2233)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x06)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x0C)  # 3: Ctrl Cmd
        exp.append(0x11)  # 4: Send Rate
        exp.append(0xbb)  # 5: Send Rate
        exp.append(0x22)  # 6: Send Rate
        exp.append(0x33)  # 7: Send Rate
        self.assertSequenceEqual(msg, exp)

    def test_ControlV101_SetQueueThresh(self):
        """ Verifies v1.0.1 Set Queue Thresh Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_1()

        msg = spec.build_ctrl_message('SET_QUEUE_THRESH', send_threshold=0x23)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x0D)  # 3: Ctrl Cmd
        exp.append(0x23)  # 4: Send Threshold
        self.assertSequenceEqual(msg, exp)

    def test_ControlV101_SetEnableBLE(self):
        """ Verifies v1.0.1 Set Enable BLE Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_1()

        msg = spec.build_ctrl_message('SET_ENABLE_BLE', enable=True)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x01)  # 2: Ctrl Cmd
        exp.append(0x00)  # 3: Ctrl Cmd
        exp.append(0x01)  # 4: Enable BLe
        self.assertSequenceEqual(msg, exp)

    def test_ControlV101_GetStatus(self):
        """ Verifies v1.0.1 Get Status Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_1()

        msg = spec.build_ctrl_message('GET_STATUS')
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 1: Msg Len
        exp.append(0x01)  # 2: Ctrl Cmd
        exp.append(0x06)  # 3: Ctrl Cmd
        self.assertSequenceEqual(msg, exp)

    def test_ControlV101_SetEnableLocation(self):
        """ Verifies v1.0.1 Set Enable Location Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_1()

        msg = spec.build_ctrl_message('SET_ENABLE_LOCATION', enable=True)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x01)  # 2: Ctrl Cmd
        exp.append(0x07)  # 3: Ctrl Cmd
        exp.append(0x01)  # 4: Enable
        self.assertSequenceEqual(msg, exp)

    def test_ControlV101_TriggerAssert(self):
        """ Verifies v1.0.1 Trigger Assert Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_1()

        msg = spec.build_ctrl_message('TRIGGER_ASSERT')
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 1: Msg Len
        exp.append(0x05)  # 2: Ctrl Cmd
        exp.append(0x00)  # 3: Ctrl Cmd
        self.assertSequenceEqual(msg, exp)

    def test_ControlV101_SetSyncDC(self):
        """ Verifies v1.0.1 Set Sync DC Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_1()

        msg = spec.build_ctrl_message('SET_SYNC_DC', sync=0x99)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x12)  # 3: Ctrl Cmd
        exp.append(0x99)  # 4: DC Sync
        self.assertSequenceEqual(msg, exp)

    def test_ControlV101_SetSchedule(self):
        """ Verifies v1.0.1 Set Schedule Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_1()

        msg = spec.build_ctrl_message('SET_SCHEDULE',
                                      sched=b'\x00\x00\x00\x00\x00\x00\x00\x00'
                                            b'\x00\x00\x00\x00\x00\x00\x00\x00'
                                            b'\x00\x00\x00\x00\x00')
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x17)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x20)  # 3: Ctrl Cmd
        for x in range(21):
            exp.append(0x00)
        self.assertSequenceEqual(msg, exp)

    def test_ControlV101_SetAckMode(self):
        """ Verifies v1.0.1 Set Ack Mode Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_1()

        msg = spec.build_ctrl_message('SET_ACK_MODE', mode=0x00)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x01)  # 2: Ctrl Cmd
        exp.append(0x08)  # 3: Ctrl Cmd
        exp.append(0x00)  # 4: Mode
        self.assertSequenceEqual(msg, exp)

    def test_ControlV101_SetTXPower(self):
        """ Verifies v1.0.1 Set TX Power Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_1()

        msg = spec.build_ctrl_message('SET_TX_POWER', tx_pwr=0x55)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x01)  # 2: Ctrl Cmd
        exp.append(0x09)  # 3: Ctrl Cmd
        exp.append(0x55)  # 4: TX Power
        self.assertSequenceEqual(msg, exp)

    def test_ControlV101_ConfigBLEFrontEnd(self):
        """ Verifies v1.0.1 Config BLE Frontend Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_1()
        with self.assertRaises(ControlMessageNotSupported):
            spec.build_ctrl_message('CONFIG_BLE_FRONT_END', config=0x27)

    def test_ControlV101_SampleBatt(self):
        """ Verifies v1.0.1 Sample Battery Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_1()
        with self.assertRaises(ControlMessageNotSupported):
            spec.build_ctrl_message('SAMPLE_BATT')

    def test_ControlV101_SetDST(self):
        """ Verifies v1.0.1 Set DST Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_1()
        with self.assertRaises(ControlMessageNotSupported):
            spec.build_ctrl_message('SET_DST', enable=True)

    def test_ControlV101_SetDutyCycle(self):
        """ Verifies v1.0.1 Set Duty Cycle Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_1()
        with self.assertRaises(ControlMessageNotSupported):
            spec.build_ctrl_message('SET_DUTY_CYCLE', window=0x55)

    def test_ControlV101_SetGWRssi(self):
        """ Verifies v1.0.1 Set GW RSSI Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_1()
        with self.assertRaises(ControlMessageNotSupported):
            spec.build_ctrl_message('SET_SYM_GW_RSSI', rssi=0x95)

    def test_ControlV101_SetScanMode(self):
        """ Verifies v1.0.1 Set Scan Mode Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_1()
        with self.assertRaises(ControlMessageNotSupported):
            spec.build_ctrl_message('SET_SYM_SCAN_MODE', mode=0x00)

    def test_ControlV101_SetScanAttempts(self):
        """ Verifies v1.0.1 Set Scan Attempts Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_1()
        with self.assertRaises(ControlMessageNotSupported):
            spec.build_ctrl_message('SET_SYM_SCAN_ATTEMPTS', attempts=0x55)

    def test_ControlV101_SetScanHopInterval(self):
        """ Verifies v1.0.0 Set Scan Hop Interval Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_1()
        with self.assertRaises(ControlMessageNotSupported):
            spec.build_ctrl_message('SET_SYM_HOP_INT', interval=0x11223344)

    def test_ControlV101_SetMaxGWError(self):
        """ Verifies v1.0.1 Set Duty Cycle Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_1()
        with self.assertRaises(ControlMessageNotSupported):
            spec.build_ctrl_message('SET_MAX_GW_ERROR', max_err=0x90)

    def test_ControlV101_SetInfoScanInterval(self):
        """ Verifies v1.0.1 Set Info Scan Interval Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_1()

        with self.assertRaises(ControlMessageNotSupported):
            spec.build_ctrl_message('SET_SYM_INFO_SCAN_INT',
                                    interval=0xaabb4433)

    def test_SetConfigModeV101(self):
        """ Verifies v1.0.1 Config Mode Construction. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_0_1()

        msg = spec.build_message("SetConfigMode",
                                 timeout=2348,
                                 net_tok=0x3a2d1d4c,
                                 app_tok=b'\xa8\xa2\x1c\xa1\x3b\xc8\x32\xd1'
                                         b'\xaa\x39',
                                 key=b'\x11\x1a\x9c\xad\xbd\x9b\x0e\x1a\xc7'
                                         b'\xc4\xa8\xb2\xe2\xd9\xe4\xc5')
        exp = bytearray()
        exp.append(0xb0)  # 00: Msg Type
        exp.append(0x22)  # 01: Msg Len
        exp.append(0x00)  # 02: Timeout
        exp.append(0x00)  # 03: Timeout
        exp.append(0x09)  # 04: Timeout
        exp.append(0x2c)  # 05: Timeout
        exp.append(0x3a)  # 06: Network Token
        exp.append(0x2d)  # 07: Network Token
        exp.append(0x1d)  # 08: Network Token
        exp.append(0x4c)  # 09: Network Token
        exp.append(0xa8)  # 10: Application Token
        exp.append(0xa2)  # 11: Application Token
        exp.append(0x1c)  # 12: Application Token
        exp.append(0xa1)  # 13: Application Token
        exp.append(0x3b)  # 14: Application Token
        exp.append(0xc8)  # 15: Application Token
        exp.append(0x32)  # 16: Application Token
        exp.append(0xd1)  # 17: Application Token
        exp.append(0xaa)  # 18: Application Token
        exp.append(0x39)  # 19: Application Token
        exp.append(0x11)  # 20: Key
        exp.append(0x1a)  # 21: Key
        exp.append(0x9c)  # 22: Key
        exp.append(0xad)  # 23: Key
        exp.append(0xbd)  # 24: Key
        exp.append(0x9b)  # 25: Key
        exp.append(0x0e)  # 26: Key
        exp.append(0x1a)  # 27: Key
        exp.append(0xc7)  # 28: Key
        exp.append(0xc4)  # 29: Key
        exp.append(0xa8)  # 30: Key
        exp.append(0xb2)  # 31: Key
        exp.append(0xe2)  # 32: Key
        exp.append(0xd9)  # 33: Key
        exp.append(0xe4)  # 34: Key
        exp.append(0xc5)  # 35: Key
        self.assertSequenceEqual(msg, exp)

    def test_UnicastV110(self):
        """ Verifies v1.1.0 Unicast Construction. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_1_0()

        # Mac Address is required.
        with self.assertRaises(MissingDownlinkArgument):
            spec.build_message('Unicast')

        # Normal Message
        msg = spec.build_message('Unicast',
                                 endnode_addr=b'\xaa\xbb\xcc\xdd\xee\xff',
                                 time_to_live_s=30,
                                 uuid=0x1234,
                                 data=bytearray(b'\x12\x12\x23'))
        exp = bytearray()
        exp.append(0x01)  # 00: Msg Type
        exp.append(0x0f)  # 01: Msg Len
        exp.append(0xaa)  # 02: Endnode Address
        exp.append(0xbb)  # 03: Endnode Address
        exp.append(0xcc)  # 04: Endnode Address
        exp.append(0xdd)  # 05: Endnode Address
        exp.append(0xee)  # 06: Endnode Address
        exp.append(0xff)  # 07: Endnode Address
        exp.append(0x00)  # 08: Time to Live
        exp.append(0x1e)  # 09: Time to Live
        exp.append(0x00)  # 10: UUID
        exp.append(0x00)  # 11: UUID
        exp.append(0x12)  # 12: UUID
        exp.append(0x34)  # 13: UUID
        exp.append(0x12)  # 14: Data
        exp.append(0x12)  # 15: Data
        exp.append(0x23)  # 16: Data
        self.assertSequenceEqual(msg, exp)

        # Message with Unused Keys
        msg = spec.build_message('Unicast',
                                 msg_spec_vers_major=1,
                                 msg_spec_vers_minor=0,
                                 msg_spec_vers_tag=0,
                                 endnode_addr=b'\xaa\xbb\xcc\xdd\xee\xff',
                                 time_to_live_s=30,
                                 uuid=0x1234,
                                 data=bytearray(b'\x12\x12\x23'))
        exp = bytearray()
        exp.append(0x01)  # 00: Msg Type
        exp.append(0x0f)  # 01: Msg Len
        exp.append(0xaa)  # 02: Endnode Address
        exp.append(0xbb)  # 03: Endnode Address
        exp.append(0xcc)  # 04: Endnode Address
        exp.append(0xdd)  # 05: Endnode Address
        exp.append(0xee)  # 06: Endnode Address
        exp.append(0xff)  # 07: Endnode Address
        exp.append(0x00)  # 08: Time to Live
        exp.append(0x1e)  # 09: Time to Live
        exp.append(0x00)  # 10: UUID
        exp.append(0x00)  # 11: UUID
        exp.append(0x12)  # 12: UUID
        exp.append(0x34)  # 13: UUID
        exp.append(0x12)  # 14: Data
        exp.append(0x12)  # 15: Data
        exp.append(0x23)  # 16: Data
        self.assertSequenceEqual(msg, exp)

    def test_MulticastV110(self):
        """ Verifies v1.1.0 Multicast Construction. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_1_0()

        # App Token is required.
        with self.assertRaises(MissingDownlinkArgument):
            spec.build_message('Multicast')

        # Normal Message
        msg = spec.build_message('Multicast',
                                 app_tok=b'\xaa\xbb\xcc\xdd\xee\xff\xaa\xbb'
                                 b'\xcc\xdd',
                                 time_to_live_s=30,
                                 uuid=0x1234,
                                 data=bytearray(b'\x12\x12\x23'))
        exp = bytearray()
        exp.append(0x02)  # 00: Msg Type
        exp.append(0x13)  # 01: Msg Len
        exp.append(0xaa)  # 02: Application Token
        exp.append(0xbb)  # 03: Application Token
        exp.append(0xcc)  # 04: Application Token
        exp.append(0xdd)  # 05: Application Token
        exp.append(0xee)  # 06: Application Token
        exp.append(0xff)  # 07: Application Token
        exp.append(0xaa)  # 08: Application Token
        exp.append(0xbb)  # 09: Application Token
        exp.append(0xcc)  # 10: Application Token
        exp.append(0xdd)  # 11: Application Token
        exp.append(0x00)  # 12: Time to Live
        exp.append(0x1e)  # 13: Time to Live
        exp.append(0x00)  # 14: UUID
        exp.append(0x00)  # 15: UUID
        exp.append(0x12)  # 16: UUID
        exp.append(0x34)  # 17: UUID
        exp.append(0x12)  # 18: Data
        exp.append(0x12)  # 19: Data
        exp.append(0x23)  # 20: Data
        self.assertSequenceEqual(msg, exp)

        # Message with Unused Keys
        msg = spec.build_message('Multicast',
                                 msg_spec_vers_major=1,
                                 msg_spec_vers_minor=0,
                                 msg_spec_vers_tag=1,
                                 app_tok=b'\xaa\xbb\xcc\xdd\xee\xff\xaa\xbb'
                                 b'\xcc\xdd',
                                 time_to_live_s=30,
                                 uuid=0x1234,
                                 data=bytearray(b'\x12\x12\x23'))
        exp = bytearray()
        exp.append(0x02)  # 00: Msg Type
        exp.append(0x13)  # 01: Msg Len
        exp.append(0xaa)  # 02: Application Token
        exp.append(0xbb)  # 03: Application Token
        exp.append(0xcc)  # 04: Application Token
        exp.append(0xdd)  # 05: Application Token
        exp.append(0xee)  # 06: Application Token
        exp.append(0xff)  # 07: Application Token
        exp.append(0xaa)  # 08: Application Token
        exp.append(0xbb)  # 09: Application Token
        exp.append(0xcc)  # 10: Application Token
        exp.append(0xdd)  # 11: Application Token
        exp.append(0x00)  # 12: Time to Live
        exp.append(0x1e)  # 13: Time to Live
        exp.append(0x00)  # 14: UUID
        exp.append(0x00)  # 15: UUID
        exp.append(0x12)  # 16: UUID
        exp.append(0x34)  # 17: UUID
        exp.append(0x12)  # 18: Data
        exp.append(0x12)  # 19: Data
        exp.append(0x23)  # 20: Data
        self.assertSequenceEqual(msg, exp)

    def test_ControlV110_SetAPType(self):
        """ Verifies v1.1.0 Set AP Type Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_1_0()

        msg = spec.build_ctrl_message('SET_AP_TYPE', ap_type=0x01)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x02)  # 3: Ctrl Cmd
        exp.append(0x01)  # 4: AP Type
        self.assertSequenceEqual(msg, exp)

    def test_ControlV110_SetLocGroup(self):
        """ Verifies v1.1.0 Set Location Group Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_1_0()

        msg = spec.build_ctrl_message('SET_LOCATION_GROUP', loc_group=0x14)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x03)  # 3: Ctrl Cmd
        exp.append(0x14)  # 4: Loc Group
        self.assertSequenceEqual(msg, exp)

    def test_ControlV110_SetLocWeight(self):
        """ Verifies v1.1.0 Set Location Weight Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_1_0()

        msg = spec.build_ctrl_message('SET_LOCATION_WEIGHT', loc_weight=0x79)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x04)  # 3: Ctrl Cmd
        exp.append(0x79)  # 4: Loc Weight
        self.assertSequenceEqual(msg, exp)

    def test_ControlV110_SetRssiAdjust(self):
        """ Verifies v1.1.0 Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_1_0()

        msg = spec.build_ctrl_message('SET_RSSI_ADJ', rssi_adj=0x54)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x05)  # 3: Ctrl Cmd
        exp.append(0x54)  # 4: Rssi Adj
        self.assertSequenceEqual(msg, exp)

    def test_ControlV110_SetAdvRate(self):
        """ Verifies v1.1.0 Set Advertising Rate Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_1_0()

        msg = spec.build_ctrl_message('SET_ADV_RATE', adv_rate=0xaa)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x04)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x06)  # 3: Ctrl Cmd
        exp.append(0x00)  # 4: Advertising Rate
        exp.append(0xaa)  # 5: Advertising Rate
        self.assertSequenceEqual(msg, exp)

    def test_ControlV110_SetAdvRefresh(self):
        """ Verifies v1.1.0 Advertising Refresh Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_1_0()

        msg = spec.build_ctrl_message('SET_ADV_REFRESH', adv_refresh=0x2398)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x04)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x07)  # 3: Ctrl Cmd
        exp.append(0x23)  # 4: Advertising Refresh
        exp.append(0x98)  # 4: Advertising Refresh
        self.assertSequenceEqual(msg, exp)

    def test_ControlV110_SetTimeSyncRate(self):
        """ Verifies v1.1.0 Set Time Sync Rate Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_1_0()

        msg = spec.build_ctrl_message('SET_TIME_SYNC_RATE',
                                      sync_time_rate=0x64a8b2ee)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x06)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x08)  # 3: Ctrl Cmd
        exp.append(0x64)  # 4: Sync Time Rate
        exp.append(0xa8)  # 5: Sync Time Rate
        exp.append(0xb2)  # 6: Sync Time Rate
        exp.append(0xee)  # 7: Sync Time Rate
        self.assertSequenceEqual(msg, exp)

    def test_ControlV110_SetConnTimeout(self):
        """ Verifies v1.1.0 Set Connection Timeout Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_1_0()

        msg = spec.build_ctrl_message('SET_CONN_TIMEOUT',
                                      conn_timeout=0x1b92c23d)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x06)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x09)  # 3: Ctrl Cmd
        exp.append(0x1b)  # 4: Connection Timeout
        exp.append(0x92)  # 5: Connection Timeout
        exp.append(0xc2)  # 6: Connection Timeout
        exp.append(0x3d)  # 7: Connection Timeout
        self.assertSequenceEqual(msg, exp)

    def test_ControlV110_SetStatusRate(self):
        """ Verifies v1.1.0 Set Status Rate Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_1_0()

        msg = spec.build_ctrl_message('SET_STATUS_RATE',
                                      status_rate=0x5b2acc32)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x06)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x0a)  # 3: Ctrl Cmd
        exp.append(0x5b)  # 4: Status Rate
        exp.append(0x2a)  # 5: Status Rate
        exp.append(0xcc)  # 6: Status Rate
        exp.append(0x32)  # 7: Status Rate
        self.assertSequenceEqual(msg, exp)

    def test_ControlV110_SetMailboxRate(self):
        """ Verifies v1.1.0 Set Mailbox Rate Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_1_0()

        msg = spec.build_ctrl_message('SET_MAILBOX_RATE',
                                      mailbox_int=0x79b18dc2)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x06)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x0B)  # 3: Ctrl Cmd
        exp.append(0x79)  # 4: Mailbox Rate
        exp.append(0xb1)  # 5: Mailbox Rate
        exp.append(0x8d)  # 6: Mailbox Rate
        exp.append(0xc2)  # 7: Mailbox Rate
        self.assertSequenceEqual(msg, exp)

    def test_ControlV110_SetQueueRate(self):
        """ Verifies v1.1.0 Set Queue Rate Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_1_0()

        msg = spec.build_ctrl_message('SET_QUEUE_SEND_RATE',
                                      send_rate=0x11bb2233)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x06)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x0C)  # 3: Ctrl Cmd
        exp.append(0x11)  # 4: Send Rate
        exp.append(0xbb)  # 5: Send Rate
        exp.append(0x22)  # 6: Send Rate
        exp.append(0x33)  # 7: Send Rate
        self.assertSequenceEqual(msg, exp)

    def test_ControlV110_SetQueueThresh(self):
        """ Verifies v1.1.0 Set Queue Thresh Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_1_0()

        msg = spec.build_ctrl_message('SET_QUEUE_THRESH', send_threshold=0x23)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x0D)  # 3: Ctrl Cmd
        exp.append(0x23)  # 4: Send Threshold
        self.assertSequenceEqual(msg, exp)

    def test_ControlV110_SetEnableBLE(self):
        """ Verifies v1.1.0 Set Enable BLE Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_1_0()

        msg = spec.build_ctrl_message('SET_ENABLE_BLE', enable=True)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x01)  # 2: Ctrl Cmd
        exp.append(0x00)  # 3: Ctrl Cmd
        exp.append(0x01)  # 4: Enable BLe
        self.assertSequenceEqual(msg, exp)

    def test_ControlV110_GetStatus(self):
        """ Verifies v1.1.0 Get Status Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_1_0()

        msg = spec.build_ctrl_message('GET_STATUS')
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 1: Msg Len
        exp.append(0x01)  # 2: Ctrl Cmd
        exp.append(0x06)  # 3: Ctrl Cmd
        self.assertSequenceEqual(msg, exp)

    def test_ControlV110_SetEnableLocation(self):
        """ Verifies v1.1.0 Set Enable Location Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_1_0()

        msg = spec.build_ctrl_message('SET_ENABLE_LOCATION', enable=True)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x01)  # 2: Ctrl Cmd
        exp.append(0x07)  # 3: Ctrl Cmd
        exp.append(0x01)  # 4: Enable
        self.assertSequenceEqual(msg, exp)

    def test_ControlV110_TriggerAssert(self):
        """ Verifies v1.1.0 Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_1_0()

        msg = spec.build_ctrl_message('TRIGGER_ASSERT')
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 1: Msg Len
        exp.append(0x05)  # 2: Ctrl Cmd
        exp.append(0x00)  # 3: Ctrl Cmd
        self.assertSequenceEqual(msg, exp)

    def test_ControlV110_SetSyncDC(self):
        """ Verifies v1.1.0 Set Sync DC Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_1_0()

        msg = spec.build_ctrl_message('SET_SYNC_DC', sync=0x99)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x12)  # 3: Ctrl Cmd
        exp.append(0x99)  # 4: DC Sync
        self.assertSequenceEqual(msg, exp)

    def test_ControlV110_SetSchedule(self):
        """ Verifies v1.1.0 Set Schedule Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_1_0()

        msg = spec.build_ctrl_message('SET_SCHEDULE',
                                      sched=b'\x00\x00\x00\x00\x00\x00\x00\x00'
                                            b'\x00\x00\x00\x00\x00\x00\x00\x00'
                                            b'\x00\x00\x00\x00\x00')
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x17)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x20)  # 3: Ctrl Cmd
        for x in range(21):
            exp.append(0x00)
        self.assertSequenceEqual(msg, exp)

    def test_ControlV119_SetAckMode(self):
        """ Verifies v1.1.0 Set Ack Mode Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_1_0()

        msg = spec.build_ctrl_message('SET_ACK_MODE', mode=0x00)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x01)  # 2: Ctrl Cmd
        exp.append(0x08)  # 3: Ctrl Cmd
        exp.append(0x00)  # 4: Mode
        self.assertSequenceEqual(msg, exp)

    def test_ControlV110_SetTXPower(self):
        """ Verifies v1.1.0 Set TX Power Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_1_0()

        msg = spec.build_ctrl_message('SET_TX_POWER', tx_pwr=0x55)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x01)  # 2: Ctrl Cmd
        exp.append(0x09)  # 3: Ctrl Cmd
        exp.append(0x55)  # 4: TX Power
        self.assertSequenceEqual(msg, exp)

    def test_ControlV110_ConfigBLEFrontEnd(self):
        """ Verifies v1.1.0 Config BLE Frontend Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_1_0()
        with self.assertRaises(ControlMessageNotSupported):
            spec.build_ctrl_message('CONFIG_BLE_FRONT_END', config=0x27)

    def test_ControlV110_SampleBatt(self):
        """ Verifies v1.1.0 Sample Battery Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_1_0()
        with self.assertRaises(ControlMessageNotSupported):
            spec.build_ctrl_message('SAMPLE_BATT')

    def test_ControlV110_SetDST(self):
        """ Verifies v1.1.0 Set DST Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_1_0()
        with self.assertRaises(ControlMessageNotSupported):
            spec.build_ctrl_message('SET_DST', enable=True)

    def test_ControlV110_SetDutyCycle(self):
        """ Verifies v1.1.0 Set Duty Cycle Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_1_0()
        with self.assertRaises(ControlMessageNotSupported):
            spec.build_ctrl_message('SET_DUTY_CYCLE', window=0x55)

    def test_ControlV110_SetGWRssi(self):
        """ Verifies v1.1.0 Set GW RSSI Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_1_0()
        with self.assertRaises(ControlMessageNotSupported):
            spec.build_ctrl_message('SET_SYM_GW_RSSI', rssi=0x95)

    def test_ControlV110_SetScanMode(self):
        """ Verifies v1.1.0 Set Scan Mode Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_1_0()
        with self.assertRaises(ControlMessageNotSupported):
            spec.build_ctrl_message('SET_SYM_SCAN_MODE', mode=0x00)

    def test_ControlV110_SetScanAttempts(self):
        """ Verifies v1.1.0 Set Scan Attempts Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_1_0()
        with self.assertRaises(ControlMessageNotSupported):
            spec.build_ctrl_message('SET_SYM_SCAN_ATTEMPTS', attempts=0x55)

    def test_ControlV110_SetScanHopInterval(self):
        """ Verifies v1.1.0 Set Scan Hop Interval Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_1_0()
        with self.assertRaises(ControlMessageNotSupported):
            spec.build_ctrl_message('SET_SYM_HOP_INT', interval=0x11223344)

    def test_ControlV110_SetMaxGWError(self):
        """ Verifies v1.1.0 Set Duty Cycle Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_1_0()
        with self.assertRaises(ControlMessageNotSupported):
            spec.build_ctrl_message('SET_MAX_GW_ERROR', max_err=0x90)

    def test_ControlV110_SetInfoScanInterval(self):
        """ Verifies v1.1.0 Set Info Scan Interval Control Message. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_1_0()

        with self.assertRaises(ControlMessageNotSupported):
            spec.build_ctrl_message('SET_SYM_INFO_SCAN_INT',
                                    interval=0xaabb4433)

    def test_SetConfigModeV110(self):
        """ Verifies v1.1.0 Config Mode Construction. """
        spec = af_devs.access_point.AccessPointMessageSpecV1_1_0()

        msg = spec.build_message("SetConfigMode",
                                 timeout=2348,
                                 net_tok=0x3a2d1d4c,
                                 app_tok=b'\xa8\xa2\x1c\xa1\x3b\xc8\x32\xd1'
                                         b'\xaa\x39',
                                 key=b'\x11\x1a\x9c\xad\xbd\x9b\x0e\x1a\xc7'
                                         b'\xc4\xa8\xb2\xe2\xd9\xe4\xc5')
        exp = bytearray()
        exp.append(0xb0)  # 00: Msg Type
        exp.append(0x22)  # 01: Msg Len
        exp.append(0x00)  # 02: Timeout
        exp.append(0x00)  # 03: Timeout
        exp.append(0x09)  # 04: Timeout
        exp.append(0x2c)  # 05: Timeout
        exp.append(0x3a)  # 06: Network Token
        exp.append(0x2d)  # 07: Network Token
        exp.append(0x1d)  # 08: Network Token
        exp.append(0x4c)  # 09: Network Token
        exp.append(0xa8)  # 10: Application Token
        exp.append(0xa2)  # 11: Application Token
        exp.append(0x1c)  # 12: Application Token
        exp.append(0xa1)  # 13: Application Token
        exp.append(0x3b)  # 14: Application Token
        exp.append(0xc8)  # 15: Application Token
        exp.append(0x32)  # 16: Application Token
        exp.append(0xd1)  # 17: Application Token
        exp.append(0xaa)  # 18: Application Token
        exp.append(0x39)  # 19: Application Token
        exp.append(0x11)  # 20: Key
        exp.append(0x1a)  # 21: Key
        exp.append(0x9c)  # 22: Key
        exp.append(0xad)  # 23: Key
        exp.append(0xbd)  # 24: Key
        exp.append(0x9b)  # 25: Key
        exp.append(0x0e)  # 26: Key
        exp.append(0x1a)  # 27: Key
        exp.append(0xc7)  # 28: Key
        exp.append(0xc4)  # 29: Key
        exp.append(0xa8)  # 30: Key
        exp.append(0xb2)  # 31: Key
        exp.append(0xe2)  # 32: Key
        exp.append(0xd9)  # 33: Key
        exp.append(0xe4)  # 34: Key
        exp.append(0xc5)  # 35: Key
        self.assertSequenceEqual(msg, exp)


if __name__ == '__main__':

    coloredlogs.install(level=LOG_LEVEL)

    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    # Validate library before Authentication.
    suite.addTests(loader.loadTestsFromTestCase(AccessPointTests))
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)
    suite = unittest.TestSuite()
