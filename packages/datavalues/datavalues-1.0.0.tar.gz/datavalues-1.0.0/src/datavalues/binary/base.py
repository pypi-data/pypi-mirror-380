from datavalues.base.core import BaseDataClass

class BinaryByteClass(BaseDataClass):
    _type_factor = 2

class BinaryBitClass(BaseDataClass):
    _type_factor = 2
    _is_bits = True