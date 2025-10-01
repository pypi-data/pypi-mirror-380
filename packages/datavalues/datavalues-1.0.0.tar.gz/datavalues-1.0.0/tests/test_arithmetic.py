import pytest
from datavalues import GigaByte

def test_add_sub_div_basic():
    assert GigaByte(10) - GigaByte(5) == 5
    assert GigaByte(5) + GigaByte(5) == 10
    assert GigaByte(10) / GigaByte(2) == 5.0  # truediv returns float

def test_add_returns_equivalent_object():
    assert GigaByte(10) + GigaByte(5) == GigaByte(15)

def test_division_is_float_and_ratio():
    result = GigaByte(99) / GigaByte(41)
    assert isinstance(result, float)
    import math
    assert result == pytest.approx(99 / 41, rel=1e-12, abs=0.0)

def test_multiplication_rules():
    assert GigaByte(10) * 10 == GigaByte(100)
    with pytest.raises(TypeError):
        _ = GigaByte(2) * GigaByte(5)

def test_inplace_ops_behave():
    value = GigaByte(20)
    value += 15
    assert value == 35
    value -= 25
    assert value == 10
    value /= 5
    assert value == 2
    value //= 2
    assert value == 1
    value *= 25
    assert value == 25
