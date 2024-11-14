#6.5 Write code using find() and string slicing (see section 6.10) to extract the
#number at the end of the line below. Convert the extracted value to a floating point number and print it out.


text = "X-DSPAM-Confidence:    0.8475"


#let's find the index of the strings that can be converted to float
pos1 = text.find('0')
#print(pos1) use this to get the result or the index
pos2 = text.find('5', pos1)
#print(pos2) use this to get the result or the index

#Now that we know that it is the index lets slice the string. Make sure to add +1 because t
finder = text[pos1:pos2 + 1]

#after slicing the string convert it to float and print it
floater = float(finder)
print(floater)