""" Unittesting for the Conductor/Airfinder libraries!

What to Unit Test?
-------------------------
* Pythonic Objects
* Inheritence
* Basic API Functionality

What NOT to Unit Test?
-------------------------
* Embedded Devices (Waiting for message responses, sending live commands)
"""
import datetime
import logging
import unittest
from getpass import getpass
from os import getenv
from time import sleep

import coloredlogs

import conductor
import conductor.airfinder as af

###############################################################################
# Test Configuration Constants
###############################################################################
EXPECTED_VERSION = "1.6.0a4"  # Must match installed conductor-py version.
ACCOUNT_EMAIL = "thomas.steinholz@link-labs.com"  # Account to use for testing.
PASSWORD = None  # Will use password when avalible.
USE_DEV = False  # When Develop Instance is required for testing.
LOG_LEVEL = "DEBUG"  # Log Level tests and of all submodules.

# Conductor Devices
TEST_MODULE_ID = "$301$0-0-0-03000266f"
TEST_LTEM_ID = "$303$0-0-0001450-2bf6618ab"
TEST_GW_ID = ""

# Airfinder Devices
TEST_AP_ID = "$301$0-0-0-03000a37a"
TEST_AP_MAC1 = "C0:30:00:00:a3:7a"  # TODO: Add building ap w/ mac
TEST_AP_MAC2 = "C0300000a37a"

TEST_TAG_ID = "$501$0-0-0000d8e-0907594f8"
TEST_TAG_MAC1 = ""
TEST_TAG_MAC2 = ""

TEST_ALERT_TAG_ID = ""
TEST_ALERT_TAG_MAC1 = ""
TEST_ALERT_TAG_MAC2 = ""

TEST_LOC_ID = ""
TEST_LOC_MAC1 = ""
TEST_LOC_MAC2 = ""

TEST_ST_ID = ""
TEST_ST_MAC1 = ""
TEST_ST_MAC2 = ""

TEST_SITE_ID = ""
TEST_AREA_ID = ""
TEST_ZONE_ID = ""

TEST_APP_TOKEN = "404ab41ac7fbb6411729"
#TEST_NET_TOKEN = ll_ifc.OPEN_NET_TOKEN # "3479e39e" # TODO: Use Test Token


LOG = logging.getLogger(__name__)

################################################################################
# Test Enviornment NOTE: Utilizing these Global variables bypasses the unit
# test's lack-of-context, please be mindful of these obj's state.
################################################################################
## Production Credentials
c_account_p = conductor.account.ConductorAccount(getenv("UNIT_USER"), conductor.PRODUCTION, getenv("UNIT_PASS"))
af_user_p = af.User(getenv("UNIT_USER"), conductor.PRODUCTION, getenv("UNIT_PASS"))

## Hospitality Credentials
c_account_h = conductor.account.ConductorAccount(getenv("UNIT_USER"), conductor.HOSPITALITY, getenv("UNIT_PASS"))
af_user_h = af.User(getenv("UNIT_USER"), conductor.HOSPITALITY, getenv("UNIT_PASS"))

## Develop Credentials
if USE_DEV:
    c_account_d = conductor.account.ConductorAccount(getenv("UNIT_USER"), conductor.DEVELOP, getenv("UNIT_PASS"))
    af_user_d = af.User(getenv("UNIT_USER"), conductor.DEVELOP, getenv("UNIT_PASS"))


################################################################################
# Test Definitions
################################################################################

