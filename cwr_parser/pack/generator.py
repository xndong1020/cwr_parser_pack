import json
from typing import List

from .record_processor import record_processor

from music_metadata.edi.file import EdiFile

import pandas as pd


def _base_generator(filename: str) -> List:
    def readFile(filename):
        filehandle = open(filename, "rb")
        return filehandle

    ediFile = EdiFile(readFile(filename))

    header = ediFile.get_header()
    # print("header", header)
    submitter_data = header.get_submitter_dict(2)
    # print(json.dumps(submitter_data, indent=4, sort_keys=True))

    records = []

    for group in ediFile.get_groups():
        # print('Group Name - ', group)
        # print('Group Header -', group.header())
        for transaction in group.get_transactions():
            if not transaction.valid and transaction.errors:
                for error in transaction.errors:
                    print("error - ", error)
            else:
                for record in transaction.records:
                    result = record_processor(record.record_type, record.line)
                    if result is not None:
                        records.append(result.asdict())

        # print('Group trailer -', group.trailer())

        return records


def json_generator(filename: str) -> None:
    records = _base_generator(filename)
    # Directly from dictionary
    with open("json_data.json", "w") as outfile:
        json.dump(records, outfile)


def csv_generator(filename: str) -> None:
    records = _base_generator(filename)
    dfd = pd.DataFrame(records)
    dfd.to_csv("data.csv", index=True)
