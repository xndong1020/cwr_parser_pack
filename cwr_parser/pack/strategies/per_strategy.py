"""
5.17. PER: Performing Artist

The name of a person or group performing this work either in public or on a recording.
"""


from ..models import Per


def per_strategy(line: str):
    if len(line) < 118:
        line = line.rjust(118, " ")

    """
    [Mandatory] 
    Set Record Type = PER (Performing Artist)
    """
    record_prefix = line[:19].strip()
    performing_artist = Per(record_prefix)

    """
    [Mandatory]  Submitting publisher’s unique identifier for this Writer.
    """
    performing_artist_last_name = line[19:64].strip()
    performing_artist.performing_artist_last_name = performing_artist_last_name

    """
    [Optional]  First name associated with the performing artist identified in the previous field.
    """
    performing_artist_first_name = line[64:94].strip()
    performing_artist.performing_artist_first_name = performing_artist_first_name

    """
    [Optional]  First name associated with the performing artist identified in the previous field.
    """
    performing_artist_ipi_name_number = line[94:105].strip()
    performing_artist.performing_artist_ipi_name_number = (
        performing_artist_ipi_name_number
    )

    """ Version 2.0 Field """

    """
    [Optional]  First name associated with the performing artist identified in the previous field.
    """
    performing_artist_ipi_base_number = line[105:].strip()
    performing_artist.performing_artist_ipi_base_number = (
        performing_artist_ipi_base_number
    )

    # print(performing_artist.asdict())

    return performing_artist
