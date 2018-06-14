import psycopg2
import time
# connect to a DB
# create a cursor object
# write an SQL query
# Commit changes
# close DB connection

def create_table():
    print("in create table")
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgre' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (ITEM TEXT, QUANTITY INTEGER, PRICE REAL)")
    conn.commit()
    conn.close()
    # time.sleep(5)

def insert(item, quantity, price):
    print("in insert table")
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgre' host='localhost' port='5432'")
    cur = conn.cursor()
    # cur.execute("INSERT INTO store VALUES ('%s','%s','%s')" % (item, quantity, price))
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)", (item, quantity, price))
    conn.commit()
    conn.close()
    # time.sleep(5)

def view():
    print("in view table")
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgre' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    # time.sleep(5)
    return rows


def delete(item):
    print("in delete table")
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgre' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item= %s", (item,))
    conn.commit()
    conn.close()

def update(quantity, price, item):
    print("in update table")
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgre' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity= %s, price= %s WHERE item = %s", (quantity, price, item))
    conn.commit()
    conn.close()


# create_table()
# insert('Orange', 20, 6)

# print(view())
# delete(("Apple"))
update(21,7,"Orange")
print(view())
