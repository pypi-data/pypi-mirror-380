# -*- coding: utf-8 -*-
#
# File: testPortlets.py
#
# GNU General Public License (GPL)
#

from Products.MeetingCPASLalouviere.tests.MeetingCPASLalouviereTestCase import MeetingCPASLalouviereTestCase
from Products.MeetingCommunes.tests.testPortlets import testPortlets as mctp


class testPortlets(MeetingCPASLalouviereTestCase, mctp):
    '''Tests the portlets methods.'''


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(testPortlets, prefix='test_pm_'))
    return suite
