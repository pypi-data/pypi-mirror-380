# -*- coding: utf-8 -*-
#
# GNU General Public License (GPL)
#

__author__ = """Gauthier Bastien <gauthier@imio.be>"""
__docformat__ = 'plaintext'

# ------------------------------------------------------------------------------
from Products.PloneMeeting.interfaces import \
    IMeetingItemWorkflowConditions, IMeetingItemWorkflowActions, \
    IMeetingWorkflowActions, IMeetingWorkflowConditions


# ------------------------------------------------------------------------------
class IMeetingItemPBLalouviereWorkflowActions(IMeetingItemWorkflowActions):
    """This interface represents a meeting item as viewed by the specific
       item workflow that is defined in this MeetingCommunes product."""
    def doPresent():
        """
          Triggered while doing the 'present' transition
        """
    def doAcceptButModify():
        """
          Triggered while doing the 'accept_but_modify' transition
        """
    def doPreAccept():
        """
          Triggered while doing the 'pre_accept' transition
        """


class IMeetingItemPBLalouviereWorkflowConditions(IMeetingItemWorkflowConditions):
    """This interface represents a meeting item as viewed by the specific
       item workflow that is defined in this MeetingCommunes product."""
    def mayDecide():
        """
          Guard for the 'decide' transition
        """
    def isLateFor():
        """
          is the MeetingItem considered as late
        """
    def mayFreeze():
        """
          Guard for the 'freeze' transition
        """


class IMeetingPBLalouviereWorkflowActions(IMeetingWorkflowActions):
    """This interface represents a meeting as viewed by the specific meeting
       workflow that is defined in this MeetingCommunes product."""
    def doClose():
        """
          Triggered while doing the 'close' transition
        """
    def doDecide():
        """
          Triggered while doing the 'decide' transition
        """
    def doFreeze():
        """
          Triggered while doing the 'freeze' transition
        """
    def doBackToCreated():
        """
          Triggered while doing the 'doBackToCreated' transition
        """


class IMeetingPBLalouviereWorkflowConditions(IMeetingWorkflowConditions):
    """This interface represents a meeting as viewed by the specific meeting
       workflow that is defined in this MeetingCommunes product."""
    def mayFreeze():
        """
          Guard for the 'freeze' transition
        """
    def mayClose():
        """
          Guard for the 'close' transitions
        """
    def mayDecide():
        """
          Guard for the 'decide' transition
        """
    def mayChangeItemsOrder():
        """
          Check if the user may or not changes the order of the items on the meeting
        """
# ------------------------------------------------------------------------------
