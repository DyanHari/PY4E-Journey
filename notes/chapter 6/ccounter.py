counter = 0
sum = 0
print('before', counter, sum)
for thing in [9, 41, 12, 3, 74, 15]:
    counter = counter + 1
    sum = sum + thing
    print (counter, thing)
print('After', 'count', counter,'sum', sum, 'avrg', sum / counter)