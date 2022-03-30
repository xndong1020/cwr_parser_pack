from ..models.rev import Rev


def rev_strategy(line: str):
    if len(line) < 260:
        line = line.rjust(260, " ")

    """
    [Mandatory] 
    Set Record Type = NWR (New Work Registration) for new
    registrations, REV (Revised Registration) for revisions, or
    ISW (Notification of ISWC) or EXC (Existing Work in
    Conflict) for outgoing notifications.
    """
    record_prefix = line[:19].strip()
    revised_registration = Rev(record_prefix)

    """
    [Mandatory] Name/Title of the work. 
    """
    work_title = line[19:79].strip()
    revised_registration.work_title = work_title

    """
    [Optional] The code representing the language of this title. These
    values reside in the Language Code Table.
    """
    language_code = line[79:81].strip()
    revised_registration.language_code = language_code

    """
    [Mandatory] Number assigned to the work by the publisher submitting
    or receiving the file. This number must be unique for the
    publisher.
    """
    submitter_work = line[81:95].strip()
    revised_registration.submitter_work = submitter_work

    """
    [Optional] The International Standard Work Code assigned to this
    work.
    """
    iswc = line[95:106].strip()
    revised_registration.iswc = iswc

    """
    [Optional] Original copyright date of the work.
    """
    copyright_date = line[106:114].strip()
    revised_registration.copyright_date = copyright_date

    """
    [Optional] Original copyright number of the work.
    """
    copyright_number = line[114:126].strip()
    revised_registration.copyright_number = copyright_number

    """
    [Mandatory] Number assigned to the work by the publisher submitting
    or receiving the file. This number must be unique for the
    publisher.
    """
    musical_work_distribution = line[126:129].strip()
    revised_registration.musical_work_distribution = musical_work_distribution

    """
    [Optional] Original copyright number of the work.
    """
    category_duration = line[129:135].strip()
    revised_registration.category_duration = category_duration

    """
    [Mandatory] Indicates whether or not the work has ever been recorded.
    """
    recorded_indicator = line[135:136].strip()
    revised_registration.recorded_indicator = recorded_indicator

    """
    [Optional] Indicates whether this work contains music, text, and/or both. Values reside in the Text Music Relationship Table.
    """
    text_music_relationship = line[136:139].strip()
    revised_registration.text_music_relationship = text_music_relationship

    """
    [Optional] If this is a composite work, this field will indicate the type of composite. Values reside in the Composite Type Table.
    """
    relationship_composite_type = line[139:142].strip()
    revised_registration.relationship_composite_type = relationship_composite_type

    """
    [Mandatory] Indicates relationships between this work and other
    works. Note that this field is used to indicate whether or
    not this work is an arrangement. Values reside in the
    Version Type Table.
    """
    version_type = line[142:145].strip()
    revised_registration.version_type = version_type

    """
    [Optional] If this is an excerpt, this field will indicate the type of excerpt. Values reside in the Excerpt Type Table.
    """
    excerpt_type = line[145:148].strip()
    revised_registration.excerpt_type = excerpt_type

    """
    [Conditional] If Version Type is equal to “MOD”, this field indicates the
    type of music arrangement. Values reside in the Music
    Arrangement Table.
    """
    if revised_registration.version_type == "MOD":
        music_arrangement = line[148:151].strip()
        revised_registration.music_arrangement = music_arrangement

    """
    [Conditional] If Version Type is equal to “MOD”, this field indicates the
    type of lyric adaptation. Values reside in the Lyric
    Adaptation Table.
    """
    if revised_registration.version_type == "MOD":
        lyric_adaptation = line[151:154].strip()
        revised_registration.lyric_adaptation = lyric_adaptation

    """
    [Optional] The name of a business contact person at the organization that originated this transaction.
    """
    contact_name = line[154:184].strip()
    revised_registration.contact_name = contact_name

    """
    [Optional] An identifier associated with the contact person at the organization that originated this transaction.
    """
    contact_id = line[184:194].strip()
    revised_registration.contact_id = contact_id

    """
    [Optional] These values reside in the CWR Work Type table.
    """
    cwr_work_type = line[194:196].strip()
    revised_registration.cwr_work_type = cwr_work_type

    """
    [Conditional] Indicates whether this work is originally intended for
    performance on stage.
    Note that this field is mandatory for registrations with the
    UK societies.
    """
    # TODO: Check if it is for UK societies
    grand_rights_ind = line[196:197].strip()
    revised_registration.grand_rights_ind = grand_rights_ind

    """
    [Conditional] If Composite Type is entered, this field represents the
    number of components contained in this composite.
    Note that this is required for composite works where
    ASCAP is represented on the work.
    """
    if revised_registration.relationship_composite_type:
        composite_component_count = line[200:208].strip()
        revised_registration.composite_component_count = composite_component_count

    """
            *** Society Specific Fields for Version 2.0 ***
    """

    """
    [Optional] For registrations with GEMA: Indicates the date that the
    printed, new edition published by the submitting publisher
    appeared. This information is especially relevant for the
    notification of sub-published works by GEMA-sub-
    publishers.
    """
    date_of_publication_of_printed_edition = line[200:208].strip()
    revised_registration.date_of_publication_of_printed_edition = (
        date_of_publication_of_printed_edition
    )

    """
    [Optional] For registrations with GEMA: By entering Y (Yes), the
    submitting GEMA-sub-publisher declares that the
    exceptional clause of the GEMA distribution rules with
    regard to printed editions applies (GEMA-Verteilungsplan
    A Anhang III).
    """
    exceptional_clause = line[208:209].strip()
    revised_registration.exceptional_clause = exceptional_clause

    """
            *** Additional Fields for Version 2.0 ***
    """

    """
    [Optional] Indicates the number assigned to this work, usually by the
    composer. Part numbers are to be added with an # e.g.
    28#3 (meaning Opus 28 part 3).
    """
    opus_number = line[209:234].strip()
    revised_registration.opus_number = opus_number

    """
    [Optional] The work catalogue number. The abbreviated name of the
    catalogue is to be added (like BWV, KV), without dots. Part
    numbers are to be added with an # e.g. KV 297#1 (meaning
    Köchel Verzeichnis Nr.297 part 1).
    """
    catalogue_number = line[234:259].strip()
    revised_registration.catalogue_number = catalogue_number

    """
            *** Fields for Version 2.1 ***
    """

    """
    [Optional] Indicates that this work should be processed faster
    because it is on the charts, is by a well-known composer,
    etc.
    """
    priority_flag = line[259:].strip()
    revised_registration.priority_flag = priority_flag

    # print(revised_registration.asdict())

    return revised_registration
