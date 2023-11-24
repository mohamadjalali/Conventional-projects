from pprint import pprint
from math import pi
from numbers import Real


class Resource:

    def __init__(self, name, manufacturer, total=0, allocated=0):
        self._name = name
        self._manufacturer = manufacturer
        self._total = total
        self._allocated = allocated


    def __str__(self):
        pass


    def __repr__(self):
        return f'Resource(name={self.name}, manufacturer={self.manufacturer}, '\
                f'total={self.total}, allocated={self.allocated})'


    @property
    def total(self):
        return self._total


    @property
    def allocated(self):
        return self._allocated


    @property
    def name(self):
        return self._name


    def _error_handling(self, n):
        if not isinstance(n, Real):
            raise TypeError("The value must be 'real' number.")
        if n < 0:
            raise ValueError("The value must be non-zero.")
        return n


    @property
    def manufacturer(self):
        return self._manufacturer


    def claim(self, n):
        if self._error_handling(n):
            if n <= self._total:
                self._total -= n
                self._allocated += n
            else:
                raise ValueError("The demand is greater than the total available.")


    def freeup(self, n):
        if self._error_handling(n):
            if n <= self._allocated:
                self._allocated -= n
                self._total += n
            else:
                raise ValueError("'n' argument is given more than the total number of allocations.")


    def died(self):
        self._total = 0
        self._allocated = 0


    def purchased(self, n):
        self._total += n

    
    @property
    def category(self):
        return self.name.lower()



class CPU(Resource):

    def __init__(self, cores, socket, power_watts, name, manufacturer, total=0, allocated=0):
        super().__init__(name, manufacturer, total, allocated)
        self.cores   = cores
        self.socket  = socket
        self.power_watts = power_watts
    

    def __repr__(self):
        return f'CPU(name={self.name}, manufacturer={self.manufacturer},'\
                f'total={self.total}, allocated={self.allocated}, '\
                f'cores={self.cores}, socket={self.socket}, power_watts={self.power_watts})'


class Storage():
    
    def __init__(self, capacity_GB):
        self.capacity_GB = capacity_GB
        


class HDD(Resource):
    
    def __init__(self, size, rpm):
        self.size = size
        self.rpm  = rpm



class SSD(Resource):

    def __init__(self, interface):
        self.interface = interface



r = Resource('Mouse X33', 'Razor', 5)
cpu = CPU(8, '22', 12, '13900K', 'INTEL', 20)
cpu.claim(9)
print(repr(cpu))

