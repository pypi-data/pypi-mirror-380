from datavalues import Byte, GigaByte

def test_relational_ops():
    assert GigaByte(1) > Byte(1)
    assert Byte(1) < GigaByte(1)

def test_equality_and_ordering():
    assert GigaByte(1) == GigaByte(1)
    assert GigaByte(1) <= GigaByte(1)
    assert GigaByte(1) >= GigaByte(1)
    assert GigaByte(1) >= Byte(1)
    assert Byte(1) <= GigaByte(1)
