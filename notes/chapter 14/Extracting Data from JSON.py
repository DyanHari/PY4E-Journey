from urllib.request import urlopen
import ssl
import json

# This part of the code sets up an SSL context that ignores certificate errors, which can be helpful when accessing websites with self-signed certificates.
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = ('http://py4e-data.dr-chuck.net/comments_2110053.json')

html = urlopen(url, context=ctx).read()
rawdata = json.loads(html)

pdata = rawdata['comments']
print('Number of comments:', len(pdata))

sumdata = list()

for item in pdata:
    #print(item ['count'])
    count = int(item['count'])
    sumdata.append(count)

print(sumdata)
print('Sum = ', sum(sumdata))



