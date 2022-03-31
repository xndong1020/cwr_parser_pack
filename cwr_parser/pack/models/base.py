from dataclasses import dataclass


@dataclass
class EntityBase:
    record_prefix: str
    _record_type: str
    _transaction_sequence_number: str
    _record_sequence_number: str

    @property
    def record_type(self) -> str:
        self._record_type = (
            self.record_prefix[:3] if len(self.record_prefix) == 19 else None
        )
        return self._record_type

    @record_type.setter
    def record_type(self, value):
        self._record_type = value

    @property
    def transaction_sequence_number(self) -> str:
        self._transaction_sequence_number = (
            self.record_prefix[3:11] if len(self.record_prefix) == 19 else None
        )
        return self._transaction_sequence_number

    @transaction_sequence_number.setter
    def transaction_sequence_number(self, value):
        self._transaction_sequence_number = value

    @property
    def record_sequence_number(self) -> str:
        self._record_sequence_number = (
            self.record_prefix[11:19] if len(self.record_prefix) == 19 else None
        )
        return self._record_sequence_number

    @record_sequence_number.setter
    def record_sequence_number(self, value):
        self._record_sequence_number = value

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
            # hide private fields
            if not k.startswith("_"):
                tmpDict[k] = v
        tmpDict["record_type"] = self.record_type
        tmpDict["transaction_sequence_number"] = self.transaction_sequence_number
        tmpDict["record_sequence_number"] = self.record_sequence_number
        return tmpDict
