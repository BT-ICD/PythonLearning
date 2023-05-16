'''
A Python program to create a static method that calculate the square root value of a given number.
'''
import math
class Sample:
    @staticmethod
    def calculat(x):
        result = math.sqrt(x)
        return result
num = float(input("Enter a number: "))
res = Sample.calculat(num)
print('Result is ', res)