class ConductorTests(unittest.TestCase):
    """ Validates basic library functions. """

    def __init__(self, test_name):
        super().__init__(test_name)

    def setUp(self):
        """ TODO """
        pass

    def tearDown(self):
        """ TODO """
        pass

    # def test_Version(self):
    #     """ Verify the correct version of the test is being run. """
    #     self.assertEqual(EXPECTED_VERSION, conductor.CONDUCTOR_LIBRARY_VERSION)
    #     pass

    def test_VersionConstruction(self):
        """ Verifies that versions are being constructed correctly. """
        v = conductor.util.Version(1, 2, 3)
        self.assertEqual(v.major, 1)
        self.assertEqual(v.minor, 2)
        self.assertEqual(v.tag, 3)

    def test_VersionComparisionEqual(self):
        """ Verifies the version comparisions overrides are working. """
        LOG.info("")
        v1 = conductor.util.Version(1, 2, 3)
        v2 = conductor.util.Version(1, 2, 3)
        LOG.info("{} == {} = True".format(v1, v2))
        self.assertTrue(v1 == v2)

        v2.major = 3
        LOG.info("{} == {} = False".format(v1, v2))
        self.assertFalse(v1 == v2)

        v2.major = v1.major
        v2.minor = 1
        LOG.info("{} == {} = False".format(v1, v2))
        self.assertFalse(v1 == v2)

        v2.minor = v1.minor
        v2.tag = 2
        LOG.info("{} == {} = False".format(v1, v2))
        self.assertFalse(v1 == v2)

        v2.tag = v1.tag
        LOG.info("{} == {} = True".format(v1, v2))
        self.assertTrue(v1 == v2)

        v1.major = 3
        LOG.info("{} == {} = False".format(v1, v2))
        self.assertFalse(v1 == v2)

        v1.major = v2.major
        v1.minor = 1
        LOG.info("{} == {} = False".format(v1, v2))
        self.assertFalse(v1 == v2)

        v1.minor = v2.minor
        v1.tag = 2
        LOG.info("{} == {} = False".format(v1, v2))
        self.assertFalse(v1 == v2)

        v1.tag = v2.tag
        LOG.info("{} == {} = True".format(v1, v2))
        self.assertTrue(v1 == v2)

    def test_VersionComparisionNotEqual(self):
        """ Verifies the version comparisions overrides are working. """
        LOG.info("")
        v1 = conductor.util.Version(1, 2, 3)
        v2 = conductor.util.Version(4, 5, 6)
        LOG.info("{} != {} = True".format(v1, v2))
        self.assertTrue(v1 != v2)

        v2.tag = v1.tag
        LOG.info("{} != {} = True".format(v1, v2))
        self.assertTrue(v1 != v2)

        v2.minor = v1.minor
        LOG.info("{} != {} = True".format(v1, v2))
        self.assertTrue(v1 != v2)

        v2.major = v1.major
        LOG.info("{} != {} = False".format(v1, v2))
        self.assertFalse(v1 != v2)

        v2.minor = v2.minor + 1
        LOG.info("{} != {} = True".format(v1, v2))
        self.assertTrue(v1 != v2)

        v2.tag = v2.tag + 1
        LOG.info("{} != {} = True".format(v1, v2))
        self.assertTrue(v1 != v2)

    def test_VersionComparisionLessThan(self):
        """ Verifies the version comparisions overrides are working. """
        LOG.info("")
        v1 = conductor.util.Version(1, 2, 3)
        v2 = conductor.util.Version(4, 4, 4)
        LOG.info("{} < {} = True".format(v1, v2))
        self.assertTrue(v1 < v2)

        v1.major = v2.major + 1
        LOG.info("{} < {} = False".format(v1, v2))
        self.assertFalse(v1 < v2)

        v1.major = v2.major
        LOG.info("{} < {} = True".format(v1, v2))
        self.assertTrue(v1 < v2)

        v1.minor = v2.minor + 1
        LOG.info("{} < {} = False".format(v1, v2))
        self.assertFalse(v1 < v2)

        v1.minor = v2.minor
        LOG.info("{} < {} = True".format(v1, v2))
        self.assertTrue(v1 < v2)

        v1.tag = v2.tag
        LOG.info("{} < {} = False".format(v1, v2))
        self.assertFalse(v1 < v2)

    def test_VersionComparisionLessThanOrEqual(self):
        """ Verifies the version comparisions overrides are working. """
        LOG.info("")
        v1 = conductor.util.Version(1, 2, 3)
        v2 = conductor.util.Version(4, 4, 4)
        LOG.info("{} <= {} = True".format(v1, v2))
        self.assertTrue(v1 <= v2)

        v1.major = v2.major + 1
        LOG.info("{} <= {} = False".format(v1, v2))
        self.assertFalse(v1 <= v2)

        v1.major = v2.major
        LOG.info("{} <= {} = True".format(v1, v2))
        self.assertTrue(v1 <= v2)

        v1.minor = v2.minor + 1
        LOG.info("{} <= {} = False".format(v1, v2))
        self.assertFalse(v1 <= v2)

        v1.minor = v2.minor
        LOG.info("{} <= {} = True".format(v1, v2))
        self.assertTrue(v1 <= v2)

        v1.tag = v2.tag
        LOG.info("{} <= {} = True".format(v1, v2))
        self.assertTrue(v1 <= v2)

    def test_VersionComparisionGreaterThan(self):
        """ Verifies the version comparisions overrides are working. """
        LOG.info("")
        v1 = conductor.util.Version(4, 4, 4)
        v2 = conductor.util.Version(3, 3, 3)
        LOG.info("{} > {} = True".format(v1, v2))
        self.assertTrue(v1 > v2)

        v1.major = v2.major - 2
        LOG.info("{} > {} = False".format(v1, v2))
        self.assertFalse(v1 > v2)

        v1.major = v1.major + 1
        LOG.info("{} > {} = False".format(v1, v2))
        self.assertFalse(v1 > v2)

        v1.major = v2.major
        LOG.info("{} > {} = True".format(v1, v2))
        self.assertTrue(v1 > v2)

        v1.minor = v2.minor - 2
        LOG.info("{} > {} = False".format(v1, v2))
        self.assertFalse(v1 > v2)

        v1.minor = v1.minor + 1
        LOG.info("{} > {} = False".format(v1, v2))
        self.assertFalse(v1 > v2)

        v1.minor = v2.minor
        LOG.info("{} > {} = True".format(v1, v2))
        self.assertTrue(v1 > v2)

        v1.tag = v2.tag - 2
        LOG.info("{} > {} = False".format(v1, v2))
        self.assertFalse(v1 > v2)

        v1.tag = v1.tag + 1
        LOG.info("{} > {} = False".format(v1, v2))
        self.assertFalse(v1 > v2)

        v1.tag = v2.tag
        LOG.info("{} > {} = False".format(v1, v2))
        self.assertFalse(v1 > v2)

    def test_VersionComparisionGreatorThanOrEqual(self):
        """ Verifies the version comparisions overrides are working. """
        LOG.info("")
        v1 = conductor.util.Version(4, 4, 4)
        v2 = conductor.util.Version(3, 3, 3)
        LOG.info("{} >= {} = True".format(v1, v2))
        self.assertTrue(v1 >= v2)

        v1.major = 1
        LOG.info("{} >= {} = False".format(v1, v2))
        self.assertFalse(v1 >= v2)

        v1.major = v1.major + 1
        LOG.info("{} >= {} = False".format(v1, v2))
        self.assertFalse(v1 >= v2)

        v1.major = v2.major
        LOG.info("{} >= {} = True".format(v1, v2))
        self.assertTrue(v1 >= v2)

        v1.minor = 1
        LOG.info("{} >= {} = False".format(v1, v2))
        self.assertFalse(v1 >= v2)

        v1.minor = v1.minor + 1
        LOG.info("{} >= {} = False".format(v1, v2))
        self.assertFalse(v1 >= v2)

        v1.minor = v1.minor + 1 # Equal To
        LOG.info("{} >= {} = True".format(v1, v2))
        self.assertTrue(v1 >= v2)

        v1.minor = v1.minor + 1 # Greater Than
        LOG.info("{} >= {} = True".format(v1, v2))
        self.assertTrue(v1 >= v2)

        v1.minor = v2.minor
        v1.tag = 1
        LOG.info("{} >= {} = False".format(v1, v2))
        self.assertFalse(v1 >= v2)

        v1.tag = v1.tag + 1
        LOG.info("{} >= {} = False".format(v1, v2))
        self.assertFalse(v1 >= v2)

        v1.tag = v1.tag + 1 # Equal To
        LOG.info("{} >= {} = True".format(v1, v2))
        self.assertTrue(v1 >= v2)

        v1.tag = v1.tag + 1 # Greater Than
        LOG.info("{} >= {} = True".format(v1, v2))
        self.assertTrue(v1 >= v2)


