import sqlite3

# Connect to the database (it will be created if it doesn't exist)
conn = sqlite3.connect('football.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS clubs
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   country TEXT NOT NULL);''')


clubs = [
    ("Real Madrid", "Spain"),
    ("Barcelona", "Spain"),
    ("Manchester City", "England")
]
cursor.executemany("INSERT INTO clubs (name, country) VALUES (?, ?)", clubs)
# Commit the changes and close the connection
conn.commit()
conn.close()
