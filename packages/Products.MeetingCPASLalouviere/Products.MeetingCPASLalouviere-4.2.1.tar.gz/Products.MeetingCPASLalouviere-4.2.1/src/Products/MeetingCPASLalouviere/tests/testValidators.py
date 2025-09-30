# -*- coding: utf-8 -*-
#
# File: testValidators.py
#
# GNU General Public License (GPL)
#

from Products.MeetingCPASLalouviere.tests.MeetingCPASLalouviereTestCase import MeetingCPASLalouviereTestCase
from Products.MeetingCommunes.tests.testValidators import testValidators as mctv


class testValidators(MeetingCPASLalouviereTestCase, mctv):
    """
        Tests the validators.
    """


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(testValidators, prefix='test_pm_'))
    return suite
