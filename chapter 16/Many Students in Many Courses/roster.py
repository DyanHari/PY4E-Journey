import json
import sqlite3

# this code is like connecting to a file and opening that file but do it on sql
conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# the first three line of codes are to prevent duplicating of table or error rather
# the other codes are for creating tables
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

# now lets open the file that were going to put on our database
fname = 'roster_data.json'

#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

# let's open the file and make it a string
str_data = open(fname).read()
json_data = json.loads(str_data)


for entry in json_data:
    # now that were looping lets categorized each string by indexing it
    name = entry[0]
    title = entry[1]
    role = entry[2]

    print((name, title, role))

    # this line of codes is the one responsible for putting the name string on the name row of the User table
    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( name, ) )
    # now the name that we just put on our database lets put an id on it. The database is the one numbering it because
    # we made it auto increment
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    # now the number for the data that we just put read and remember its id number
    user_id = cur.fetchone()[0]

    # pretty much the same above
    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    # now on our member table the user id and course id that we remember or take note of put it on this table.
    # by the way ? is placeholders for the value that were going to put
    # for the role our loop is the one responsible for putting value on it by indexing[2] on entry string
    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ?)''',
        ( user_id, course_id, role) )

    conn.commit()