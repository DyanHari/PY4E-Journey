import re

# Open the file and read its contents
with open('outputold.txt', 'r') as file:
    lines = file.readlines()

# List to hold university names
universities = []

# Regex pattern to match numbers
number_pattern = re.compile(r'^\d+$')

# Loop through lines and extract university names
for line in lines:
    line = line.strip()
    if line != "State Univ. & Colleges" and not number_pattern.match(line):
        universities.append(line)

# Print the extracted university names
for university in universities:
    print(university)
