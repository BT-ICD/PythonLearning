'''
To get a string representation of an object using __repr__ method
References:
    Python String Interpolation    https://www.programiz.com/python-programming/string-interpolation
    https://docs.python.org/3/reference/datamodel.html#object.__repr__
    https://docs.python.org/3/library/functions.html#eval
'''
class Rectangle:
    def __init__(self, length=0, width=0):
        self.length = length
        self.width = width
    @property
    def length(self):
        return self._length
    @length.setter
    def length(self, length):
        if(length<0):
            raise ValueError('Length should not be negative')
        self._length=length

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,width):
        if (width < 0):
            raise ValueError('Width should not be negative')
        self._width = width
    def area(self):
        return self.length* self.width
    def perimeter (self):
        return 2* (self.length+ self.width)
    def __repr__(self):
        # return f"Rectangle(length ={self.length}, width={self.width})"
        return f"{self.__class__.__name__}(length ={self.length}, width={self.width})"

r1 = Rectangle(10,20);
print('Area: ',r1.area())
print('Perimeter: ',r1.perimeter())

strR1 = repr(r1)
print(strR1) #<__main__.Rectangle object at 0x0000019167B48410>

r2 =eval(strR1) #from string to object
print(r2.length)
print(r2.width)
