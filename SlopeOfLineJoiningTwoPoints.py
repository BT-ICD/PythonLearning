'''
To find slope of a line joining points
slope m = y2-y1/x2-x1
example slope of points A(0,2) and B(-2,6) is -2
example slope of points A(5,5) and B(4,2) is 3
'''
x1=int(input("Enter x1"))
y1=int(input("Enter y1"))
x2=int(input("Enter x2"))
y2=int(input("Enter y2"))
slope = (y2-y1)/(x2-x1)
print("Slope is ",slope)