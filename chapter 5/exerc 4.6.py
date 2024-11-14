#4.6 Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
# Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours.
# Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation.
# The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
# You should use input to read a string and float() to convert the string to a number.
# Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. Do not name your variable sum or use the sum() function.

#lets create a function that will compute the pay
def computepay(h, r):
    return h * r

#lets create some variables for hours and rates
hrs = input("Enter Hours:")
rate = input("Enter rate:")

#then lets initialize the variables to become float
hours = float(hrs)
rates = float(rate)

#lets create an if statement to check the worker's eligibility for overtime pay
if hours > 40:
    #lets create a new variable called pay so we can utilize the function that we created earlier. Together lets get the hours and rates by puttin it inside the parenthesis
    p = computepay(hours, rates)
    #just like last time we need to compute for the OT pay so were removing the regular hours of the worker and then multiplying the rate by time and a half or 0.5
    otpay = computepay(hours - 40, rates * 0.5)
    #now lets compute the grosspay meaning the regular pay added by ot pay
    gross = p + otpay
    print("Pay", gross)


else:
    # if the worker is not eligible for the OT pay then this code will execute
    p = computepay(hours, rates)
    print("Pay", p)


