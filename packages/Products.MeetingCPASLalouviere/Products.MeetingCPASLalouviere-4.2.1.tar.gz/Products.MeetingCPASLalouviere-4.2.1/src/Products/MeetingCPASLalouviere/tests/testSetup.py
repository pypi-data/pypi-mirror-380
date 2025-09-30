# -*- coding: utf-8 -*-
#
# File: testSetup.py
#
# GNU General Public License (GPL)
#

from Products.MeetingCPASLalouviere.tests.MeetingCPASLalouviereTestCase import MeetingCPASLalouviereTestCase
from Products.MeetingCommunes.tests.testSetup import testSetup as mcts


class testSetup(MeetingCPASLalouviereTestCase, mcts):
    '''Tests the setup, especially registered profiles.'''


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(testSetup, prefix='test_pm_'))
    return suite
