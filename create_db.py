import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS entries (
    id TEXT PRIMARY KEY,
    title TEXT,
    text TEXT,
    image_url TEXT
)
''')
conn.commit()
conn.close()
