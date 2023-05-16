'''
Example: Class Method
Develop Bird class.
All birds in the nature have only 2 wings.
So, we can take ‘wings’ as a class variable.
Copy of this class variable is available to all the instances of Bird class. The class method fly() can be called as Bird.fly()

A Python program to use class method to handle the common features of all instances of the Bird class.
'''
class Bird:
    wings=2
    @classmethod
    def fly(cls,name):
        print('{} flies with {} wings'.format(name,cls.wings))
Bird.fly('Sparrow')
Bird.fly('Pigeon')