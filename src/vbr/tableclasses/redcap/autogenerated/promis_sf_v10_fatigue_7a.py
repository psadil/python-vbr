"""Autogenerated 2021-10-12T11:54:28.832435 by redcap_classfiles.py
"""

from vbr.pgrest import *
from vbr.tableclasses import Constants
from vbr.pgrest.constraints import Signature

from ..rcconstants import REDCapConstants
from ..rcaptable import RcapTable

__all__ = ['RcapPromisSfV10Fatigue7A']

class RcapPromisSfV10Fatigue7A(RcapTable):
    """Promis Sf V10 Fatigue 7A
    """
    __redcap_form_name = 'promis_sf_v10_fatigue_7a'
    promis_sf_v10_fatigue_7a_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    promis_sf_v10_fatigue_7a_complete = Column(Integer, ForeignKey('status.status_id'))
    # Ignored multiline Field Name in Data Dictionary
    # Field Type: radio
    # Choices: 1, Never | 2, Rarely | 3, Sometimes | 4, Often | 5, Always
    fat7atiredscl = Column(Integer, nullable=True, comments=None)
    # Ignored multiline Field Name in Data Dictionary
    # Field Type: radio
    # Choices: 1, Never | 2, Rarely | 3, Sometimes | 4, Often | 5, Always
    fat7aexhaustionscl = Column(Integer, nullable=True, comments=None)
    # Ignored multiline Field Name in Data Dictionary
    # Field Type: radio
    # Choices: 1, Never | 2, Rarely | 3, Sometimes | 4, Often | 5, Always
    fat7anoenergytscl = Column(Integer, nullable=True, comments=None)
    # Ignored multiline Field Name in Data Dictionary
    # Field Type: radio
    # Choices: 1, Never | 2, Rarely | 3, Sometimes | 4, Often | 5, Always
    fat7aworklimitscl = Column(Integer, nullable=True, comments=None)
    # Ignored multiline Field Name in Data Dictionary
    # Field Type: radio
    # Choices: 1, Never | 2, Rarely | 3, Sometimes | 4, Often | 5, Always
    fat7athinkclearscl = Column(Integer, nullable=True, comments=None)
    # Ignored multiline Field Name in Data Dictionary
    # Field Type: radio
    # Choices: 1, Never | 2, Rarely | 3, Sometimes | 4, Often | 5, Always
    fat7abathscl = Column(Integer, nullable=True, comments=None)
    # Ignored multiline Field Name in Data Dictionary
    # Field Type: radio
    # Choices: 5, Never | 4, Rarely | 3, Sometimes | 2, Often | 1, Always
    fat7aexercisescl = Column(Integer, nullable=True, comments=None)