class ConductorAccountTests(unittest.TestCase):
    """ Validates ConductorAccount functions. """

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


class ConductorAssetGroupTests(unittest.TestCase):
    """ Validates AssetGroups functions. """

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


class ConductorDeviceGatewayTests(unittest.TestCase):
    """ Validates Gateway functions. """

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


class ConductorDeviceModuleTests(unittest.TestCase):
    """ Validates Module functions. """

    def __init__(self, test_name):
        super().__init__(test_name)

    def setUp(self):
        """ TODO """
        pass

    def tearDown(self):
        """ TODO """
        pass

    def test_Construction(self):
        """ Verifies the construction of a Module. """
        mod = c_account_p.get_module(TEST_MODULE_ID)
        self.assertIsNotNone(mod.session)
        self.assertIsInstance(mod.subject_id, str)
        self.assertIsInstance(mod.instance, str)
        self.assertIsInstance(mod._data, dict)

    def test_Properties(self):
        """ Verifies nothing. """
        mod = c_account_p.get_module(TEST_MODULE_ID)
        self.assertIsInstance(mod.downlink_mode, conductor.Module.DownlinkMode)
        self.assertIsInstance(mod.module_firmware_version, conductor.util.Version)
        self.assertIsInstance(mod.last_modified_time, datetime.datetime)
        self.assertIsInstance(mod.last_mailbox_request_time, datetime.datetime)
        self.assertIsInstance(mod.initial_detection_time, datetime.datetime)
        self.assertIsInstance(mod.registration_time, datetime.datetime)
        self.assertIsInstance(mod.application_token, conductor.tokens.AppToken)
        self.assertIsInstance(mod.gateway, conductor.Gateway)


