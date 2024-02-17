import math
from pprint import pprint
from functools import wraps



def func_logger(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        result = fn(*args, **kwargs)
        print(f'Log {fn.__qualname__}({args}, {kwargs}) = {result}')
        return result
    return inner


def class_logger(cls):
    for name, obj in vars(cls).items():
        if callable(obj):
            print('decorating:', cls, name)
            setattr(cls, name, func_logger(obj))
    return cls



@class_logger
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def greet(self):
        return f'Hello, my name is: {self.name}, and I am {self.age} years old'


p = Person('Mohammad', 28)
print(p.greet())
