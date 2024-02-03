from functools import total_ordering
import operator


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
        self._value = value

    
    @property
    def modulus(self):
        return self._modulus

    
    def __repr__(self):
        return f'Mod({self.value}, {self.modulus})'
    

    def __int__(self):
        print('__int__ reper')
        return self.value
    
    
    def _get_value(self, other):
        if isinstance(self, int):
            return other % self.modulus
        if isinstance(other, Mod) and self.modulus == other.modulus:
            return other.value
        raise TypeError('Incompatible types.')

    
    def _perform_operation(self, other, op, *, in_place=False):
        other_value  = self._get_value(other)
        value_result = op(self.value, other_value)
        if in_place:
            self.value = value_result % self.modulus
            return self
        else:
            return Mod(value_result, self.modulus)

    
    def __eq__(self, other):
        other_value = self._get_value(other)
        return self.value == other_value
        

    def __hash__(self):
        return hash((self.value, self.modulus))


    def __neg__(self):
        return Mod(-self.value, self.modulus)


    def __add__(self, other):
        return self._perform_operation(other, operator.pow)


    def __sub__(self, other):
        return self._perform_operation(other, operator.pow)

    
    def __mul__(self, other):
        return self._perform_operation(other, operator.pow)


    def __pow__(self, other):
        return self._perform_operation(other, operator.pow)

    
    def __iadd__(self, other):
        return self._perform_operation(other, operator.pow, in_place=True)

    
    def __isub__(self, other):
        return self._perform_operation(other, operator.pow, in_place=True)
    

    def __imul__(self, other):
        return self._perform_operation(other, operator.pow, in_place=True)

    def __ipow__(self, other):
        return self._perform_operation(other, operator.pow, in_place=True)


    def __lt__(self, other):
        other_value = self._get_value(other)
        return self.value < other_value



if __name__ == "__main__":
    a = Mod(4, 12)  
    b = Mod(15, 12)
    print(a > b)

