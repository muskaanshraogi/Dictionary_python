import sqlite3

def create():
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    con.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    con.commit()
    con.close()

def insert(title,author,year,isbn):
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    con.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
    con.commit()
    con.close()

def view():
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    con.close()
    return rows

def search(title="", author="", year="", isbn=""):
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
    rows = cur.fetchall()
    con.close()
    return rows

def delete(id):
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    con.execute("DELETE FROM book WHERE id=?",(id,))
    con.commit()
    con.close()

def update(id,title,author,year,isbn):
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    con.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
    con.commit()
    con.close()

create()
#insert("Harry Potter","JK Rowling",1997,197877611)
#insert("The Fault in our Stars","John Green",2002,19755551)
#insert("The Alchemist","Paulo Coelho",1988,192389002)
#print(view())