# -*- coding: utf-8 -*-
#
# File: testUtils.py
#
# GNU General Public License (GPL)
#


from Products.MeetingCPASLalouviere.tests.MeetingCPASLalouviereTestCase import MeetingCPASLalouviereTestCase
from Products.MeetingCommunes.tests.testUtils import testUtils as mctu


class testUtils(MeetingCPASLalouviereTestCase, mctu):
    ''' '''

    def _default_permission_mail_recipents(self):
        return [u'M. Budget Impact Editor <budgetimpacteditor@plonemeeting.org>',
                u'M. PMCreator One <pmcreator1@plonemeeting.org>',
                u'M. PMCreator One bee <pmcreator1b@plonemeeting.org>',
                u'M. PMObserver One <pmobserver1@plonemeeting.org>',
                u'M. PMReviewer Level One <pmreviewerlevel1@plonemeeting.org>',
                u'M. PMReviewer Level Two <pmreviewerlevel2@plonemeeting.org>',
                u'M. PMReviewer One <pmreviewer1@plonemeeting.org>',
                u'M. Power Observer1 <powerobserver1@plonemeeting.org>',
                u'Site administrator <siteadmin@plonemeeting.org>',
                u'pmN1 <pmn1@plonemeeting.org>',
                u'pmN2 <pmn2@plonemeeting.org>',
                u'pmPresident <pmpresident@plonemeeting.org>',
                u'pmSecretaire <pmsecretaire@plonemeeting.org>']

    def _modify_permission_mail_recipents(self):
        return [u'M. PMCreator One <pmcreator1@plonemeeting.org>',
                u'M. PMCreator One bee <pmcreator1b@plonemeeting.org>',
                u'M. PMReviewer Level One <pmreviewerlevel1@plonemeeting.org>',
                u'M. PMReviewer Level Two <pmreviewerlevel2@plonemeeting.org>',
                u'M. PMReviewer One <pmreviewer1@plonemeeting.org>',
                u'Site administrator <siteadmin@plonemeeting.org>',
                u'pmN1 <pmn1@plonemeeting.org>',
                u'pmN2 <pmn2@plonemeeting.org>',
                u'pmPresident <pmpresident@plonemeeting.org>',
                u'pmSecretaire <pmsecretaire@plonemeeting.org>']


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(testUtils, prefix='test_pm_'))
    return suite
