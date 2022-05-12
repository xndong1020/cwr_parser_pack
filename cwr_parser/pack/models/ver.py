from dataclasses import dataclass

from ..models.base import EntityBase


@dataclass
class Ver(EntityBase):
    original_work_title: str
    iswc_of_original_work: str
    language_code: str
    writer_1_last_name: str
    writer_1_first_name: str
    source: str
    writer_1_ipi_name_no: str
    writer_1_ipi_base_no: str
    writer_2_last_name: str
    writer_2_first_name: str
    writer_2_ipi_name_no: str
    writer_2_ipi_base_no: str
    submitter_work_no: str

    def __init__(self, record_prefix):
        EntityBase.__init__(self, record_prefix)

    def __getitem__(self, key: str):
        return getattr(self, key)

    def __setitem__(self, key: str, new_value):
        setattr(self, key, new_value)
