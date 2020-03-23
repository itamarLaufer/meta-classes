import pytest
Const = None


class ConstClass(object):
    __metaclass__ = Const

    fruit = 'banana'

    def __init__(self, name):
        self.name = name

    def greet(self):
        print 'Hi it\'s {} and according to everyone the best fruit is {}.'.format(self.name, self.fruit)


def test_const_class():
    with pytest.raises(AttributeError):
        ConstClass.fruit = 'apple'

    with pytest.raises(AttributeError):
        ConstClass.greet = lambda (self): 7

    with pytest.raises(AttributeError):
        ConstClass.__init__ = int.__init__
