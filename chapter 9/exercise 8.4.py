fname = input("Enter file name: ")
fh = open(fname)
lst = list()

#lets read the file amd add a print statement to check
read = fh.read()
#after checking if it works now we can split it try to also print the splitted file
split = read.split()

#now we need a loop to filter the duplicated words in the file
for i in split:
    #this simply means if words not in the list go add it. else skip it
    if i not in lst:
        lst.append(i)

#sort the list so it will be arranged alphabetically
lst.sort()
print(lst)


