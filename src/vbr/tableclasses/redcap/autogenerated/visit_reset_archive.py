"""Autogenerated 2024-09-18T10:32:28.945301 by redcap_classfiles.py
"""

from ....pgrest import *
from ...constants import Constants
from ..rcconstants import REDCapConstants

from ..rcaptable import RcapTable

__all__ = ['RcapVisitResetArchive']


class RcapVisitResetArchive(RcapTable):
    """Visit Reset Archive
    """
    __redcap_form_name = 'visit_reset_archive'
    visit_reset_archive_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    visit_reset_archive_complete = Column(Integer,
                                          ForeignKey('status.status_id'))
    # Date of archive and event reset
    # Field Type: text
    # Choices: N/A
    reset_date = Column(String, nullable=True, comments=None)
