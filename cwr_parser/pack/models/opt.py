from dataclasses import dataclass
from typing import List

from ..models.base import EntityBase
from ..models.error import Error


@dataclass
class Opt(EntityBase):
    interested_party_number: str
    constant: str
    pr_ownership_share: str
    mr_ownership_share: str
    sr_ownership_share: str
    inclusion_exclusion_indicator: str
    tis_numeric_code: str
    sequence_number: str

    def __init__(self, record_prefix):
        EntityBase.__init__(self, record_prefix)

    def __getitem__(self, key: str):
        return getattr(self, key)

    def __setitem__(self, key: str, new_value):
        setattr(self, key, new_value)
