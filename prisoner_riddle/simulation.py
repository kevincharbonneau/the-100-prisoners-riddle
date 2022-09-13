from typing import Callable
from prisoner_riddle.models import Prison, Room


def simulate(count: int, strategy: Callable):
    prison = Prison(count)
    room = Room(count)

    if (count % 2) != 0:
        raise ValueError("Count should be able to be divided by 2.")

    try_count = int(count / 2)

    for prisoner in prison.prisoners:
        found = strategy(prisoner, room, try_count)
        if not found:
            return False
    
    return True
