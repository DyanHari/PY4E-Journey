import urllib.request, urllib.error
from bs4 import BeautifulSoup
import ssl

# This part of the code sets up an SSL context that ignores certificate errors, which can be helpful when accessing websites with self-signed certificates.
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter URL: ') # The URL to start retrieving data from.
count = int(input('Enter count: ')) # The number of times to follow the link.
pos = int(input('Enter position: ')) # The position of the link to follow on each page.

#method by copilot
#name_part = url.split('known_by_')[1]
#firstname = name_part.split('.')[0]

#method by me to append the first name or the name on the url that the user entered
pos1 = url.find('Fikret')
pos2 = url.find('.html')
print(pos1, pos2)
firstn = url[pos1:pos2]

namelist = list()
namelist.append(firstn)

for i in range(count):
    print("Retrieving:", url)
    html = urllib.request.urlopen(url, context=ctx).read() #Opens the URL and reads its HTML content.
    soup = BeautifulSoup(html, 'html.parser') #Parses the HTML content using BeautifulSoup.
    tags = soup('a') #Finds all anchor (<a>) tags on the page.

    name = tags[pos - 1].text.strip() #Extracts the text (name) from the anchor tag at the specified position and strips any extra whitespace.
    namelist.append(name)

    url = tags[pos - 1].get('href', None) #Updates the URL to the link at the specified position for the next iteration.

print('Sequence of name: ', namelist)
print('Last name on the sequence', namelist[-1])



