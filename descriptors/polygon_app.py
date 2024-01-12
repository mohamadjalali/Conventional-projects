from pprint import pprint
from collections.abc import Sequence



class Int:
    
    def __init__(self, min_length=None, max_length=None):
        self.min_length = min_length
        self.max_length = max_length


    def __set_name__(self, owner_class, prop_name):
        self.name = prop_name

    
    def __set__(self, instance, value):

        if not isinstance(value, int):
            raise ValueError("{self.name} must be an integer")

        if self.min_length is not None and value < self.min_length:
            raise ValueError(f"{self.name} least be at {self.min_length}")

        if self.max_length is not None and value > self.max_length:
            raise ValueError(f"{self.name} value cannot be greater than {self.max_length}.")

        instance.__dict__[self.name] = value

    
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        return instance.__dict__.get(self.name, None)

    

class Point2D:
    x = Int(0, 600)
    y = Int(0, 600)

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
   
    def __repr__(self):
        return f'Person(x={self.x}, y={self.y})'


    def __str__(self):
        return f'x={self.x}, y={self.y}'





class PolygonValidation:

    def __init__(self, min_length=None, max_length=None):
        self.min_length = min_length
        self.max_length = max_length


    def __set_name__(self, owner_cls, name):
        self.name = name


    def __set__(self, instance, value):
        if not isinstance(value, Sequence):
            raise ValueError(f"{self.name} must be a sequence type")

        if self.min_length is not None and len(value) < self.min_length:
            raise ValueError(f"{self.name} must contain at least {self.min_length} elements.")

        if self.max_length is not None and len(value) > self.max_length:
            raise ValueError(f"{self.name} cannot contain more than {self.max_length} elements.")
        
        for index, item in enumerate(value):
            if not isinstance(item, Point2D):
                raise ValueError(f"Item at index {index} is not a Point instance.")

        instance.__dict__[self.name] = list(value)


    def __get__(self, instance, owner_cls):
        if instance is None:
            return self
        
        if self.name not in instance.__dict__:
            instance.__dict__[self.name] = []
        return instance.__dict__.get(self.name, None)



class Polygon:
    vertices = PolygonValidation(min_length=3, max_length=4)

    def __init__(self, *vertices):
        self.vertices = vertices


    def append(self, value):
        if not isinstance(value, Point2D):
            raise ValueError('Can only append Point2D instances')
        
        max_length = type(self).vertices.max_length
        if max_length is not None and len(self.vertices) >= max_length:
            raise ValueError(f"Vetices length is at max ({max_length})")
        
        self.vertices.append(value)
    
    
    def __iadd__(self, other):
        self.append(other)
        return self


    def __contains__(self, pt):
        pass


