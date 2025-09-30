# -*- coding: utf-8 -*-
#
# GNU General Public License (GPL)
#

from Products.MeetingCPASLalouviere.testing import MLL_TESTING_PROFILE_FUNCTIONAL
from Products.MeetingCPASLalouviere.tests.helpers import MeetingCPASLalouviereTestingHelpers
from Products.MeetingCommunes.tests.MeetingCommunesTestCase import MeetingCommunesTestCase


class MeetingCPASLalouviereTestCase(
    MeetingCommunesTestCase, MeetingCPASLalouviereTestingHelpers
):
    """Base class for defining MeetingCPASLalouviere test cases."""

    layer = MLL_TESTING_PROFILE_FUNCTIONAL
    cfg1_id = 'meeting-config-bp'
    cfg2_id = 'meeting-config-cas'

    def setUp(self):
        super(MeetingCPASLalouviereTestCase, self).setUp()
