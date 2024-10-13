"""Autogenerated 2024-09-18T10:32:28.862890 by redcap_classfiles.py
"""

from ....pgrest import *
from ...constants import Constants
from ..rcconstants import REDCapConstants

from ..rcaptable import RcapTable

__all__ = ['RcapPainDetectQuestionnairePdq']


class RcapPainDetectQuestionnairePdq(RcapTable):
    """Pain Detect Questionnaire Pdq
    """
    __redcap_form_name = 'pain_detect_questionnaire_pdq'
    pain_detect_questionnaire_pdq_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    pain_detect_questionnaire_pdq_complete = Column(
        Integer, ForeignKey('status.status_id'))
    # Assessment Date
    # Field Type: text
    # Choices: N/A
    pdqassessdate = Column(String, nullable=True, comments=None)
    # a. Do you suffer from a <span style="text-decoration: underli...
    # Field Type: radio
    # Choices: 0, Never | 1, Hardly Noticed | 2, Slightly | 3, Moderately | 4, Strongly | 5, Very Strongly
    pdburnsens = Column(Integer, nullable=True, comments=None)
    # b. Do you have a <span style="text-decoration: underline;">ti...
    # Field Type: radio
    # Choices: 0, Never | 1, Hardly Noticed | 2, Slightly | 3, Moderately | 4, Strongly | 5, Very Strongly
    pdtinglsens = Column(Integer, nullable=True, comments=None)
    # c. Is <span style="text-decoration: underline;">light touchin...
    # Field Type: radio
    # Choices: 0, Never | 1, Hardly Noticed | 2, Slightly | 3, Moderately | 4, Strongly | 5, Very Strongly
    pdlttouch = Column(Integer, nullable=True, comments=None)
    # d. Do you have <span style="text-decoration: underline;">sudd...
    # Field Type: radio
    # Choices: 0, Never | 1, Hardly Noticed | 2, Slightly | 3, Moderately | 4, Strongly | 5, Very Strongly
    pdsudpanatt = Column(Integer, nullable=True, comments=None)
    # e. Is <span style="text-decoration: underline;">cold or heat<...
    # Field Type: radio
    # Choices: 0, Never | 1, Hardly Noticed | 2, Slightly | 3, Moderately | 4, Strongly | 5, Very Strongly
    pdbathwtr = Column(Integer, nullable=True, comments=None)
    # f. Do you suffer from a sensation of <span style="text-decora...
    # Field Type: radio
    # Choices: 0, Never | 1, Hardly Noticed | 2, Slightly | 3, Moderately | 4, Strongly | 5, Very Strongly
    pdnumb = Column(Integer, nullable=True, comments=None)
    # g. Does <span style="text-decoration: underline;">slight pres...
    # Field Type: radio
    # Choices: 0, Never | 1, Hardly Noticed | 2, Slightly | 3, Moderately | 4, Strongly | 5, Very Strongly
    pdslightpress = Column(Integer, nullable=True, comments=None)
    # 2. Please mark the box next to the one picture that best desc...
    # Field Type: radio
    # Choices: 1, <img src="\images\paindetect_slight_fluct_2.png"> Persistent pain with <span style="text-decoration: underline;">slight fluctuations</span> | 2, <img src="\images\paindetect_pp_wpainattacks_2.png"> Persistent pain with <span style="text-decoration: underline;">pain attacks</span> | 3, <img src="\images\paindetect_nopp_wpainattacks_2.png"> <span style="text-decoration: underline;">Pain attacks</span> without pain between them | 4, <img src="\images\paindetect_pain_wpainattacks_2.png"> <span style="text-decoration: underline;">Pain attacks</span> with pain between them
    pdqpaincourse = Column(Integer, nullable=True, comments=None)
    # Does your pain ever radiate to other regions of your body?
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    pdradiateregions = Column(Boolean, nullable=True, comments=None)
