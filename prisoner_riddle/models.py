from random import shuffle
from dataclasses import dataclass
from typing import List


@dataclass
class Prisoner:
    number: int

@dataclass
class Box:
    paper_number: int
    box_number: int

class Room:
    _boxes: List[Box]

    def __init__(self, count:int) -> None:
        papers = list(range(1, count + 1))
        shuffle(papers)

        self._boxes = [Box(papers[i], i + 1) for i in range(count)]

    def _find(self, box_number: int):
        for i, box in enumerate(self.boxes):
            if box.box_number == box_number:
                return i
    
    def look(self, box_number: int):
        index = self._find(box_number)
        return index, self._boxes[index].paper_number

    def remove(self, index: int):
        self._boxes.pop(index)

    @property
    def boxes(self):
        return self._boxes

class Prison:
    _prisoners: List[Prisoner]
    _max: int

    def __init__(self, count:int) -> None:
        self._max = count
        self._prisoners = [Prisoner(i + 1) for i in range(count)]

    @property
    def prisoners(self):
        for i in range(self._max):
            yield self._prisoners[i]
