import sqlite3


def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, nazev TEXT, autor TEXT, rok INTEGER, ISBN INTEGER)")
    conn.commit()
    conn.close()


def insert(nazev, autor, rok, ISBN):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (nazev, autor, rok, ISBN))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(nazev="", autor="", rok="", ISBN=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE nazev = ? OR autor = ? OR rok = ? OR ISBN = ?", (nazev, autor, rok, ISBN))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id = ?", (id,))
    conn.commit()
    conn.close()


def update(id, nazev, autor, rok, ISBN):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET nazev = ?, autor = ?, rok = ?, ISBN = ? WHERE id = ?", (nazev, autor, rok, ISBN, id))
    conn.commit()
    conn.close()


connect()
