import sqlite3
import time
# connect to a DB
# create a cursor object
# write an SQL query
# Commit changes
# close DB connection

def create_table():
    print("in create table")
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (ITEM TEXT, QUANTITY INTEGER, PRICE REAL)")
    conn.commit()
    conn.close()
    # time.sleep(5)

def insert(item, quantity, price):
    print("in insert table")
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (?,?,?)",(item, quantity, price))
    conn.commit()
    conn.close()
    # time.sleep(5)

def view():
    print("in view table")
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    # time.sleep(5)
    return rows


def delete(item):
    print("in delete table")
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item= ?", (item,))
    conn.commit()
    conn.close()

def update(quantity, price, item):
    print("in update table")
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity= ?, price= ? WHERE item = ?", (quantity, price, item))
    conn.commit()
    conn.close()


create_table()
# insert('Whiskey glass', 20, 6)
print(view())
# delete(("Water glass"))
update(21,7,"Whiskey glass")
print(view())
