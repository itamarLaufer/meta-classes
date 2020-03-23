import pytest

from const import Const


class ConstClass(object):
    __metaclass__ = Const

    fruit = 'banana'

    def __init__(self, name):
        self.name = name

    def greet(self):
        print 'Hi it\'s {} and according to everyone the best fruit is {}.'.format(self.name, self.fruit)


def test_const_class():
    with pytest.raises(TypeError):
        ConstClass.fruit = 'apple'

    with pytest.raises(TypeError):
        ConstClass.greet = lambda (self): 7

    with pytest.raises(TypeError):
        ConstClass.__init__ = int.__init__


def test_instance_properties_are_mutable():
    instance = ConstClass('Jack')
    instance.name = 'Martin'
    instance.fruit = 'apple'
    instance.vegetable = 'tomato'
