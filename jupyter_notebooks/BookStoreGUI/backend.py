import sqlite3

class Database():
    # """docstring for [object Object]."""
    # def __init__(self, arg):
    #     super([object Object], self).__init__()
    #     self.arg = arg

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book ( id INTEGER PRIMARY KEY, title text, author text, year INTEGER, isbn INTEGER)")
        self.conn.commit()


    def insert(self, title , author, year, isbn):
        self.cur.execute("INSERT INTO book VALUES(NULL, ?,?,?,? )", (title , author, year, isbn))
        self.conn.commit()


    def view(self):
        print("in view table")
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        return rows

    def search(self,title="", author="", year="", isbn=""):
        print("in search table")
        self.cur.execute("SELECT * FROM book where title=? or author=? or year=? or isbn=?",(title, author, year, isbn))
        rows = self.cur.fetchall()
        return rows

    def delete(self,id):
        print("in delete table")
        self.cur.execute("DELETE FROM book WHERE id = ? ", (id,))
        self.conn.commit()


    def update(self,id, title="", author="", year="", isbn=""):
        print("in update table")
        self.cur.execute("UPDATE book SET title= ?, author=?, year=?, isbn=?  WHERE id = ?", (title, author, year, isbn, id))
        self.conn.commit()

    def __del__(self):
        self.conn.commit()
        self.conn.close()

# connect()
# insert ( "The Secret", "Singh", 2018, 34322232)
# delete(5)
# update(7, "The New Secret", "Singh", 2018, 423323234)
# print(view())
# print(search(author="Vikas"))
# print(view())
