"""
SWT: Writer Territory of Control page.49
This record was introduced in version 2.0. The SWT record specifies collection shares for a writer and the
application territory or territories for the collection shares. Note that SWT records must follow an SWR, NWN
(Non-Roman Alphabet Writer Name) or another SWT record and cannot be used with OWR records. One
SWT record must be used for every territory that is included or excluded. The most frequent case will be that
the writer collects one share percentage for the world (2136). It often happens that a writer collects a higher
percentage for his home territory only. In this case there would be an SPT with one percentage for the world;
an exclude SPT for the home territory with zero percentage; and an include SPT for the home territory with
the percentage collected there.
"""


from ..models.swt import Swt


def swt_strategy(line: str):
    if len(line) < 52:
        line = line.rjust(52, " ")

    """
    [Mandatory] 
    Set Record Type = SWT (writer Territory of Control)
    """
    record_prefix = line[:19].strip()
    writer_territory_of_control = Swt(record_prefix)

    """
    [Mandatory]  Submitting publisher’s unique identifier for this Writer.
    """
    interested_party_number = line[19:28].strip()
    writer_territory_of_control.interested_party_number = interested_party_number

    """
    [Conditional] Defines the percentage of the total royalty distributed for
    performance of the work which will be collected by (paid
    to) the publisher within the above Territory. It can be a
    range from 0 to 50.00.
    """
    pr_collection_share = line[28:33].strip()
    writer_territory_of_control.pr_collection_share = pr_collection_share

    """
    [Conditional] Defines the percentage of the total royalty distributed for
    sales of CDs, Cassette Tapes, etc. in which the work is
    included which will be collected by (paid to) the publisher.
    It can be a range from 0 to 100.00.
    """
    mr_collection_share = line[33:38].strip()
    writer_territory_of_control.mr_collection_share = mr_collection_share

    """
    [Conditional] Defines the percentage of the total royalty distributed for
    Synchronization rights to the work which will be collected
    by (paid to) the publisher. It can be a range from 0 to
    100.00.
    """
    sr_collection_share = line[38:43].strip()
    writer_territory_of_control.sr_collection_share = sr_collection_share

    """  Version 2.0 Fields """

    """
    [Mandatory]  This is a marker which shows whether the territory
    specified in this record is part of the territorial scope of the
    agreement or not. Possible entries are I (= territory
    included) and E (= territory excluded).
    """
    inclusion_exclusion_indicator = line[43:44].strip()
    writer_territory_of_control.inclusion_exclusion_indicator = (
        inclusion_exclusion_indicator
    )

    """
    [Mandatory]  A territory within which this publisher claims the right to
    collect payment for performance or use of this work.
    These values reside in the TIS Code Table.
    """
    tis_numeric_code = line[44:48].strip()
    writer_territory_of_control.tis_numeric_code = tis_numeric_code

    """
    [Optional] If the shares for the writer interest change as a result of
    sub-publication in this territory or for a similar reason, set
    this field to “Y”.
    """
    shares_change = line[48:49].strip()
    writer_territory_of_control.shares_change = shares_change

    """  Version 2.1 Fields """
    sequence_number = line[49:].strip()
    writer_territory_of_control.sequence_number = sequence_number

    # print(writer_territory_of_control.asdict())
    return writer_territory_of_control
