""""
SPT: Publisher Territory of Control page.43

The SPT record defines the territory and the collection shares for the preceding SPU publisher. Note that SPT
records follow an SPU, NPN (Non-Roman alphabet Publisher Name), or another SPT record. The SPT record
cannot be used with OPU records. Include one SPT record for each territory, or groups of territories for which
the preceding publisher has collection rights. It is also possible to use a combination of include and exclude
SPT records. For example, to specify collection shares for all of Europe except Switzerland, you can provide
an SPT record to include Europe, and one to exclude Switzerland. By its nature, the SPT used to exclude a
territory should not have any share percentages greater than zero. It is possible to have all zero shares on an
SPT that includes one or more territories. Such a record would be used to record a publisher’s place in the
chain of agreements.
"""


from cwr_parser_pack.models import Spt


def spt_strategy(line: str):
    if len(line) < 58:
        line = line.rjust(58, " ")

    """
    [Mandatory] 
    Set Record Type = SPT (Publisher Territory of Control)
    """
    record_prefix = line[:19].strip()
    publisher_territory_of_control = Spt(record_prefix)

    """
    [Mandatory]  Submitting publisher’s unique identifier for this Publisher.
    """
    interested_party_number = line[19:28].strip()
    publisher_territory_of_control.interested_party_number = interested_party_number

    """
    [Mandatory]  Set this field equal to spaces.
    """
    constant = line[28:34].strip()
    publisher_territory_of_control.constant = constant

    """
    [Conditional] Defines the percentage of the total royalty distributed for
    performance of the work which will be collected by (paid
    to) the publisher within the above Territory. It can be a
    range from 0 to 50.00.
    """
    pr_ownership_share = line[34:39].strip()
    publisher_territory_of_control.pr_ownership_share = pr_ownership_share

    """
    [Conditional] Defines the percentage of the total royalty distributed for
    sales of CDs, Cassette Tapes, etc. in which the work is
    included which will be collected by (paid to) the publisher.
    It can be a range from 0 to 100.00.
    """
    mr_ownership_share = line[39:44].strip()
    publisher_territory_of_control.mr_ownership_share = mr_ownership_share

    """
    [Conditional] Defines the percentage of the total royalty distributed for
    Synchronization rights to the work which will be collected
    by (paid to) the publisher. It can be a range from 0 to
    100.00.
    """
    sr_ownership_share = line[44:49].strip()
    publisher_territory_of_control.sr_ownership_share = sr_ownership_share

    """  Version 2.0 Fields """

    """
    [Mandatory]  This is a marker which shows whether the territory
    specified in this record is part of the territorial scope of the
    agreement or not. Possible entries are I (= territory
    included) and E (= territory excluded).
    """
    inclusion_exclusion_indicator = line[49:50].strip()
    publisher_territory_of_control.inclusion_exclusion_indicator = (
        inclusion_exclusion_indicator
    )

    """
    [Mandatory]  A territory within which this publisher claims the right to
    collect payment for performance or use of this work.
    These values reside in the TIS Code Table.
    """
    tis_numeric_code = line[50:54].strip()
    publisher_territory_of_control.tis_numeric_code = tis_numeric_code

    """
    [Optional] If the shares for the writer interest change as a result of
    sub-publication in this territory or for a similar reason, set
    this field to “Y”.
    """
    shares_change = line[54:55].strip()
    publisher_territory_of_control.shares_change = shares_change

    """  Version 2.1 Fields """
    sequence_number = line[55:].strip()
    publisher_territory_of_control.sequence_number = sequence_number

    # print(publisher_territory_of_control.asdict())
    return publisher_territory_of_control
