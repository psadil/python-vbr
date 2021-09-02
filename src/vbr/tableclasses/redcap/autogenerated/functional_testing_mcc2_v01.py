"""Autogenerated 2021-09-02T14:32:59.963064 by redcap_classfiles.py
"""

from vbr.pgrest import *
from vbr.tableclasses import Constants
from vbr.pgrest.constraints import Signature

from ..rcconstants import REDCapConstants
from ..rcaptable import RcapTable

__all__ = ['RcapFunctionalTestingMcc2V01']


class RcapFunctionalTestingMcc2V01(RcapTable):
    """Functional Testing Mcc2 V01
    """
    __redcap_form_name = 'functional_testing_mcc2_v01'
    functional_testing_mcc2_v01_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    functional_testing_mcc2_v01_complete = Column(
        Integer, ForeignKey('status.status_id'))
    # 1a. Initial Pain Rating
    # Field Type: dropdown
    # Choices: 0, 0 | 0.5, 0.5 | 1.0, 1.0 | 1.5, 1.5 | 2.0, 2.0 | 2.5, 2.5 | 3.0, 3.0 | 3.5, 3.5 | 4.0, 4.0 | 4.5, 4.5 | 5.0, 5.0 | 5.5, 5.5 | 6.0, 6.0 | 6.5, 6.5 | 7.0, 7.0 | 7.5, 7.5 | 8.0, 8.0 | 8.5, 8.5 | 9.0, 9.0 | 9.5, 9.5 | 10, 10
    ftdbcdeepbrthinitscl = Column(Numeric, nullable=False, comments=None)
    # 1b. Initial Pain Rating: (double entry)
    # Field Type: dropdown
    # Choices: 0, 0 | 0.5, 0.5 | 1.0, 1.0 | 1.5, 1.5 | 2.0, 2.0 | 2.5, 2.5 | 3.0, 3.0 | 3.5, 3.5 | 4.0, 4.0 | 4.5, 4.5 | 5.0, 5.0 | 5.5, 5.5 | 6.0, 6.0 | 6.5, 6.5 | 7.0, 7.0 | 7.5, 7.5 | 8.0, 8.0 | 8.5, 8.5 | 9.0, 9.0 | 9.5, 9.5 | 10, 10
    ftdbcdeepbrthinitscl2 = Column(Numeric, nullable=False, comments=None)
    # 2a. Final Pain Rating
    # Field Type: dropdown
    # Choices: 0, 0 | 0.5, 0.5 | 1.0, 1.0 | 1.5, 1.5 | 2.0, 2.0 | 2.5, 2.5 | 3.0, 3.0 | 3.5, 3.5 | 4.0, 4.0 | 4.5, 4.5 | 5.0, 5.0 | 5.5, 5.5 | 6.0, 6.0 | 6.5, 6.5 | 7.0, 7.0 | 7.5, 7.5 | 8.0, 8.0 | 8.5, 8.5 | 9.0, 9.0 | 9.5, 9.5 | 10, 10
    ftdbcdeepbrthfinalscl = Column(Numeric, nullable=False, comments=None)
    # 2b. Final Pain Rating: (double entry)
    # Field Type: dropdown
    # Choices: 0, 0 | 0.5, 0.5 | 1.0, 1.0 | 1.5, 1.5 | 2.0, 2.0 | 2.5, 2.5 | 3.0, 3.0 | 3.5, 3.5 | 4.0, 4.0 | 4.5, 4.5 | 5.0, 5.0 | 5.5, 5.5 | 6.0, 6.0 | 6.5, 6.5 | 7.0, 7.0 | 7.5, 7.5 | 8.0, 8.0 | 8.5, 8.5 | 9.0, 9.0 | 9.5, 9.5 | 10, 10
    ftdbcdeepbrthfinalscl2 = Column(Numeric, nullable=False, comments=None)
    # 3a. Final Pain Rating
    # Field Type: dropdown
    # Choices: 0, 0 | 0.5, 0.5 | 1.0, 1.0 | 1.5, 1.5 | 2.0, 2.0 | 2.5, 2.5 | 3.0, 3.0 | 3.5, 3.5 | 4.0, 4.0 | 4.5, 4.5 | 5.0, 5.0 | 5.5, 5.5 | 6.0, 6.0 | 6.5, 6.5 | 7.0, 7.0 | 7.5, 7.5 | 8.0, 8.0 | 8.5, 8.5 | 9.0, 9.0 | 9.5, 9.5 | 10, 10
    ftdbccoughfinalscl = Column(Numeric, nullable=False, comments=None)
    # 3b. Final Pain Rating: (double entry)
    # Field Type: dropdown
    # Choices: 0, 0 | 0.5, 0.5 | 1.0, 1.0 | 1.5, 1.5 | 2.0, 2.0 | 2.5, 2.5 | 3.0, 3.0 | 3.5, 3.5 | 4.0, 4.0 | 4.5, 4.5 | 5.0, 5.0 | 5.5, 5.5 | 6.0, 6.0 | 6.5, 6.5 | 7.0, 7.0 | 7.5, 7.5 | 8.0, 8.0 | 8.5, 8.5 | 9.0, 9.0 | 9.5, 9.5 | 10, 10
    ftdbccoughfinalscl2 = Column(Numeric, nullable=False, comments=None)
    # Test completed
    # Field Type: yesno
    # Choices: N/A
    ftdbctestcmpltyn = Column(Boolean, nullable=False, comments=None)
    # If no, choose one of the following
    # Field Type: radio
    # Choices: 1, Did not attempt either deep breathing or coughing tasks | 2, Did not complete deep breathing portion only | 3, Did not complete coughing portion only
    ftdbctestcmpltno = Column(Integer, nullable=False, comments=None)
