text = "X-DSPAM-Confidence:    0.8475"


#lets find the index of the strings that can be converted to float
pos1 = text.find('0')
pos2 = text.find('5', pos1)

finder = text[pos1:pos2 + 1]
floater = float(finder)
print(floater)