# -*- coding: utf-8 -*-
#
# File: testFaceted.py
#
# GNU General Public License (GPL)
#

from Products.MeetingCPASLalouviere.tests.MeetingCPASLalouviereTestCase import MeetingCPASLalouviereTestCase
from Products.MeetingCommunes.tests.testFaceted import testFaceted as mctf


class testFaceted(MeetingCPASLalouviereTestCase, mctf):
    '''Tests the faceted navigation.'''


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(testFaceted, prefix='test_pm_'))
    return suite