class ConductorDeviceLTEmModuleTests(unittest.TestCase):
    """ Validates LTEmModule functions. """

    def __init__(self, test_name):
        super().__init__(test_name)

    def setUp(self):
        """ TODO """
        pass

    def tearDown(self):
        """ TODO """
        pass

    def test_Properties(self):
        """ Verifies nothing. """
        mod = c_account_p.get_module(TEST_LTEM_ID)

        # Inherited Fields (Module)
        self.assertIsInstance(mod.downlink_mode, conductor.Module.DownlinkMode)
        self.assertIsNone(mod.module_firmware_version)
        self.assertIsInstance(mod.last_modified_time, datetime.datetime)
        self.assertIsInstance(mod.last_mailbox_request_time, datetime.datetime)
        self.assertIsInstance(mod.initial_detection_time, datetime.datetime)
        self.assertIsInstance(mod.registration_time, datetime.datetime)
        self.assertIsInstance(mod.application_token, conductor.tokens.AppToken)
        self.assertIsInstance(mod.gateway, conductor.Gateway)

        # LTEm Fields
        self.assertIsInstance(mod.cell_data_usage, int)
        self.assertIsInstance(mod.last_cell_id, int)
        self.assertIsInstance(mod.last_cell_tac, int)
        self.assertIsInstance(mod.iccid, int)
        self.assertIsInstance(mod.imei, int)
        self.assertIsInstance(mod.ip_address, str)
        self.assertIsInstance(mod.version, conductor.util.Version)
        self.assertIsInstance(mod.modem_versions, tuple)
        self.assertIsInstance(mod.provisioned_status, str)
        self.assertIsInstance(mod.mdn, int)
        self.assertIsInstance(mod.min, int)
        self.assertIsInstance(mod.msisdn, int)
        self.assertIsInstance(mod.last_slot, int)


class ConductorEventCountTests(unittest.TestCase):
    """ Validates EventCount functions. """

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


class ConductorDownlinkMessageTests(unittest.TestCase):
    """ Validates DownlinkMessage functions. """

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


class ConductorUplinkMessageTests(unittest.TestCase):
    """ Validates UplinkMessage functions. """

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


class ConductorSubjectTests(unittest.TestCase):
    """ Validates ConductorSubject functions. """

    def __init__(self, test_name):
        super().__init__(test_name)

    def setUp(self):
        """ TODO """
        pass

    def tearDown(self):
        """ TODO """
        pass


class ConductorUplinkSubjectTests(unittest.TestCase):
    """ Validates UplinkSubject functions. """

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


class ConductorDownlinkSubjectTests(unittest.TestCase):
    """ Validates DownlinkSubject functions. """

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


class ConductorSubscriptionTests(unittest.TestCase):
    """ Validates basic Subscription functions. """

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


class ConductorSubWebsocketTests(unittest.TestCase):
    """ Validates Websocket Subscription functions. """

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


class ConductorSubZMQTests(unittest.TestCase):
    """ Validates ZMQ Subscription functions. """

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


class ConductorNetTokenTests(unittest.TestCase):
    """ Validates Network Token functions. """

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


class ConductorAppTokenTests(unittest.TestCase):
    """ Validates Application Token functions. """

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


