"""Autogenerated 2021-11-02T15:33:22.659954 by redcap_classfiles.py
"""

from vbr.pgrest import *
from vbr.tableclasses import Constants
from vbr.pgrest.constraints import Signature

from ..rcconstants import REDCapConstants
from ..rcaptable import RcapTable

__all__ = ['RcapGeneralSensorySensitivityV02Gss8']


class RcapGeneralSensorySensitivityV02Gss8(RcapTable):
    """General Sensory Sensitivity V02 Gss8
    """
    __redcap_form_name = 'general_sensory_sensitivity_v02_gss8'
    general_sensory_sensitivity_v02_gss8_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    general_sensory_sensitivity_v02_gss8_complete = Column(
        Integer, ForeignKey('status.status_id'))
    # Sensitivity to bright lights
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    gss8photophobia = Column(Boolean, nullable=True, comments=None)
    # Sensitivity to sounds
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    gss8phonophobia = Column(Boolean, nullable=True, comments=None)
    # Sensitivity to odors (e.g., perfumes, detergents, gasoline)
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    gss8odorsensitiv = Column(Boolean, nullable=True, comments=None)
    # Sensitivity to certain flavors (e.g., sour, sweet, bitter)
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    gss8flavorsensitiv = Column(Boolean, nullable=True, comments=None)
    # Sensitivity to touch or physical contact (e.g., certain fabri...
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    gss8touchsensitiv = Column(Boolean, nullable=True, comments=None)
    # Problems with balance
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    gss8balance = Column(Boolean, nullable=True, comments=None)
    # Problems with nausea
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    gss8nausea = Column(Boolean, nullable=True, comments=None)
    # Problems with rapid heart rate
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    gss8rapidhr = Column(Boolean, nullable=True, comments=None)
