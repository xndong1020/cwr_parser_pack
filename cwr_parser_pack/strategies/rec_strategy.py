"""
5.19. REC: Recording Detail

The REC record contains information on the first commercial release of the work.
"""


from models import Rec


def rec_strategy(line: str):
    if len(line) < 266:
        line = line.rjust(266, " ")

    """
    [Mandatory] 
    Set Record Type = SWT (writer Territory of Control)
    """
    record_prefix = line[:19].strip()
    recording_detail = Rec(record_prefix)

    """
    [Optional] 
    Date the work was or will be first released for public
    consumption. This date can be a past, present, or future
    date.
    """
    first_release_date = line[19:27].strip()
    recording_detail.first_release_date = first_release_date

    """
    [Optional] Fill with blanks.
    """
    constant = line[27:87].strip()
    recording_detail.constant = constant

    """
    [Optional] Duration of the first release of the work.
    """
    first_release_duration = line[87:93].strip()
    recording_detail.first_release_duration = first_release_duration

    """
    [Optional] Duration of the first release of the work.
    """
    duration_constant = line[93:98].strip()
    recording_detail.duration_constant = duration_constant

    """   Version 2.0 Fields   """

    """
    [Optional] The name of the album in which the work was included if the work was first released as part of an album.
    """
    first_album_title = line[98:158].strip()
    recording_detail.first_album_title = first_album_title

    """
    [Optional] Name of the organization that produced and released the album in which the first release of the work was included.
    """
    first_album_label = line[158:218].strip()
    recording_detail.first_album_label = first_album_label

    """
    [Optional] Number assigned by the organization releasing the album
    for internal purposes such as sales and distribution
    tracking.
    """
    first_release_catalog_number = line[218:236].strip()
    recording_detail.first_release_catalog_number = first_release_catalog_number

    """
    [Optional] European Article Number of release (EAN-13)
    """
    ean = line[236:249].strip()
    recording_detail.ean = ean

    """
    [Optional] International Standard Recording Code of the recording of the work on the release (according to ISO 3901).
    """
    isrc = line[249:261].strip()
    recording_detail.isrc = isrc

    """
    [Optional] Code that identifies the content of the recording: “A” (audio), “V” (video).
    """
    recording_format = line[261:262].strip()
    recording_detail.recording_format = recording_format

    """
    [Optional] Identifies the recording procedure: “A” (Analogue), “D” (Digital), “U” (Unknown).
    """
    recording_technique = line[262:263].strip()
    recording_detail.recording_technique = recording_technique

    """   Version 2.1 Fields   """

    media_type = line[263:].strip()
    recording_detail.media_type = media_type

    # print(recording_detail.asdict())
    return recording_detail
