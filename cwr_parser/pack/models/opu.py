from dataclasses import dataclass
from typing import List

from ..models.base import EntityBase
from ..models.error import Error


@dataclass
class Opu(EntityBase):
    publisher_sequence_number: str
    interested_party_number: str
    international_standard_agreement_code: str
    pr_affiliation_society_number: str
    pr_ownership_share: float
    mr_affiliation_society_number: str
    mr_ownership_share: float
    sr_society_number: str
    sr_ownership_share: float
    publisher_ipi_name_number: str
    publisher_ipi_base_number: str
    publisher_name: str
    publisher_type: str
    publisher_unknown_indicator: str
    society_assigned_agreement_number: str
    submitter_agreement_number: str
    special_agreements_indicator: str
    filler: str
    first_recording_refusal_ind: str
    tax_id_number: str
    usa_license_ind: str
    work_title: str
    agreement_type: str

    def __init__(self, record_prefix):
        EntityBase.__init__(self, record_prefix)

    def __getitem__(self, key: str):
        return getattr(self, key)

    def __setitem__(self, key: str, new_value):
        setattr(self, key, new_value)
