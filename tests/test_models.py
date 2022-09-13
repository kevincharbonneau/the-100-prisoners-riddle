import pytest

from prisoner_riddle.models import Room


@pytest.fixture
def room():
    return Room(10)


def test_look(room: Room):
    room.boxes[0].paper_number = 1
    index, paper_number = room.look(1)
    
    assert index == 0
    assert paper_number == 1

def test_find(room: Room):
    index = room._find(1)
    assert index == 0

def test_remove_size_reduced(room: Room):
    room.remove(0)
    assert len(room.boxes) == 9

def test_remove_out_of_range(room: Room):
    room.remove(9)
    with pytest.raises(IndexError) as exc_info:
        foo = room.boxes[9]
        assert "list index out of range" in str(exc_info.value)
