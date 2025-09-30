# -*- coding: utf-8 -*-
#
# GNU General Public License (GPL)
#

from AccessControl import ClassSecurityInfo
from AccessControl.class_init import InitializeClass
from collections import OrderedDict
from collective.contact.plonegroup.utils import get_all_suffixes
from copy import deepcopy
from Products.MeetingCommunes.adapters import CustomMeetingConfig
from Products.MeetingCommunes.adapters import CustomToolPloneMeeting
from Products.MeetingCommunes.adapters import MeetingItemCommunesWorkflowActions
from Products.MeetingCommunes.interfaces import IMeetingItemCommunesWorkflowActions
from Products.PloneMeeting.config import AddAnnex
from Products.PloneMeeting.interfaces import IMeetingConfigCustom
from Products.PloneMeeting.interfaces import IToolPloneMeetingCustom
from Products.PloneMeeting.MeetingConfig import MeetingConfig
from Products.PloneMeeting.model import adaptations
from Products.PloneMeeting.model.adaptations import _addIsolatedState
from zope.i18n import translate
from zope.interface import implements


customWfAdaptations = list(deepcopy(MeetingConfig.wfAdaptations))
customWfAdaptations.append('propose_to_budget_reviewer')
# disable not compatible waiting advice wfa
# customWfAdaptations.remove('waiting_advices_adviser_may_validate')
# customWfAdaptations.remove('waiting_advices_from_before_last_val_level')
# customWfAdaptations.remove('waiting_advices_from_every_val_levels')
# customWfAdaptations.remove('waiting_advices_from_last_val_level')
# customWfAdaptations.remove('waiting_advices_given_advices_required_to_validate')
# customWfAdaptations.remove('waiting_advices_given_and_signed_advices_required_to_validate')
MeetingConfig.wfAdaptations = tuple(customWfAdaptations)

class LLMeetingConfig(CustomMeetingConfig):
    """Adapter that adapts a meetingConfig implementing IMeetingConfig to the
       interface IMeetingConfigCustom."""

    implements(IMeetingConfigCustom)
    security = ClassSecurityInfo()

    def _extraSearchesInfo(self, infos):
        """Add some specific searches."""
        super(LLMeetingConfig, self)._extraSearchesInfo(infos)
        cfg = self.getSelf()
        itemType = cfg.getItemTypeName()
        extra_infos = [
            (
                "searchproposedtobudgetreviewer",
                {
                    "subFolderId": "searches_items",
                    "active": True,
                    "query": [
                        {
                            "i": "portal_type",
                            "o": "plone.app.querystring.operation.selection.is",
                            "v": [itemType, ],
                        },
                        {
                            "i": "review_state",
                            "o": "plone.app.querystring.operation.selection.is",
                            "v": ["proposed_to_budget_reviewer"],
                        },
                    ],
                    "sort_on": u"modified",
                    "sort_reversed": True,
                    "showNumberOfItems": True,
                    "tal_condition": "",
                    "roles_bypassing_talcondition": ["Manager", ],
                },
            ),
            (
                "searchproposedton1",
                {
                    "subFolderId": "searches_items",
                    "active": True,
                    "query": [
                        {
                            "i": "portal_type",
                            "o": "plone.app.querystring.operation.selection.is",
                            "v": [itemType, ],
                        },
                        {
                            "i": "review_state",
                            "o": "plone.app.querystring.operation.selection.is",
                            "v": ["proposed_to_n1"],
                        },
                        {
                            'i': 'CompoundCriterion',
                            'o': 'plone.app.querystring.operation.compound.is',
                            'v': ['items-of-my-groups']
                        },
                    ],
                    "sort_on": u"modified",
                    "sort_reversed": True,
                    "showNumberOfItems": True,
                    "tal_condition": "python:tool.userIsAmong(['n1', 'n2', 'secretaire', 'reviewers'])",
                    "roles_bypassing_talcondition": ["Manager", ],
                },
            ),
            (
                "searchproposedton2",
                {
                    "subFolderId": "searches_items",
                    "active": True,
                    "query": [
                        {
                            "i": "portal_type",
                            "o": "plone.app.querystring.operation.selection.is",
                            "v": [itemType, ],
                        },
                        {
                            "i": "review_state",
                            "o": "plone.app.querystring.operation.selection.is",
                            "v": ["proposed_to_n2"],
                        },
                        {
                            'i': 'CompoundCriterion',
                            'o': 'plone.app.querystring.operation.compound.is',
                            'v': ['items-of-my-groups']
                        },
                    ],
                    "sort_on": u"modified",
                    "sort_reversed": True,
                    "showNumberOfItems": True,
                    "tal_condition": "python:tool.userIsAmong(['n2', 'secretaire', 'reviewers'])",
                    "roles_bypassing_talcondition": ["Manager", ],
                },
            ),
            (
                "searchproposedtosecretaire",
                {
                    "subFolderId": "searches_items",
                    "active": True,
                    "query": [
                        {
                            "i": "portal_type",
                            "o": "plone.app.querystring.operation.selection.is",
                            "v": [itemType, ],
                        },
                        {
                            "i": "review_state",
                            "o": "plone.app.querystring.operation.selection.is",
                            "v": ["proposed_to_secretaire"],
                        },
                        {
                            'i': 'CompoundCriterion',
                            'o': 'plone.app.querystring.operation.compound.is',
                            'v': ['items-of-my-groups']
                        },
                    ],
                    "sort_on": u"modified",
                    "sort_reversed": True,
                    "showNumberOfItems": True,
                    "tal_condition": "python:tool.userIsAmong(['secretaire', 'reviewers'])",
                    "roles_bypassing_talcondition": ["Manager", ],
                },
            ),
            (
                "searchproposedtopresident",
                {
                    "subFolderId": "searches_items",
                    "active": True,
                    "query": [
                        {
                            "i": "portal_type",
                            "o": "plone.app.querystring.operation.selection.is",
                            "v": [itemType, ],
                        },
                        {
                            "i": "review_state",
                            "o": "plone.app.querystring.operation.selection.is",
                            "v": ["proposed_to_president"],
                        },
                        {
                            'i': 'CompoundCriterion',
                            'o': 'plone.app.querystring.operation.compound.is',
                            'v': ['items-of-my-groups']
                        },
                    ],
                    "sort_on": u"modified",
                    "sort_reversed": True,
                    "showNumberOfItems": True,
                    "tal_condition": "python:tool.userIsAmong(['reviewers'])",
                    "roles_bypassing_talcondition": ["Manager", ],
                },
            ),
        ]
        infos.update(OrderedDict(extra_infos))
        return infos

    def _custom_reviewersFor(self):
        '''Manage reviewersFor Bourgmestre because as some 'creators' suffixes are
           used after reviewers levels, this break the _highestReviewerLevel and other
           related hierarchic level functionalities.'''
        reviewers = [
            ('reviewers', ['proposed_to_president',
                           'proposed_to_secretaire',
                           'proposed_to_n2',
                           'proposed_to_n1',
                           ]),
            ('secretaire',
             ['proposed_to_secretaire',
              'proposed_to_n2',
              'proposed_to_n1',]),
            ('n2',
             ['proposed_to_n2',
              'proposed_to_n1',]),
            ('n1',
             ['proposed_to_n1',]),
        ]
        return OrderedDict(reviewers)

    def get_item_custom_suffix_roles(self, item, item_state):
        '''See doc in interfaces.py.'''
        suffix_roles = {}
        if item_state == 'proposed_to_budget_reviewer':
            for suffix in get_all_suffixes(item.getProposingGroup()):
                suffix_roles[suffix] = ['Reader']
                if suffix == 'budgetimpactreviewers':
                    suffix_roles[suffix] += ['Contributor', 'Editor', 'Reviewer']

        return True, suffix_roles


