import pytest
from stuff.accum import Accumulator


# @pytest.fixture
# def accum():
#     return Accumulator()


@pytest.mark.regression
def test_accumulator_init(accum):
    assert accum.count == 0


def test_accumulator_add_one(accum):
    accum.add()
    assert accum.count == 1


def test_accumulator_add_three(accum):
    accum.add(3)
    assert accum.count == 3


def test_accumulator_add_twice(accum):
    accum.add()
    accum.add(2)
    assert accum.count == 3


def test_accumulator_cannot_set_count_directly(accum):
    with pytest.raises(AttributeError):
        accum.count = 10
