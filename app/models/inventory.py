from app.utils import validators as valid

class Resource:

    def __init__(self, name, manufacturer, total=0, allocated=0):
        self._name = name
        self._manufacturer = manufacturer
        self._total = total
        if not valid.validate_integer('allocated', allocated, 0, self._total,\
            "The demand is greater than the total available.",\
            "The demand cannot be less than zero."):
            self._total -= allocated
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


    @property
    def manufacturer(self):
        return self._manufacturer


    def claim(self, n):
        if not valid.validate_integer('claim', n, 0, self._total,\
            custom_max_message="The demand is greater than the total available."):
            self._total -= n
            self._allocated += n


    def freeup(self, n):
        if not valid.validate_integer('claim', n, 0, self._total,\
            custom_max_message="The demand is greater than the total available."):
            if n <= self._allocated:
                self._allocated -= n
                self._total += n


    def died(self):
        self._total = 0
        self._allocated = 0


    def purchased(self, n):
        if not valid.validate_integer('purchased', n):
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

    def __init__(self, interface, name, manufacturer, total=0, allocated=0):
        super().__init__(name, manufacturer, total, allocated)
        self.interface = interface
        
    def __repr__(self):
        return f'SSD(interface={self.interface}, name={self.name}, manufacturer={self.manufacturer}, '\
                f'total={self.total}, allocated={self.allocated})'


r = Resource('Mouse X33', 'Razor', 5)
cpu = CPU(8, '22', 12, '13900K', 'INTEL', 20)
cpu.claim(20)
ssd = SSD('NVMe', 'EVO 860', 'Samsung', 70, 5)
