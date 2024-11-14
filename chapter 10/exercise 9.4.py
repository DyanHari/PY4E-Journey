#these code simple gets the user input for the filename and open the file name that the user entered
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

#lets create an empty dictionary called count
count = dict()
#this loop line reads the file line by line
for line in handle:
    #if those line doesnt start from the string "From:" skip it
    if not line.startswith('From:'):
        continue
    #now those strings that start with "From:" we'll split it so it can be two strings that will be put on a list
    words = line.split()
    #now lets create a seperate list for only the email part. lets call the index[1] which is the email part of the list that we created on the upper part now we have a list
    #of email that removes the word "From:"
    emails = [words[1]]
    #now lets create loop that will all the emails/word by word
    for email in emails:
        #count those emails using the get() method and store it on the count dictionaries that we made
        count[email] = count.get(email, 0) + 1

#lets create a variable to check who has the most sent email on the file
bigword = None
bigcount = None

#lets create a loop that will check the key and value in count dictionary
for email,count in count.items():
    #count is greater than the old value of the bigcount then it will become the new bigcount and bigword
    if bigcount is None or count > bigcount:
        bigword = email
        bigcount = count

print(bigword, bigcount)
