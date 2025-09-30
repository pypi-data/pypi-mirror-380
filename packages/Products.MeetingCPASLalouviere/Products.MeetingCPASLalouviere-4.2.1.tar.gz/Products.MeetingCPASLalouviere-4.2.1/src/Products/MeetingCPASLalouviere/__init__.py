# -*- coding: utf-8 -*-
#
# GNU General Public License (GPL)
#

__author__ = """Andre Nuyens <andre.nuyens@imio.be>"""
__docformat__ = 'plaintext'


# There are three ways to inject custom code here:
#
#   - To set global configuration variables, create a file AppConfig.py.
#       This will be imported in config.py, which in turn is imported in
#       each generated class and in this file.
#   - To perform custom initialisation after types have been registered,
#       use the protected code section at the bottom of initialize().

import logging
logger = logging.getLogger('MeetingCPASLalouviere')
logger.debug('Installing Product')

from Products.CMFCore import DirectoryView
from config import product_globals

DirectoryView.registerDirectory('skins', product_globals)


import adapters  # noqa


def initialize(context):
    """initialize product (called by zope)"""
