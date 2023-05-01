import sqlite3

class initDB:

    def __init__(self, parameters=None):
        self.parameters = parameters
    
    def start(self):
        connection = sqlite3.connect('database.db')

        with open('schema.sql') as f:
            connection.executescript(f.read())
        
        cur = connection.cursor()

        cur.execute("INSERT INTO posts (id,title, content) VALUES (?, ?, ?)",(1,'First Post', 'Hello world!'))
        cur.execute("INSERT INTO posts (id,title, content) VALUES (?, ?, ?)",(2,'Second Post', 'Hello there!'))

        connection.commit()

        # posts = connection.execute('SELECT * FROM posts').fetchall()
        # for i in posts:
        #     print(i)

        connection.close()
        return True