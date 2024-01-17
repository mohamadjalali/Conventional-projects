from numbers import Integral
from pprint import pprint


class BaseValidator:

    def __init__(self, min_=None, max_=None):
        self._min = min_
        self._max = max_


    def __set_name__(self, owner_class, prop_name):
        self.prop_name = prop_name


    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        return instance.__dict__.get(self.prop_name, None)
    

    def validate(self):
        # Thid will need to be implemented specifically by each subclass
        pass


    def __set__(self, instance, value):
        self.validate(value)
        instance.__dict__[self.prop_name] = value




class CharField(BaseValidator):

    def __init__(self, min_, max_):
        min_ = max(min_ or 0, 0)
        super().__init__(min_, max_)


    def validate(self, value):
        if not isinstance(value, str):
            raise ValueError(f"{self.prop_name} must be string character.")
        
        if self._min is not None and len(value) < self._min:
            raise ValueError(f"{self.prop_name} must least at {self._min}")
        
        if self._max is not None and len(value) > self._max:
            raise ValueError(f"{self.prop_name} cannot greater than {self._max}")



class IntegerField(BaseValidator):

    def validate(self, value):
        if not isinstance(value, Integral):
            raise ValueError(f"{self.prop_name} must be integer value")
        
        if self._min is not None and value < self._min:
            raise ValueError(f"{self.prop_name} must least at {self._min}")
        
        if self._max is not None and value > self._max:
            raise ValueError(f"{self.prop_name} cannot greater than {self._max}")


class Person:
    number = IntegerField(0, max_=100)
    name   = CharField(0, 10)



if __name__ == '__main__':
    p = Person()
    p.number = 100
    p.name = 'Mohammad' 
    print(p.number)
    print(p.name)
