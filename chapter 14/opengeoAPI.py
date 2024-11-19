import urllib.request, urllib.parse
import json, ssl

#this is the url where we are going to get our data from
serviceUrl = 'https://py4e-data.dr-chuck.net/opengeo?'

# This part of the code sets up an SSL context that ignores certificate errors, which can be helpful when accessing websites with self-signed certificates.
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#lets create an infinite loop that will prompts the user to input a location.
while True:
    address = input('Enter location: ')
    #if the user entered an empty location we will break the loop
    if len(address) < 1: break

    #now lets clean the address that the user entered
    address = address.strip()

    #lets create an empty dictionary to hold parameters
    parms = dict()

    #now inside the dictionary lets create a key with the pair value of the cleaned address that the user entered
    parms['q'] = address

    #now lets combine the base URL with the address that the user entered
    url = serviceUrl + urllib.parse.urlencode(parms)

    #lets print it to check if its valid
    print('Retrieving', url)

    #Opens the URL and retrieves the data.
    uh = urllib.request.urlopen(url, context=ctx)

    #Reads the data and decodes it from bytes to a string.
    data = uh.read().decode()

    #Prints how many characters were retrieved and shows a preview of the first 20 characters.
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))


    #now the try and except will try to convert the data into a JSON object if it fails
    #error will occur. this is to ensure that the user entered a valid address
    try:
        js = json.loads(data)
    except:
        js = None

    #now if the js object is valid this line of code will check if it contains a key called 'features'
    # if it does not have 'feature' the loop will stop
    if not js or 'features' not in js:
        print('=== Download Error ===')
        print(data)
        break

    #on this code it will check if the key features have any value or if its empty.
    #if it does not have value the loop will stop
    if len(js['features']) == 0:
        print('=== Object not found ===')
        print(data)
        break

    #the json.dump and indent formats the object in a nice way
    #print(json.dumps(js, indent=4))

    #now this code means lets go the the features which is index [0]
    #inside the features lets go to the properties and inside of that is the plus code
    #indent it so it is formatted in a presentable way
    plusc = json.dumps(js['features'][0]['properties']['plus_code'], indent=4)
    #now lets print it
    print('Plus code', plusc)
