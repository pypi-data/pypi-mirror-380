from datavalues.base.core import BaseDataClass

__all__ = ['Bit', 'Byte']

class Bit(BaseDataClass):
    _unit_factor = 0
    _is_bits = True

class Byte(BaseDataClass):
    _unit_factor = 0