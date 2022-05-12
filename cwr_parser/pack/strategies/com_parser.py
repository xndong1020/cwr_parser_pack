"""
5.23. COM: Component

If the work being registered is a composite work, the COM record will identify an individual component of
the composite.
"""


from ..models import Com


def com_parser(line: str):
    print("com", line, len(line))
    if len(line) < 308:
        line = line.rjust(308, " ")

    """
    [Mandatory] 
    Set Record Type = COM (Composite Component)
    """
    record_prefix = line[:19].strip()
    com_obj = Com(record_prefix)

    """
    [Mandatory] 
    The title of the original work from which a portion was
    taken and included in the composite work.
    """
    title = line[19:79].strip()
    com_obj.title = title

    """
    [Optional] 
    The International Standard Work Code assigned to the
    original work from which a portion was taken and included
    in this composite work
    """
    iswc_of_component = line[79:90].strip()
    com_obj.iswc_of_component = iswc_of_component

    """
    [Optional] 
    The number that the submitting party uses to refer to this
    composite component.
    """
    submitter_work_no = line[90:104].strip()
    com_obj.submitter_work_no = submitter_work_no

    """
    [Optional] 
    The duration of this composite component.
    """
    duration = line[104:110].strip()
    com_obj.duration = duration

    """
    [Mandatory] 
    Last name of the first writer of this component. Note that
    if the submitter does not have the ability to split first and
    last names, the entire name should be entered in this field
    in the format “Last Name, First Name” including the
    comma after the last name.
    """
    writer_1_last_name = line[110:155].strip()
    com_obj.writer_1_last_name = writer_1_last_name

    """
    [Optional] 
    First name of the first writer of this component.
    """
    writer_1_first_name = line[155:185].strip()
    com_obj.writer_1_first_name = writer_1_first_name

    """
    [Optional] 
    The IPI Name number assigned to the first writer of this
    component.
    """
    writer_1_ipi_name_no = line[185:196].strip()
    com_obj.writer_1_ipi_name_no = writer_1_ipi_name_no

    """
    [Optional] 
    Last name of the second writer of this component. Note
    that if the submitter does not have the ability to split first
    and last names, the entire name should be entered in this
    field in the format “Last Name, First Name” including the
    comma after the last name.
    """
    writer_2_last_name = line[196:241].strip()
    com_obj.writer_2_last_name = writer_2_last_name

    """
    [Optional] 
    First name of the second writer of this component.
    """
    writer_2_first_name = line[241:271].strip()
    com_obj.writer_2_first_name = writer_2_first_name

    """
    [Optional] 
    The IPI Name number assigned to the second writer of this
    component.
    """
    writer_2_ipi_name_no = line[271:282].strip()
    com_obj.writer_2_ipi_name_no = writer_2_ipi_name_no

    ### Version 2.0 Fields ###

    """
    [Optional] 
    The IPI base number assigned to this writer. These values
    reside in the IPI database.
    """
    writer_1_ipi_base_no = line[282:295].strip()
    com_obj.writer_1_ipi_base_no = writer_1_ipi_base_no

    """
    [Optional] 
    The IPI base number assigned to this writer. These values
    reside in the IPI database.
    """
    writer_2_ipi_base_no = line[295:].strip()
    com_obj.writer_2_ipi_base_no = writer_2_ipi_base_no

    # print(alternate_title_obj.asdict())
    return com_obj
