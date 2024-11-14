#5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.
# Enter 7, 2, bob, 10, and 4 and match the output below.

#lets create an empty variable. None is different than 0
largest = None
smallest = None

#lets create a while loop that with an if statement inside
while True:

    #variable for getting the user input
    num = input("Enter a number: ")

    #now if the user enter the word done it will get the maximum and minimum number and will end the loop
    if num == "done":
        print("Maximum is", largest)
        print("Minimum is", smallest)
        break

    #now lets use try and except so the program wont have an error if the user type a value that is not integer
    try:
        #lets initialize the user input to int
        number = int(num)

        #lets create an if statement that check which number is the smallest
        if smallest is None:
            #this means that if the smallest value is none then the value of the smallest will become the number that the user typed.
            smallest = number
        elif number < smallest:
            # now we need this elif statement that compare the number that the user just entered and the number that the user last entered or the last one that labelled as smallest by the program.
            smallest = number

        # lets create an if statement that check which number is the highest
        if largest is None:
            # this means that if the smallest value is none then the value of the largest will become the number that the user typed.
            largest = number
        elif number > largest:
            # now we need this elif statement that compare the number that the user just entered and the number that the user last entered or the last one that labelled as largest by the program.
            largest = number

    except:
        print('Invalid input')

