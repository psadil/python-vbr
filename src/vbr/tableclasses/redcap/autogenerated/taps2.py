"""Autogenerated 2021-11-02T15:33:22.621532 by redcap_classfiles.py
"""

from vbr.pgrest import *
from vbr.tableclasses import Constants
from vbr.pgrest.constraints import Signature

from ..rcconstants import REDCapConstants
from ..rcaptable import RcapTable

__all__ = ['RcapTaps2']


class RcapTaps2(RcapTable):
    """Taps2
    """
    __redcap_form_name = 'taps2'
    taps2_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    taps2_complete = Column(Integer, ForeignKey('status.status_id'))
    # In the PAST 3 MONTHS, did you smoke a cigarette containing to...
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    taps2tobaccoyn = Column(Boolean, nullable=True, comments=None)
    # a. In the PAST 3 MONTHS, did you usually smoke more than 10 c...
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    taps2tobaccogr10yn = Column(Boolean, nullable=True, comments=None)
    # a.1. How many cigarettes per day on average?
    # Field Type: text
    # Choices: N/A
    taps2tobaccogr10ycnt = Column(String, nullable=True, comments=None)
    # b. In the PAST 3 MONTHS, did you usually smoke within 30 minu...
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    taps2tobaccowakingyn = Column(Boolean, nullable=True, comments=None)
    # In the PAST 3 MONTHS, did you have a drink containing alcohol?
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    taps2alcoholyn = Column(Boolean, nullable=True, comments=None)
    # Ignored multiline Field Name in Data Dictionary
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    taps2alcoholfem4yn = Column(Boolean, nullable=True, comments=None)
    # Ignored multiline Field Name in Data Dictionary
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    taps2alcoholmale5yn = Column(Boolean, nullable=True, comments=None)
    # c In the PAST 3 MONTHS, have you tried and failed to control,...
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    taps2alcoholfailyn = Column(Boolean, nullable=True, comments=None)
    # d In the PAST 3 MONTHS, has anyone expressed concern about yo...
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    taps2alcoholconcernyn = Column(Boolean, nullable=True, comments=None)
    # 3 In the PAST 3 MONTHS, did you use marijuana (hash, weed)?
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    taps2mjuseyn = Column(Boolean, nullable=True, comments=None)
    # a. In the PAST 3 MONTHS, have you had a strong desire or urge...
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    taps2mjweeklyyn = Column(Boolean, nullable=True, comments=None)
    # b. In the PAST 3 MONTHS, has anyone expressed concern about y...
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    taps2mjconcernyn = Column(Boolean, nullable=True, comments=None)
    # In the PAST 3 MONTHS, did you use cocaine, crack, or methamph...
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    taps2stimulantyn = Column(Boolean, nullable=True, comments=None)
    # a. In the PAST 3 MONTHS, did you use cocaine, crack, or metha...
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    taps2stimulantweeklyyn = Column(Boolean, nullable=True, comments=None)
    # b. In the PAST 3 MONTHS, has anyone expressed concern about y...
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    taps2stimulntconcernyn = Column(Boolean, nullable=True, comments=None)
    # In the PAST 3 MONTHS, did you use heroin?
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    taps2heroinyn = Column(Boolean, nullable=True, comments=None)
    # a. In the PAST 3 MONTHS, have you tried and failed to control...
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    taps2heroinfailyn = Column(Boolean, nullable=True, comments=None)
    # b. In the PAST 3 MONTHS, has anyone expressed concern about y...
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    taps2heroinconcernyn = Column(Boolean, nullable=True, comments=None)
    # In the PAST 3 MONTHS, did you use a prescription opiate pain ...
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    taps2rxopiateyn = Column(Boolean, nullable=True, comments=None)
    # a. In the PAST 3 MONTHS, have you tried and failed to control...
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    taps2rxopiatefailyn = Column(Boolean, nullable=True, comments=None)
    # b. In the PAST 3 MONTHS, has anyone expressed concern about y...
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    taps2rxopiateconcernyn = Column(Boolean, nullable=True, comments=None)
    # In the PAST 3 MONTHS, did you use a medication for anxiety or...
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    taps2anxietyslpmedyn = Column(Boolean, nullable=True, comments=None)
    # a. In the PAST 3 MONTHS, have you had a strong desire or urge...
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    taps2anxietyslpweeklyyn = Column(Boolean, nullable=True, comments=None)
    # b. In the PAST 3 MONTHS, has anyone expressed concern about y...
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    taps2anxietyslpconcyn = Column(Boolean, nullable=True, comments=None)
    # In the PAST 3 MONTHS, did you use a medication for ADHD (for ...
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    taps2adhdmedyn = Column(Boolean, nullable=True, comments=None)
    # a. In the PAST 3 MONTHS, did you use a medication for ADHD (f...
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    taps2adhdmedweeklyyn = Column(Boolean, nullable=True, comments=None)
    # b. In the PAST 3 MONTHS, has anyone expressed concern about y...
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    taps2adhdmedconcernyn = Column(Boolean, nullable=True, comments=None)
    # In the PAST 3 MONTHS, did you use any other illegal or recrea...
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    taps2otherdrugsyn = Column(Boolean, nullable=True, comments=None)
    # a. In the PAST 3 MONTHS, what were the other drug(s) you used?
    # Field Type: text
    # Choices: N/A
    taps2otherdrugstxt = Column(String, nullable=True, comments=None)
