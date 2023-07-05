from typing import List
from project.room import Room

class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: List[Room] = []

    @property
    def guests(self):
        return sum([r.guests for r in self.rooms])

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room) -> None:
        if room not in self.rooms:
            self.rooms.append(room)

    def take_room(self, room_number: int, people_amount: int) -> None:
        try:
            room = next(filter(lambda r: r.number == room_number, self.rooms))
            room.take_room(people_amount)

        except StopIteration:
            pass

    def free_room(self, room_number: int) -> None:
        try:
            room = next(filter(lambda r: r.number == room_number, self.rooms))
            room.free_room()
        except StopIteration:
            pass

    def status(self) -> str:
        free_rooms_numbers = []
        taken_rooms_numbers = []

        for r in self.rooms:
            if r.is_taken:
                taken_rooms_numbers.append(str(r.number))

            else:
                free_rooms_numbers.append(str(r.number))

        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {', '.join(free_rooms_numbers)}\n" \
               f"Taken rooms: {', '.join(taken_rooms_numbers)}"
