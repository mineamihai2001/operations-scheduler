import datetime
import os
import json

from domain.Room import Room


class RoomManager:
    rooms: list[Room]

    def __init__(self) -> None:
        self.rooms = list()

    def add(self, room: Room):
        self.rooms.append(room)

    def remove(self, room: Room):
        self.rooms.remove(room)

    def get_by_name(self, room_name: str) -> Room | None:
        return list(filter(lambda x: x.name == room_name, self.rooms))[0]

    def remove_by_name(self, room_name: str) -> bool:
        room: Room = list(filter(lambda x: x.name == room_name, self.rooms))[0]
        self.remove(room)
        return True if room else False

    def serialize(self) -> dict[str, list[dict[str, float]]]:
        serialized_rooms = [room.serialize() for room in self.rooms]
        return {k: v for d in serialized_rooms for k, v in d.items()}

    def save(self):
        out:str = os.path.join(f"saved{os.path.sep}serialized_rooms_manager_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json")
        with open(out, "w+") as file:
            _json = json.dumps(self.serialize())
            file.write(_json)

    def print_all(self) -> None:
        print(self.serialize())
