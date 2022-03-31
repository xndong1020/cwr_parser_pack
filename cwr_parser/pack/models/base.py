from dataclasses import dataclass


@dataclass
class EntityBase:
    record_prefix: str

    @property
    def record_type(self) -> str:
        return self.record_prefix[:3] if len(self.record_prefix) == 19 else None

    @property
    def transaction_sequence_number(self) -> str:
        return self.record_prefix[3:11] if len(self.record_prefix) == 19 else None

    @property
    def record_sequence_number(self) -> str:
        return self.record_prefix[11:19] if len(self.record_prefix) == 19 else None

    def __init__(self, record_prefix: str):
        self.record_prefix = record_prefix

    def __getitem__(self, key: str):
        return getattr(self, key)

    def asdict(self) -> dict:
        """
        Custom method to return a dict which is selective.
        """
        tmpDict = {}
        for k, v in self.__dict__.items():
            tmpDict[k] = v
        # Now we need to add attr5 which by default won't be picked up
        # by the standard __dict__ method because it is a pure property
        tmpDict["record_type"] = self.record_type
        tmpDict["transaction_sequence_number"] = self.transaction_sequence_number
        tmpDict["record_sequence_number"] = self.record_sequence_number
        return tmpDict
