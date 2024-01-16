from numbers import Integral


class Validation:

    def __init__(self, type_, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value
        self._type = type_


    def __set_name__(self, owner_class, prop_name):
        self.prop_name = prop_name


    def __set__(self, instance, value):
        if not isinstance(value, self._type):
            raise ValueError(f"{self.prop_name} must be integer value")
        
        if self.min_value is not None and len(value) < self.min_value:
            raise ValueError(f"{self.prop_name} must least at {self.min_value}")
        
        if self.max_value is not None and len(value) > self.max_value:
            raise ValueError(f"{self.prop_name} cannot greater than {self.max_value}")
        
        instance.__dict__[self.prop_name] = value


    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        return instance.__dict__.get(self.prop_name, None)




class CharField():
    x = Validation(str, max_value=100)


class IntegerField():
    x = Validation(Integral, 5, 100)



char    = CharField()
integer = IntegerField()

integer.x = 6
print(integer.__dict__)

