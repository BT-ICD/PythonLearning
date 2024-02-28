'''
Program to convert total seconds into minutes and seconds
60 seconds = 1 mninute
'''
totalseconds = int(input("Enter Seconds "));
minutes = totalseconds//60
remainingseconds = totalseconds%60

print("Total seconds", totalseconds)
print("Minutes  = ", minutes, "Seconds = ", remainingseconds)