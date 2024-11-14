fruit = 'banana'
index = 0
letter = fruit[index]
for letter in fruit:
    print(index, letter)
    index = index + 1


#letter counter
word = "John Harry M. Duavis"
count = 0
for letter in word:
    if letter == 'r' :
        count = count +1
print('count', count)

#startswith
line = 'Please have a nice day'
line.startswith('Please')