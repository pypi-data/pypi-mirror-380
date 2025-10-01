""" This module wraps the Conductor API. """

# Single source of truth for version: read from packaged file
from pkgutil import get_data

try:
    __version__ = get_data(__name__, "_version.txt").decode("utf-8").strip()
except Exception:  # pragma: no cover - very defensive; ensures import won't fail
    __version__ = "0.0.0"

# Backwards compatibility constant
CONDUCTOR_LIBRARY_VERSION = __version__

PRODUCTION = 'conductor.link-labs'
HOSPITALITY = 'hospitality.airfinder'
UAT = 'hospitality-uat.airfinder'
TEST = 'test.airfinder'
DEVELOP = 'dev.link-labs'

INSTANCES = [PRODUCTION, DEVELOP, HOSPITALITY, UAT, TEST]

import conductor
from conductor.account import ConductorAccount
from conductor.asset_group import AssetGroup
from conductor.devices.gateway import Gateway
from conductor.devices.module import Module
from conductor.event_count import EventCount
from conductor.subject import ConductorSubject, UplinkSubject, DownlinkSubject
from conductor.subscriptions import ZeroMQSubscription
from conductor.tokens import AppToken, NetToken
import conductor.util
