# -*- coding: utf-8 -*-
#
# GNU General Public License (GPL)
#

from collective.contact.plonegroup.utils import get_all_suffixes
from collective.contact.plonegroup.utils import select_org_for_function
from imio.helpers.content import get_vocab_values
from Products.CMFCore.permissions import DeleteObjects
from Products.CMFCore.permissions import ModifyPortalContent
from Products.CMFCore.permissions import View
from Products.MeetingCommunes.tests.testWFAdaptations import testWFAdaptations as mctwfa
from Products.MeetingCPASLalouviere.tests.MeetingCPASLalouviereTestCase import MeetingCPASLalouviereTestCase
from Products.PloneMeeting.config import WriteBudgetInfos
from Products.PloneMeeting.config import WriteInternalNotes
from zope.event import notify
from zope.i18n import translate
from zope.lifecycleevent import ObjectModifiedEvent


class testWFAdaptations(MeetingCPASLalouviereTestCase, mctwfa):
    '''Tests various aspects of votes management.'''

    def _default_waiting_advices_state(self):
        return 'itemcreated__or__proposed_to_n1__or__proposed_to_n2__or__' \
            'proposed_to_secretaire__or__proposed_to_president_waiting_advices'

    def _waiting_advices_adviser_send_back_states(self):
        return ['backTo_itemcreated_from_waiting_advices',
                'backTo_proposed_to_n1_from_waiting_advices',
                'backTo_proposed_to_n2_from_waiting_advices',
                'backTo_proposed_to_president_from_waiting_advices',
                'backTo_proposed_to_secretaire_from_waiting_advices',
                'backTo_validated_from_waiting_advices']

    def _item_validation_shortcuts_inactive(self):
        '''Test when 'item_validation_shortcuts' is inactive.'''
        self._enable_mc_Prevalidation(self.meetingConfig)
        super(testWFAdaptations, self)._item_validation_shortcuts_inactive()

    def test_pm_WFA_availableWFAdaptations(self):
        '''Test what are the available wfAdaptations.
           This way, if we add a wfAdaptations, the test will 'break' until it is adapted...'''
        self.assertEqual(
            sorted(get_vocab_values(self.meetingConfig, 'WorkflowAdaptations')),
            ['accepted_but_modified',
             'accepted_out_of_meeting',
             'accepted_out_of_meeting_and_duplicated',
             'accepted_out_of_meeting_emergency',
             'accepted_out_of_meeting_emergency_and_duplicated',
             'decide_item_when_back_to_meeting_from_returned_to_proposing_group',
             'delayed',
             'hide_decisions_when_under_writing',
             'hide_decisions_when_under_writing__po__powerobservers',
             'hide_decisions_when_under_writing__po__restrictedpowerobservers',
             'hide_decisions_when_under_writing_check_returned_to_proposing_group',
             'item_validation_no_validate_shortcuts',
             'item_validation_shortcuts',
             'itemdecided',
             'mark_not_applicable',
             'meeting_remove_global_access',
             'meetingmanager_correct_closed_meeting',
             'no_decide',
             'no_freeze',
             'no_publication',
             'only_creator_may_delete',
             'postpone_next_meeting',
             'postpone_next_meeting_keep_internal_number',
             'postpone_next_meeting_transfer_annex_scan_id',
             'pre_accepted',
             'presented_item_back_to_itemcreated',
             'presented_item_back_to_proposed_to_n1',
             'presented_item_back_to_proposed_to_n2',
             'presented_item_back_to_proposed_to_president',
             'presented_item_back_to_proposed_to_secretaire',
             'propose_to_budget_reviewer',
             'refused',
             'removed',
             'removed_and_duplicated',
             'return_to_proposing_group',
             'return_to_proposing_group_with_all_validations',
             'return_to_proposing_group_with_last_validation',
             'reviewers_take_back_validated_item',
             'transfered',
             'transfered_and_duplicated',
             'waiting_advices',
             'waiting_advices_adviser_may_validate',
             'waiting_advices_adviser_send_back',
             'waiting_advices_from_before_last_val_level',
             'waiting_advices_from_every_val_levels',
             'waiting_advices_from_last_val_level',
             'waiting_advices_given_advices_required_to_validate',
             'waiting_advices_given_and_signed_advices_required_to_validate',
             'waiting_advices_proposing_group_send_back'])

    def _process_transition_for_correcting_item(self, item, all):
        if all:
            self.changeUser('pmCreator1')
            self.do(item, 'goTo_returned_to_proposing_group_proposed_to_n1')
            self.failIf(self.hasPermission(ModifyPortalContent, item))
            self.changeUser('pmN1')
            self.do(item, 'goTo_returned_to_proposing_group_proposed_to_n2')
            self.failIf(self.hasPermission(ModifyPortalContent, item))
            self.changeUser('pmN2')
            self.do(item, 'goTo_returned_to_proposing_group_proposed_to_secretaire')

        self.changeUser('pmManager')
        self.do(item, 'goTo_returned_to_proposing_group_proposed_to_president')

    def _get_developers_reviewers_groups(self):
        return [self.developers_n1,
                self.developers_n2,
                self.developers_secretaire,
                self.developers_reviewers]

    def test_pm_WFA_pre_validation(self):
        pass

    def test_pm_WFA_waiting_advices_with_prevalidation(self):
        pass

    def test_pm_WFA_waiting_advices_from_every_val_levels(self):
        pass

    def test_pm_Validate_workflowAdaptations_removed_waiting_advices(self):
        pass

    def test_pm_WFA_waiting_advices_from_last_and_before_last_val_level(self):
        pass

    def test_pm_WFA_waiting_advices_may_edit(self):
        pass

    def test_pm_WFA_waiting_advices_unknown_state(self):
        pass

    def test_pm_WFA_waiting_advices_adviser_send_back(self):
        pass

    def test_pm_WFA_waiting_advices_given_advices_required_to_validate(self):
        pass

    def _waiting_advices_active(self):
        '''Tests while 'waiting_advices' wfAdaptation is active.'''
        cfg = self.meetingConfig
        # by default it is linked to the 'proposed' state
        itemWF = cfg.getItemWorkflow(True)
        waiting_state_name = '{0}_waiting_advices'.format(
            self._stateMappingFor('proposed_first_level'))
        waiting_transition_name = 'wait_advices_from_{0}'.format(
            self._stateMappingFor('proposed_first_level'))
        self.assertIn(waiting_state_name, itemWF.states.keys())

        # the budget impact editors functionnality still works even if 'remove_modify_access': True
        cfg.setItemBudgetInfosStates((waiting_state_name,))
        # check that the internalNotes functionnality works as well
        # enable field internalNotes
        self._enableField('internalNotes', reload=True)
        # make internal notes editable by copyGroups
        self._activate_config('itemInternalNotesEditableBy',
                              'reader_copy_groups')
        cfg.setItemCopyGroupsStates((waiting_state_name,))

        # right, create an item and set it to 'waiting_advices'
        self.changeUser('pmCreator1')
        item = self.create('MeetingItem', copyGroups=[self.vendors_reviewers])
        self.proposeItem(item, first_level=True)
        # 'pmCreator1' is not able to set item to 'waiting_advices'
        self.assertFalse(self.transitions(item))
        # 'pmReviewer1' may do it but by default is not able to edit it
        self.changeUser('pmManager')
        # no advice asked so a No() instance is returned for now
        self.assertNotIn(waiting_transition_name, self.transitions(item))
        advice_required_to_ask_advices = translate('advice_required_to_ask_advices',
                                                   domain='PloneMeeting',
                                                   context=self.request)
        proposed_state = self._stateMappingFor('proposed_first_level')
        self.assertEqual(
            translate(item.wfConditions().mayWait_advices(
                proposed_state, waiting_state_name).msg, context=self.request),
            advice_required_to_ask_advices)
        # ask an advice so transition is available
        item.setOptionalAdvisers((self.vendors_uid,))
        item._update_after_edit()
        # still not available because no advice may be asked in state waiting_state_name
        self.assertNotIn(waiting_state_name, self.vendors.item_advice_states)
        self.assertNotIn(waiting_transition_name, self.transitions(item))

        # do things work
        self.vendors.item_advice_states = ("{0}__state__{1}".format(
            cfg.getId(), waiting_state_name),)
        # clean MeetingConfig.getItemAdviceStatesForOrg
        notify(ObjectModifiedEvent(self.vendors))

        self.assertIn(waiting_transition_name, self.transitions(item))
        self._setItemToWaitingAdvices(item, waiting_transition_name)
        self.assertEqual(item.query_state(), waiting_state_name)
        self.assertFalse(self.hasPermission(ModifyPortalContent, item))
        self.assertFalse(self.hasPermission(DeleteObjects, item))

        # pmCreator1 may view but not edit
        self.changeUser('pmCreator1')
        self.assertTrue(self.hasPermission(View, item))
        self.assertFalse(self.hasPermission(ModifyPortalContent, item))
        self.assertFalse(self.hasPermission(DeleteObjects, item))
        self.assertFalse(self.transitions(item))

        # budget impact editors access are correct even when 'remove_modify_access': True
        self.changeUser('budgetimpacteditor')
        self.assertTrue(self.hasPermission(WriteBudgetInfos, item))

        # check internalNotes editable by copyGroups
        self.changeUser('pmReviewer2')
        self.assertTrue(self.hasPermission(View, item))
        self.assertTrue(self.hasPermission(WriteInternalNotes, item))
        # change text and add image
        text = '<p>Internal note with image <img src="%s"/>.</p>' % self.external_image1
        item.setInternalNotes(text)
        item.at_post_edit_script()

        # right come back to 'proposed'
        self.changeUser('pmReviewerLevel1')
        self.do(item, 'backTo_%s_from_waiting_advices' % self._stateMappingFor('proposed_first_level'))
        self.assertEqual(item.query_state(), self._stateMappingFor('proposed_first_level'))

    def test_pm_WFA_waiting_advices_from_before_last_val_level(self):
        '''Set item to waiting_advices from before last validation level.'''
        cfg = self.meetingConfig
        # ease override by subproducts
        if not self._check_wfa_available(['waiting_advices',
                                          'waiting_advices_proposing_group_send_back',
                                          'waiting_advices_from_before_last_val_level']):
            return

        cfg.setItemAdviceStates((self._default_waiting_advices_state(), ))
        self._activate_wfas(('waiting_advices',
                             'waiting_advices_proposing_group_send_back',
                             'waiting_advices_from_before_last_val_level'))

        # make itemcreated last validation level for vendors and proposed for developers
        # select developers for suffix reviewers
        select_org_for_function(self.developers_uid, 'reviewers')
        self.assertFalse('reviewers' in get_all_suffixes(self.vendors_uid))

        # developers
        self.changeUser('pmCreator1')
        item = self.create('MeetingItem', optionalAdvisers=(self.vendors_uid, ))
        self.assertListEqual(self.transitions(item), ['proposeToN1'])
        self.proposeItem(item)
        self.changeUser('pmReviewer1')
        # itemcreated, advice is askable as before last validation level
        self.assertFalse([tr for tr in self.transitions(item)
                         if tr.startswith('wait_advices_from_')])
        # ask advice
        # only sendable back to last level
        self.do(item, 'backToProposedToSecretaire')
        self.do(item, 'wait_advices_from_proposed_to_secretaire')
        self.changeUser('pmSecretaire')
        self.assertEqual(self.transitions(item), ['backTo_proposed_to_secretaire_from_waiting_advices'])

    def test_pm_WFA_waiting_advices_from_last_val_level(self):
        '''Set item to waiting_advices from last validation level.'''
        cfg = self.meetingConfig
        # ease override by subproducts
        if not self._check_wfa_available(['waiting_advices',
                                          'waiting_advices_proposing_group_send_back',
                                          'waiting_advices_from_last_val_level']):
            return

        self._activate_wfas(('waiting_advices',
                             'waiting_advices_proposing_group_send_back',
                             'waiting_advices_from_last_val_level'))
        cfg.setItemAdviceStates(self._default_waiting_advices_state())

        # make itemcreated last validation level for vendors and proposed for developers
        # select developers for suffix reviewers
        select_org_for_function(self.developers_uid, 'reviewers')
        self.assertFalse('reviewers' in get_all_suffixes(self.vendors_uid))

        # developers
        self.changeUser('pmCreator1')
        item = self.create('MeetingItem', optionalAdvisers=(self.vendors_uid, ))
        # itemcreated, advice not askable
        self.assertFalse([tr for tr in self.transitions(item)
                          if tr.startswith('wait_advices_from_')])
        self.proposeItem(item)
        self.changeUser('pmReviewer1')
        self.assertTrue([tr for tr in self.transitions(item)
                         if tr.startswith('wait_advices_from_')])
        # ask advice
        # only sendable back to last level
        self.do(item, self._wait_advice_from_proposed_state_transition())
        self.assertEqual(self.transitions(item), [self._wait_advice_from_proposed_state_back_transition()])

    def _no_validation_active(self):
        '''Test when no item validation levels are enabled,
           item is created in state "validated".'''
        item = self.create('MeetingItem')
        self.assertEqual(item.query_state(), 'validated')
        # disabled item validation levels does not have access
        # adding decision annex may be adapted
        creators_roles = ['Reader']
        if item.may_add_annex_decision(self.meetingConfig, item.query_state()):
            creators_roles.append('Contributor')
        self.assertEqual(item.__ac_local_roles__[self.developers_creators], creators_roles)
        self.assertEqual(item.__ac_local_roles__[self.developers_n1], creators_roles)
        self.assertEqual(item.__ac_local_roles__[self.developers_n2], creators_roles)
        self.assertEqual(item.__ac_local_roles__[self.developers_secretaire], creators_roles)
        self.assertEqual(item.__ac_local_roles__[self.developers_reviewers], creators_roles)
        self.assertEqual(item.__ac_local_roles__[self.developers_observers], ['Reader'])

    def test_pm_Validate_workflowAdaptations_removed_return_to_proposing_group_with_all_validations(self):
        pass

    def test_pm_WFA_return_to_proposing_group_with_all_validations(self):
        pass


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(testWFAdaptations, prefix='test_pm_'))
    return suite
