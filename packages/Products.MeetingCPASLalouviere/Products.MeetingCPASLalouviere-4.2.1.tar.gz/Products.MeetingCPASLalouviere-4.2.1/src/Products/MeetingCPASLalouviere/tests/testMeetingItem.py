# -*- coding: utf-8 -*-
#
# File: testMeetingItem.py
#
# GNU General Public License (GPL)
#

from Products.MeetingCPASLalouviere.tests.MeetingCPASLalouviereTestCase import MeetingCPASLalouviereTestCase
from Products.MeetingCommunes.tests.testMeetingItem import testMeetingItem as mctmi


class testMeetingItem(MeetingCPASLalouviereTestCase, mctmi):
    """
        Tests the MeetingItem class methods.
    """

    def _users_to_remove_for_mailling_list(self):
        return ["pmBudgetReviewer1", "pmBudgetReviewer2", "pmSecretaire", "pmN1", "pmN2", "pmPresident"]


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    # launch only tests prefixed by 'test_mc_' to avoid launching the tests coming from pmtmi
    suite.addTest(makeSuite(testMeetingItem, prefix='test_pm_'))
    return suite
