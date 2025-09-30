# -*- coding: utf-8 -*-
#
# File: testToolPloneMeeting.py
#
# GNU General Public License (GPL)
#

from Products.MeetingCPASLalouviere.tests.MeetingCPASLalouviereTestCase import MeetingCPASLalouviereTestCase
from Products.MeetingCommunes.tests.testToolPloneMeeting import testToolPloneMeeting as mctt


class testToolPloneMeeting(MeetingCPASLalouviereTestCase, mctt):
    '''Tests the ToolPloneMeeting class methods.'''


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(testToolPloneMeeting, prefix='test_pm_'))
    return suite
