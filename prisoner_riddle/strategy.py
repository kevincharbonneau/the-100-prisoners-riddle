import random
from prisoner_riddle.models import Prisoner, Room


def open_boxes_strategically(prisoner: Prisoner, room: Room, try_count: int):
    number = prisoner.number

    for i in range(try_count):
        # print(f"prisoner #{prisoner.number} is at try #{i + 1}" +
        #       " and is opening box #{number}")
        index, number = room.look(number)
        # print(f"he revealed paper #{number}")
        if number == prisoner.number:
            # room.remove(index)
            return True

    return False


def open_boxes_random(prisoner: Prisoner, room: Room, try_count: int):
    for i in range(try_count):
        # print(f"prisoner #{prisoner.number} is at try #{i + 1}" +
        #       " and is opening box #{number}")
        index, number = room.look(random.randint(1, (try_count * 2)))
        # print(f"he revealed paper #{number}")
        if number == prisoner.number:
            # room.remove(index)
            return True

    return False
