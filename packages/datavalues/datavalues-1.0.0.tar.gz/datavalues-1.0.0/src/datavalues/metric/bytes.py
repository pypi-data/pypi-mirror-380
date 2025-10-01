from datavalues.metric.base import MetricByteClass

class KiloByte(MetricByteClass):
    _unit_factor = 1

class MegaByte(MetricByteClass):
    _unit_factor = 2

class GigaByte(MetricByteClass):
    _unit_factor = 3

class TeraByte(MetricByteClass):
    _unit_factor = 4

class PetaByte(MetricByteClass):
    _unit_factor = 5

class ExaByte(MetricByteClass):
    _unit_factor = 6

class ZettaByte(MetricByteClass):
    _unit_factor = 7

class YottaByte(MetricByteClass):
    _unit_factor = 8

class RonnaByte(MetricByteClass):
    _unit_factor = 9

class QuettaByte(MetricByteClass):
    _unit_factor = 10