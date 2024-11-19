#lets import the necessary library which is urllib to extract data from the web and xml etree so we can read XML files.
from urllib.request import urlopen
import ssl
import xml.etree.ElementTree as ET


# This part of the code sets up an SSL context that ignores certificate errors, which can be helpful when accessing websites with self-signed certificates.
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


#this is the url where we are going to extract data from
url = ('http://py4e-data.dr-chuck.net/comments_2110052.xml')

#now this line of code open that url and read the data of it
html = urlopen(url, context=ctx).read()

#now lets transform the data that we got to string using fromstring()
data = ET.fromstring(html)

#now this code is an XPath selector string to look through the entire tree of XML for any tag named 'count'
#lst = data.findall('comments/comment/count') this is another way of writing the code
lst = data.findall('.//count')

#this is to check if were getting any data from the url and how many data we got from what we need.
print('data count:', len(lst))

#now lets create an empty list so we can use it later for computing the sum
values = list()

#now lets iterate through the entire list of the data that we extracted and split it value by value
for item in lst:
    #lets grab those data and get the text only by using .text and also making those text to integers
    items = int(item.text)
    #lets append the data onto the list
    values.append(items)

#lets see if our loop works correctly
print(values)
#now that it works correctly lets compute the sum of those by using sum()
print(sum(values))

