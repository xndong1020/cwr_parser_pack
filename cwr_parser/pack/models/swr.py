from dataclasses import dataclass
from typing import List

from ..models.base import EntityBase
from ..models.error import Error


@dataclass
class Swr(EntityBase):
    interested_party_number: str
    writer_last_name: str
    writer_first_name: str
    writer_unknown_indicator: str
    writer_designation_code: str
    tax_id_number: str
    writer_ipi_name_number: str
    pr_affiliation_society_number: str
    pr_ownership_share: str
    mr_society_number: str
    mr_ownership_share: str
    sr_society_number: str
    sr_ownership_share: str
    reversionary_indicator: str
    first_recording_refusal_ind: str
    work_for_hire_indicator: str
    filler: str
    writer_ipi_base_number: str
    personal_number: str
    usa_license_ind: str

    def __init__(self, record_prefix):
        EntityBase.__init__(self, record_prefix)

    def __getitem__(self, key: str):
        return getattr(self, key)

    def __setitem__(self, key: str, new_value):
        setattr(self, key, new_value)
