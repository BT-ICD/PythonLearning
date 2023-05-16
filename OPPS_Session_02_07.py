'''
A Python program to create a static method that counts the number of instances created for a class.
'''
class MyClass:
    n=0
    def __init__(self):
        MyClass.n= MyClass.n+1
    @staticmethod
    def numOfObjects():
        print('Number of instances created {}'.format(MyClass.n))

obj1 = MyClass()
obj2 = MyClass()
obj3 = MyClass()

MyClass.numOfObjects()