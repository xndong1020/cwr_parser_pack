import json

from dataclasses import dataclass
from typing import List

from ..models.base import EntityBase
from ..models.error import Error


@dataclass
class Visan:
    version: str
    isan: str
    episode: str

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=2)


@dataclass
class Orn(EntityBase):
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

    def __init__(self, record_prefix):
        self.visan = Visan("", "", "")
        EntityBase.__init__(self, record_prefix)

    def __getitem__(self, key: str):
        return getattr(self, key)

    def __setitem__(self, key: str, new_value):
        setattr(self, key, new_value)
