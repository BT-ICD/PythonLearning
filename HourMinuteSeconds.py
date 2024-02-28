'''
Program to find hours, minutes and seconds from total seconds
Example: 3740 seconds => Hour  = 1 Minutes = 2 Seconds = 20
Example: 7320 seconds => Hour  = 2 Minutes = 2 Seconds = 00
'''
totalseconds = int(input("Enter Seconds "));
hours = totalseconds//3600
remainigseconds = totalseconds%3600
minutes = remainigseconds//60
seconds = remainigseconds%60

print("Total seconds", totalseconds)
print("Hours = ",hours,"Minutes  = ", minutes, "Seconds = ", seconds)