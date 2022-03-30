from strategies import (
    spu_strategy,
    nwr_strategy,
    spt_strategy,
    opu_strategy,
    swr_strategy,
    swt_strategy,
    pwr_strategy,
    owr_strategy,
    per_strategy,
    rec_strategy,
    alt_strategy,
    orn_strategy,
    rev_strategy,
)

options = {
    "SPU": spu_strategy,  # SPU: Publisher Controlled By Submitter
    "OPU": opu_strategy,  # OPU: Other Publisher
    "NWR": nwr_strategy,  # NWR: New work record 4.2
    "REV": rev_strategy,  # REV: Revised Registration 4.3
    "SPT": spt_strategy,  # SPT: Publisher Territory of Control
    "SWR": swr_strategy,  # SWR: Writer Controlled By Submitter
    "OWR": owr_strategy,  # OWR: Other Writer
    "SWT": swt_strategy,  # SWT: Writer Territory of Control
    "PWR": pwr_strategy,  # PWR: Publisher For Writer
    "PER": per_strategy,  # PER: Performing Artist 5.17
    "REC": rec_strategy,  # REC: Recording Detail 5.19
    "ALT": alt_strategy,  # ALT: Alternate Title 5.13
    "ORN": orn_strategy,  # ORN: Work Origin 5.20
}


def record_processor(record_type: str, line: str):
    return options[record_type](line)
    # if (
    #     record_type == "NWR"
    #     or record_type == "SPU"
    #     or record_type == "SPT"
    #     or record_type == "OPU"
    #     or record_type == "SWR"
    #     or record_type == "OWR"
    #     or record_type == "SWT"
    #     or record_type == "PWR"
    #     or record_type == "PER"
    #     or record_type == "REC"
    #     or record_type == "ALT"
    #     or record_type == "ORN"
    #     or record_type == "REV"
    # ):
    #     return options[record_type](line)
