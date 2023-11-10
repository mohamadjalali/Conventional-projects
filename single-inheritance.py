from pprint import pprint
from math import pi
from numbers import Real


class Circle:

    def __init__(self, r):
        self._set_radius(r)
        self._area  = None
        self._perimeter = None


    @property
    def radius(self):
        return self._r


    def _set_radius(self, r):
        if isinstance(r, Real) and r > 0:
            self._r = r
            self._area = None
            self._perimeter = None
        else:
            raise ValueError('Radius must be a positive real number.')


    @radius.setter
    def radius(self, r):
       self._set_radius(r) 


    @property
    def area(self):
        if self._area is None:
            self._area = pi * (self.radius ** 2)
        return self._area

    
    @property
    def perimeter(self):
        if self.perimeter is None:
            self._perimeter = 2 * pi * self.radius
        return self._perimeter



class UnitCircle(Circle):
    
    def __init__(self, r):
        super().__init__(r)


    @property
    def radius(self):
        return super().radius


if __name__ == "__main__":
    u = UnitCircle(50)
    u._set_radius(100)
    print(u.radius)

