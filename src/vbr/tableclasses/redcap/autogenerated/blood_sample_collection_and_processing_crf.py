"""Autogenerated 2021-10-12T12:09:19.983343 by redcap_classfiles.py
"""

from vbr.pgrest import *
from vbr.tableclasses import Constants
from vbr.pgrest.constraints import Signature

from ..rcconstants import REDCapConstants
from ..rcaptable import RcapTable

__all__ = ['RcapBloodSampleCollectionAndProcessingCrf']


class RcapBloodSampleCollectionAndProcessingCrf(RcapTable):
    """Blood Sample Collection And Processing Crf
    """
    __redcap_form_name = 'blood_sample_collection_and_processing_crf'
    blood_sample_collection_and_processing_crf_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    blood_sample_collection_and_processing_crf_complete = Column(
        Integer, ForeignKey('status.status_id'))
    # Number of hours since last drank anything except water
    # Field Type: text
    # Choices: N/A
    bscp_hrs_since_water = Column(String, nullable=True, comments=None)
    # Number of hours since last food intake
    # Field Type: text
    # Choices: N/A
    bscp_hrs_since_food = Column(String, nullable=True, comments=None)
    # How would you describe the amount of caffeine you had in the ...
    # Field Type: radio
    # Choices: 1, The usual amount | 2, Less than the usual amount | 3, More than the usual amount | 4, Not applicable
    bscp_caff_cups_amt = Column(Integer, nullable=True, comments=None)
    # b. Number of hours since last had caffeine/stimulants
    # Field Type: text
    # Choices: N/A
    bscp_hrs_since_cafstim = Column(String, nullable=True, comments=None)
    # Have you received any vaccine in the last two weeks?
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    bscp_any_vacc = Column(Boolean, nullable=True, comments=None)
    # Did you verify patients name and date of birth
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    bscp_verify_pt = Column(Boolean, nullable=True, comments=None)
    # 6a. Research assistant initials
    # Field Type: text
    # Choices: N/A
    bscp_ra_initials = Column(String, nullable=True, comments=None)
    # Initials of person or lab performing phlebotomy
    # Field Type: text
    # Choices: N/A
    bscp_phleb_by_init = Column(String, nullable=True, comments=None)
    # Blood sample
    # Field Type: checkbox
    # Choices: 1, Not obtained
    bscp_sample_obtained = Column(Boolean, nullable=True, comments=None)
    # 7.a. Reason not obtained
    # Field Type: radio
    # Choices: 1, Unable to obtain blood (>2 sticks) | 2, Patient request to stop (pain, paresthesia) | 3, Patient condition (lightheaded, fainted) | 4, Hematoma after needle stick (bruising, ecchymosis) | 5, Other
    bscp_no_sample_reason = Column(Integer, nullable=True, comments=None)
    # Sample kit barcode
    # Field Type: text
    # Choices: N/A
    bscp_samplekit_brcd = Column(String, nullable=True, comments=None)
    # Time completed blood draw
    # Field Type: text
    # Choices: N/A
    bscp_time_blood_draw = Column(String, nullable=True, comments=None)
    # Lavender #1
    # Field Type: checkbox
    # Choices: 1, Not obtained
    bscp_lav1_not_obt = Column(Boolean, nullable=True, comments=None)
    # Lavender #1 barcode
    # Field Type: text
    # Choices: N/A
    bscp_lav1_brcd = Column(String, nullable=True, comments=None)
    # PAXgene DNA tube
    # Field Type: checkbox
    # Choices: 1, Not obtained
    bscp_paxg_not_obt = Column(Boolean, nullable=True, comments=None)
    # PAXgene DNA tube barcode
    # Field Type: text
    # Choices: N/A
    bscp_paxg_brcd = Column(String, nullable=True, comments=None)
    # Time completed centrifuging
    # Field Type: text
    # Choices: N/A
    bscp_time_centrifuge = Column(String, nullable=True, comments=None)
    # Lavender #1 barcode
    # Field Type: text
    # Choices: N/A
    bscp_lav1_centrif_brcd = Column(String, nullable=True, comments=None)
    # Plug cap tube barcode
    # Field Type: text
    # Choices: N/A
    bscp_plugcap_centrif_brcd = Column(String, nullable=True, comments=None)
    # Assess the degree of hemolysis of the plasma (Lavender tube) ...
    # Field Type: radio
    # Choices: 0, 0 | .25, 0.25 | .5, 0.5 | 1, 1 | 2, 2 | 4, 4 | 8, 8
    bscp_deg_of_hemolysis = Column(Numeric, nullable=True, comments=None)
    # Plasma aliquot (2") freezer box barcode
    # Field Type: text
    # Choices: N/A
    bscp_aliquot_box_brcd = Column(String, nullable=True, comments=None)
    # Buffy coat (blue microfuge) tube
    # Field Type: checkbox
    # Choices: 1, N/A
    bscp_buffycoat_na = Column(Boolean, nullable=True, comments=None)
    # Buffy coat (blue microfuge) tube barcode
    # Field Type: text
    # Choices: N/A
    bscp_buffycoat_brcd = Column(String, nullable=True, comments=None)
    # Plasma aliquot barcode
    # Field Type: text
    # Choices: N/A
    bscp_plasma_brcd = Column(String, nullable=True, comments=None)
    # Number of aliquots
    # Field Type: dropdown
    # Choices: 0, 0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8
    bscp_aliq_cnt = Column(Integer, nullable=True, comments=None)
    # PAXgene DNA (3") freezer box
    # Field Type: text
    # Choices: N/A
    bscp_paxg_box_brcd = Column(String, nullable=True, comments=None)
    # PAXgene DNA tube
    # Field Type: checkbox
    # Choices: 1, N/A
    bscp_paxg_aliq_na = Column(Boolean, nullable=True, comments=None)
    # PAXgene DNA tube barcode
    # Field Type: text
    # Choices: N/A
    bscp_paxg_aliq_brcd = Column(String, nullable=True, comments=None)
    # Time placed in freezer
    # Field Type: text
    # Choices: N/A
    bscp_aliquot_freezer_time = Column(String, nullable=True, comments=None)
    # Did a protocol deviation occur
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    bscp_protocol_dev = Column(Boolean, nullable=True, comments=None)
    # Reason for protocol deviation
    # Field Type: radio
    # Choices: 1, Unable to obtain blood sample -technical reason | 2, Unable to obtain blood sample -patient related | 3, Sample handling/processing error
    bscp_protocol_dev_reason = Column(Integer, nullable=True, comments=None)
    # Initials of person that processed blood
    # Field Type: text
    # Choices: N/A
    bscp_procby_initials = Column(String, nullable=True, comments=None)
