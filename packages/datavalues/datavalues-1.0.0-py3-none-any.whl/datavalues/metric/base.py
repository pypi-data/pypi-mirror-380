from datavalues.base.core import BaseDataClass

class MetricByteClass(BaseDataClass):
    _type_factor = 1000

class MetricBitClass(BaseDataClass):
    _type_factor = 1000
    _is_bits = True