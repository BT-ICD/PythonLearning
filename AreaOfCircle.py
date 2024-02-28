'''
Program to find area and circumference of a Circle
Area of Circle =PI * radius * radius
Circumference of a circle  = 2* PI * radius
'''
import math
radius = int(input("Enter radius of a circle"))
area = math.pi * math.pow(radius,2)
circumference = 2* math.pi* radius

print("Area a circle is",area)
print('Circumference of a circle is', circumference)
