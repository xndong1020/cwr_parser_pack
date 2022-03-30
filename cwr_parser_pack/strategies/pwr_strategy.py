"""
5.12. PWR: Publisher For Writer

The PWR record is used to indicate the publisher that represents the writer designated on the previous SWR
record for writers that are published (total writer ownership shares for each right are less than 100%). PWR
must not be submitted for OWR records. Use a separate PWR record to document each publisher that
represents the writer.
"""


from cwr_parser_pack.models import Pwr


def pwr_strategy(line: str):
    if len(line) < 110:
        line = line.rjust(110, " ")

    """
    [Mandatory] 
    Set Record Type = SWT (writer Territory of Control)
    """
    record_prefix = line[:19].strip()
    publisher_for_writer = Pwr(record_prefix)

    """
    [Mandatory]
    The publisher interested party number pointing back to
    the SPU record for the original publisher/income
    participant representing this writer.
    """
    publisher_ip_number = line[19:28].strip()
    publisher_for_writer.publisher_ip_number = publisher_ip_number

    """
    [Mandatory]
    The name of the publisher indicated by the Interested Party # field.
    """
    publisher_name = line[28:73].strip()
    publisher_for_writer.publisher_name = publisher_name

    """  Version 2.0 Fields  """

    """
    [Optional]
    The unique number assigned to this agreement by the submitter.
    """
    submitter_agreement_number = line[73:87].strip()
    publisher_for_writer.submitter_agreement_number = submitter_agreement_number

    """
    [Optional]
    The unique number assigned to this agreement by the submitter.
    """
    society_assigned_agreement_number = line[87:101].strip()
    publisher_for_writer.society_assigned_agreement_number = (
        society_assigned_agreement_number
    )

    """  Version 2.1 Fields  """

    """
    [Mandatory]
    The writer interested party number pointing back to the SWR record in an explicit link.
    """
    writer_ip_number = line[101:].strip()
    publisher_for_writer.writer_ip_number = writer_ip_number

    # print(publisher_for_writer.asdict())

    return publisher_for_writer
