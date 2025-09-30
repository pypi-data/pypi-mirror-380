# -*- coding: utf-8 -*-
#
# File: testChangeItemOrderView.py
#
# GNU General Public License (GPL)
#

from Products.MeetingCPASLalouviere.tests.MeetingCPASLalouviereTestCase import MeetingCPASLalouviereTestCase
from Products.MeetingCommunes.tests.testChangeItemOrderView import testChangeItemOrderView as mctciov


class testChangeItemOrderView(MeetingCPASLalouviereTestCase, mctciov):
    '''Tests the ChangeItemOrderView class methods.'''


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(testChangeItemOrderView, prefix='test_pm_'))
    return suite
