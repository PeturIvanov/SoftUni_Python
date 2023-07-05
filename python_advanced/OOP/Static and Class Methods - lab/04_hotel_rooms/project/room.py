from typing import Optional


class Room:
    def __init__(self, number: int, capacity: int):
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False

    def take_room(self, amount_people: int) -> Optional[str]:
        if self.is_taken or self.capacity < amount_people:
            return f"Room number {self.number} cannot be taken"

        self.guests += amount_people
        self.is_taken = True

    def free_room(self) -> Optional[str]:
        if not self.is_taken:
            return f"Room number {self.number} is not taken"

        self.is_taken = False
        self.guests = 0