class AirfinderUserTests(unittest.TestCase):
    """ Validates the Airfinder User class. """

    def __init__(self, test_name):
        super().__init__(test_name)

    def setUp(self):
        """ TODO """
        pass

    def tearDown(self):
        """ TODO """
        pass

    def testConstruction(self):
        """ Verifies the construction of the airfinder user. """
        self.assertIsNotNone(af_user_p.session)
        self.assertIsNotNone(af_user_h.session)
        self.assertEqual(af_user_p.instance, conductor.PRODUCTION)
        self.assertEqual(af_user_h.instance, conductor.HOSPITALITY)
        self.assertIsNotNone(af_user_p.subject_id)
        self.assertIsNotNone(af_user_h.subject_id)

    def testDeleteSiteBySite(self):
        """ Verifies we can delete site's by their object. """
        site = None
        for s in af_user_p.get_sites():
            # NOTE: To fix a failed test...
            if s.name == "edioklewqwdfzxdfdf3":
                site = s
        if not site:
            site = af_user_p.create_site("edioklewqwdfzxdfdf3")

        self.assertIsNotNone(site)
        self.assertIsNotNone(site.session)
        self.assertIsNotNone(site.subject_id)
        self.assertEqual(site.instance, conductor.PRODUCTION)
        self.assertIsNotNone(site._data)
        self.assertEqual(site.name, "edioklewqwdfzxdfdf3")

        af_user_p.delete_site(site)
        sleep(5)

        # Look for site.
        site = None
        for s in af_user_p.get_sites():
            if s.name == "edioklewqwdfzxdfdf3":
                site = s
        self.assertIsNone(site)

    def testDeleteSiteBySiteId(self):
        """ Verifies we can delete site's by their ID. """
        site = None
        for s in af_user_p.get_sites():
            # NOTE: To fix a failed test...
            if s.name == "asdfqwerasdfzxcvasdfgwe3":
                site = s
        if not site:
            site = af_user_p.create_site("asdfqwerasdfzxcvasdfgwe3")

        self.assertIsNotNone(site)
        self.assertIsNotNone(site.session)
        self.assertIsNotNone(site.subject_id)
        self.assertEqual(site.instance, conductor.PRODUCTION)
        self.assertIsNotNone(site._data)
        self.assertEqual(site.name, "asdfqwerasdfzxcvasdfgwe3")

        site_id = site.subject_id
        af_user_p.delete_site(site.subject_id)
        sleep(5)

        # Look for site.
        with self.assertRaises(conductor.subject.FailedAPICallException):
            af_user_p.get_site(site_id)

        #site = None
        #for s in af_user_p.get_sites():
        #    if s.name == "asdfqwerasdfzxcvasdfgwe":
        #        site = s
        #self.assertIsNone(site)

    def testGetSiteById(self):
        """ Verifies we can get Site by ID. """
        sites = af_user_p.get_sites()
        self.assertIsInstance(sites, list)

        site1 = sites[3]
        site2 = af_user_p.get_site(site1.subject_id)

        self.assertEqual(site1.subject_id, site2.subject_id)
        self.assertEqual(site1.instance, site2.instance)
        self.assertIsNotNone(site2._data)


class AccessPointAirfinderTests(unittest.TestCase):
    """ Validates the Airfinder Access Point class. """

    def __init__(self, test_name):
        super().__init__(test_name)

    def setUp(self):
        """ TODO """
        pass

    def tearDown(self):
        """ TODO """
        pass

    def test_Construction(self):
        """ Validates the construction of an Access Point. """
        ap = af_user_p.get_access_point(TEST_AP_ID)

        self.assertIsInstance(ap, af.AccessPoint)
        self.assertIsNotNone(ap.session)
        self.assertEqual(ap.subject_id, TEST_AP_ID)
        self.assertEqual(ap.instance, conductor.PRODUCTION)
        self.assertIsNotNone(ap._data)

    def test_ConstructionDataGeneration(self):
        """ Validates the _data field will be populated when missing. """
        mod = c_account_p.get_module(TEST_AP_ID)

        ap = af.AccessPoint(session=mod.session, subject_id=TEST_AP_ID,
                            instance=conductor.PRODUCTION)

        self.assertIsInstance(ap, af.AccessPoint)
        self.assertIsNotNone(ap.session)
        self.assertEqual(ap.subject_id, TEST_AP_ID)
        self.assertEqual(ap.instance, conductor.PRODUCTION)
        self.assertIsNotNone(ap._data)

    def test_InvalidConstructionMissingSession(self):
        """ Validate construction fails with a missing session. """
        with self.assertRaises(Exception):
            af.AccessPoint(subject_id=TEST_AP_ID)

    def test_InvalidConstructionMissingID(self):
        """ Validate construction fails with a missing subject_id. """
        mod = c_account_p.get_module(TEST_AP_ID)
        self.assertIsNotNone(mod.session)

        with self.assertRaises(Exception):
            af.AccessPoint(mod.session)

    def test_InvalidConstructionMissingAll(self):
        """ Validate construction fails when given nothing. """
        with self.assertRaises(Exception):
            af.AccessPoint()

    def test_Properties(self):
        """ Verifies the AccessPoint properties. """
        ap = af_user_p.get_access_point(TEST_AP_ID)

        # Inherited Fields (Module)
        self.assertIsInstance(ap._md, dict)
        self.assertIsInstance(ap.downlink_mode, conductor.Module.DownlinkMode)
        self.assertIsInstance(ap.module_firmware_version, conductor.util.Version)
        self.assertIsInstance(ap.gateway, conductor.devices.gateway.Gateway)
        self.assertIsInstance(ap.last_modified_time, datetime.datetime)
        self.assertIsNone(ap.last_mailbox_request_time)  # APs are DL Always ON
        self.assertIsInstance(ap.initial_detection_time, datetime.datetime)
        self.assertIsInstance(ap.registration_time, datetime.datetime)
        self.assertIsInstance(ap.application_token, conductor.tokens.AppToken)

        # AccessPioint Fields
        self.assertIsInstance(ap.device_type, str)
        self.assertIsInstance(ap.assert_count, int)
        self.assertIsInstance(ap.avg_rssi, float)
        self.assertIsInstance(ap.battery_percent, float)
        self.assertIsInstance(ap.blacklist_len, int)
        self.assertIsInstance(ap.node_count, int)
