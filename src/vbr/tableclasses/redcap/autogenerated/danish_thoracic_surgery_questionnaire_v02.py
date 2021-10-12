"""Autogenerated 2021-10-12T12:09:20.000685 by redcap_classfiles.py
"""

from vbr.pgrest import *
from vbr.tableclasses import Constants
from vbr.pgrest.constraints import Signature

from ..rcconstants import REDCapConstants
from ..rcaptable import RcapTable

__all__ = ['RcapDanishThoracicSurgeryQuestionnaireV02']


class RcapDanishThoracicSurgeryQuestionnaireV02(RcapTable):
    """Danish Thoracic Surgery Questionnaire V02
    """
    __redcap_form_name = 'danish_thoracic_surgery_questionnaire_v02'
    danish_thoracic_surgery_questionnaire_v02_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    danish_thoracic_surgery_questionnaire_v02_complete = Column(
        Integer, ForeignKey('status.status_id'))
    # Running
    # Field Type: radio
    # Choices: 96, I never do this activity | 4, I never do this activity due to pain | 3, Pain impairs me a lot | 2, Pain impairs me somewhat | 1, Pain impairs me a little | 0, Pain impairs me not at all
    dtsrunningscl = Column(Integer, nullable=True, comments=None)
    # Carrying groceries, heavy bags, or luggage.
    # Field Type: radio
    # Choices: 96, I never do this activity | 4, I never do this activity due to pain | 3, Pain impairs me a lot | 2, Pain impairs me somewhat | 1, Pain impairs me a little | 0, Pain impairs me not at all
    dtscarryingscl = Column(Integer, nullable=True, comments=None)
    # Washing hair, lifting the arm, moving shoulder or opening cup...
    # Field Type: radio
    # Choices: 96, I never do this activity | 4, I never do this activity due to pain | 3, Pain impairs me a lot | 2, Pain impairs me somewhat | 1, Pain impairs me a little | 0, Pain impairs me not at all
    dtswashingscl = Column(Integer, nullable=True, comments=None)
    # Cleaning (vacuum, washing floor).
    # Field Type: radio
    # Choices: 96, I never do this activity | 4, I never do this activity due to pain | 3, Pain impairs me a lot | 2, Pain impairs me somewhat | 1, Pain impairs me a little | 0, Pain impairs me not at all
    dtscleaningscl = Column(Integer, nullable=True, comments=None)
    # Walking 0.5 mile.
    # Field Type: radio
    # Choices: 96, I never do this activity | 4, I never do this activity due to pain | 3, Pain impairs me a lot | 2, Pain impairs me somewhat | 1, Pain impairs me a little | 0, Pain impairs me not at all
    dtswalkingscl = Column(Integer, nullable=True, comments=None)
    # Ascending stairs.
    # Field Type: radio
    # Choices: 96, I never do this activity | 4, I never do this activity due to pain | 3, Pain impairs me a lot | 2, Pain impairs me somewhat | 1, Pain impairs me a little | 0, Pain impairs me not at all
    dtsstairsscl = Column(Integer, nullable=True, comments=None)
    # Kneeling or stooping.
    # Field Type: radio
    # Choices: 96, I never do this activity | 4, I never do this activity due to pain | 3, Pain impairs me a lot | 2, Pain impairs me somewhat | 1, Pain impairs me a little | 0, Pain impairs me not at all
    dtskneelingscl = Column(Integer, nullable=True, comments=None)
    # Standing for 30 minutes.
    # Field Type: radio
    # Choices: 96, I never do this activity | 4, I never do this activity due to pain | 3, Pain impairs me a lot | 2, Pain impairs me somewhat | 1, Pain impairs me a little | 0, Pain impairs me not at all
    dtsstandingscl = Column(Integer, nullable=True, comments=None)
    # Getting out of bed.
    # Field Type: radio
    # Choices: 96, I never do this activity | 4, I never do this activity due to pain | 3, Pain impairs me a lot | 2, Pain impairs me somewhat | 1, Pain impairs me a little | 0, Pain impairs me not at all
    dtsoutofbedscl = Column(Integer, nullable=True, comments=None)
    # Swimming.
    # Field Type: radio
    # Choices: 96, I never do this activity | 4, I never do this activity due to pain | 3, Pain impairs me a lot | 2, Pain impairs me somewhat | 1, Pain impairs me a little | 0, Pain impairs me not at all
    dtsswimmingscl = Column(Integer, nullable=True, comments=None)
    # Cycling.
    # Field Type: radio
    # Choices: 96, I never do this activity | 4, I never do this activity due to pain | 3, Pain impairs me a lot | 2, Pain impairs me somewhat | 1, Pain impairs me a little | 0, Pain impairs me not at all
    dtscyclingscl = Column(Integer, nullable=True, comments=None)
    # Driving a car (driver).
    # Field Type: radio
    # Choices: 96, I never do this activity | 4, I never do this activity due to pain | 3, Pain impairs me a lot | 2, Pain impairs me somewhat | 1, Pain impairs me a little | 0, Pain impairs me not at all
    dtsdrivingscl = Column(Integer, nullable=True, comments=None)
    # Lying on the side of my operation.
    # Field Type: radio
    # Choices: 96, I never do this activity | 4, I never do this activity due to pain | 3, Pain impairs me a lot | 2, Pain impairs me somewhat | 1, Pain impairs me a little | 0, Pain impairs me not at all
    dtslyingopsidescl = Column(Integer, nullable=True, comments=None)
    # Coughing or taking a deep breath.
    # Field Type: radio
    # Choices: 96, I never do this activity | 4, I never do this activity due to pain | 3, Pain impairs me a lot | 2, Pain impairs me somewhat | 1, Pain impairs me a little | 0, Pain impairs me not at all
    dtscoughingscl = Column(Integer, nullable=True, comments=None)
    # Sitting in a chair for 30 minutes.
    # Field Type: radio
    # Choices: 96, I never do this activity | 4, I never do this activity due to pain | 3, Pain impairs me a lot | 2, Pain impairs me somewhat | 1, Pain impairs me a little | 0, Pain impairs me not at all
    dtssittingscl = Column(Integer, nullable=True, comments=None)
    # Concentrating on watching TV.
    # Field Type: radio
    # Choices: 96, I never do this activity | 4, I never do this activity due to pain | 3, Pain impairs me a lot | 2, Pain impairs me somewhat | 1, Pain impairs me a little | 0, Pain impairs me not at all
    dtswatchtvscl = Column(Integer, nullable=True, comments=None)
    # Sleeping.
    # Field Type: radio
    # Choices: 96, I never do this activity | 4, I never do this activity due to pain | 3, Pain impairs me a lot | 2, Pain impairs me somewhat | 1, Pain impairs me a little | 0, Pain impairs me not at all
    dtssleepscl = Column(Integer, nullable=True, comments=None)