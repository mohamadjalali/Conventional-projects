from app.utils.validators import validate_integer


class Resource:

    def __init__(self, name, manufacturer, total=0, allocated=0):
        self._name = name
        self._manufacturer = manufacturer

        validate_integer('total', total, min_value=0)
        self._total = total

        validate_integer(
            'allocated', allocated, 0, total,\
            "The demand cannot be less than zero.",\
            "The demand is greater than the total available."
        )
        self._allocated = allocated

    
    @property
    def name(self):
        return self._name


    @property
    def manufacturer(self):
        """
        Returns:
            str: the resource manufacturer
        """
        return self._manufacturer


    @property
    def total(self):
        """
        Returns:
            int: the total inventory count
        """
        return self._total


    @property
    def allocated(self):
        """
        Returns:
            int: number of resources in use
        """
        return self._allocated
    
    
    @property
    def category(self):
        return type(self).__name__.lower()

    
    @property
    def available(self):
        return self.total - self.allocated

    
    def __str__(self):
        return self.name


    def __repr__(self):
        return f'{self.name} ({self.category} - {self.manufacturer}): '\
               f'total={self.total}, allocated={self.allocated}'

    
    def claim(self, num):
        validate_integer(
            'num', num, 1, self.available,
            custom_max_message="The demand is greater than the total available."
            )
        self._allocated += num

    
    def freeup(self, num):
        """
        Retrun an inventory item to the available pool

        Args:
            num (int): Number of items to return (cannot exceed number in use)

            Returns:
                
        """
        validate_integer(
            'num', num, 1, self._allocated,
            custom_max_message="Cannot return more than allocated."
            )
        self._allocated -= num


    def died(self, num):
        """
        Number of items to deallocate and remove from the inventory pool
        altogether

        Args:
            num (int): Number of items that have died

            Returns:
                
        """
        validate_integer(
            'num', num, 1, self._allocated,
            custom_max_message="Cannot retire more than allocated."
            )
        self._total -= num
        self._allocated -= num


    def purchased(self, num):
        """
        Number of items to deallocate and remove from the inventory pool
        altogether

        Args:
            num (int): Number of items that have died

            Returns:
                
        """
        validate_integer('num', num, 1)
        self._total += num
    

    
class CPU(Resource):

    def __init__(
            self, name, manufacturer, total, allocated,
            cores, socket, power_watts
        ):
        super().__init__(name, manufacturer, total, allocated)

        validate_integer('cores', cores, 1)
        validate_integer('power_watts', power_watts, 1)

        self._cores  = cores
        self._socket = socket
        self._power_watts = power_watts
    

    @property
    def cores(self):
        """
        The cores count for this CPU

        Returns:
            int
        """
        return self._cores


    @property
    def socket(self):
        """
        The socket type for this CPU

        Returns:
            str
        """
        return self._socket

    
    @property
    def power_watts(self):
        """
        The rated wattage of this CPU

        Returns:
            int
        """
        return self._power_watts


    def __repr__(self):
        return f'{self.category}: {self.name} ({self.socket} - x{self.cores})'



class Storage(Resource):
    """
    A base class for storage devices - probably not used directly
    """
    
    def __init__(self, name, manufacturer, total, allocated, capacity_gb):
        """
        
        Args:
            name (str): display name of resource
            manufacturer (str): resource manufacturer
            total (int): current total amount of resources
            allocated (int): current count of in-use resources
            capacity_gb (int): storage capacity (in GB)
        """

        super().__init__(name, manufacturer, total, allocated)
        validate_integer('capacity_gb', capacity_gb, 1)
        self._capacity_gb = capacity_gb
        

    @property
    def capacity_gb(self):
        """
        Indicated the capacity (in GB) of the storage device

        Returns:
            int
        """
        return self._capacity_gb


    def __repr__(self):
        return f'{self.category}: {self.capacity_gb} GB'



class HDD(Storage):

    """

    Args:
        name (str): display name of resource
        manufacturer (str): resource manufacturer
        total (int): current total amount of resources
        allocated (int): current count of in-use resources
        capacity_gb (int): storage capacity (in GB)
        size (str): indicated the device size (must be either 2.5" or 3.5"
        rpm (int): revolutions per minute is a unit of measurement used to quantify rotational speed.
    """
    
    def __init__(self, name, manufacturer, total, allocated, capacity_gb, size, rpm):
        super().__init__(name, manufacturer, total, allocated, capacity_gb)
        
        if not size in ['2.5"', '3.5"']:
            raise ValueError(f'Invalid Hdd size. Must be one of 2.5" or 3.5"')
        validate_integer('rpm', rpm, 1_000, 50_000)

        self._size = size
        self._rpm  = rpm

    
    @property
    def size(self):
        """
        The HDD size (2.5" / 3.5"

        Returns:
            str
        """
        return self._size


    @property
    def rpm(self):
        """
        The HDD spin speed (rpm)

        Returns:
            int
        """
        return self._rpm
    

    def __repr__(self):
        s = super().__repr__()
        return f'{s} ({self.size}, {self.rpm} rpm)'



class SSD(Storage):
    """

    Args:
        name (str): display name of resource
        manufacturer (str): resource manufacturer
        total (int): current total amount of resources
        allocated (int): current count of in-use resources
        capacity_gb (int): storage capacity (in GB)
        interface (str) indicates the device interface (e.g. PCIe NVMe 3.0 x4)
    """

    def __init__(
            self, name, manufacturer, total, allocated,
            capacity_gb, interface
        ):
        super().__init__(name, manufacturer, total, allocated, capacity_gb)
        self._interface = interface


    @property
    def interface(self):
        """
        interface used by SSD (e.g. PCIe NVMe 3.0 x4)

        Returns:
           str 
        """
        return self._interface

    
    def __repr__(self):
        s = super().__repr__()
        return f'{s} ({self.interface})'


"""
hdd_resource =  {
        'name': 'Blue WD10EZEX',
        'manufacturer': 'Western Digital',
        'total': 20,
        'allocated': 8,
        'capacity_gb': 1024,
        'size': '3.5"',
        'rpm': 5400
    }


ssd_resource =  {
        'name': 'EVO 870',
        'manufacturer': 'SAMSUNG',
        'total': 20,
        'allocated': 8,
        'capacity_gb': 500,
        'interface': 'SATA III'
    }

if __name__ == '__main__':
    print(repr(HDD(**hdd_resource)))
    print(repr(SSD(**ssd_resource)))
"""
