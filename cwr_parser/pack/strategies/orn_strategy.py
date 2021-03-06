"""
5.20. ORN: Work Origin page.59

The purpose of this record is to describe the origin of the work. The origin may be a library, or an audio-visual
production or both. If the work originated in an AV production, additional information regarding the usage
of the work within the production can be helpful. Note that the cue sheet is always the final authority for
usage data. Many identifiers for the audio-visual production have been added with version 2.1 including the
reference as used in the CIS tool, AV Index.
"""


from ..models import Orn, Visan


def orn_strategy(line: str):
    if len(line) < 348:
        line = line.rjust(348, " ")

    """
    [Mandatory] 
    Set Record Type = ALT (Alternate Title)
    """
    record_prefix = line[:19].strip()
    work_origin = Orn(record_prefix)

    """
    [Mandatory] Indicates the type of production from which this work
    originated. These values reside in the Intended Purpose
    Table.
    """
    intended_purpose = line[19:22].strip()
    work_origin.intended_purpose = intended_purpose

    """
    [Conditional] Name of the production from which this work originated.
    This field is required when CWR Work Type on the NWR
    record equals “FM”.
    """
    production_title = line[22:82].strip()
    work_origin.production_title = production_title

    """
    [Conditional] If Intended Purpose is equal to LIB (Library Work), enter
    the identifier associated with the CD upon which the work
    appears.
    """
    cd_identifier = line[82:97].strip()
    work_origin.cd_identifier = cd_identifier

    """
    [Optional] If Intended Purpose is equal to LIB (Library Work), enter
    the track number on the CD Identifier where the work
    appears.
    """
    cut_number = line[97:101].strip()
    work_origin.cut_number = cut_number

    """ Version 2.1 Fields  """

    """
    [Conditional] The library from which this work originated.
    """
    library = line[101:161].strip()
    work_origin.library = library

    """
    [Optional] An indication of the primary use of the work within the AV
    production. The definitive source for cue usage is the cue
    sheet.
    """
    bltvr = line[161:162].strip()
    work_origin.bltvr = bltvr

    visan_obj = Visan("", "", "")

    """
    [Optional] Version portion of the V-ISAN
    """
    version = line[162:170].strip()
    visan_obj.version = version

    """
    [Optional] ISAN
    """
    isan = line[170:182].strip()
    visan_obj.isan = isan

    """
    [Optional] Unique identifier for episode.
    """
    episode = line[182:186].strip()
    visan_obj.episode = episode

    work_origin.visan = visan_obj.toJSON()

    """
    [Optional] Check digit to verify accuracy of ISAN.
    """
    check_digit = line[186:187].strip()
    work_origin.check_digit = check_digit

    """
    [Optional] The number generated by the production company to identify the work.
    """
    production_number = line[187:199].strip()
    work_origin.production_number = production_number

    """
    [Optional] Title of the episode from which this work originated.
    """
    episode_title = line[199:259].strip()
    work_origin.episode_title = episode_title

    """
    [Optional] Title of the episode from which this work originated.
    """
    episode_number = line[259:279].strip()
    work_origin.episode_number = episode_number

    """
    [Optional] Title of the episode from which this work originated.
    """
    year_of_production = line[279:283].strip()
    work_origin.year_of_production = year_of_production

    """
    [Optional] The Society code of the society whose audio visual work
    detail entry is referenced in the AV Index. These values
    reside on the Society Code Table.
    """
    avi_society_code = line[283:286].strip()
    work_origin.avi_society_code = avi_society_code

    """
    [Optional] Unique number used internally by the “owning” society to
    identify the audio-visual work as referenced in the AV
    Index.
    """
    audio_visual_number = line[286:].strip()
    work_origin.audio_visual_number = audio_visual_number

    # print(work_origin.asdict())
    return work_origin
