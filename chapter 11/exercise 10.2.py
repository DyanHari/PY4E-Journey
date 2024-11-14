# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.


#this block of codes is for the file to be open on what ever the user inputted
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

#lets create an empty dictionary
count = dict()
#lets create a for loop that will read every line of the file
for line in handle:
    #but we have a condition if the line doesnt start from the string "From " then this loop will ignore it
    if not line.startswith('From '):
        continue

    #lets seperate the line word by word
    words = line.split()
    #then lets get the time part only (I used print statement to check it)
    time = words[5]

    #then lets seperate the time part again because it look like this 09:14:16 2008 according to the activity we only need the hour so lets split it with the ':'
    hours = time.split(':')
    #after that we only need the first part which is the hour that can be called index [0]
    sephours = [hours[0]]
    #now lets create a loop that will put those hour in the dictionary that we made earlier while also counting it.
    for hour in sephours:
        count[hour] = count.get(hour, 0) + 1

#now lets print it in the order that the activity want us to do so lets create a loop that will iterate through every key and value in the dictionary while printing it.
for k, v in sorted(count.items()):
    print(k, v)