class Const(type):
    def __setattr__(cls, key, value):
        raise TypeError('The class {} is a const class and mutating its attributes is forbidden.'.format(cls.__name__))
