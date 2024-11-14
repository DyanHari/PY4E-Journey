largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        print("Maximum is", largest)
        print("Minimum is", smallest)
        break
    try:
        number = int(num)

        if smallest is None:
            smallest = number
        elif number < smallest:
            smallest = number

        if largest is None:
            largest = number
        elif number > largest:
            largest = number
    except:
        print('Invalid input')

