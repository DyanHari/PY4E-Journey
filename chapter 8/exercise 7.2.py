# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")

#we need total variable to get the total of the float's. we need the dividend so we can use it to get the average later
total = 0
dividend = 0

#we did the try and except so we can prevent user error and traceback error
try:
    fh = open(fname)

except:
    print('The file name you enter does not exist!')
    quit()

for line in fh:
    #we need the strip to clean the strings or remove the spaces
    line = line.strip()

    #we need and if statement inside the loop so we can get what we need which is X-DSPAM....
    if not line.startswith("X-DSPAM-Confidence:"):
        continue

    #we only need the value so we need to find the position of : because thats where the value starts
    pos1 = line.find(':')

    #lets now slice it.the second index value we use the len or length function so the program will determine the end of the string for us
    slice = line[pos1 + 1:len(line)]

    # this is how we get the total of the the values. everytime the loop runs it will get the sliced value of the X-DSPAM
    total = total + float(slice)

    #this is to also count the number of X-DSPAM values that we will use as the dividend
    dividend = dividend + 1

print('Average spam Confidence:', total / dividend)
