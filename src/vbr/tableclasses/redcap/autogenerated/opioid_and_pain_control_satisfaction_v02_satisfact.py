"""Autogenerated 2021-09-02T14:32:59.883477 by redcap_classfiles.py
"""

from vbr.pgrest import *
from vbr.tableclasses import Constants
from vbr.pgrest.constraints import Signature

from ..rcconstants import REDCapConstants
from ..rcaptable import RcapTable

__all__ = ['RcapOpioidAndPainControlSatisfactionV02Satisfact']


class RcapOpioidAndPainControlSatisfactionV02Satisfact(RcapTable):
    """Opioid And Pain Control Satisfaction V02 Satisfact
    """
    __redcap_form_name = 'opioid_and_pain_control_satisfaction_v02_satisfact'
    opioid_and_pain_control_satisfaction_v02_satisfact_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    opioid_and_pain_control_satisfaction_v02_satisfact_complete = Column(
        Integer, ForeignKey('status.status_id'))
    # a. How would you rate the amount of opioid pain medication yo...
    # Field Type: radio
    # Choices: 1, much less than I needed | 2, less than I needed | 3, about right | 4, more than I needed | 5, much more than I needed | 6, not applicable, I was not prescribed opioids after hospital discharge
    opcsamountrxscl = Column(Integer, nullable=False, comments=None)
    # b. How would you rate your satisfaction with pain control aft...
    # Field Type: radio
    # Choices: 0, 0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10
    opcspainctrlsatisscl = Column(Integer, nullable=False, comments=None)
    # c. How would you describe your pain control since surgery?
    # Field Type: radio
    # Choices: 1, Much worse than you expected | 2, Worse than you expected | 3, About what you expected | 4, Better than you expected | 5, Much better than you expected
    opcspainctrlscl = Column(Integer, nullable=False, comments=None)
