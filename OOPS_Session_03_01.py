'''
@property decorator
'''
class Square:
    def __init__(self, length=0):
        self._length=length

    @property
    def length(self):
        return self._length
    @length.setter
    def length(self,value):
        if(value>=0):
            self._length = value
        else:
            raise ValueError('Length should not be negative')

s1= Square(5)
print(s1.length)
s1.length=10
print(s1.length)
# s1.length=-10
# print(s1.length)