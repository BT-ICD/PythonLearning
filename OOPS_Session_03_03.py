'''
To get a string representation of an object using __str__ method
References:

'''
import json
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
    def __str__(self):
        # return f"{self.length},{self.width}"
        strData = json.dumps(self.__dict__)
        return  strData
r1 = Rectangle(10,20);
print('Area: ',r1.area())
print('Perimeter: ',r1.perimeter())

strR1 = str(r1)
print(strR1) #<__main__.Rectangle object at 0x0000025590278450>
print('Rectangle size is ',r1)
#__repr__ is for programmer where as __str__ is user friendly (leave out technical details such as class name)

