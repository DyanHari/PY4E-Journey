fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

#lets open the file
fh = open(fname)
#declare a variable as the counter
count = 0

#lets create a for loop to read the file line by line
for line in fh:
    #lets remove  the spaces on the file to clean it
    line = line.strip()
    #this means that if the line doesnt start with the word "From:" skip it!
    if not line.startswith("From:"):
        continue
    #lets split the line because we only need to get the email adddress it is seperated
    # by space so we can use .split() the line looks like this From: asdjklasdjkasdkj@gmail.com
    words = line.split()

    #lets print the second index which is 1
    print(words[1])
    #count the number of email
    count = count + 1


print("There were", count, "lines in the file with From as the first word")
