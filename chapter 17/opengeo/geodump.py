import sqlite3
import json
import codecs

conn = sqlite3.connect('opengeo.sqlite')
cur = conn.cursor()

cur.execute('SELECT * FROM Locations') # Executes an SQL command to select all rows from the Locations table.

fhand = codecs.open('where.js', 'w', "utf-8") # Opens a file named where.js in write mode with UTF-8 encoding.
fhand.write("myData = [\n") # Writes the initial part of the JavaScript array definition to the file.

count = 0 # Keeps track of how many records have been processed.

# Process Each Row from the Database
for row in cur :
    data = str(row[1].decode()) # Converts the geodata (which is in bytes) to a string.
    try: js = json.loads(str(data)) # Parses the string as JSON.
    except: continue

    # Skips rows where the features array in the JSON is empty.
    if len(js['features']) == 0: continue

    # Extract Latitude, Longitude, and Name
    try:
        # inside the list features theres a dictionary named geometry.
        # inside geometry theres a list called coordinates where we can found latitude and longitude
        lat = js['features'][0]['geometry']['coordinates'][1]
        lng = js['features'][0]['geometry']['coordinates'][0]
        # same logic above
        where = js['features'][0]['properties']['display_name']
        # Removes any single quotes from the name to avoid issues in the JavaScript file.
        where = where.replace("'", "")
    except:
        print('Unexpected format')
        print(js)

    # Write to the Output File or where.js
    try :
        print(where, lat, lng)

        count = count + 1
        # Adds a comma and newline before appending new data to separate the entries.
        if count > 1 : fhand.write(",\n")
        # Adds a comma and newline before appending new data to separate the entries.
        output = "["+str(lat)+","+str(lng)+", '"+where+"']"
        fhand.write(output) # Writes the formatted data to the file.
    except:
        continue

fhand.write("\n];\n") # Closes the JavaScript array definition.
cur.close()
fhand.close()
print(count, "records written to where.js")
print("Open where.html to view the data in a browser")

