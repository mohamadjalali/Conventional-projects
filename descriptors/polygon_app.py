from pprint import pprint
from collections.abc import Sequence



class Int:
    
    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value


    def __set_name__(self, owner_class, prop_name):
        self.name = prop_name

    
    def __set__(self, instance, value):

        if not isinstance(value, int):
            raise ValueError("{self.name} must be an integer")

        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"{self.name} least be at {self.min_value}")

        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"{self.name} value cannot be greater than {self.max_value}.")

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
        return f'Point2D(x={self.x}, y={self.y})'


    def __str__(self):
        return f'x={self.x}, y={self.y}'


    def __eq__(self, other):
        return isinstance(other, Point2D) and self.x == other.x and self.y == other.y

    
    def __hash__(self):
        return hash((self.x, self.y))



class Point2DSequence:

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

        for index, item in enumerate(value):
            if not isinstance(item, Point2D):
                raise ValueError(f"Item at index {index} is not a Point2D instance")

        instance.__dict__[self.name] = list(value)


    def __get__(self, instance, owner_cls):
        if instance is None:
            return self
        
        if self.name not in instance.__dict__:
            instance.__dict__[self.name] = []
        return instance.__dict__.get(self.name, None)



class Polygon:
    vertices = Point2DSequence(min_length=3)

    def __init__(self, *vertices):
        self.vertices = vertices


    def append(self, pt):
        if not isinstance(pt, Point2D):
            raise ValueError('Can only append Point2D instances')
        
        max_length = type(self).vertices.max_length
        if max_length is not None and len(self.vertices) >= max_length:
            raise ValueError(f"Vetices length is at max ({max_length})")
        
        self.vertices.append(pt)
    
    
    def __iadd__(self, other):
        self.append(other)
        return self


    def __len__(self):
        return len(self.vertices)


    def __getitem__(self, index):
        return self.vertices[index]


    def __contains__(self, pt):
        return pt in self.vertices



class Triangle(Polygon):
    vertices = Point2DSequence(min_length=3, max_length=3)


class Rectangle(Polygon):
    vertices = Point2DSequence(min_length=4, max_length=4)


#p = Polygon(Point2D(10, 10), Point2D(5, 9), Point2D(15, 15))
#print(p.vertices)
