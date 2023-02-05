from domain.Room import Room
from domain.RoomManager import RoomManager
from domain.operations.Operation import Operation
from domain.operations.procedures.Anaesthesia import Anaesthesia
from domain.operations.procedures.Surgical import Surgical

data: dict[str, list[dict[str, float]]] = {
    "room_1": [
        {
            "anaesthesia": 3,
            "surgical": 4
        },
        {
            "anaesthesia": 2,
            "surgical": 3
        },
    ],
    "room_2": [
        {
            "anaesthesia": 3,
            "surgical": 5
        },
        {
            "anaesthesia": 1,
            "surgical": 2
        },
    ],
    "room_3": [
        {
            "anaesthesia": 2,
            "surgical": 4
        },
        {
            "anaesthesia": 2,
            "surgical": 4
        },
    ],
}

if __name__ == "__main__":
    room_manager = RoomManager()
    for name, room_details in data.items():
        room = Room(name)
        operations: list[Operation] = list()
        for operation_details in room_details:
            operation = Operation(Anaesthesia(operation_details["anaesthesia"]), Surgical(
                operation_details["surgical"]))
            room.add_operation(operation)
        room_manager.add(room)
    room_manager.print_all()
    room_manager.save()