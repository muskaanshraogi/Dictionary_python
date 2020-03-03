import sqlite3

class database:

    def __init__(self):
        self.con = sqlite3.connect("books.db")
        self.cur = self.con.cursor()
        self.con.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        self.con.commit()
        

    def insert(self,title,author,year,isbn):
        self.con.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
        self.con.commit()
    

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        return rows

    def search(self,title="", author="", year="", isbn=""):
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
        rows = self.cur.fetchall()
        return rows

    def delete(self,id):
        self.con.execute("DELETE FROM book WHERE id=?",(id,))
        self.con.commit()

    def update(self,id,title,author,year,isbn):
        self.con.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
        self.con.commit()

    def __del__(self):
        self.con.close()