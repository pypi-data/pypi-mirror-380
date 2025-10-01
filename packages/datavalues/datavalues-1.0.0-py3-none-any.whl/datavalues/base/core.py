from abc import ABCMeta as _ABCMeta
from functools import wraps as _wraps


class BaseDataClass(metaclass=_ABCMeta):
    """Base Data Model for use in the package

    Args:
        metaclass (_type_, optional): _description_. Defaults to _ABCMeta.

    Raises:
        TypeError: _description_
        TypeError: _description_
        TypeError: _description_
        RuntimeError: _description_
        ValueError: _description_

    Returns:
        _type_: _description_
    """
    
    # Factorial variables
    ## These variables are used in the `to_bits` method; more details on that in the method itself
    _type_factor = 0
    _unit_factor = 0
    _is_bits = False
    
    _unit = '' # Unit name to display (i.e. MB or gb)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.value})'

    def __str__(self):
        return f'{self.value} {self.__class__.__name__}s'
    
    def __init__(self, value: float|int):
        self.value = value

    def to_bits(self):
        """This method will convert any data unit into the base bits unit for further maths

        Returns:
            int|float: The converted value in bits
        """
        calc = (self.value * (self._type_factor ** self._unit_factor))
        if self._is_bits:
            return calc
        else:
            return calc * 8
        
    @classmethod
    def from_bits(cls, value):
        calc = value / (cls._type_factor ** cls._unit_factor)
        if cls._is_bits:
            return cls(calc)
        else:
            return cls(calc / 8)

    def convert(self, unit):
        if not issubclass(unit, BaseDataClass):
            raise TypeError(f'Conversion target must be a data class. Supplied: {unit.__class__}')
        return unit.from_bits(self.to_bits())

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return self.__class__(self.value + other)
        if issubclass(type(other), BaseDataClass):
            return self.__class__.from_bits(self.to_bits() + other.to_bits())
        raise ValueError(f"Got invalid input type: {type(other)}")

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return self.from_bits(self.value - other)
        if issubclass(type(other), BaseDataClass):
            return self.__class__.from_bits(self.to_bits() - other.to_bits())
        raise ValueError(f"Got invalid input type: {type(other)}")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self.__class__(self.value * other)
        if issubclass(type(other), BaseDataClass):
            raise TypeError('Cannot multiply data objects')
        raise ValueError(f"Got invalid input type: {type(other)}")

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return self.__class__(self.value / other)
        if issubclass(type(other), BaseDataClass):
            return self.to_bits() / other.to_bits()
        raise ValueError(f"Got invalid input type: {type(other)}")

    def __floordiv__(self, other):
        if isinstance(other, (int, float)):
            return self.__class__(self.value // other)
        if issubclass(type(other), BaseDataClass):
            return self.to_bits() // other.to_bits()
        raise ValueError(f"Got invalid input type: {type(other)}")

    def __iadd__(self, other):
        if isinstance(other, (int, float)):
            return self.__class__(self.value + other)
        if issubclass(type(other), BaseDataClass):
            return self.__class__.from_bits(self.to_bits() + other.to_bits())
        raise ValueError(f"Got invalid input type: {type(other)}")

    def __isub__(self, other):
        if isinstance(other, (int, float)):
            return self.__class__(self.value - other)
        if issubclass(type(other), BaseDataClass):
            return self.__class__.from_bits(self.to_bits() - other.to_bits())
        raise ValueError(f"Got invalid input type: {type(other)}")

    def __imul__(self, other):
        if isinstance(other, (int, float)):
            return self.__class__(self.value * other)
        if issubclass(type(other), BaseDataClass):
            raise TypeError('Cannot multiply data objects')
        raise ValueError(f"Got invalid input type: {type(other)}")

    def __itruediv__(self, other):
        if isinstance(other, (int, float)):
            return self.__class__(self.value / other)
        if issubclass(type(other), BaseDataClass):
            return self.__class__.from_bits(self.to_bits() / other.to_bits())
        raise ValueError(f"Got invalid input type: {type(other)}")

    def __ifloordiv__(self, other):
        if isinstance(other, (int, float)):
            return self.__class__(self.value // other)
        if issubclass(type(other), BaseDataClass):
            return self.__class__.from_bits(self.to_bits() // other.to_bits())
        raise ValueError(f"Got invalid input type: {type(other)}")

    def __eq__(self, other):
        if isinstance(other, (int, float)):
            return self.value == other
        if issubclass(type(other), BaseDataClass):
            return self.to_bits() == other.to_bits()
        raise ValueError(f"Got invalid input type: {type(other)}")

    def __lt__(self, other):
        if isinstance(other, (int, float)):
            return self.value < other
        if issubclass(type(other), BaseDataClass):
            return self.to_bits() < other.to_bits()
        raise ValueError(f"Got invalid input type: {type(other)}")

    def __gt__(self, other):
        if isinstance(other, (int, float)):
            return self.value > other
        if issubclass(type(other), BaseDataClass):
            return self.to_bits() > other.to_bits()
        raise ValueError(f"Got invalid input type: {type(other)}")

    def __le__(self, other):
        if isinstance(other, (int, float)):
            return self.value <= other
        if issubclass(type(other), BaseDataClass):
            return self.to_bits() <= other.to_bits()
        raise ValueError(f"Got invalid input type: {type(other)}")

    def __ge__(self, other):
        if isinstance(other, (int, float)):
            return self.value >= other
        if issubclass(type(other), BaseDataClass):
            return self.to_bits() >= other.to_bits()
        raise ValueError(f"Got invalid input type: {type(other)}")
