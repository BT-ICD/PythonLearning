'''
Program to understand instance variable.
'''
class Sample:
    def __init__(self):
        self.x=10
    def incrementX(self):
        self.x+=1

s1 = Sample()
s2 = Sample()
s3 = Sample()

s1.incrementX()
s1.incrementX()
s2.incrementX()

print('s1.x is ',s1.x)
print('s2.x is ',s2.x)
print('s3.x is ',s3.x)