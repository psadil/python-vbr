"""Autogenerated 2021-11-02T15:33:22.736054 by redcap_classfiles.py
"""

from vbr.pgrest import *
from vbr.tableclasses import Constants
from vbr.pgrest.constraints import Signature

from ..rcconstants import REDCapConstants
from ..rcaptable import RcapTable

__all__ = ['RcapImagingItemsV01']


class RcapImagingItemsV01(RcapTable):
    """Imaging Items V01
    """
    __redcap_form_name = 'imaging_items_v01'
    imaging_items_v01_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    imaging_items_v01_complete = Column(Integer,
                                        ForeignKey('status.status_id'))
    # Currently, how sad are you?
    # Field Type: radio
    # Choices: 0, Not at all | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, Extremely
    img_sad = Column(Integer, nullable=True, comments=None)
    # Currently, how energetic are you?
    # Field Type: radio
    # Choices: 0, Not at all | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, Extremely
    img_energetic = Column(Integer, nullable=True, comments=None)
    # Currently, how angry are you?
    # Field Type: radio
    # Choices: 0, Not at all | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, Extremely
    img_angry = Column(Integer, nullable=True, comments=None)
    # Currently, how hopeful are you?
    # Field Type: radio
    # Choices: 0, Not at all | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, Extremely
    img_hopeful = Column(Integer, nullable=True, comments=None)
    # Currently, how nervous are you?
    # Field Type: radio
    # Choices: 0, Not at all | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, Extremely
    img_nervous = Column(Integer, nullable=True, comments=None)
    # Currently, how happy are you?
    # Field Type: radio
    # Choices: 0, Not at all | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, Extremely
    img_happy = Column(Integer, nullable=True, comments=None)
    # Rate the overall QUALITY of your SLEEP in the past 24 hours.
    # Field Type: radio
    # Choices: 0, Extremely poor | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, Extremely good
    img_qual_sleep_24 = Column(Integer, nullable=True, comments=None)
    # Field Name was empty in Data Dictionary
    # Field Type: text
    # Choices: N/A
    imgpainanatsiteareatxt = Column(String, nullable=True, comments=None)
