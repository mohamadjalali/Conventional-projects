from functools import total_ordering

@total_ordering
class Mod:

    def __init__(self, value,  modulus):
        if not isinstance(modulus, int):
            raise TypeError("Modulus must be integer number")
        if modulus <= 0:
            raise ValueError("Modulus must be positive number")
        if not isinstance(value, int):
            raise TypeError("Value argument not valid, must be integer number")
        self._modulus = modulus
        self._value = value % modulus


    @property
    def value(self):
        return self._value
    
    
    @value.setter
    def value(self, value):
        self._value += value

    
    @property
    def modulus(self):
        return self._modulus

    
    def __repr__(self):
        return f'Mod({self.value}, {self.modulus})'
    

    def __int__(self):
        print('__int__ reper')
        return self.value
    

    def __eq__(self, other):
        if isinstance(other, Mod):
            if self.modulus != other.modulus:
                return NotImplemented
            else:
                return self.value == other.value

        elif isinstance(other, int):
            return other % self.modulus == self.value
        else:
            return NotImplemented

    
    def __hash__(self):
        return hash((self.value, self.modulus))


    def __le__(self, other):
        return self.value <= other.value

mod = Mod(16, 6)
mod_1 = 22
print(hash(mod))