#        self.assertIsInstance(ap.downlink_counts, af.AccessPoint.DownlinkCounts)
        self.assertIsInstance(ap.is_lost, bool)
        self.assertIsInstance(ap.last_event_time, datetime.datetime)
        self.assertIsInstance(ap.last_msg_type, int)
        self.assertIsInstance(ap.last_reset_cause, int)
        self.assertIsInstance(ap.msg_count, int)
        self.assertIsInstance(ap.network_loading, int)
        self.assertIsInstance(ap.reset_count, int)
        self.assertIsInstance(ap.rp_count, int)
        self.assertIsInstance(ap.rssi_collect_time, datetime.datetime)
        self.assertIsInstance(ap.last_payload_len, int)
        self.assertIsNone(ap.version)  # NOTE: v1 AP doesn't have version
        self.assertIsInstance(ap.symble_version, conductor.util.Version)
        self.assertIsInstance(ap.sys_time, datetime.datetime)
#        self.assertIsInstance(ap.task_stats, af.AccessPoint.TaskStats)
#        self.assertIsInstance(ap.uplink_queue_stats, af.AccessPoint.UplinkQueueStats)
        self.assertIsInstance(ap.uptime, int)

#        if bool(ap._md.get('assertOccured')):
#            self.assertIsInstance(ap.last_assert_info, af.AccessPoint.AssertInfo)
#        else:
#            self.assertIsNone(ap.last_assert_info)


class AlertTagAirfinderTests(unittest.TestCase):
    """ Validates the Airfinder [Hospitality] Alert Tag class. """

    def __init__(self, test_name):
        super().__init__(test_name)

    def setUp(self):
        """ TODO """
        pass

    def tearDown(self):
        """ TODO """
        pass

    def test_Construction(self):
        """ Validates the construction of an Alert Tag. """
        #at = af_user_h.get_node("F7A2992D0E5B")

        #self.assertIsInstance(at, af.AlertTag)
        #self.assertIsNotNone(at._data)
        # TODO: Validate Other Fields


class AreaAirfinderTests(unittest.TestCase):
    """ Validates the Airfinder Area class. """

    def __init__(self, test_name):
        super().__init__(test_name)

    def setUp(self):
        """ TODO """
        pass

    def tearDown(self):
        """ TODO """
        pass

    def test_TODO(self):
        """ TODO """
        pass


class LocationAirfinderTests(unittest.TestCase):
    """ Validates the Airfinder Location class. """

    def __init__(self, test_name):
        super().__init__(test_name)

    def setUp(self):
        """ TODO """
        pass

    def tearDown(self):
        """ TODO """
        pass

    def test_Construction(self):
        """ Validates the construction of a Location Beacon. """
        lb = af_user_p.get_node("CC7566EB6155")

        self.assertIsInstance(lb, af.Location)
        self.assertIsNotNone(lb._data)
        # TODO: Validate Other Fields


class SiteAirfinderTests(unittest.TestCase):
    """ Validates the Airfinder Site class """

    def __init__(self, test_name):
        super().__init__(test_name)

    def setUp(self):
        """ TODO """
        pass

    def tearDown(self):
        """ TODO """
        pass

    def test_TODO(self):
        """ TODO """
        pass


