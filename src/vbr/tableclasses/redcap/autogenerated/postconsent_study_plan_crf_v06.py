"""Autogenerated 2021-10-12T11:27:30.813793 by redcap_classfiles.py
"""

from vbr.pgrest import *
from vbr.tableclasses import Constants
from vbr.pgrest.constraints import Signature

from ..rcconstants import REDCapConstants
from ..rcaptable import RcapTable

__all__ = ['RcapPostconsentStudyPlanCrfV06']

class RcapPostconsentStudyPlanCrfV06(RcapTable):
    """Postconsent Study Plan Crf V06
    """
    __redcap_form_name = 'postconsent_study_plan_crf_v06'
    postconsent_study_plan_crf_v06_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    postconsent_study_plan_crf_v06_complete = Column(Integer, ForeignKey('status.status_id'))
    # Stated willingness to comply with all base study activities f...
    # Field Type: radio
    # Choices: 1, yes | 0, no
    sp_inclcomply = Column(Boolean, nullable=False, comments=None)
    # Between the ages of 18 to < 85 years.
    # Field Type: radio
    # Choices: 1, yes | 0, no
    sp_inclage1884 = Column(Boolean, nullable=False, comments=None)
    # Individuals scheduled to undergo thoracic surgery: Individual...
    # Field Type: radio
    # Choices: 1, yes | 0, no
    sp_inclsurg = Column(Boolean, nullable=False, comments=None)
    # Patient undergoing knee replacement for an inflammatory arthr...
    # Field Type: radio
    # Choices: 1, yes | 0, no
    sp_exclarthkneerep = Column(Boolean, nullable=False, comments=None)
    # Patient undergoing revision surgery with an infectious diagno...
    # Field Type: radio
    # Choices: 1, yes | 0, no
    sp_exclinfdxjoint = Column(Boolean, nullable=False, comments=None)
    # Patient undergoing:  bilateral knee replacements, planned sta...
    # Field Type: radio
    # Choices: 1, yes | 0, no
    sp_exclbilkneerep = Column(Boolean, nullable=False, comments=None)
    # Patient unable to provide informed consent; or unable to read...
    # Field Type: radio
    # Choices: 1, yes | 0, no
    sp_exclnoreadspkenglish = Column(Boolean, nullable=False, comments=None)
    # Confirm surgical incision site
    # Field Type: radio
    # Choices: 1, Right Knee | 2, Left Knee
    sp_surgsite = Column(Integer, nullable=False, comments=None)
    # MRI compatibility screening
    # Field Type: radio
    # Choices: 1, Pt has MR imaging contraindications, exclude from study | 2, MRI compatibility screen incomplete, need additional information from patient | 3, MRI screen complete, needs follow-up to determine compatibility by investigator | 4, Complete, cleared for imaging (no known contraindications)
    sp_mricompatscr = Column(Integer, nullable=False, comments=None)
    # Confirm Surgery Date
    # Field Type: text
    # Choices: N/A
    sp_surg_date = Column(String, nullable=False, comments=None)
    # V1 (Pre-Op) date
    # Field Type: text
    # Choices: N/A
    sp_v1_preop_date = Column(String, nullable=False, comments=None)
    # V1 (Pre-Op) time
    # Field Type: text
    # Choices: N/A
    sp_v1_preop_time = Column(String, nullable=False, comments=None)
    # V1 (Pre-Op) time AM/PM
    # Field Type: dropdown
    # Choices: AM, AM | PM, PM
    sp_v1_preop_time_ampm = Column(String, nullable=False, comments=None)
    # V2 (~6 week Follow-up) date
    # Field Type: text
    # Choices: N/A
    sp_v2_6wk_date = Column(String, nullable=False, comments=None)
    # V3 (~3 month Follow-up) date
    # Field Type: text
    # Choices: N/A
    sp_v3_3mo_date = Column(String, nullable=False, comments=None)
    # Please indicate how the patient would like to receive Pre-Vis...
    # Field Type: radio
    # Choices: 1, E-mail | 2, Push notification via app | 3, In-person (provide paper version) | 4, Phone (via coordinator)
    sp_previsit_survey_pref = Column(Integer, nullable=False, comments=None)
    # Please indicate how the patient would like to receive Daily T...
    # Field Type: radio
    # Choices: 1, E-mail | 2, Push notification via app | 3, In-person (provide paper version) | 4, Phone (via coordinator)
    sp_daily_survey_pref = Column(Integer, nullable=False, comments=None)
    # Send electronic surveys to this participant? If YES, electron...
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    sp_assess_remote = Column(Boolean, nullable=False, comments=None)
    # Completed informed consent
    # Field Type: radio
    # Choices: 1, yes | 0, no
    sp_inclinfconsdone = Column(Boolean, nullable=False, comments=None)
    # Patient has undergone prior thoracic surgery within 3-months.
    # Field Type: radio
    # Choices: 1, yes | 0, no
    sp_exclprevbilthorpro = Column(Boolean, nullable=False, comments=None)
    # Patient undergoing:  a bilateral thoracic procedure. another ...
    # Field Type: radio
    # Choices: 1, yes | 0, no
    sp_exclothmajorsurg = Column(Boolean, nullable=False, comments=None)
    # Planned surgical incision site
    # Field Type: radio
    # Choices: 1, Right chest | 2, Left chest
    sp_plansurgincissite = Column(Integer, nullable=False, comments=None)