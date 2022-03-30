"""
5.13. ALT: Alternate Title page.51

This record identifies alternate titles for this work. The language code is used to identify titles that have been
translated into a language other than the original. Note that this applies to translation of the title only - not
a translation of the work. Including record type VER would indicate a work translation.
"""


from ..models import Alt


def alt_strategy(line: str):
    if len(line) < 83:
        line = line.rjust(83, " ")

    """
    [Mandatory] 
    Set Record Type = ALT (Alternate Title)
    """
    record_prefix = line[:19].strip()
    alternate_title_obj = Alt(record_prefix)

    """
    [Mandatory] 
    AKA or pseudonym of the work title.
    """
    alternate_title = line[19:79].strip()
    alternate_title_obj.alternate_title = alternate_title

    """
    [Mandatory] 
    Indicates the type of alternate title presented on this record. These values reside in the Title Type Table.
    """
    title_type = line[79:81].strip()
    alternate_title_obj.title_type = title_type

    """
    [Conditional] 
    The code representing the language that this alternate
    title has been translated into. These values reside in the
    Language Code Table. A language Code Must be entered if
    the Title Type is equal to “OL” or “AL”
    """
    language_code = line[81:].strip()
    alternate_title_obj.language_code = language_code

    # print(alternate_title_obj.asdict())
    return alternate_title_obj
