#3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error.
# If the score is between 0.0 and 1.0, print a grade using the following table:
##>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

#lets create a variable that will take the score input of the user
score = input("Enter Score: ")

#now lets use the try and except to reduce the human error or traceback error.
try:
    #lets initialize the score as float
    grade = float(score)
    #now lets create an if elif statement so the grade can be catergorized based on the score
    if grade >= 0.9:
        print('A')
    elif grade >= 0.8:
        print('B')
    elif grade >= 0.7:
        print('C')
    elif grade >= 0.6:
        print('D')
    elif grade < 0.6:
        print('F')
    else:
        print('The grade you enter is invalid or out of range')
except:
    print("error enter a valid number!")