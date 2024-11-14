# 3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
# You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.

#lets create some variables that will get the input and variables that will hold the value for hours and rate
hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)


#now lets create a condition that if the hours rendered by the employer is greater than 40 then he is eligible for overtime pay
if h > 40:
    #lets compute for the regular pay
    regpay = h * r

    #now the for the OT pay substract the regular hours so the remaining hours will be counted as overtime hour
    #then the rate will be 1.5 times than normal or .5
    otpay = (h - 40) * (r * 0.5)

    #lets compute those two
    pay = regpay + otpay
    print(pay)

#if the employee did not qualify for the overtime hour then this code will be execute
else:
    pay = h * r
    print(pay)
