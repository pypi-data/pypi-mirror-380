import pytest
from datavalues import (
    Bit, KiloBit, MegaBit, GigaBit, TeraBit, PetaBit, ExaBit, ZettaBit, YottaBit, RonnaBit, QuettaBit,
    Byte, KiloByte, MegaByte, GigaByte, TeraByte, PetaByte, ExaByte, ZettaByte, YottaByte, RonnaByte, QuettaByte,
    KibiBit, MebiBit, GibiBit, TebiBit, PebiBit, ExbiBit, ZebiBit, YobiBit, RobiBit, QuebiBit,
    KibiByte, MebiByte, GibiByte, TebiByte, PebiByte, ExbiByte, ZebiByte, YobiByte, RobiByte, QuebiByte,
)

@pytest.mark.parametrize("higher,lower,factor", [
    # Metric bits (×1000)
    (KiloBit, Bit, 1000),
    (MegaBit, KiloBit, 1000),
    (GigaBit, MegaBit, 1000),
    (TeraBit, GigaBit, 1000),
    (PetaBit, TeraBit, 1000),
    (ExaBit, PetaBit, 1000),
    (ZettaBit, ExaBit, 1000),
    (YottaBit, ZettaBit, 1000),
    (RonnaBit, YottaBit, 1000),
    (QuettaBit, RonnaBit, 1000),
])
def test_metric_bit_conversions(higher, lower, factor):
    assert higher(1).convert(lower) == factor

@pytest.mark.parametrize("higher,lower,factor", [
    # Metric bytes (×1000)
    (KiloByte, Byte, 1000),
    (MegaByte, KiloByte, 1000),
    (GigaByte, MegaByte, 1000),
    (TeraByte, GigaByte, 1000),
    (PetaByte, TeraByte, 1000),
    (ExaByte, PetaByte, 1000),
    (ZettaByte, ExaByte, 1000),
    (YottaByte, ZettaByte, 1000),
    (RonnaByte, YottaByte, 1000),
    (QuettaByte, RonnaByte, 1000),
])
def test_metric_byte_conversions(higher, lower, factor):
    assert higher(1).convert(lower) == factor

@pytest.mark.parametrize("higher,lower,factor", [
    # Binary bits (×1024)
    (KibiBit, Bit, 1024),
    (MebiBit, KibiBit, 1024),
    (GibiBit, MebiBit, 1024),
    (TebiBit, GibiBit, 1024),
    (PebiBit, TebiBit, 1024),
    (ExbiBit, PebiBit, 1024),
    (ZebiBit, ExbiBit, 1024),
    (YobiBit, ZebiBit, 1024),
    (RobiBit, YobiBit, 1024),
    (QuebiBit, RobiBit, 1024),
])
def test_binary_bit_conversions(higher, lower, factor):
    assert higher(1).convert(lower) == factor

@pytest.mark.parametrize("higher,lower,factor", [
    # Binary bytes (×1024)
    (KibiByte, Byte, 1024),
    (MebiByte, KibiByte, 1024),
    (GibiByte, MebiByte, 1024),
    (TebiByte, GibiByte, 1024),
    (PebiByte, TebiByte, 1024),
    (ExbiByte, PebiByte, 1024),
    (ZebiByte, ExbiByte, 1024),
    (YobiByte, ZebiByte, 1024),
    (RobiByte, YobiByte, 1024),
    (QuebiByte, RobiByte, 1024),
])
def test_binary_byte_conversions(higher, lower, factor):
    assert higher(1).convert(lower) == factor
