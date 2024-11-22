import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

handle = open('tracks.csv')

# Another One Bites The Dust,Queen,Greatest Hits,55,100,217103
#   0                          1      2           3  4   5

for line in handle:
    #this is for splitting the file line by line and splitting the line by comma(,)
    line = line.strip();
    pieces = line.split(',')

    #Check if enough pieces. if its not skip it!
    if len(pieces) < 6 : continue

    #now lets name those seperated words by comma with these codes.
    #the comment above are the reference
    name = pieces[0]
    artist = pieces[1]
    album = pieces[2]
    count = pieces[3]
    rating = pieces[4]
    length = pieces[5]
    genre = pieces[6]

    print(name, artist, album, count, rating, length, genre)

    # This command tries to add a new artist's name to the Artist table.
    # if its already there ignore it
    # INTO Artist (name): Specifies which table and column to insert the data into.
    # VALUES ( ? ): The question mark is a placeholder for the value being inserted.
    # ( artist, ): This is a tuple containing the artist's name, which replaces the ? placeholder.
    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', ( artist, ) )
    # This command looks up the unique ID number for the artist just inserted.
    # SELECT id: Requests the ID column from the table.
    # FROM Artist WHERE name = ?: Specifies to look in the Artist table for the row where the name matches the given artist.
    # (artist, ): The artist's name that was just inserted, used to find their corresponding ID.
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0] #Fetches and stores the artist's ID number.

    cur.execute('''INSERT OR IGNORE INTO Genre (name) 
            VALUES ( ? )''', (genre,))
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre,))
    genre_id = cur.fetchone()[0]


    #Adds the album to the Album table if it isn't already there, along with the artist's ID.
    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id, ) )
    #Looks up the album's ID number.
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0] #Fetches and stores the album's ID number.

    #Adds or updates the track in the Track table with its title, album ID, genre ID, length, rating, and play count.
    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ?, ?)''',
        ( name, album_id, genre_id, length, rating, count) )

    conn.commit()
