"""
5.16. VER: Original Work Title for Versions. page 55/79

If the work being registered is a version of another work, the VER record is used to indicate the title of the
original work from which the version has been derived.
"""


from ..models import Ver


def ver_parser(line: str):
    if len(line) < 364:
        line = line.rjust(364, " ")

    """
    [Mandatory] 
    Set Record Type = VER (Original Work Title for Versions)
    """
    record_prefix = line[:19].strip()
    ver_obj = Ver(record_prefix)

    """
    [Mandatory] 
    Original title of the work from which this version was derived.
    """
    original_work_title = line[19:79].strip()
    ver_obj.original_work_title = original_work_title

    """
    [Optional] 
    The International Standard Work Code assigned to the work from which this version has been derived.   
    """
    iswc_of_original_work = line[79:90].strip()
    ver_obj.iswc_of_original_work = iswc_of_original_work

    """
    [Optional] 
    The code defining the language in which the work was originally written. These values reside in the Language Code Table.
    """
    language_code = line[90:92].strip()
    ver_obj.language_code = language_code

    """
    [Optional] 
    Last name of the original writer/composer of the work
    from which this version has been derived. Note that if the
    submitter does not have the ability to split first and last
    names, the entire name should be entered in this field in
    the format “Last Name, First Name” including the comma
    after the last name.
    """
    writer_1_last_name = line[92:137].strip()
    ver_obj.writer_1_last_name = writer_1_last_name

    """
    [Optional] 
    Last name of the original writer/composer of the work
    from which this version has been derived. Note that if the
    submitter does not have the ability to split first and last
    names, the entire name should be entered in this field in
    the format “Last Name, First Name” including the comma
    after the last name.
    """
    writer_1_first_name = line[137:167].strip()
    ver_obj.writer_1_first_name = writer_1_first_name

    """
    [Optional] 
    Last name of the original writer/composer of the work
    from which this version has been derived. Note that if the
    submitter does not have the ability to split first and last
    names, the entire name should be entered in this field in
    the format “Last Name, First Name” including the comma
    after the last name.
    """
    source = line[167:227].strip()
    ver_obj.source = source

    ### Version 2.0 Fields ###

    """
    [Optional] 
    The IPI Name number assigned to the first writer of the
    original work.
    """
    writer_1_ipi_name_no = line[227:238].strip()
    ver_obj.writer_1_ipi_name_no = writer_1_ipi_name_no

    """
    [Optional] 
    The IPI base number assigned to this writer. These values
    reside in the IPI database.
    """
    writer_1_ipi_base_no = line[238:251].strip()
    ver_obj.writer_1_ipi_base_no = writer_1_ipi_base_no

    """
    [Optional] 
    The IPI base number assigned to this writer. These values
    reside in the IPI database.
    """
    writer_1_ipi_base_no = line[238:251].strip()
    ver_obj.writer_1_ipi_base_no = writer_1_ipi_base_no

    """
    [Optional] 
    Last name of the second writer of the original work. Note
    that if the submitter does not have the ability to split first
    and last names, the entire name should be entered in this
    field in the format “Last Name, First Name” including the
    comma after the last name
    """
    writer_2_last_name = line[251:296].strip()
    ver_obj.writer_2_last_name = writer_2_last_name

    """
    [Optional] 
    First name of the second writer of the original work.
    """
    writer_2_first_name = line[296:326].strip()
    ver_obj.writer_2_first_name = writer_2_first_name

    """
    [Optional] 
    The IPI Name number assigned to the second writer of this
    original work.
    """
    writer_2_ipi_name_no = line[326:337].strip()
    ver_obj.writer_2_ipi_name_no = writer_2_ipi_name_no

    """
    [Optional] 
    The IPI base number assigned to this writer. These values
    reside in the IPI database.
    """
    writer_2_ipi_base_no = line[337:350].strip()
    ver_obj.writer_2_ipi_base_no = writer_2_ipi_base_no

    """
    [Optional] 
    The IPI base number assigned to this writer. These values
    reside in the IPI database.
    """
    submitter_work_no = line[350:].strip()
    ver_obj.submitter_work_no = submitter_work_no

    # print(alternate_title_obj.asdict())
    return ver_obj
