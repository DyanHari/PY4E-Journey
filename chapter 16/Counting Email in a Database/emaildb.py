import sqlite3

# Connect to the SQLite database and create a cursor
conn = sqlite3.connect('../emaildb.sqlite')
cur = conn.cursor()

#This command deletes any old version of a table called Counts if it already exists.
# This way, you can start fresh each time.
cur.execute('DROP TABLE IF EXISTS Counts')

# Create the Counts table
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)

for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()

    # This gets the second word in the line, which is the email address.
    #because the text goes like this From: Juan@email.com and
    #it will bercome like this ['From:' 'Juan@email.com']
    email = pieces[1]
    #now lets split the Juan@email.com and it will become like this
    #['Juan' 'email.com']
    splorg = email.split('@')
    #This gets the part after the @, which is the organization (or domain name).
    org = splorg[1]

    #This checks if the organization is already in the Counts table.
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    #This fetches one row of results from the database. so we can use it as a checker for if condition statement
    row = cur.fetchone()
    #If the organization is not found in the table, it adds a new row with a count of 1.
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))

    #If the organization is already in the table, it increases the count by 1.
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))

    #This saves all the changes to the database.
    conn.commit()

# Query the database to get the top 10 organizations by email count:
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

#Print the results:
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

#Close the connection
cur.close()

#Summary
#In simple terms, this script reads an email file, counts how many emails come from each organization, and stores these counts in a database.
# Finally, it prints out the top 10 organizations with the most emails.