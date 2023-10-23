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
        self._value = value

    
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


    def __neg__(self):
        return Mod(-self.value, self.modulus)


    def __add__(self, other):
        if isinstance(other, Mod) and self.modulus == other.modulus:
            return Mod(self.value + other.value, self.modulus)
        elif isinstance(other, int):
            return Mod(self.value + other, self.modulus)
        return NotImplemented


    def __sub__(self, other):
        if isinstance(other, Mod) and self.modulus == other.modulus:
            return Mod(self.value - other.value, self.modulus)
        elif isinstance(other, int):
            return Mod(self.value - other, self.modulus)
        return NotImplemented


    def __mul__(self, other):
        # we can use both formula: (A * (B Modulu C) Modulu C) OR (A * B) Modulu C
        if isinstance(other, Mod) and self.modulus == other.modulus:
            return Mod(self.value * (other.value % self.modulus), self.modulus)
        elif isinstance(other, int):
            return Mod(self.value * (other % self.modulus), self.modulus)
        return NotImplemented
       

    def __pow__(self, other):
        # we can use both formula: (A ** (B Modulu C) Modulu C) OR (A ** B) Modulu C
        if isinstance(other, Mod) and self.modulus == other.modulus:
            return Mod(self.value ** (other.value % self.modulus), self.modulus)
        elif isinstance(other, int):
            return Mod(self.value ** (other % self.modulus), self.modulus)
        return NotImplemented

    
    def __iadd__(self, other):
        if isinstance(other, Mod) and self.modulus == other.modulus:
            self.value = (self.value + other.value) % self.modulus
            return self
        elif isinstance(other, int):
            self.value = (self.value + other) % self.modulus
            return self
        return NotImplemented


    def __isub__(self, other):
        if isinstance(other, Mod) and self.modulus == other.modulus:
            self.value = (self.value - other.value) % self.modulus
            return self
        elif isinstance(other, int):
            self.value = (self.value - other) % self.modulus
            return self
        return NotImplemented


    def __imul__(self, other):
        if isinstance(other, Mod) and self.modulus == other.modulus:
            self.value = (self.value * other.value) % self.modulus
            return self
        elif isinstance(other, int):
            self.value = (self.value * (other % self.modulus)) % self.modulus
            return self
        return NotImplemented

    
    def __ipow__(self, other):
        if isinstance(other, Mod) and self.modulus == other.modulus:
            self.value = (self.value ** other.value) % self.modulus
            return self
        elif isinstance(other, int):
            self.value = (self.value ** (other % self.modulus)) % self.modulus
            return self
        return NotImplemented


    def __lt__(self, other):
        if isinstance(other, Mod) and self.modulus == other.modulus:
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other % self.modulus
        return NotImplemented


    def _is_compatible(self, other):
        return isinstance(other, Mod) or (isinstance(other, int) and self.modulus == other.modulus)



if __name__ == "__main__":
    print(Mod(3, 12) == Mod(15, 12))
    print(Mod(3, 12) +  Mod(25, 7))
