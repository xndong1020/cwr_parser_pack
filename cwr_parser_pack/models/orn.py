from typing import List

from cwr_parser_pack.models.base import EntityBase
from cwr_parser_pack.models.error import Error


class Visan:
    version: str
    isan: str
    episode: str


class Orn(EntityBase):
    errors: List[Error]
    intended_purpose: str
    production_title: str
    cd_identifier: str
    library: str
    bltvr: str
    visan: Visan
    check_digit: str
    production_number: str
    episode_title: str
    episode_number: str
    year_of_production: str
    avi_society_code: str
    audio_visual_number: str

    def __init__(self, record_prefix, errors: List[str] = []):
        self.errors = errors
        EntityBase.__init__(self, record_prefix)
