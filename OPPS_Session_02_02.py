'''
Example to understand class variable
'''
class Sample:
    #class variable X
    x=10

#This is a class method

    @classmethod
    def setx(cls):
        cls.x+=1
#create 2 instances
s1= Sample()
s2= Sample()
print('s1.x is ',s1.x)
print('s2.x is ',s2.x)

s1.setx()
print('s1.x is ',s1.x)
print('s2.x is ',s2.x)

Sample.setx()
print('s1.x is ',s1.x)
print('s2.x is ',s2.x)
