from pprint import pprint
from domain.operations.Operation import Operation


class Room:
    name: str
    operations: list[Operation]

    def __init__(self, name: str, operations: list[Operation] = list()) -> None:
        self.name = name
        self.operations = operations.copy()

    def add_operation(self, operation: Operation):
        self.operations.append(operation)

    def serialize(self) -> dict[str, list[dict[str, float]]]:
        return {
            self.name: [
                {
                    "anaesthesia": operation.anaesthesia.procedure_length,
                    "surgical": operation.surgical.procedure_length,
                } for operation in self.operations
            ]
        }

    def print(self) -> None:
        pprint(self.serialize())
