import urllib.request, urllib.parse
import json, ssl

serviceUrl = 'https://py4e-data.dr-chuck.net/opengeo?'

# This part of the code sets up an SSL context that ignores certificate errors, which can be helpful when accessing websites with self-signed certificates.
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    address = address.strip()
    parms = dict()
    parms['q'] = address

    url = serviceUrl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'features' not in js:
        print('=== Download Error ===')
        print(data)
        break

    if len(js['features']) == 0:
        print('=== Object not found ===')
        print(data)
        break

    print(json.dumps(js, indent=4))

    lat = js['features'][0]['properties']['lat']
    lon = js['features'][0]['properties']['lon']
    print('lat', lat, 'lon', lon)
    location = js['features'][0]['properties']['formatted']
    print(location)