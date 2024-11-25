import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys

# https://py4e-data.dr-chuck.net/opengeo?q=Ann+Arbor%2C+MI
# The base URL for querying location data from a web service.
serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

# Additional detail for urllib
# http.client.HTTPConnection.debuglevel = 1

#connect with the database or create a new sql data base
conn = sqlite3.connect('opengeo.sqlite')
cur = conn.cursor()

#create a new table
cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#now lets explore our own datasets that compiles different state universities at the philippines
fh = open("output.txt")

count = 0 # Keeps track of how many addresses have been processed.
nofound = 0 # Counts how many addresses could not be found.

for line in fh:
    if count > 100 : # Stops after processing 100 addresses.
        print('Retrieved 100 locations, restart to retrieve more')
        break

    address = line.strip() # Clean the data's for the address
    print('')
    # Checking if geodata is Already in the Database
    cur.execute("SELECT geodata FROM Locations WHERE address= ?",
        (memoryview(address.encode()), ))

    # If the address is found, it skips to the next line. Otherwise, it continues to fetch the data.
    try:
        # fetchone access a row and to avoid redundancy it checks if the address is already fetched on our database
        data = cur.fetchone()[0]
        print("Found in database", address)
        continue

    except:
        pass

    # If the geodata for the address is not found in the database, the script constructs
    # a URL to fetch the data from a web service

    # Creates a dictionary to store the address on a dictionary so it can be encoded to html format
    parms = dict()
    parms['q'] = address

    # Constructs the full URL with the address. This is where the address
    # is being constructed after storing it on a dictionary
    url = serviceurl + urllib.parse.urlencode(parms)

    # print the constructed url
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    # Reads and decodes the response data that we got from opening the url.
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))
    count = count + 1

    try:
        # Converts the fetched data into a JSON format.
        # Ensures the data is valid and contains the necessary information.
        js = json.loads(data)
    except:
        print(data)  # We print in case unicode causes an error
        continue

    if not js or 'features' not in js:
        print('==== Download error ===')
        print(data)
        break

    if len(js['features']) == 0:
        print('==== Object not found ====')
        nofound = nofound + 1

    # Adds the new address and its data/geodata to the database.
    cur.execute('''INSERT INTO Locations (address, geodata)
        VALUES ( ?, ? )''',
        (memoryview(address.encode()), memoryview(data.encode()) ) )

    # Saves the changes to the database.
    conn.commit()

    if count % 10 == 0 :
        print('Pausing for a bit...')
        time.sleep(5)

if nofound > 0:
    print('Number of features for which the location could not be found:', nofound)

print("Run geodump.py to read the data from the database so you can vizualize it on a map.")
