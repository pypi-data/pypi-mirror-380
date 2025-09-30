# -*- coding: utf-8 -*-
#
# File: testMeetingGroup.py
#
# GNU General Public License (GPL)
#

from Products.MeetingCPASLalouviere.tests.MeetingCPASLalouviereTestCase import MeetingCPASLalouviereTestCase
from Products.PloneMeeting.tests.testContacts import testContacts as pmtc


class testContacts(pmtc, MeetingCPASLalouviereTestCase):
    '''Tests the contacts related methods.'''


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(testContacts, prefix='test_pm_'))
    return suite