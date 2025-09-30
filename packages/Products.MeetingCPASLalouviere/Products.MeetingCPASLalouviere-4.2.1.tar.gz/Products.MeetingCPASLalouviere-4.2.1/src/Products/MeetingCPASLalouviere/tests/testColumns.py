# -*- coding: utf-8 -*-
#
# File: testColumns.py
#
# GNU General Public License (GPL)
#

from Products.MeetingCPASLalouviere.tests.MeetingCPASLalouviereTestCase import MeetingCPASLalouviereTestCase
from Products.MeetingCommunes.tests.testColumns import testColumns as mctc


class testColumns(MeetingCPASLalouviereTestCase, mctc):
    ''' '''


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(testColumns, prefix='test_pm_'))
    return suite
