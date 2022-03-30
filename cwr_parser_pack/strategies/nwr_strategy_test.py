from cwr_parser_pack.strategies.nwr_strategy import nwr_strategy


valid_line = "NWR0000000000000000FIRST AND LAST                                                00000000052029           20180101            POP000000Y      ORI         LISA FIENE                                N00000000000U                                                  N"


def test_record_prefix_is_required():
    result = nwr_strategy("")
    assert len(result["errors"]) > 0
    assert "record prefix is missing. " in result["errors"]

    result = nwr_strategy(valid_line)
    assert len(result["errors"]) == 0
    assert "record prefix is missing. " not in result["errors"]

def test_work_titlex_is_required():
    result = nwr_strategy("")
    assert len(result["errors"]) > 0
    assert "work title is missing. " in result["errors"]

    result = nwr_strategy(valid_line)
    assert len(result["errors"]) == 0
    assert "work title is missing. " not in result["errors"]

def test_submitter_work_is_required():
    result = nwr_strategy("")
    assert len(result["errors"]) > 0
    assert "submitter work is missing. " in result["errors"]

    result = nwr_strategy(valid_line)
    assert len(result["errors"]) == 0
    assert "submitter work is missing. " not in result["errors"]

def test_musical_work_is_required():
    result = nwr_strategy("")
    assert len(result["errors"]) > 0
    assert "musical work distribution is missing. " in result["errors"]

    result = nwr_strategy(valid_line)
    assert len(result["errors"]) == 0
    assert "musical work distribution is missing. " not in result["errors"]

def test_recorded_indicator_is_required():
    result = nwr_strategy("")
    assert len(result["errors"]) > 0
    assert "recorded indicator is missing. " in result["errors"]

    result = nwr_strategy(valid_line)
    assert len(result["errors"]) == 0
    assert "recorded indicator is missing. " not in result["errors"]
