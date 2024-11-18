#2.3 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25).
# You should use input to read a string and float() to convert the string to a number. Do not worry about error checking or bad user data.

#lets get the user input so the program can compute for the hours and rate
hrs = input("Enter Hours:")
rate = input("Enter Rate:")

#now lets compute that by multiplying the hours and rate
pay = float(hrs) * float(rate)

#this code print the result!
print('Pay:', pay)