"""
5.13. ALT: Alternate Title page.51

This record identifies alternate titles for this work. The language code is used to identify titles that have been
translated into a language other than the original. Note that this applies to translation of the title only - not
a translation of the work. Including record type VER would indicate a work translation.
"""


from ..models import Xrf


def xrf_parser(line: str):
    if len(line) < 38:
        line = line.rjust(38, " ")

    """
    [Mandatory] 
    Set Record Type = XRF (Work Code Cross Reference)
    """
    record_prefix = line[:19].strip()
    xrf_obj = Xrf(record_prefix)

    """
    [Mandatory] 
    Number assigned to the Organisation (e.g. Society, publisher, DSP etc...) which generated the Work Code. These values reside in the Transmitter Code Table, or can be “ISW” for ISWC or “ISR” for ISRC. Note: Do not use “000”or “099”.
    """
    organisation_code = line[19:23].strip()
    xrf_obj.organisation_code = organisation_code

    """
    [Mandatory] 
    An identifier that relates to this work Transaction which was issued by the Organisation identified in Organisation Code.
    """
    identifier = line[23:37].strip()
    xrf_obj.identifier = identifier

    """
    [Mandatory] 
    The type of identifier. These values reside in the Identifier Type Table.
    """
    identifier_type = line[37:38].strip()
    xrf_obj.identifier_type = identifier_type

    """
    [Mandatory] 
    Indicates whether the Identifier is valid or not. These values reside in the Identifier Validity Table.
    """
    identifier_validity = line[38:].strip()
    xrf_obj.identifier_validity = identifier_validity

    # print(alternate_title_obj.asdict())
    return xrf_obj
