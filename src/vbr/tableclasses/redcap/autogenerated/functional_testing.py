"""Autogenerated 2021-10-12T12:09:19.968949 by redcap_classfiles.py
"""

from vbr.pgrest import *
from vbr.tableclasses import Constants
from vbr.pgrest.constraints import Signature

from ..rcconstants import REDCapConstants
from ..rcaptable import RcapTable

__all__ = ['RcapFunctionalTesting']


class RcapFunctionalTesting(RcapTable):
    """Functional Testing
    """
    __redcap_form_name = 'functional_testing'
    functional_testing_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    functional_testing_complete = Column(Integer,
                                         ForeignKey('status.status_id'))
    # Initial Pain Rating
    # Field Type: dropdown
    # Choices: 0, 0 | 0.5, 0.5 | 1.0, 1.0 | 1.5, 1.5 | 2.0, 2.0 | 2.5, 2.5 | 3.0, 3.0 | 3.5, 3.5 | 4.0, 4.0 | 4.5, 4.5 | 5.0, 5.0 | 5.5, 5.5 | 6.0, 6.0 | 6.5, 6.5 | 7.0, 7.0 | 7.5, 7.5 | 8.0, 8.0 | 8.5, 8.5 | 9.0, 9.0 | 9.5, 9.5 | 10, 10
    walk10initialpainscl = Column(Numeric, nullable=True, comments=None)
    # Initial Pain Rating: (double entry)
    # Field Type: dropdown
    # Choices: 0, 0 | 0.5, 0.5 | 1.0, 1.0 | 1.5, 1.5 | 2.0, 2.0 | 2.5, 2.5 | 3.0, 3.0 | 3.5, 3.5 | 4.0, 4.0 | 4.5, 4.5 | 5.0, 5.0 | 5.5, 5.5 | 6.0, 6.0 | 6.5, 6.5 | 7.0, 7.0 | 7.5, 7.5 | 8.0, 8.0 | 8.5, 8.5 | 9.0, 9.0 | 9.5, 9.5 | 10, 10
    walk10initialpainscl1 = Column(Numeric, nullable=True, comments=None)
    # Final Pain Rating
    # Field Type: dropdown
    # Choices: 0, 0 | 0.5, 0.5 | 1.0, 1.0 | 1.5, 1.5 | 2.0, 2.0 | 2.5, 2.5 | 3.0, 3.0 | 3.5, 3.5 | 4.0, 4.0 | 4.5, 4.5 | 5.0, 5.0 | 5.5, 5.5 | 6.0, 6.0 | 6.5, 6.5 | 7.0, 7.0 | 7.5, 7.5 | 8.0, 8.0 | 8.5, 8.5 | 9.0, 9.0 | 9.5, 9.5 | 10, 10
    walk10finalpainscl = Column(Numeric, nullable=True, comments=None)
    # Final Pain Rating: (double entry)
    # Field Type: dropdown
    # Choices: 0, 0 | 0.5, 0.5 | 1.0, 1.0 | 1.5, 1.5 | 2.0, 2.0 | 2.5, 2.5 | 3.0, 3.0 | 3.5, 3.5 | 4.0, 4.0 | 4.5, 4.5 | 5.0, 5.0 | 5.5, 5.5 | 6.0, 6.0 | 6.5, 6.5 | 7.0, 7.0 | 7.5, 7.5 | 8.0, 8.0 | 8.5, 8.5 | 9.0, 9.0 | 9.5, 9.5 | 10, 10
    walk10finalpainscl1 = Column(Numeric, nullable=True, comments=None)
    # Time
    # Field Type: text
    # Choices: N/A
    walk10time = Column(String, nullable=True, comments=None)
    # Time: (double entry)
    # Field Type: text
    # Choices: N/A
    walk10time1 = Column(String, nullable=True, comments=None)
    # Test completed
    # Field Type: yesno
    # Choices: N/A
    walk10completeyn = Column(Boolean, nullable=True, comments=None)
    # If no, reason why?
    # Field Type: radio
    # Choices: 1, Did not attempt | 2, Initiated but unable to complete | 3, Other
    walk10incompletereason = Column(Integer, nullable=True, comments=None)
    # Any assistance used (personal and/or device)
    # Field Type: yesno
    # Choices: N/A
    walk10assistyn = Column(Boolean, nullable=True, comments=None)
    # Field Name was empty in Data Dictionary
    # Field Type: checkbox
    # Choices: 1, Cane (all types)
    walk10assist_cane = Column(Boolean, nullable=True, comments=None)
    # Field Name was empty in Data Dictionary
    # Field Type: checkbox
    # Choices: 1, Crutches (1 or 2, any gait pattern)
    walk10assist_crutch = Column(Boolean, nullable=True, comments=None)
    # Field Name was empty in Data Dictionary
    # Field Type: checkbox
    # Choices: 1, Walker (all types)
    walk10assist_walkder = Column(Boolean, nullable=True, comments=None)
    # Field Name was empty in Data Dictionary
    # Field Type: checkbox
    # Choices: 1, Personal assistance (any type of 'hands-on' assistance or support during task, even if only briefly or for balance)
    walk10assist_perssuppt = Column(Boolean, nullable=True, comments=None)
    # Field Name was empty in Data Dictionary
    # Field Type: checkbox
    # Choices: 1, Other
    walk10assist_other = Column(Boolean, nullable=True, comments=None)
    # Other, specify
    # Field Type: text
    # Choices: N/A
    walk10assist_othertxt = Column(String, nullable=True, comments=None)
    # Blood Pressure Screening
    # Field Type: radio
    # Choices: 1, Within study range (90/60 to 160/90 mmHg) | 2, Out of study range (< 90/60 OR > 160/90 mmHg)
    tstsbpscreen = Column(Integer, nullable=True, comments=None)
    # Initial Pain Rating
    # Field Type: dropdown
    # Choices: 0, 0 | 0.5, 0.5 | 1.0, 1.0 | 1.5, 1.5 | 2.0, 2.0 | 2.5, 2.5 | 3.0, 3.0 | 3.5, 3.5 | 4.0, 4.0 | 4.5, 4.5 | 5.0, 5.0 | 5.5, 5.5 | 6.0, 6.0 | 6.5, 6.5 | 7.0, 7.0 | 7.5, 7.5 | 8.0, 8.0 | 8.5, 8.5 | 9.0, 9.0 | 9.5, 9.5 | 10, 10
    tstsprepainscl = Column(Numeric, nullable=True, comments=None)
    # Initial Pain Rating: (double entry)
    # Field Type: dropdown
    # Choices: 0, 0 | 0.5, 0.5 | 1.0, 1.0 | 1.5, 1.5 | 2.0, 2.0 | 2.5, 2.5 | 3.0, 3.0 | 3.5, 3.5 | 4.0, 4.0 | 4.5, 4.5 | 5.0, 5.0 | 5.5, 5.5 | 6.0, 6.0 | 6.5, 6.5 | 7.0, 7.0 | 7.5, 7.5 | 8.0, 8.0 | 8.5, 8.5 | 9.0, 9.0 | 9.5, 9.5 | 10, 10
    tstsprepainscl1 = Column(Numeric, nullable=True, comments=None)
    # Final Pain Rating
    # Field Type: dropdown
    # Choices: 0, 0 | 0.5, 0.5 | 1.0, 1.0 | 1.5, 1.5 | 2.0, 2.0 | 2.5, 2.5 | 3.0, 3.0 | 3.5, 3.5 | 4.0, 4.0 | 4.5, 4.5 | 5.0, 5.0 | 5.5, 5.5 | 6.0, 6.0 | 6.5, 6.5 | 7.0, 7.0 | 7.5, 7.5 | 8.0, 8.0 | 8.5, 8.5 | 9.0, 9.0 | 9.5, 9.5 | 10, 10
    tstspostpainscl = Column(Numeric, nullable=True, comments=None)
    # Final Pain Rating: (double entry)
    # Field Type: dropdown
    # Choices: 0, 0 | 0.5, 0.5 | 1.0, 1.0 | 1.5, 1.5 | 2.0, 2.0 | 2.5, 2.5 | 3.0, 3.0 | 3.5, 3.5 | 4.0, 4.0 | 4.5, 4.5 | 5.0, 5.0 | 5.5, 5.5 | 6.0, 6.0 | 6.5, 6.5 | 7.0, 7.0 | 7.5, 7.5 | 8.0, 8.0 | 8.5, 8.5 | 9.0, 9.0 | 9.5, 9.5 | 10, 10
    tstspostpainscl1 = Column(Numeric, nullable=True, comments=None)
    # Time
    # Field Type: text
    # Choices: N/A
    tststime = Column(String, nullable=True, comments=None)
    # Time: (double entry)
    # Field Type: text
    # Choices: N/A
    tststime1 = Column(String, nullable=True, comments=None)
    # Test completed
    # Field Type: yesno
    # Choices: N/A
    tstscompleteyn = Column(Boolean, nullable=True, comments=None)
    # If no, reason why?
    # Field Type: radio
    # Choices: 0, Did not attempt: Participant declined or deemed unsafe | 1, Initiated, but subject unable to complete (indicate # of reps completed below) | 2, Other
    tstsnonreasonyn = Column(Integer, nullable=True, comments=None)
    # # of reps completed
    # Field Type: radio
    # Choices: 0, 0 | 1, 1 | 2, 2 | 3, 3 | 4, 4
    tstsnumbrepsyn = Column(Integer, nullable=True, comments=None)
    # Any assistance used (personal and/or chair)
    # Field Type: yesno
    # Choices: N/A
    tstsassistyn = Column(Boolean, nullable=True, comments=None)
    # Field Name was empty in Data Dictionary
    # Field Type: checkbox
    # Choices: 1, push-off from arms of chair or use of assistive device
    tstsassist_1 = Column(Boolean, nullable=True, comments=None)
    # Field Name was empty in Data Dictionary
    # Field Type: checkbox
    # Choices: 1, personal assistance (any type of 'hands-on' assistance or support during task, even if only briefly or for balance)
    tstsassist_2 = Column(Boolean, nullable=True, comments=None)
