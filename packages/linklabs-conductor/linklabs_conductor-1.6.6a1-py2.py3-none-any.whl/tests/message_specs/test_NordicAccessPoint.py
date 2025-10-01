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


class NordicAccessPointTests(unittest.TestCase):

    def __init__(self, test_name):
        super().__init__(test_name)

    def test_UnicastV200(self):
        """ Verifies v2.0.0 Unicast Construction. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_0()

        # Mac Address is required.
        with self.assertRaises(MissingDownlinkArgument):
            spec.build_message('Unicast')

        # Mess Spec Version is not required.
        msg = spec.build_message('Unicast',
                                 endnode_addr=b'\xaa\xbb\xcc\xdd\xee\xff',
                                 time_to_live_s=30,
                                 uuid=0x1234,
                                 data=bytearray(b'\x12\x12\x23'))
        exp = bytearray()
        exp.append(0x01)  # 00: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x00)  # 03: Msg Spec Tag
        exp.append(0x0f)  # 04: Msg Len
        exp.append(0xaa)  # 05: Endnode Address
        exp.append(0xbb)  # 06: Endnode Address
        exp.append(0xcc)  # 07: Endnode Address
        exp.append(0xdd)  # 08: Endnode Address
        exp.append(0xee)  # 09: Endnode Address
        exp.append(0xff)  # 10: Endnode Address
        exp.append(0x00)  # 11: Time to Live
        exp.append(0x1e)  # 12: Time to Live
        exp.append(0x00)  # 13: UUID
        exp.append(0x00)  # 14: UUID
        exp.append(0x12)  # 15: UUID
        exp.append(0x34)  # 16: UUID
        exp.append(0x12)  # 17: Data
        exp.append(0x12)  # 18: Data
        exp.append(0x23)  # 19: Data
        self.assertSequenceEqual(msg, exp)

        # Normal Message
        msg = spec.build_message('Unicast',
                                 msg_spec_vers_major=2,
                                 msg_spec_vers_minor=0,
                                 msg_spec_vers_tag=0,
                                 endnode_addr=b'\xaa\xbb\xcc\xdd\xee\xff',
                                 time_to_live_s=30,
                                 uuid=0x1234,
                                 data=bytearray(b'\x12\x12\x23'))
        exp = bytearray()
        exp.append(0x01)  # 00: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 01: Msg Spec Minor
        exp.append(0x00)  # 01: Msg Spec Tag
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

    def test_MulticastV200(self):
        """ Verifies v2.0.0 Multicast Construction. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_0()

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
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x00)  # 03: Msg Spec Tag
        exp.append(0x13)  # 04: Msg Len
        exp.append(0xaa)  # 05: Application Token
        exp.append(0xbb)  # 06: Application Token
        exp.append(0xcc)  # 07: Application Token
        exp.append(0xdd)  # 08: Application Token
        exp.append(0xee)  # 09: Application Token
        exp.append(0xff)  # 10: Application Token
        exp.append(0xaa)  # 11: Application Token
        exp.append(0xbb)  # 12: Application Token
        exp.append(0xcc)  # 13: Application Token
        exp.append(0xdd)  # 14: Application Token
        exp.append(0x00)  # 15: Time to Live
        exp.append(0x1e)  # 16: Time to Live
        exp.append(0x00)  # 17: UUID
        exp.append(0x00)  # 18: UUID
        exp.append(0x12)  # 19: UUID
        exp.append(0x34)  # 20: UUID
        exp.append(0x12)  # 21: Data
        exp.append(0x12)  # 22: Data
        exp.append(0x23)  # 23: Data
        self.assertSequenceEqual(msg, exp)

        # Message with Unused Keys
        msg = spec.build_message('Multicast',
                                 msg_spec_vers_major=2,
                                 msg_spec_vers_minor=0,
                                 msg_spec_vers_tag=0,
                                 app_tok=b'\xaa\xbb\xcc\xdd\xee\xff\xaa\xbb'
                                         b'\xcc\xdd',
                                 time_to_live_s=30,
                                 uuid=0x1234,
                                 data=bytearray(b'\x12\x12\x23'))
        exp = bytearray()
        exp.append(0x02)  # 00: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x00)  # 03: Msg Spec Tag
        exp.append(0x13)  # 04: Msg Len
        exp.append(0xaa)  # 05: Application Token
        exp.append(0xbb)  # 06: Application Token
        exp.append(0xcc)  # 07: Application Token
        exp.append(0xdd)  # 08: Application Token
        exp.append(0xee)  # 09: Application Token
        exp.append(0xff)  # 10: Application Token
        exp.append(0xaa)  # 11: Application Token
        exp.append(0xbb)  # 12: Application Token
        exp.append(0xcc)  # 13: Application Token
        exp.append(0xdd)  # 14: Application Token
        exp.append(0x00)  # 15: Time to Live
        exp.append(0x1e)  # 16: Time to Live
        exp.append(0x00)  # 17: UUID
        exp.append(0x00)  # 18: UUID
        exp.append(0x12)  # 19: UUID
        exp.append(0x34)  # 20: UUID
        exp.append(0x12)  # 21: Data
        exp.append(0x12)  # 22: Data
        exp.append(0x23)  # 23: Data
        self.assertSequenceEqual(msg, exp)

    def test_ControlV200_SetAPType(self):
        """ Verifies v2.0.0 Set AP Type Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_0()

        msg = spec.build_ctrl_message('SET_AP_TYPE', ap_type=0x01)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x00)  # 03: Msg Spec Tag
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x02)  # 3: Ctrl Cmd
        exp.append(0x01)  # 4: AP Type
        self.assertSequenceEqual(msg, exp)

    def test_ControlV200_SetLocGroup(self):
        """ Verifies v2.0.0 Set Location Group Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_0()

        msg = spec.build_ctrl_message('SET_LOCATION_GROUP', loc_group=0x14)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x00)  # 03: Msg Spec Tag
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x03)  # 3: Ctrl Cmd
        exp.append(0x14)  # 4: Loc Group
        self.assertSequenceEqual(msg, exp)

    def test_ControlV200_SetLocWeight(self):
        """ Verifies v2.0.0 Set Location Weight Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_0()

        msg = spec.build_ctrl_message('SET_LOCATION_WEIGHT', loc_weight=0x79)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x00)  # 03: Msg Spec Tag
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x04)  # 3: Ctrl Cmd
        exp.append(0x79)  # 4: Loc Weight
        self.assertSequenceEqual(msg, exp)

    def test_ControlV200_SetRssiAdjust(self):
        """ Verifies v2.0.0 Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_0()

        msg = spec.build_ctrl_message('SET_RSSI_ADJ', rssi_adj=0x54)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x00)  # 03: Msg Spec Tag
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x05)  # 3: Ctrl Cmd
        exp.append(0x54)  # 4: Rssi Adj
        self.assertSequenceEqual(msg, exp)

    def test_ControlV200_SetAdvRate(self):
        """ Verifies v2.0.0 Set Advertising Rate Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_0()

        msg = spec.build_ctrl_message('SET_ADV_RATE', adv_rate=0xaa)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x00)  # 03: Msg Spec Tag
        exp.append(0x04)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x06)  # 3: Ctrl Cmd
        exp.append(0x00)  # 4: Advertising Rate
        exp.append(0xaa)  # 5: Advertising Rate
        self.assertSequenceEqual(msg, exp)

    def test_ControlV200_SetAdvRefresh(self):
        """ Verifies v2.0.0 Advertising Refresh Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_0()

        msg = spec.build_ctrl_message('SET_ADV_REFRESH', adv_refresh=0x2398)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x00)  # 03: Msg Spec Tag
        exp.append(0x04)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x07)  # 3: Ctrl Cmd
        exp.append(0x23)  # 4: Advertising Refresh
        exp.append(0x98)  # 4: Advertising Refresh
        self.assertSequenceEqual(msg, exp)

    def test_ControlV200_SetTimeSyncRate(self):
        """ Verifies v2.0.0 Set Time Sync Rate Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_0()

        msg = spec.build_ctrl_message('SET_TIME_SYNC_RATE',
                                      sync_time_rate=0x64a8b2ee)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x00)  # 03: Msg Spec Tag
        exp.append(0x06)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x08)  # 3: Ctrl Cmd
        exp.append(0x64)  # 4: Sync Time Rate
        exp.append(0xa8)  # 5: Sync Time Rate
        exp.append(0xb2)  # 6: Sync Time Rate
        exp.append(0xee)  # 7: Sync Time Rate
        self.assertSequenceEqual(msg, exp)

    def test_ControlV200_SetConnTimeout(self):
        """ Verifies v2.0.0 Set Connection Timeout Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_0()

        msg = spec.build_ctrl_message('SET_CONN_TIMEOUT',
                                      conn_timeout=0x1b92c23d)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x00)  # 03: Msg Spec Tag
        exp.append(0x06)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x09)  # 3: Ctrl Cmd
        exp.append(0x1b)  # 4: Connection Timeout
        exp.append(0x92)  # 5: Connection Timeout
        exp.append(0xc2)  # 6: Connection Timeout
        exp.append(0x3d)  # 7: Connection Timeout
        self.assertSequenceEqual(msg, exp)

    def test_ControlV200_SetStatusRate(self):
        """ Verifies v2.0.0 Set Status Rate Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_0()

        msg = spec.build_ctrl_message('SET_STATUS_RATE',
                                      status_rate=0x5b2acc32)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x00)  # 03: Msg Spec Tag
        exp.append(0x06)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x0a)  # 3: Ctrl Cmd
        exp.append(0x5b)  # 4: Status Rate
        exp.append(0x2a)  # 5: Status Rate
        exp.append(0xcc)  # 6: Status Rate
        exp.append(0x32)  # 7: Status Rate
        self.assertSequenceEqual(msg, exp)

    def test_ControlV200_SetMailboxRate(self):
        """ Verifies v2.0.0 Set Mailbox Rate Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_0()

        msg = spec.build_ctrl_message('SET_MAILBOX_RATE',
                                      mailbox_int=0x79b18dc2)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x00)  # 03: Msg Spec Tag
        exp.append(0x06)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x0B)  # 3: Ctrl Cmd
        exp.append(0x79)  # 4: Mailbox Rate
        exp.append(0xb1)  # 5: Mailbox Rate
        exp.append(0x8d)  # 6: Mailbox Rate
        exp.append(0xc2)  # 7: Mailbox Rate
        self.assertSequenceEqual(msg, exp)

    def test_ControlV200_SetQueueRate(self):
        """ Verifies v2.0.0 Set Queue Rate Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_0()

        msg = spec.build_ctrl_message('SET_QUEUE_SEND_RATE',
                                      send_rate=0x11bb2233)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x00)  # 03: Msg Spec Tag
        exp.append(0x06)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x0C)  # 3: Ctrl Cmd
        exp.append(0x11)  # 4: Send Rate
        exp.append(0xbb)  # 5: Send Rate
        exp.append(0x22)  # 6: Send Rate
        exp.append(0x33)  # 7: Send Rate
        self.assertSequenceEqual(msg, exp)

    def test_ControlV200_SetQueueThresh(self):
        """ Verifies v2.0.0 Set Queue Thresh Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_0()

        msg = spec.build_ctrl_message('SET_QUEUE_THRESH', send_threshold=0x23)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x00)  # 03: Msg Spec Tag
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x0D)  # 3: Ctrl Cmd
        exp.append(0x23)  # 4: Send Threshold
        self.assertSequenceEqual(msg, exp)

    def test_ControlV200_SetEnableBLE(self):
        """ Verifies v2.0.0 Set Enable BLE Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_0()

        msg = spec.build_ctrl_message('SET_ENABLE_BLE', enable=True)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x00)  # 03: Msg Spec Tag
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x01)  # 2: Ctrl Cmd
        exp.append(0x00)  # 3: Ctrl Cmd
        exp.append(0x01)  # 4: Enable BLe
        self.assertSequenceEqual(msg, exp)

    def test_ControlV200_GetStatus(self):
        """ Verifies v2.0.0 Get Status Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_0()

        msg = spec.build_ctrl_message('GET_STATUS')
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x00)  # 03: Msg Spec Tag
        exp.append(0x02)  # 1: Msg Len
        exp.append(0x01)  # 2: Ctrl Cmd
        exp.append(0x06)  # 3: Ctrl Cmd
        self.assertSequenceEqual(msg, exp)

    def test_ControlV200_SetEnableLocation(self):
        """ Verifies v2.0.0 Set Enable Location Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_0()

        msg = spec.build_ctrl_message('SET_ENABLE_LOCATION', enable=True)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x00)  # 03: Msg Spec Tag
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x01)  # 2: Ctrl Cmd
        exp.append(0x07)  # 3: Ctrl Cmd
        exp.append(0x01)  # 4: Enable
        self.assertSequenceEqual(msg, exp)

    def test_ControlV200_TriggerAssert(self):
        """ Verifies v2.0.0 Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_0()

        msg = spec.build_ctrl_message('TRIGGER_ASSERT')
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x00)  # 03: Msg Spec Tag
        exp.append(0x02)  # 1: Msg Len
        exp.append(0x05)  # 2: Ctrl Cmd
        exp.append(0x00)  # 3: Ctrl Cmd
        self.assertSequenceEqual(msg, exp)

    def test_ControlV200_SetSyncDC(self):
        """ Verifies v2.0.0 Set Sync DC Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_0()

        msg = spec.build_ctrl_message('SET_SYNC_DC', sync=0x99)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x00)  # 03: Msg Spec Tag
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x12)  # 3: Ctrl Cmd
        exp.append(0x99)  # 4: DC Sync
        self.assertSequenceEqual(msg, exp)

    def test_ControlV200_SetSchedule(self):
        """ Verifies v2.0.0 Set Schedule Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_0()

        msg = spec.build_ctrl_message('SET_SCHEDULE',
                                      sched=b'\x00\x00\x00\x00\x00\x00\x00\x00'
                                            b'\x00\x00\x00\x00\x00\x00\x00\x00'
                                            b'\x00\x00\x00\x00\x00')
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x00)  # 03: Msg Spec Tag
        exp.append(0x17)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x20)  # 3: Ctrl Cmd
        for x in range(21):
            exp.append(0x00)
        self.assertSequenceEqual(msg, exp)

    def test_ControlV200_SetAckMode(self):
        """ Verifies v2.0.0 Set Ack Mode Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_0()

        msg = spec.build_ctrl_message('SET_ACK_MODE', mode=0x00)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x00)  # 03: Msg Spec Tag
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x01)  # 2: Ctrl Cmd
        exp.append(0x08)  # 3: Ctrl Cmd
        exp.append(0x00)  # 4: Mode
        self.assertSequenceEqual(msg, exp)

    def test_ControlV200_SetTXPower(self):
        """ Verifies v2.0.0 Set TX Power Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_0()

        msg = spec.build_ctrl_message('SET_TX_POWER', tx_pwr=0x55)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x00)  # 03: Msg Spec Tag
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x01)  # 2: Ctrl Cmd
        exp.append(0x09)  # 3: Ctrl Cmd
        exp.append(0x55)  # 4: TX Power
        self.assertSequenceEqual(msg, exp)

    def test_ControlV200_ConfigBLEFrontEnd(self):
        """ Verifies v2.0.0 Config BLE Frontend Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_0()

        msg = spec.build_ctrl_message('CONFIG_BLE_FRONT_END', config=0x27)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x00)  # 03: Msg Spec Tag
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x01)  # 2: Ctrl Cmd
        exp.append(0x0A)  # 3: Ctrl Cmd
        exp.append(0x27)  # 4: TX Power
        self.assertSequenceEqual(msg, exp)

    def test_ControlV200_SampleBatt(self):
        """ Verifies v2.0.0 Sample Battery Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_0()

        msg = spec.build_ctrl_message('SAMPLE_BATT')
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x00)  # 03: Msg Spec Tag
        exp.append(0x02)  # 1: Msg Len
        exp.append(0x01)  # 2: Ctrl Cmd
        exp.append(0x03)  # 3: Ctrl Cmd
        self.assertSequenceEqual(msg, exp)

    def test_ControlV200_SetDST(self):
        """ Verifies v2.0.0 Set DST Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_0()

        msg = spec.build_ctrl_message('SET_DST', enable=True)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x00)  # 03: Msg Spec Tag
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x21)  # 3: Ctrl Cmd
        exp.append(0x01)  # 4: Enable
        self.assertSequenceEqual(msg, exp)

    def test_ControlV200_SetDutyCycle(self):
        """ Verifies v2.0.0 Set Duty Cycle Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_0()

        msg = spec.build_ctrl_message('SET_DUTY_CYCLE', window=0x55)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x00)  # 03: Msg Spec Tag
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x22)  # 3: Ctrl Cmd
        exp.append(0x55)  # 4: Window
        self.assertSequenceEqual(msg, exp)

    def test_ControlV200_SetGWRssi(self):
        """ Verifies v2.0.0 Set GW RSSI Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_0()
        with self.assertRaises(ControlMessageNotSupported):
            spec.build_ctrl_message('SET_SYM_GW_RSSI', rssi=0x95)

    def test_ControlV200_SetScanMode(self):
        """ Verifies v2.0.0 Set Scan Mode Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_0()
        with self.assertRaises(ControlMessageNotSupported):
            spec.build_ctrl_message('SET_SYM_SCAN_MODE', mode=0x00)

    def test_ControlV200_SetScanAttempts(self):
        """ Verifies v2.0.0 Set Scan Attempts Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_0()
        with self.assertRaises(ControlMessageNotSupported):
            spec.build_ctrl_message('SET_SYM_SCAN_ATTEMPTS', attempts=0x55)

    def test_ControlV200_SetScanHopInterval(self):
        """ Verifies v2.0.0 Set Scan Hop Interval Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_0()
        with self.assertRaises(ControlMessageNotSupported):
            spec.build_ctrl_message('SET_SYM_HOP_INT', interval=0x11223344)

    def test_ControlV200_SetMaxGWError(self):
        """ Verifies v2.0.0 Set Duty Cycle Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_0()
        with self.assertRaises(ControlMessageNotSupported):
            spec.build_ctrl_message('SET_MAX_GW_ERROR', max_err=0x90)

    def test_ControlV200_SetInfoScanInterval(self):
        """ Verifies v2.0.0 Set Info Scan Interval Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_0()

        with self.assertRaises(ControlMessageNotSupported):
            spec.build_ctrl_message('SET_SYM_INFO_SCAN_INT',
                                    interval=0xaabb4433)

    def test_SetConfigModeV200(self):
        """ Verifies v2.0.0 Config Mode Construction. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_0()

        msg = spec.build_message("SetConfigMode",
                                 timeout=2348,
                                 net_tok=0x3a2d1d4c,
                                 app_tok=b'\xa8\xa2\x1c\xa1\x3b\xc8\x32\xd1'
                                         b'\xaa\x39',
                                 key=b'\x11\x1a\x9c\xad\xbd\x9b\x0e\x1a\xc7'
                                     b'\xc4\xa8\xb2\xe2\xd9\xe4\xc5')
        exp = bytearray()
        exp.append(0xb0)  # 00: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x00)  # 03: Msg Spec Tag
        exp.append(0x22)  # 04: Msg Len
        exp.append(0x00)  # 05: Timeout
        exp.append(0x00)  # 06: Timeout
        exp.append(0x09)  # 07: Timeout
        exp.append(0x2c)  # 08: Timeout
        exp.append(0x3a)  # 09: Network Token
        exp.append(0x2d)  # 10: Network Token
        exp.append(0x1d)  # 11: Network Token
        exp.append(0x4c)  # 12: Network Token
        exp.append(0xa8)  # 13: Application Token
        exp.append(0xa2)  # 14: Application Token
        exp.append(0x1c)  # 15: Application Token
        exp.append(0xa1)  # 16: Application Token
        exp.append(0x3b)  # 17: Application Token
        exp.append(0xc8)  # 18: Application Token
        exp.append(0x32)  # 19: Application Token
        exp.append(0xd1)  # 20: Application Token
        exp.append(0xaa)  # 21: Application Token
        exp.append(0x39)  # 22: Application Token
        exp.append(0x11)  # 23: Key
        exp.append(0x1a)  # 24: Key
        exp.append(0x9c)  # 25: Key
        exp.append(0xad)  # 26: Key
        exp.append(0xbd)  # 27: Key
        exp.append(0x9b)  # 28: Key
        exp.append(0x0e)  # 29: Key
        exp.append(0x1a)  # 30: Key
        exp.append(0xc7)  # 31: Key
        exp.append(0xc4)  # 32: Key
        exp.append(0xa8)  # 33: Key
        exp.append(0xb2)  # 34: Key
        exp.append(0xe2)  # 35: Key
        exp.append(0xd9)  # 36: Key
        exp.append(0xe4)  # 37: Key
        exp.append(0xc5)  # 38: Key
        self.assertSequenceEqual(msg, exp)

    def test_UnicastV201(self):
        """ Verifies v2.0.1 Unicast Construction. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_1()

        # Mac Address is required.
        with self.assertRaises(MissingDownlinkArgument):
            spec.build_message('Unicast')

        # Mess Spec Version is not required.
        msg = spec.build_message('Unicast',
                                 endnode_addr=b'\xaa\xbb\xcc\xdd\xee\xff',
                                 time_to_live_s=30,
                                 uuid=0x1234,
                                 data=bytearray(b'\x12\x12\x23'))
        exp = bytearray()
        exp.append(0x01)  # 00: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x01)  # 03: Msg Spec Tag
        exp.append(0x0f)  # 04: Msg Len
        exp.append(0xaa)  # 05: Endnode Address
        exp.append(0xbb)  # 06: Endnode Address
        exp.append(0xcc)  # 07: Endnode Address
        exp.append(0xdd)  # 08: Endnode Address
        exp.append(0xee)  # 09: Endnode Address
        exp.append(0xff)  # 10: Endnode Address
        exp.append(0x00)  # 11: Time to Live
        exp.append(0x1e)  # 12: Time to Live
        exp.append(0x00)  # 13: UUID
        exp.append(0x00)  # 14: UUID
        exp.append(0x12)  # 15: UUID
        exp.append(0x34)  # 16: UUID
        exp.append(0x12)  # 17: Data
        exp.append(0x12)  # 18: Data
        exp.append(0x23)  # 19: Data
        self.assertSequenceEqual(msg, exp)

        # Normal Message
        msg = spec.build_message('Unicast',
                                 msg_spec_vers_major=2,
                                 msg_spec_vers_minor=0,
                                 msg_spec_vers_tag=1,
                                 endnode_addr=b'\xaa\xbb\xcc\xdd\xee\xff',
                                 time_to_live_s=30,
                                 uuid=0x1234,
                                 data=bytearray(b'\x12\x12\x23'))
        exp = bytearray()
        exp.append(0x01)  # 00: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 01: Msg Spec Minor
        exp.append(0x01)  # 01: Msg Spec Tag
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

    def test_MulticastV201(self):
        """ Verifies v2.0.1 Multicast Construction. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_1()

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
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x01)  # 03: Msg Spec Tag
        exp.append(0x13)  # 04: Msg Len
        exp.append(0xaa)  # 05: Application Token
        exp.append(0xbb)  # 06: Application Token
        exp.append(0xcc)  # 07: Application Token
        exp.append(0xdd)  # 08: Application Token
        exp.append(0xee)  # 09: Application Token
        exp.append(0xff)  # 10: Application Token
        exp.append(0xaa)  # 11: Application Token
        exp.append(0xbb)  # 12: Application Token
        exp.append(0xcc)  # 13: Application Token
        exp.append(0xdd)  # 14: Application Token
        exp.append(0x00)  # 15: Time to Live
        exp.append(0x1e)  # 16: Time to Live
        exp.append(0x00)  # 17: UUID
        exp.append(0x00)  # 18: UUID
        exp.append(0x12)  # 19: UUID
        exp.append(0x34)  # 20: UUID
        exp.append(0x12)  # 21: Data
        exp.append(0x12)  # 22: Data
        exp.append(0x23)  # 23: Data
        self.assertSequenceEqual(msg, exp)

        # Message with Unused Keys
        msg = spec.build_message('Multicast',
                                 msg_spec_vers_major=2,
                                 msg_spec_vers_minor=0,
                                 msg_spec_vers_tag=1,
                                 app_tok=b'\xaa\xbb\xcc\xdd\xee\xff\xaa\xbb'
                                         b'\xcc\xdd',
                                 time_to_live_s=30,
                                 uuid=0x1234,
                                 data=bytearray(b'\x12\x12\x23'))
        exp = bytearray()
        exp.append(0x02)  # 00: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x01)  # 03: Msg Spec Tag
        exp.append(0x13)  # 04: Msg Len
        exp.append(0xaa)  # 05: Application Token
        exp.append(0xbb)  # 06: Application Token
        exp.append(0xcc)  # 07: Application Token
        exp.append(0xdd)  # 08: Application Token
        exp.append(0xee)  # 09: Application Token
        exp.append(0xff)  # 10: Application Token
        exp.append(0xaa)  # 11: Application Token
        exp.append(0xbb)  # 12: Application Token
        exp.append(0xcc)  # 13: Application Token
        exp.append(0xdd)  # 14: Application Token
        exp.append(0x00)  # 15: Time to Live
        exp.append(0x1e)  # 16: Time to Live
        exp.append(0x00)  # 17: UUID
        exp.append(0x00)  # 18: UUID
        exp.append(0x12)  # 19: UUID
        exp.append(0x34)  # 20: UUID
        exp.append(0x12)  # 21: Data
        exp.append(0x12)  # 22: Data
        exp.append(0x23)  # 23: Data
        self.assertSequenceEqual(msg, exp)

    def test_ControlV201_SetAPType(self):
        """ Verifies v2.0.1 Set AP Type Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_1()

        msg = spec.build_ctrl_message('SET_AP_TYPE', ap_type=0x01)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x01)  # 03: Msg Spec Tag
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x02)  # 3: Ctrl Cmd
        exp.append(0x01)  # 4: AP Type
        self.assertSequenceEqual(msg, exp)

    def test_ControlV201_SetLocGroup(self):
        """ Verifies v2.0.1 Set Location Group Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_1()

        msg = spec.build_ctrl_message('SET_LOCATION_GROUP', loc_group=0x14)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x01)  # 03: Msg Spec Tag
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x03)  # 3: Ctrl Cmd
        exp.append(0x14)  # 4: Loc Group
        self.assertSequenceEqual(msg, exp)

    def test_ControlV201_SetLocWeight(self):
        """ Verifies v2.0.1 Set Location Weight Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_1()

        msg = spec.build_ctrl_message('SET_LOCATION_WEIGHT', loc_weight=0x79)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x01)  # 03: Msg Spec Tag
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x04)  # 3: Ctrl Cmd
        exp.append(0x79)  # 4: Loc Weight
        self.assertSequenceEqual(msg, exp)

    def test_ControlV201_SetRssiAdjust(self):
        """ Verifies v2.0.1 Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_1()

        msg = spec.build_ctrl_message('SET_RSSI_ADJ', rssi_adj=0x54)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x01)  # 03: Msg Spec Tag
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x05)  # 3: Ctrl Cmd
        exp.append(0x54)  # 4: Rssi Adj
        self.assertSequenceEqual(msg, exp)

    def test_ControlV201_SetAdvRate(self):
        """ Verifies v2.0.1 Set Advertising Rate Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_1()

        msg = spec.build_ctrl_message('SET_ADV_RATE', adv_rate=0xaa)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x01)  # 03: Msg Spec Tag
        exp.append(0x04)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x06)  # 3: Ctrl Cmd
        exp.append(0x00)  # 4: Advertising Rate
        exp.append(0xaa)  # 5: Advertising Rate
        self.assertSequenceEqual(msg, exp)

    def test_ControlV201_SetAdvRefresh(self):
        """ Verifies v2.0.1 Advertising Refresh Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_1()

        msg = spec.build_ctrl_message('SET_ADV_REFRESH', adv_refresh=0x2398)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x01)  # 03: Msg Spec Tag
        exp.append(0x04)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x07)  # 3: Ctrl Cmd
        exp.append(0x23)  # 4: Advertising Refresh
        exp.append(0x98)  # 4: Advertising Refresh
        self.assertSequenceEqual(msg, exp)

    def test_ControlV201_SetTimeSyncRate(self):
        """ Verifies v2.0.1 Set Time Sync Rate Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_1()

        msg = spec.build_ctrl_message('SET_TIME_SYNC_RATE',
                                      sync_time_rate=0x64a8b2ee)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x01)  # 03: Msg Spec Tag
        exp.append(0x06)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x08)  # 3: Ctrl Cmd
        exp.append(0x64)  # 4: Sync Time Rate
        exp.append(0xa8)  # 5: Sync Time Rate
        exp.append(0xb2)  # 6: Sync Time Rate
        exp.append(0xee)  # 7: Sync Time Rate
        self.assertSequenceEqual(msg, exp)

    def test_ControlV201_SetConnTimeout(self):
        """ Verifies v2.0.1 Set Connection Timeout Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_1()

        msg = spec.build_ctrl_message('SET_CONN_TIMEOUT',
                                      conn_timeout=0x1b92c23d)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x01)  # 03: Msg Spec Tag
        exp.append(0x06)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x09)  # 3: Ctrl Cmd
        exp.append(0x1b)  # 4: Connection Timeout
        exp.append(0x92)  # 5: Connection Timeout
        exp.append(0xc2)  # 6: Connection Timeout
        exp.append(0x3d)  # 7: Connection Timeout
        self.assertSequenceEqual(msg, exp)

    def test_ControlV201_SetStatusRate(self):
        """ Verifies v2.0.1 Set Status Rate Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_1()

        msg = spec.build_ctrl_message('SET_STATUS_RATE',
                                      status_rate=0x5b2acc32)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x01)  # 03: Msg Spec Tag
        exp.append(0x06)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x0a)  # 3: Ctrl Cmd
        exp.append(0x5b)  # 4: Status Rate
        exp.append(0x2a)  # 5: Status Rate
        exp.append(0xcc)  # 6: Status Rate
        exp.append(0x32)  # 7: Status Rate
        self.assertSequenceEqual(msg, exp)

    def test_ControlV201_SetMailboxRate(self):
        """ Verifies v2.0.1 Set Mailbox Rate Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_1()

        msg = spec.build_ctrl_message('SET_MAILBOX_RATE',
                                      mailbox_int=0x79b18dc2)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x01)  # 03: Msg Spec Tag
        exp.append(0x06)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x0B)  # 3: Ctrl Cmd
        exp.append(0x79)  # 4: Mailbox Rate
        exp.append(0xb1)  # 5: Mailbox Rate
        exp.append(0x8d)  # 6: Mailbox Rate
        exp.append(0xc2)  # 7: Mailbox Rate
        self.assertSequenceEqual(msg, exp)

    def test_ControlV201_SetQueueRate(self):
        """ Verifies v2.0.1 Set Queue Rate Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_1()

        msg = spec.build_ctrl_message('SET_QUEUE_SEND_RATE',
                                      send_rate=0x11bb2233)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x01)  # 03: Msg Spec Tag
        exp.append(0x06)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x0C)  # 3: Ctrl Cmd
        exp.append(0x11)  # 4: Send Rate
        exp.append(0xbb)  # 5: Send Rate
        exp.append(0x22)  # 6: Send Rate
        exp.append(0x33)  # 7: Send Rate
        self.assertSequenceEqual(msg, exp)

    def test_ControlV201_SetQueueThresh(self):
        """ Verifies v2.0.1 Set Queue Thresh Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_1()

        msg = spec.build_ctrl_message('SET_QUEUE_THRESH', send_threshold=0x23)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x01)  # 03: Msg Spec Tag
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x0D)  # 3: Ctrl Cmd
        exp.append(0x23)  # 4: Send Threshold
        self.assertSequenceEqual(msg, exp)

    def test_ControlV201_SetEnableBLE(self):
        """ Verifies v2.0.1 Set Enable BLE Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_1()

        msg = spec.build_ctrl_message('SET_ENABLE_BLE', enable=True)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x01)  # 03: Msg Spec Tag
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x01)  # 2: Ctrl Cmd
        exp.append(0x00)  # 3: Ctrl Cmd
        exp.append(0x01)  # 4: Enable BLe
        self.assertSequenceEqual(msg, exp)

    def test_ControlV201_GetStatus(self):
        """ Verifies v2.0.1 Get Status Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_1()

        msg = spec.build_ctrl_message('GET_STATUS')
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x01)  # 03: Msg Spec Tag
        exp.append(0x02)  # 1: Msg Len
        exp.append(0x01)  # 2: Ctrl Cmd
        exp.append(0x06)  # 3: Ctrl Cmd
        self.assertSequenceEqual(msg, exp)

    def test_ControlV201_SetEnableLocation(self):
        """ Verifies v2.0.1 Set Enable Location Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_1()

        msg = spec.build_ctrl_message('SET_ENABLE_LOCATION', enable=True)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x01)  # 03: Msg Spec Tag
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x01)  # 2: Ctrl Cmd
        exp.append(0x07)  # 3: Ctrl Cmd
        exp.append(0x01)  # 4: Enable
        self.assertSequenceEqual(msg, exp)

    def test_ControlV201_SetSyncDC(self):
        """ Verifies v2.0.1 Set Sync DC Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_1()

        msg = spec.build_ctrl_message('SET_SYNC_DC', sync=0x99)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x01)  # 03: Msg Spec Tag
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x12)  # 3: Ctrl Cmd
        exp.append(0x99)  # 4: DC Sync
        self.assertSequenceEqual(msg, exp)

    def test_ControlV201_SetSchedule(self):
        """ Verifies v2.0.1 Set Schedule Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_1()

        msg = spec.build_ctrl_message('SET_SCHEDULE',
                                      sched=b'\x00\x00\x00\x00\x00\x00\x00\x00'
                                            b'\x00\x00\x00\x00\x00\x00\x00\x00'
                                            b'\x00\x00\x00\x00\x00')
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x01)  # 03: Msg Spec Tag
        exp.append(0x17)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x20)  # 3: Ctrl Cmd
        for x in range(21):
            exp.append(0x00)
        self.assertSequenceEqual(msg, exp)

    def test_ControlV201_SetAckMode(self):
        """ Verifies v2.0.1 Set Ack Mode Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_1()

        msg = spec.build_ctrl_message('SET_ACK_MODE', mode=0x00)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x01)  # 03: Msg Spec Tag
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x01)  # 2: Ctrl Cmd
        exp.append(0x08)  # 3: Ctrl Cmd
        exp.append(0x00)  # 4: Mode
        self.assertSequenceEqual(msg, exp)

    def test_ControlV201_SetTXPower(self):
        """ Verifies v2.0.1 Set TX Power Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_1()

        msg = spec.build_ctrl_message('SET_TX_POWER', tx_pwr=0x55)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x01)  # 03: Msg Spec Tag
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x01)  # 2: Ctrl Cmd
        exp.append(0x09)  # 3: Ctrl Cmd
        exp.append(0x55)  # 4: TX Power
        self.assertSequenceEqual(msg, exp)

    def test_ControlV201_TriggerAssert(self):
        """ Verifies v2.0.1 Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_1()

        msg = spec.build_ctrl_message('TRIGGER_ASSERT')
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x01)  # 03: Msg Spec Tag
        exp.append(0x02)  # 1: Msg Len
        exp.append(0x05)  # 2: Ctrl Cmd
        exp.append(0x00)  # 3: Ctrl Cmd
        self.assertSequenceEqual(msg, exp)

    def test_ControlV201_ConfigBLEFrontEnd(self):
        """ Verifies v2.0.1 Config BLE Frontend Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_1()

        msg = spec.build_ctrl_message('CONFIG_BLE_FRONT_END', config=0x27)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x01)  # 03: Msg Spec Tag
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x01)  # 2: Ctrl Cmd
        exp.append(0x0A)  # 3: Ctrl Cmd
        exp.append(0x27)  # 4: TX Power
        self.assertSequenceEqual(msg, exp)

    def test_ControlV201_SampleBatt(self):
        """ Verifies v2.0.1 Sample Battery Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_1()

        msg = spec.build_ctrl_message('SAMPLE_BATT')
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x01)  # 03: Msg Spec Tag
        exp.append(0x02)  # 1: Msg Len
        exp.append(0x01)  # 2: Ctrl Cmd
        exp.append(0x03)  # 3: Ctrl Cmd
        self.assertSequenceEqual(msg, exp)

    def test_ControlV201_SetDST(self):
        """ Verifies v2.0.1 Set DST Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_1()

        msg = spec.build_ctrl_message('SET_DST', enable=True)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x01)  # 03: Msg Spec Tag
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x21)  # 3: Ctrl Cmd
        exp.append(0x01)  # 4: Enable
        self.assertSequenceEqual(msg, exp)

    def test_ControlV201_SetDutyCycle(self):
        """ Verifies v2.0.1 Set Duty Cycle Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_1()

        msg = spec.build_ctrl_message('SET_DUTY_CYCLE', window=0x55)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x01)  # 03: Msg Spec Tag
        exp.append(0x03)  # 1: Msg Len
        exp.append(0x00)  # 2: Ctrl Cmd
        exp.append(0x22)  # 3: Ctrl Cmd
        exp.append(0x55)  # 4: Window
        self.assertSequenceEqual(msg, exp)

    def test_ControlV202_SetGWRssi(self):
        """ Verifies v2.0.2 Set GW RSSI Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_2()

        msg = spec.build_ctrl_message('SET_SYM_GW_RSSI', rssi=0x95)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x02)  # 03: Msg Spec Tag
        exp.append(0x04)  # 4: Msg Len
        exp.append(0x00)  # 5: Ctrl Cmd
        exp.append(0xB0)  # 6: Ctrl Cmd
        exp.append(0x00)  # 7: RSSI
        exp.append(0x95)  # 8: RSSI
        self.assertSequenceEqual(msg, exp)

    def test_ControlV202_SetScanMode(self):
        """ Verifies v2.0.2 Set Scan Mode Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_2()

        msg = spec.build_ctrl_message('SET_SYM_SCAN_MODE', mode=0x00)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x02)  # 03: Msg Spec Tag
        exp.append(0x04)  # 4: Msg Len
        exp.append(0x00)  # 5: Ctrl Cmd
        exp.append(0xb1)  # 6: Ctrl Cmd
        exp.append(0x00)  # 7: Mode
        exp.append(0x00)  # 8: Mode
        self.assertSequenceEqual(msg, exp)

    def test_ControlV202_SetScanAttempts(self):
        """ Verifies v2.0.2 Set Scan Attempts Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_2()

        msg = spec.build_ctrl_message('SET_SYM_SCAN_ATTEMPTS', attempts=0x55)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x02)  # 03: Msg Spec Tag
        exp.append(0x03)  # 4: Msg Len
        exp.append(0x00)  # 5: Ctrl Cmd
        exp.append(0xb2)  # 6: Ctrl Cmd
        exp.append(0x55)  # 7: Attempts
        self.assertSequenceEqual(msg, exp)

    def test_ControlV202_SetScanHopInterval(self):
        """ Verifies v2.0.2 Set Duty Cycle Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_2()

        msg = spec.build_ctrl_message('SET_SYM_HOP_INT', interval=0x11223344)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x02)  # 03: Msg Spec Tag
        exp.append(0x06)  # 4: Msg Len
        exp.append(0x00)  # 5: Ctrl Cmd
        exp.append(0xb3)  # 6: Ctrl Cmd
        exp.append(0x11)  # 7: Interval
        exp.append(0x22)  # 7: Interval
        exp.append(0x33)  # 7: Interval
        exp.append(0x44)  # 7: Interval
        self.assertSequenceEqual(msg, exp)

    def test_ControlV202_SetMaxGWError(self):
        """ Verifies v2.0.2 Set Duty Cycle Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_2()

        msg = spec.build_ctrl_message('SET_MAX_GW_ERROR', max_err=0x90)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x02)  # 03: Msg Spec Tag
        exp.append(0x03)  # 4: Msg Len
        exp.append(0x00)  # 5: Ctrl Cmd
        exp.append(0xb4)  # 6: Ctrl Cmd
        exp.append(0x90)  # 7: Max Error
        self.assertSequenceEqual(msg, exp)

    def test_ControlV202_SetInfoScanInterval(self):
        """ Verifies v2.0.2 Set Info Scan Interval Control Message. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_2()

        msg = spec.build_ctrl_message('SET_SYM_INFO_SCAN_INT',
                                      interval=0xaabb4433)
        exp = bytearray()
        exp.append(0xA0)  # 0: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x02)  # 03: Msg Spec Tag
        exp.append(0x06)  # 4: Msg Len
        exp.append(0x00)  # 5: Ctrl Cmd
        exp.append(0xb5)  # 6: Ctrl Cmd
        exp.append(0xaa)  # 7: interval
        exp.append(0xbb)  # 7: interval
        exp.append(0x44)  # 7: interval
        exp.append(0x33)  # 7: interval
        self.assertSequenceEqual(msg, exp)

    def test_SetConfigModeV202(self):
        """ Verifies v2.0.2 Config Mode Construction. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_2()

        msg = spec.build_message("SetConfigMode",
                                 timeout=2348,
                                 net_tok=0x3a2d1d4c,
                                 app_tok=b'\xa8\xa2\x1c\xa1\x3b\xc8\x32\xd1'
                                         b'\xaa\x39',
                                 key=b'\x11\x1a\x9c\xad\xbd\x9b\x0e\x1a\xc7'
                                     b'\xc4\xa8\xb2\xe2\xd9\xe4\xc5')
        exp = bytearray()
        exp.append(0xb0)  # 00: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x02)  # 03: Msg Spec Tag
        exp.append(0x22)  # 04: Msg Len
        exp.append(0x00)  # 05: Timeout
        exp.append(0x00)  # 06: Timeout
        exp.append(0x09)  # 07: Timeout
        exp.append(0x2c)  # 08: Timeout
        exp.append(0x3a)  # 09: Network Token
        exp.append(0x2d)  # 10: Network Token
        exp.append(0x1d)  # 11: Network Token
        exp.append(0x4c)  # 12: Network Token
        exp.append(0xa8)  # 13: Application Token
        exp.append(0xa2)  # 14: Application Token
        exp.append(0x1c)  # 15: Application Token
        exp.append(0xa1)  # 16: Application Token
        exp.append(0x3b)  # 17: Application Token
        exp.append(0xc8)  # 18: Application Token
        exp.append(0x32)  # 19: Application Token
        exp.append(0xd1)  # 20: Application Token
        exp.append(0xaa)  # 21: Application Token
        exp.append(0x39)  # 22: Application Token
        exp.append(0x11)  # 23: Key
        exp.append(0x1a)  # 24: Key
        exp.append(0x9c)  # 25: Key
        exp.append(0xad)  # 26: Key
        exp.append(0xbd)  # 27: Key
        exp.append(0x9b)  # 28: Key
        exp.append(0x0e)  # 29: Key
        exp.append(0x1a)  # 30: Key
        exp.append(0xc7)  # 31: Key
        exp.append(0xc4)  # 32: Key
        exp.append(0xa8)  # 33: Key
        exp.append(0xb2)  # 34: Key
        exp.append(0xe2)  # 35: Key
        exp.append(0xd9)  # 36: Key
        exp.append(0xe4)  # 37: Key
        exp.append(0xc5)  # 38: Key
        self.assertSequenceEqual(msg, exp)

    def test_vFota_Update_V204(self):
        """ Verifies v2.0.4 vFota Update Construction. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_4()
        msg = spec.build_vfota_message("UPDATE",
                                       file_version=0x11223333,
                                       file_id=0x5200F00B,
                                       time_to_live=0x5000,
                                       length_of_target_list=0x03,
                                       spread_image=0x01,
                                       img_src=0x03,
                                       scan_target=b'\x52\x50\x2d\x00',
                                       target_list=b'\x11\x11\x11\x11\x11\x11'
                                                   b'\x22\x22\x22\x22\x22\x22'
                                                   b'\x33\x33\x33\x33\x33\x33')
        exp = bytearray()
        exp.append(0xA0)  # 00: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x04)  # 03: Msg Spec Tag
        exp.append(0x27)  # 04: Msg Len
        exp.append(0x06)  # 05: Ctrl Cmd
        exp.append(0x02)  # 06: Ctrl Cmd
        exp.append(0x00)  # 07: vFota Spec Version
        exp.append(0x01)  # 08: vFota Command
        exp.append(0x11)  # 09: vFota File Version
        exp.append(0x22)  # 10: vFota File Version
        exp.append(0x33)  # 11: vFota File Version
        exp.append(0x33)  # 12: vFota File Version
        exp.append(0x52)  # 13: vFota File ID
        exp.append(0x00)  # 14: vFota File ID
        exp.append(0xF0)  # 15: vFota File ID
        exp.append(0x0B)  # 16: vFota File ID
        exp.append(0x50)  # 17: vFota Time to Live
        exp.append(0x00)  # 18: vFota Time to Live
        exp.append(0x03)  # 19: vFota Length of Target List
        exp.append(0x01)  # 20: vFota Spread Image
        exp.append(0x03)  # 21: vFota Image Source
        exp.append(0x52)  # 22: vFota Scan Target Name
        exp.append(0x50)  # 23: vFota Scan Target Name
        exp.append(0x2d)  # 24: vFota Scan Target Name
        exp.append(0x00)  # 25: vFota Scan Target Name
        exp.append(0x11)  # 26: vFota Target 1
        exp.append(0x11)  # 27: vFota Target 1
        exp.append(0x11)  # 28: vFota Target 1
        exp.append(0x11)  # 29: vFota Target 1
        exp.append(0x11)  # 30: vFota Target 1
        exp.append(0x11)  # 31: vFota Target 1
        exp.append(0x22)  # 32: vFota Target 2
        exp.append(0x22)  # 33: vFota Target 2
        exp.append(0x22)  # 34: vFota Target 2
        exp.append(0x22)  # 35: vFota Target 2
        exp.append(0x22)  # 36: vFota Target 2
        exp.append(0x22)  # 37: vFota Target 2
        exp.append(0x33)  # 38: vFota Target 3
        exp.append(0x33)  # 39: vFota Target 3
        exp.append(0x33)  # 40: vFota Target 3
        exp.append(0x33)  # 41: vFota Target 3
        exp.append(0x33)  # 42: vFota Target 3
        exp.append(0x33)  # 43: vFota Target 3
        self.assertSequenceEqual(msg, exp)

    def test_vFota_Cancel_V204(self):
        """ Verifies v2.0.4 vFota Cancel Construction. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_4()
        msg = spec.build_vfota_message("CANCEL")
        exp = bytearray()
        exp.append(0xA0)  # 00: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x04)  # 03: Msg Spec Tag
        exp.append(0x04)  # 04: Msg Len
        exp.append(0x06)  # 05: Ctrl Cmd
        exp.append(0x02)  # 06: Ctrl Cmd
        exp.append(0x00)  # 07: vFota Spec Version
        exp.append(0x02)  # 08: vFota Command
        self.assertSequenceEqual(msg, exp)

    def test_vFota_Firmware_ID_V204(self):
        """ Verifies v2.0.4 vFota Cancel Construction. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_4()
        msg = spec.build_vfota_message("FW_ID_REQ")
        exp = bytearray()
        exp.append(0xA0)  # 00: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x04)  # 03: Msg Spec Tag
        exp.append(0x04)  # 04: Msg Len
        exp.append(0x06)  # 05: Ctrl Cmd
        exp.append(0x02)  # 06: Ctrl Cmd
        exp.append(0x00)  # 07: vFota Spec Version
        exp.append(0x03)  # 08: vFota Command
        self.assertSequenceEqual(msg, exp)

    def test_vFota_Report_Request_V204(self):
        """ Verifies v2.0.4 vFota Cancel Construction. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_4()
        msg = spec.build_vfota_message("PROCESS_REPORT_REQ")
        exp = bytearray()
        exp.append(0xA0)  # 00: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x04)  # 03: Msg Spec Tag
        exp.append(0x04)  # 04: Msg Len
        exp.append(0x06)  # 05: Ctrl Cmd
        exp.append(0x02)  # 06: Ctrl Cmd
        exp.append(0x00)  # 07: vFota Spec Version
        exp.append(0x04)  # 08: vFota Command
        self.assertSequenceEqual(msg, exp)

    def test_vFota_Test_Mode_V204(self):
        """ Verifies v2.0.4 vFota Cancel Construction. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_4()
        msg = spec.build_vfota_message("TEST_MODE", state=0x02)
        exp = bytearray()
        exp.append(0xA0)  # 00: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x04)  # 03: Msg Spec Tag
        exp.append(0x05)  # 04: Msg Len
        exp.append(0x06)  # 05: Ctrl Cmd
        exp.append(0x02)  # 06: Ctrl Cmd
        exp.append(0x00)  # 07: vFota Spec Version
        exp.append(0x05)  # 08: vFota Command
        exp.append(0x02)  # 08: vFota State
        self.assertSequenceEqual(msg, exp)

    def test_vFota_DeviceReportReq_V204(self):
        """ Verifies v2.0.4 vFota Cancel Construction. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_4()
        msg = spec.build_vfota_message("DEVICE_REPORT_REQ")
        exp = bytearray()
        exp.append(0xA0)  # 00: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x04)  # 03: Msg Spec Tag
        exp.append(0x04)  # 04: Msg Len
        exp.append(0x06)  # 05: Ctrl Cmd
        exp.append(0x02)  # 06: Ctrl Cmd
        exp.append(0x00)  # 07: vFota Spec Version
        exp.append(0x06)  # 08: vFota Command
        self.assertSequenceEqual(msg, exp)

    def test_vFota_Dat_File_Request_V204(self):
        """ Verifies v2.0.4 vFota Cancel Construction. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_4()
        msg = spec.build_vfota_message("DAT_FILE_REQ", dat_length=15, dat_file=b"\x55\x55\x55\x55\x55\x55\x55\x55\x55"
                                                                                b"\x55\x55\x55\x55\x55\x55")
        exp = bytearray()
        exp.append(0xA0)  # 00: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x04)  # 03: Msg Spec Tag
        exp.append(0x14)  # 04: Msg Len
        exp.append(0x06)  # 05: Ctrl Cmd
        exp.append(0x02)  # 06: Ctrl Cmd
        exp.append(0x00)  # 07: vFota Spec Version
        exp.append(0x07)  # 08: vFota Command
        exp.append(0x0f)  # 09: vFota Dat File Length
        exp.append(0x55)  # 10: vFota Dat File
        exp.append(0x55)  # 11: vFota Dat File
        exp.append(0x55)  # 12: vFota Dat File
        exp.append(0x55)  # 13: vFota Dat File
        exp.append(0x55)  # 14: vFota Dat File
        exp.append(0x55)  # 15: vFota Dat File
        exp.append(0x55)  # 16: vFota Dat File
        exp.append(0x55)  # 17: vFota Dat File
        exp.append(0x55)  # 18: vFota Dat File
        exp.append(0x55)  # 19: vFota Dat File
        exp.append(0x55)  # 20: vFota Dat File
        exp.append(0x55)  # 21: vFota Dat File
        exp.append(0x55)  # 22: vFota Dat File
        exp.append(0x55)  # 23: vFota Dat File
        exp.append(0x55)  # 24: vFota Dat File
        self.assertSequenceEqual(msg, exp)

    def test_vFota_Status_Request_V204(self):
        """ Verifies v2.0.4 vFota Cancel Construction. """
        spec = af_devs.nordic_access_point.NordicAPMessageSpecV2_0_4()
        msg = spec.build_vfota_message("STATUS_REQ")
        exp = bytearray()
        exp.append(0xA0)  # 00: Msg Type
        exp.append(0x02)  # 01: Msg Spec Major
        exp.append(0x00)  # 02: Msg Spec Minor
        exp.append(0x04)  # 03: Msg Spec Tag
        exp.append(0x04)  # 04: Msg Len
        exp.append(0x06)  # 05: Ctrl Cmd
        exp.append(0x02)  # 06: Ctrl Cmd
        exp.append(0x00)  # 07: vFota Spec Version
        exp.append(0x08)  # 08: vFota Command
        self.assertSequenceEqual(msg, exp)


if __name__ == '__main__':

    coloredlogs.install(level=LOG_LEVEL)

    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    # Validate library before Authentication.
    suite.addTests(loader.loadTestsFromTestCase(NordicAccessPointTests))
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)
    suite = unittest.TestSuite()
