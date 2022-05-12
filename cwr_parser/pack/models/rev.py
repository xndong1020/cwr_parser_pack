from ast import Str
from dataclasses import dataclass
from typing import List

from ..models.base import EntityBase
from ..models.error import Error


@dataclass
class Rev(EntityBase):
    work_title: str
    language_code: str
    submitter_work: str
    iswc: str
    copyright_date: int
    copyright_number: str
    musical_work_distribution: str
    category_duration: str
    recorded_indicator: str
    text_music_relationship: str
    relationship_composite_type: str
    version_type: str
    excerpt_type: str
    contact_name: str
    contact_id: str
    cwr_work_type: str
    grand_rights_ind: str
    date_of_publication_of_printed_edition: str
    exceptional_clause: str
    opus_number: str
    catalogue_number: str
    priority_flag: str

    def __init__(self, record_prefix):
        EntityBase.__init__(self, record_prefix)

    def __getitem__(self, key: str):
        return getattr(self, key)

    def __setitem__(self, key: str, new_value):
        setattr(self, key, new_value)
