#Finding Numbers in a Haystack

#In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.

import re
fhand = open('regex_sum_2110048.txt')

#first lets create a list so we can put all the numbers there and sum it.
numlist = list()
#now lets create a loop that will scan the file line by line
for line in fhand:
    #now were gonna use findall and regular expression that basically says find all the number. I dont care how long is it or the range of it (0-9) just get it and take note of that number)
    #the meaning of 0-9 here is basically any number that contains 1,2,3,4,5,6 etc you get the point. For the + it means no matter how long the number get even if its million its acceptable
    #as long as its a number that are in the range. for the line is that where we are looking
    stuffs = re.findall('([0-9]+)', line)
    #now lets create a looping condition because some line may not have a number and the loop will take note of that so lets create a loop that if line doesnt contain any number
    #just skip it!
    if len(stuffs) < 1: continue
    #lets print to check if it really did get the random numbers on the file
    print(stuffs)
    #now lets create a loop that will append all the numbers that we got to the empty list that we did earlier.
    for num in stuffs:
        numbers = int(num)
        numlist.append(numbers)

#tada!!!
print(numlist)
print(len(numlist))
print(sum(numlist))


