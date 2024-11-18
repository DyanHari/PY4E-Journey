from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

#now we are using beautiful soup a simplified version of requesting or dialing a connection for a web browser.

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#now this is where the user can enter which server he needs to request a data from
url = input('Enter - ')

#this is a simplified version of a two line-ish code before. it basically connects to the url that the user enter and interpret it.
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

#lets create an empty list so we can sum the number on the table later
numlist = list()

# Retrieve all of the span tags because thats where the number or the data that we need come from
tags = soup('span')

#now lets create a for loop that will read those data line by line
for tag in tags:
    # Look at the parts of a tag
    #now that we seperated only the thing that we need lets create another for loop
    #print('comments:', tag)
    #this for loop is for splitting the numbers so we can initialize those to an int
    for comment in tag:
        comment.split()
        inter = int(comment)
        #now lets append those numbers to the list so we can solve for its sum
        numlist.append(inter)

#check if the append work
print(numlist)
#now that the append work lets sum it!
print(sum(numlist))



