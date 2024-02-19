import math
from pprint import pprint
from functools import wraps



def func_logger(fn):
    
    @wraps(fn)
    def inner(*args, **kwargs):
        result = fn(*args, **kwargs)
        print(f'log {fn.__qualname__} ({args}, {kwargs}) = {result}')
        return result
    return inner



def class_decorator(cls): 

    for name, obj in cls.__dict__.items():
        if callable(obj):
            if isinstance(obj, staticmethod):
                print(f'decorator static method {cls}, {name}')
                original_obj = obj.__func__
                decorator_func = func_logger(original_obj)
                method = staticmethod(decorator_func)
                setattr(cls, name, method)

            else:
                print(f'decorator instance method {cls}, {name}')
                original_obj = obj
                decorator_func = func_logger(original_obj)
                setattr(cls, name, decorator_func)

        elif isinstance(obj, classmethod):
            print(f'decorator class method {cls}, {name}')
            original_obj = obj.__func__
            decorator_func = func_logger(original_obj)
            method = classmethod(decorator_func)
            setattr(cls, name, method)
        
        elif isinstance(obj, property):
            print(f'decorator property {cls}, {name}')
            if obj.fget:
                obj = obj.getter(func_logger(obj.fget))
            if obj.fset:
                obj = obj.setter(func_logger(obj.fset))
            if obj.fdel:
                obj = obj.deleter(func_logger(obj.fdel))
            setattr(cls, name, obj)

    return cls



@class_decorator
class Person:


    def __init__(self, name):
        self._name = name


    def instance_method(self, a, b):
        print(f'instance_method called... {a}, {b}')


    @staticmethod
    def static_method(a, b):
        print(f'static_method called... {a}, {b}')


    @classmethod
    def class_method(cls, a, b):
        print(f'class_method called... {a}, {b}')


    @property
    def name(self):
        return self._name


p = Person('Mohammad')

#print(p.instance_method(1, 2),'\n')
#print(p.static_method(1, 2), '\n')
#print(p.class_method(1, 2))
pprint(Person.__dict__)
