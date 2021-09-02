"""Autogenerated 2021-09-02T14:32:59.860166 by redcap_classfiles.py
"""

from vbr.pgrest import *
from vbr.tableclasses import Constants
from vbr.pgrest.constraints import Signature

from ..rcconstants import REDCapConstants
from ..rcaptable import RcapTable

__all__ = ['RcapAdverseChildhoodExperienceQuestionnaireAce']


class RcapAdverseChildhoodExperienceQuestionnaireAce(RcapTable):
    """Adverse Childhood Experience Questionnaire Ace
    """
    __redcap_form_name = 'adverse_childhood_experience_questionnaire_ace'
    adverse_childhood_experience_questionnaire_ace_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    adverse_childhood_experience_questionnaire_ace_complete = Column(
        Integer, ForeignKey('status.status_id'))
    # Ignored multiline Field Name in Data Dictionary
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    aceadinhmhfroff18yrincode = Column(Boolean, nullable=False, comments=None)
    # Ignored multiline Field Name in Data Dictionary
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    aceadphyabsinfr18yrincode = Column(Boolean, nullable=False, comments=None)
    # Ignored multiline Field Name in Data Dictionary
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    acesxlabsfr18yrincode = Column(Boolean, nullable=False, comments=None)
    # Ignored multiline Field Name in Data Dictionary
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    acefllcemspoffr18yrincode = Column(Boolean, nullable=False, comments=None)
    # Ignored multiline Field Name in Data Dictionary
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    aceflngdhproffr18yrincode = Column(Boolean, nullable=False, comments=None)
    # Were your parents ever separated or divorced?
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    aceprevspdvfr18yrincode = Column(Boolean, nullable=False, comments=None)
    # Ignored multiline Field Name in Data Dictionary
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    acemtdmvlfr18yrincode = Column(Boolean, nullable=False, comments=None)
    # Did you live with anyone who was a problem drinker or alcohol...
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    acealdruslvfr18yrincode = Column(Boolean, nullable=False, comments=None)
    # Was a household member depressed or mentally ill or did a hou...
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    acedpmnischsmbfr18yincode = Column(Boolean, nullable=False, comments=None)
    # Did a household member go to prison?
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    acehsmmprfr18yrincode = Column(Boolean, nullable=False, comments=None)
