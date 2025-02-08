# Database to store order ID| seller | buyer | product | price | time

import sqlite3
import datetime


conn = sqlite3.connect("orders.db")
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS orders (
    Order_id INTEGER PRIMARY KEY,
    Seller TEXT NOT NULL,
    Buyer TEXT NOT NULL,
    Product TEXT NOT NULL,
    Price REAL NOT NULL,
    Time TEXT NOT NULL
)
''')

orders = [
    (1, 'Alice', 'Bob', 'Widget', 9.99, datetime.now().isoformat()),
    (2, 'Charlie', 'Dana', 'Gadget', 19.99, datetime.now().isoformat())
]

cursor.executemany('INSERT OR REPLACE INTO orders VALUES (?, ?, ?, ?, ?, ?)', orders)


conn.commit()

cursor.execute('SELECT * FROM orders')
rows = cursor.fetchall()

print("orders from the SQL database")

for row in rows:
  print({
        "order_id": row[0],
        "seller": row[1],
        "buyer": row[2],
        "product": row[3],
        "price": row[4],
        "time": row[5]
    })

conn.close()
