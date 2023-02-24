from enum import Enum


class ProcedureType(Enum):
    ANAESTHESIA = "anaesthesia"
    SURGICAL = "surgical"


class Procedure:
    procedure_length: float
    type: ProcedureType

    def __init__(self, type: ProcedureType, procedure_length: float) -> None:
        self.type = type
        self.procedure_length = procedure_length

    def print(self) -> None:
        print(f"Procedure -> {self.type}")
