fname = input("Enter file name: ")
fh = open(fname)
lst = list()


read = fh.read()
split = read.split()

for i in split:
    if i not in lst:
        lst.append(i)

lst.sort()
print(lst)




