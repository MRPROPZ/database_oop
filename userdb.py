import sqlite3

class SqliteUser:
    def __init__(self, name=None):
        self.conn = None
        self.cursor = None
        if name:
            self.open(name)

    def open(self, name):
        try:
            self.conn = sqlite3.connect(name)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print("Failed to connect db...")

    def insert(self, query, datainsert):
        c = self.cursor
        c.execute(query, datainsert)
        self.conn.commit()

    def delete(self, query):
        c = self.cursor
        c.execute(query)
        self.conn.commit()

    def select(self, query):
        c = self.cursor
        c.execute(query)
        return c.fetchall()

    def edit(self, query, dataupdate):
        c = self.cursor
        c.execute(query, dataupdate)
        self.conn.commit()

#test = SqliteUser("user.db")
#test.insert("INSERT INTO users(name,year,admin) VALUES(?,?,?)", ('AA', 2011, 1))
#test.insert("INSERT INTO users(name,year,admin) "
#            "VALUES('BB',2010,0)")
#print(test.select("SELECT * FROM users"))