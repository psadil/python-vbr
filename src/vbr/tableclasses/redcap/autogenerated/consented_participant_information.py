"""Autogenerated 2021-10-12T12:09:19.859861 by redcap_classfiles.py
"""

from vbr.pgrest import *
from vbr.tableclasses import Constants
from vbr.pgrest.constraints import Signature

from ..rcconstants import REDCapConstants
from ..rcaptable import RcapTable

__all__ = ['RcapConsentedParticipantInformation']


class RcapConsentedParticipantInformation(RcapTable):
    """Consented Participant Information
    """
    __redcap_form_name = 'consented_participant_information'
    consented_participant_information_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    consented_participant_information_complete = Column(
        Integer, ForeignKey('status.status_id'))
    # Record ID
    # Field Type: text
    # Choices: N/A
    record_id = Column(String, nullable=True, comments=None)
    # GUID
    # Field Type: text
    # Choices: N/A
    guid = Column(GUID, nullable=True, comments=None)
    # Screening ID
    # Field Type: text
    # Choices: N/A
    screening_id = Column(String, nullable=True, comments=None)
    # First Name
    # Field Type: text
    # Choices: N/A
    first_name = Column(String, nullable=True, comments=None)
    # Last Name
    # Field Type: text
    # Choices: N/A
    last_name = Column(String, nullable=True, comments=None)
    # Email
    # Field Type: text
    # Choices: N/A
    patient_email = Column(String, nullable=True, comments=None)
    # Mobile Phone
    # Field Type: text
    # Choices: N/A
    mobile_phone_number = Column(String, nullable=True, comments=None)
    # Home Phone
    # Field Type: text
    # Choices: N/A
    home_phone_number = Column(String, nullable=True, comments=None)
    # Preferred Contact method
    # Field Type: radio
    # Choices: 2, E-mail | 1, Text | 0, Mobile/Home
    contact_method = Column(Integer, nullable=True, comments=None)
    # August 2021 TACC Server Downtime Notification: Send downtime ...
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    downtime202108 = Column(Boolean, nullable=True, comments=None)
    # August 2021 TACC Server Maintenance Completed Notification: S...
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    maintcomp202108 = Column(Boolean, nullable=True, comments=None)