class MLLCustomToolPloneMeeting(CustomToolPloneMeeting):
    '''Adapter that adapts portal_plonemeeting.'''

    implements(IToolPloneMeetingCustom)
    security = ClassSecurityInfo()

    def performCustomWFAdaptations(
            self, meetingConfig, wfAdaptation, logger, itemWorkflow, meetingWorkflow):
        ''' '''
        if wfAdaptation == 'propose_to_budget_reviewer':
            _addIsolatedState(
                new_state_id='proposed_to_budget_reviewer',
                origin_state_id='itemcreated',
                origin_transition_id='proposeToBudgetImpactReviewer',
                origin_transition_title=translate("proposeToBudgetImpactReviewer", "plone"),
                # origin_transition_icon=None,
                origin_transition_guard_expr_name='mayCorrect()',
                back_transition_guard_expr_name="mayCorrect()",
                back_transition_id='backTo_itemcreated_from_proposed_to_budget_reviewer',
                back_transition_title=translate("validateByBudgetImpactReviewer", "plone"),
                # back_transition_icon=None
                itemWorkflow=itemWorkflow)
            state = itemWorkflow.states["proposed_to_budget_reviewer"]
            state.permission_roles[AddAnnex] = state.permission_roles[AddAnnex] + ("Editor", )
            return True
        return False


class MeetingItemMLLWorkflowActions(MeetingItemCommunesWorkflowActions):
    '''Adapter that adapts a meeting item implementing IMeetingItem to the
       interface IMeetingItemCommunesWorkflowActions'''

    implements(IMeetingItemCommunesWorkflowActions)
    security = ClassSecurityInfo()

    def doProposeToBudgetImpactReviewer(self, stateChange):
        pass


InitializeClass(MLLCustomToolPloneMeeting)
InitializeClass(LLMeetingConfig)

LLO_WAITING_ADVICES_FROM_STATES = {
    '*':
    (
        {'from_states': ('itemcreated', ),
         'back_states': ('itemcreated', ),
         'perm_cloned_state': 'itemcreated',
         'use_custom_icon': False,
         # default to "validated", this avoid using the backToValidated title that
         # is translated to "Remove from meeting"
         'use_custom_back_transition_title_for': ("validated", ),
         # we can define some back transition id for some back_to_state
         # if not, a generated transition is used, here we could have for example
         # 'defined_back_transition_ids': {"validated": "validate"}
         'defined_back_transition_ids': {},
         # if () given, a custom transition icon is used for every back transitions
         'only_use_custom_back_transition_icon_for': ("validated", ),
         'use_custom_state_title': False,
         'use_custom_transition_title_for': {},
         'remove_modify_access': True,
         'adviser_may_validate': True,
         # must end with _waiting_advices
         'new_state_id': None,
         },
    ),
}
adaptations.WAITING_ADVICES_FROM_STATES.update(LLO_WAITING_ADVICES_FROM_STATES)
