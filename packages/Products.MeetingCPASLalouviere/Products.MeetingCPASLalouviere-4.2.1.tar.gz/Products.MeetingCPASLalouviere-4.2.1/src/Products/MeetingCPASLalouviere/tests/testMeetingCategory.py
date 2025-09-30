# -*- coding: utf-8 -*-
#
# File: testMeetingCategory.py
#
# GNU General Public License (GPL)
#

from Products.MeetingCPASLalouviere.tests.MeetingCPASLalouviereTestCase import MeetingCPASLalouviereTestCase
from Products.MeetingCommunes.tests.testMeetingCategory import testMeetingCategory as mctmc


class testMeetingCategory(MeetingCPASLalouviereTestCase, mctmc):
    '''Tests the MeetingCategory class methods.'''


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(testMeetingCategory, prefix='test_pm_'))
    return suite
