from cwr_parser_pack.models import Swr


def swr_strategy(line: str):
    if len(line) < 180:
        line = line.rjust(180, " ")

    """
    [Mandatory] 
    Set Record Type = SWR (Writer Controlled by Submitter) or OWR (Other Writer)
    """
    record_prefix = line[:20].strip()
    writer_controlled_by_submitter = Swr(record_prefix)

    """
    [Conditional] Submitting publisher’s unique identifier for this Writer.
    This field is required for record type SWR and optional for
    record type OWR.
    """
    interested_party_number = line[20:29].strip()
    writer_controlled_by_submitter.interested_party_number = interested_party_number

    """
    [Conditional] The last name of this writer. Note that if the submitter
    does not have the ability to split first and last names, the
    entire name should be entered in this field in the format
    “Last Name, First Name” including the comma after the
    last name. This field is required for record type SWR and
    optional for record type OWR.
    """
    writer_last_name = line[29:74].strip()
    writer_controlled_by_submitter.writer_last_name = writer_last_name

    """
    [Optional] The first name of this writer along with all qualifying and middle names.
    """
    writer_first_name = line[74:104].strip()
    writer_controlled_by_submitter.writer_first_name = writer_first_name

    """
    [Conditional] Indicates if the name of this writer is unknown. Note that
    this field must be left blank for SWR records. For OWR
    records, this field must be set to “Y” if the Writer Last
    Name is blank.
    """
    writer_unknown_indicator = line[104:105].strip()
    writer_controlled_by_submitter.writer_unknown_indicator = writer_unknown_indicator

    """
    [Conditional] Code defining the role the writer played in the
    composition of the work. These values reside in the Writer
    Designation Table. This field is required for record type
    SWR and optional for record type OWR.
    """
    writer_designation_code = line[105:107].strip()
    writer_controlled_by_submitter.writer_designation_code = writer_designation_code

    """
    [Optional] The number used to identify this writer for domestic tax
    reporting.
    """
    tax_id_number = line[107:116].strip()
    writer_controlled_by_submitter.tax_id_number = tax_id_number

    """
    [Optional] The IPI Name # assigned to this writer.
    """
    writer_ipi_name_number = line[116:127].strip()
    writer_controlled_by_submitter.writer_ipi_name_number = writer_ipi_name_number

    """
    [Optional] Number assigned to the Performing Rights Society with
    which the writer is affiliated. These values reside on the
    Society Code Table.
    """
    pr_affiliation_society_number = line[127:130].strip()
    writer_controlled_by_submitter.pr_affiliation_society_number = (
        pr_affiliation_society_number
    )

    """
    [Optional] Defines the percentage of the writer’s ownership of the
    performance rights to the work. Within an individual SWR
    record, this value can range from 0 to 100.0. Note that
    writers both own and collect the performing right interest.
    """
    pr_ownership_share = line[130:135].strip()
    writer_controlled_by_submitter.pr_ownership_share = pr_ownership_share

    """
    [Optional] Number assigned to the Mechanical Rights Society with
    which the writer is affiliated. These values reside on the
    Society Code Table.
    """
    mr_society_number = line[135:138].strip()
    writer_controlled_by_submitter.mr_society_number = mr_society_number

    """
    [Optional] Defines the percentage of the writer’s ownership of the
    mechanical rights to the work. Within an individual SPU
    record, this value can range from 0 to 100.0.
    """
    mr_ownership_share = line[138:143].strip()
    writer_controlled_by_submitter.mr_ownership_share = mr_ownership_share

    """
    [Optional] Number assigned to the Society with which the publisher
    is affiliated for administration of synchronization rights.
    These values reside on the Society Code Table.
    """
    sr_society_number = line[143:146].strip()
    writer_controlled_by_submitter.sr_society_number = sr_society_number

    """
    [Optional] Defines the percentage of the publisher’s ownership of
    the synch rights to the work. This share does not define
    the percentage of the total money distributed that will be
    collected by the publisher. Within an individual SPU
    record, this value can range from 0 to 100.0.
    """
    sr_ownership_share = line[146:151].strip()
    writer_controlled_by_submitter.sr_ownership_share = sr_ownership_share

    """ Society/Region Specific Fields """

    """
    [Optional] Indicates writer involved in the claim.
    Note that this flag only applies to societies that recognize
    reversionary rights (for example, SOCAN).
    """
    reversionary_indicator = line[151:152].strip()
    writer_controlled_by_submitter.reversionary_indicator = reversionary_indicator

    """
    [Optional] Indicates whether the submitter has refused to give
    authority for the first recording. Note that this field is
    mandatory for registrations with the UK societies.
    """
    first_recording_refusal_ind = line[152:153].strip()
    writer_controlled_by_submitter.first_recording_refusal_ind = (
        first_recording_refusal_ind
    )

    """
    [Optional] Indicates whether or not this work was written for hire.
    """
    work_for_hire_indicator = line[153:154].strip()
    writer_controlled_by_submitter.work_for_hire_indicator = work_for_hire_indicator

    """
    [Optional] 
    """
    filler = line[154:155].strip()
    writer_controlled_by_submitter.filler = filler

    """ Version 2.0 Fields  """

    """
    [Optional] The IPI base number assigned to this writer. These values
    reside in the IPI database.
    """
    writer_ipi_base_number = line[155:168].strip()
    writer_controlled_by_submitter.writer_ipi_base_number = writer_ipi_base_number

    """
    [Optional] The personal number assigned to this writer in the country
    of his/her residence.
    """
    personal_number = line[158:180].strip()
    writer_controlled_by_submitter.personal_number = personal_number

    """ Version 2.1 Fields  """

    """
    [Optional] Indicates that rights flow through SESAC/BMI/ASCAP inthe US.
    """
    usa_license_ind = line[180:].strip()
    writer_controlled_by_submitter.usa_license_ind = usa_license_ind

    # print(writer_controlled_by_submitter.asdict())

    return writer_controlled_by_submitter
