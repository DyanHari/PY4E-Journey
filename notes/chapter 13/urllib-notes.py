import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

#this code is for counting on how many times did that word appear on the txt file
counts = dict()
for line in fhand:
    words = line.decode().split()
    #print(line.decode().strip()) this is for printing the whole text file
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