class SupertagAirfinderTests(unittest.TestCase):
    """ Validates the Airfinder Supertag Class """

    def __init__(self, test_name):
        super().__init__(test_name)

    def setUp(self):
        """ TODO """
        pass

    def tearDown(self):
        """ TODO """
        pass

    @unittest.skip("given tag no longer valid.")
    def test_Construction(self):
        """ Validates the construction of a Supertag. """
        st = af_user_p.get_node("d8e0907594f8")

        self.assertIsInstance(st, af.Supertag)
        self.assertIsNotNone(st._data)
        # TODO: Validate Other Fields


class TagAirfinderTests(unittest.TestCase):
    """ Validates the Airfinder Tag class. """

    def __init__(self, test_name):
        super().__init__(test_name)

    def setUp(self):
        """ TODO """
        pass

    def tearDown(self):
        """ TODO """
        pass

    def test_Construction(self):
        """ Validates the construction of a Tag. """
        #t = af_user_p.get_node("d8e0907594f8")
        pass
        #self.assertIsNotNone(t._data)
        #self.assertIsInstance(t.last_access_point, af.AccessPoint)
        #self.assertIsInstance(t.last_gateway, conductor.Gateway)
        #self.assertIsInstance(t.app_token, conductor.AppToken)
        #self.assertIsInstance(t.last_location0, af.Location)

    def test_Construction_InvalidAddressMinusOne(self):
        with self.assertRaises(Exception):
            af_user_p.get_node("$501$0-0-0000d8e-090594f8")

    def test_Construction_InvalidAddressPlusOne(self):
        with self.assertRaises(Exception):
            af_user_p.get_node("$501$0-0-0000d8e-09540594f8")

    def test_Construction_InvalidColonMinusOne(self):
        with self.assertRaises(Exception):
            af_user_p.get_node("d8:e0:90:75:94:8")

    def test_Construction_InvalidColonPlusOne(self):
        with self.assertRaises(Exception):
            af_user_p.get_node("d8:e0:90:75:94:f82")

    def test_Construction_InvalidMinusOne(self):
        with self.assertRaises(Exception):
            af_user_p.get_node("d8e090759f8")

    def test_Construction_InvalidPlusOne(self):
        with self.assertRaises(Exception):
            af_user_p.get_node("d8e0907594df8")

    def test_Construction_InvalidNull(self):
        with self.assertRaises(Exception):
            af_user_p.get_node("")

    @unittest.skip("given tag no longer valid.")
    def test_Construction_WithAddress(self):
        """ Validates the Address Managment of the Tag Contructor. """
        t = af_user_p.get_node(TEST_TAG_ID)

        self.assertEqual("d8:e0:90:75:94:f8",          t.mac_address) # From metadata
        self.assertEqual("$501$0-0-0000d8e-0907594f8", t.subject_id)  # From input
        self.assertIsNotNone(t._data)
        self.assertEqual(t.instance, conductor.PRODUCTION)

    @unittest.skip("given tag no longer valid.")
    def test_Construction_WithoutColons(self):
        """ Validates the Address Managment of the Tag Contructor. """
        t = af_user_p.get_node("d8e0907594f8")

        self.assertEqual("d8:e0:90:75:94:f8",          t.mac_address) # From metadata
        self.assertEqual("$501$0-0-0000d8e-0907594f8", t.subject_id)  # From input
        self.assertIsNotNone(t._data)
        self.assertEqual(t.instance, conductor.PRODUCTION)

    @unittest.skip("given tag no longer valid.")
    def test_Construction_WithColons(self):
        """ Validates the Address Managment of the Tag Contructor. """
        t = af_user_p.get_node("d8:e0:90:75:94:f8")

        self.assertEqual("d8:e0:90:75:94:f8",          t.mac_address) # From metadata
        self.assertEqual("$501$0-0-0000d8e-0907594f8", t.subject_id)  # From input
        self.assertIsNotNone(t._data)
        self.assertEqual(t.instance, conductor.PRODUCTION)


class ZoneAirfinderTests(unittest.TestCase):
    """ Validates the Airfinder Zone class. """

    def __init__(self, test_name):
        super().__init__(test_name)

    def setUp(self):
        """ TODO """
        pass

    def tearDown(self):
        """ TODO """
        pass

    def test_TODO(self):
        """ TODO """
        pass


