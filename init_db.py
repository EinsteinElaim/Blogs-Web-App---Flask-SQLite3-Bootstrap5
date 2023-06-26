import  sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as s:
    connection.executescript(s.read())

cur = connection.cursor()

cur.execute(
    "INSERT INTO posts (title, content) VALUES (?, ?)",
    ('First Post', 'Content for the first post')
)

cur.execute(
    "INSERT INTO posts (title, content) VALUES (?, ?)",
    ('Second Post', 'Content for second post')
)

connection.commit()
connection.close()