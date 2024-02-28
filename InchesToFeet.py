'''
Program to convert total inches into foot and inches
12 inches = 1 foot
'''
totalinches = int(input("Enter inches"));
foot = totalinches//12
inches = totalinches%12

print("Total inches", totalinches)
print("Foot = ", foot, "Inch = ", inches)

