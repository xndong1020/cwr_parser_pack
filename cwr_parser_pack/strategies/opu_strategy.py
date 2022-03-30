from ..models import Opu


def opu_strategy(line: str):
    if len(line) < 183:
        line = line.rjust(183, " ")

    """
    [Mandatory] 
    Set Record Type = SPU (Publisher Controlled by Submitter) or OPU (Other Publisher)
    """
    record_prefix = line[:19].strip()
    other_publisher = Opu(record_prefix)

    """
    [Mandatory] A sequential number assigned to the original publishers on this work.
    """
    publisher_sequence_number = line[19:21].strip()
    other_publisher.publisher_sequence_number = publisher_sequence_number

    """
    [Conditional] Submitting publisher’s unique identifier for this publisher.
    This field is required for record type SPU and optional for record type OPU.
    """
    interested_party_number = line[21:30].strip()
    other_publisher.interested_party_number = interested_party_number

    """
    [Conditional] The name of this publishing company. This field is required
    for record type SPU and optional for record type OPU.
    """
    publisher_name = line[30:75].strip()
    other_publisher.publisher_name = publisher_name

    """
    [Conditional] Indicates if the name of this publisher is unknown.
    Note that this field must be left blank for SPU records. For
    OPU records, this field must be set to “Y” if the Publisher
    Name is blank.
    """
    publisher_unknown_indicator = line[75:76].strip()
    other_publisher.publisher_unknown_indicator = publisher_unknown_indicator

    """
    [Conditional] Code defining this publisher’s role in the publishing of the
    work. These values reside on the Publisher Type Table.
    This field is required for record type SPU and optional for
    record type OPU.
    """
    publisher_type = line[76:78].strip()
    other_publisher.publisher_type = publisher_type

    """
    [Optional] The number used to identify this publisher for domestic
    tax reporting.
    """
    tax_id_number = line[78:87].strip()
    other_publisher.tax_id_number = tax_id_number

    """
    [Optional] The IPI Name # assigned to this publisher.
    """
    publisher_ipi_name_number = line[87:98].strip()
    other_publisher.publisher_ipi_name_number = publisher_ipi_name_number

    """
    [Optional] Indicates the agreement number unique to the submitter
    under which this publisher has acquired the rights to this
    work.
    """
    submitter_agreement_number = line[98:112].strip()
    other_publisher.submitter_agreement_number = submitter_agreement_number

    """
    [Conditional] Number assigned to the Performing Rights Society with
    which the publisher is affiliated. These values reside on
    the Society Code Table.
    """
    pr_affiliation_society_number = line[112:115].strip()
    other_publisher.pr_affiliation_society_number = pr_affiliation_society_number

    """
    [Conditional] Defines the percentage of the publisher’s ownership of
    the performance rights to the work. This share does not
    define the percentage of the total royalty distributed for
    performance of the work that will be collected by the
    publisher. Within an individual SPU record, this value can
    range from 0 to 50.0.
    """
    pr_ownership_share = line[115:120].strip()
    other_publisher.pr_ownership_share = float(pr_ownership_share)

    """
    [Conditional] Number assigned to the Mechanical Rights Society with
    which the publisher is affiliated. These values reside on
    the Society Code Table.
    """
    mr_affiliation_society_number = line[120:123].strip()
    other_publisher.mr_affiliation_society_number = mr_affiliation_society_number

    """
    [Conditional] Defines the percentage of the publisher’s ownership of
    the mechanical rights to the work. This share does not
    define the percentage of the total royalty distributed for
    sales of CDs, Cassettes, etc. containing the work that will
    be collected by the publisher. Within an individual SPU
    record, this value can range from 0 to 100.0.
    """
    mr_ownership_share = line[123:128].strip()
    other_publisher.mr_ownership_share = float(mr_ownership_share)

    """
    [Conditional] Number assigned to the Society with which the publisher
    is affiliated for administration of synchronization rights.
    These values reside on the Society Code Table.
    """
    sr_society_number = line[128:131].strip()
    other_publisher.sr_society_number = sr_society_number

    """
    [Conditional] Defines the percentage of the publisher’s ownership of
    the synch rights to the work. This share does not define
    the percentage of the total money distributed that will be
    collected by the publisher. Within an individual SPU
    record, this value can range from 0 to 100.0.
    """
    sr_ownership_share = line[131:136].strip()
    other_publisher.sr_ownership_share = float(sr_ownership_share)

    """
    [Optional] Indicates whether the submitter has refused to give authority for the first recording.
    """
    special_agreements_indicator = line[136:137].strip()
    other_publisher.special_agreements_indicator = special_agreements_indicator

    """
    [Optional] Indicates whether the submitter has refused to give authority for the first recording.
    """
    first_recording_refusal_ind = line[137:138].strip()
    other_publisher.first_recording_refusal_ind = first_recording_refusal_ind

    """
    [Optional] Fill with a blank.
    """
    filler = line[138:139].strip()
    other_publisher.filler = filler

    """  Version 2.0 Fields """

    """
    [Optional] The IPI base number assigned to this publisher.
    """
    publisher_ipi_base_number = line[139:152].strip()
    other_publisher.publisher_ipi_base_number = publisher_ipi_base_number

    """
    [Optional] The ISAC that has been assigned to the agreement under which this publisher share is to be administered.
    """
    international_standard_agreement_code = line[152:166].strip()
    other_publisher.international_standard_agreement_code = (
        international_standard_agreement_code
    )

    """
    [Optional] The agreement number assigned by the society of the sub-publisher.
    """
    society_assigned_agreement_number = line[166:180].strip()
    other_publisher.society_assigned_agreement_number = (
        society_assigned_agreement_number
    )

    """  Version 2.1 Fields """

    """
    [Optional] Code defining the category of agreement. The values reside in the Agreement Type Table.
    """
    agreement_type = line[180:182].strip()
    other_publisher.agreement_type = agreement_type

    """
    [Optional] Code defining the category of agreement. The values reside in the Agreement Type Table.
    """
    usa_license_ind = line[182:].strip()
    other_publisher.usa_license_ind = usa_license_ind

    # print(other_publisher.asdict())

    return other_publisher