if __name__ == '__main__':

    coloredlogs.install(level=LOG_LEVEL)

    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    LOG.info("Validating Test Enviornment...")
    LOG.info("")

    # Validate library before Authentication.
    suite.addTests(loader.loadTestsFromTestCase(ConductorTests))
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)
    suite = unittest.TestSuite()

    LOG.info("Moving on to authenticated tests...")
    LOG.info("")

    LOG.info("▓▓  ▒▒  ░░  _     _       _      _          _")
    LOG.info("▓▓  ▒▒     | |   (_)_ __ | | __ | |    __ _| |__  ___")
    LOG.info("▓▓  ▒▒▒▒▒▒ | |   | | '_ \\| |/ / | |   / _` | '_ \\/ __|")
    LOG.info("▓▓         | |___| | | | |   <  | |__| (_| | |_) \\__ \\")
    LOG.info("▓▓▓▓▓▓▓▓▓▓ |_____|_|_| |_|_|\\_\\ |_____\\__,_|_.__/|___/")
    LOG.info("")

    # Move on to authenticated tests.
    psw = PASSWORD
    if not psw:
        psw = getpass('Conductor/Airfinder password for {}:'.format(ACCOUNT_EMAIL))

    # Create and authenticate conductor objects.
    c_account_p = conductor.ConductorAccount(ACCOUNT_EMAIL, conductor.PRODUCTION, psw)
    af_user_p = af.User(ACCOUNT_EMAIL, conductor.PRODUCTION, psw)

    c_account_h = conductor.ConductorAccount(ACCOUNT_EMAIL, conductor.HOSPITALITY, psw)
    af_user_h = af.User(ACCOUNT_EMAIL, conductor.HOSPITALITY, psw)

    del psw # Remove from memory

    ############################################################################
    # NOTE: When develop access is required, set USE_DEV to True at top.
    ############################################################################
    if USE_DEV:
        ACCOUNT_EMAIL = "dev@link-labs.com"
        psw = getpass('Conductor/Airfinder password for {}:'.format(ACCOUNT_EMAIL))

        c_account_d = conductor.ConductorAccount(ACCOUNT_EMAIL, conductor.DEVELOP, psw)
        af_user_d = af.User(ACCOUNT_EMAIL, conductor.DEVELOP, psw)
        del psw # Remove from memory
    ############################################################################

    # Load and run the Unit Tests.

    # ----------------------- Conductor ----------------------------------------
    suite.addTests(loader.loadTestsFromTestCase(ConductorAccountTests))
    suite.addTests(loader.loadTestsFromTestCase(ConductorAssetGroupTests))
    suite.addTests(loader.loadTestsFromTestCase(ConductorDeviceGatewayTests))
    suite.addTests(loader.loadTestsFromTestCase(ConductorDeviceModuleTests))
    suite.addTests(loader.loadTestsFromTestCase(ConductorDeviceLTEmModuleTests))
    suite.addTests(loader.loadTestsFromTestCase(ConductorEventCountTests))
    suite.addTests(loader.loadTestsFromTestCase(ConductorDownlinkMessageTests))
    suite.addTests(loader.loadTestsFromTestCase(ConductorUplinkMessageTests))
    suite.addTests(loader.loadTestsFromTestCase(ConductorSubjectTests))
    suite.addTests(loader.loadTestsFromTestCase(ConductorUplinkSubjectTests))
    suite.addTests(loader.loadTestsFromTestCase(ConductorDownlinkSubjectTests))
    suite.addTests(loader.loadTestsFromTestCase(ConductorSubscriptionTests))
    suite.addTests(loader.loadTestsFromTestCase(ConductorSubWebsocketTests))
    suite.addTests(loader.loadTestsFromTestCase(ConductorSubZMQTests))
    suite.addTests(loader.loadTestsFromTestCase(ConductorNetTokenTests))
    suite.addTests(loader.loadTestsFromTestCase(ConductorAppTokenTests))
    # -----------------------  Airfinder ---------------------------------------
    suite.addTests(loader.loadTestsFromTestCase(AirfinderUserTests))
    suite.addTests(loader.loadTestsFromTestCase(AccessPointAirfinderTests))
    suite.addTests(loader.loadTestsFromTestCase(AlertTagAirfinderTests))
    suite.addTests(loader.loadTestsFromTestCase(AreaAirfinderTests))
    suite.addTests(loader.loadTestsFromTestCase(LocationAirfinderTests))
    suite.addTests(loader.loadTestsFromTestCase(SiteAirfinderTests))
    suite.addTests(loader.loadTestsFromTestCase(SupertagAirfinderTests))
    suite.addTests(loader.loadTestsFromTestCase(TagAirfinderTests))
    suite.addTests(loader.loadTestsFromTestCase(ZoneAirfinderTests))

    unittest.TextTestRunner(verbosity=2).run(suite)

