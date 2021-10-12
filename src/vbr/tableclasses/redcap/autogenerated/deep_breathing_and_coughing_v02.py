"""Autogenerated 2021-10-12T11:27:30.975161 by redcap_classfiles.py
"""

from vbr.pgrest import *
from vbr.tableclasses import Constants
from vbr.pgrest.constraints import Signature

from ..rcconstants import REDCapConstants
from ..rcaptable import RcapTable

__all__ = ['RcapDeepBreathingAndCoughingV02']

class RcapDeepBreathingAndCoughingV02(RcapTable):
    """Deep Breathing And Coughing V02
    """
    __redcap_form_name = 'deep_breathing_and_coughing_v02'
    deep_breathing_and_coughing_v02_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    deep_breathing_and_coughing_v02_complete = Column(Integer, ForeignKey('status.status_id'))
    # Ignored multiline Field Name in Data Dictionary
    # Field Type: radio
    # Choices: 0, 0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10
    dbcchestpainrestscl = Column(Integer, nullable=False, comments=None)
    # Ignored multiline Field Name in Data Dictionary
    # Field Type: radio
    # Choices: 0, 0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10
    dbcworstpainbreathscl = Column(Integer, nullable=False, comments=None)
    # Ignored multiline Field Name in Data Dictionary
    # Field Type: radio
    # Choices: 0, 0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10
    dbcworstpaincoughscl = Column(Integer, nullable=False, comments=None)