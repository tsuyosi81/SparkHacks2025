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
    Amount INT NOT NULL,
    Product TEXT NOT NULL,
    Price REAL NOT NULL,
    Time TEXT NOT NULL
)
''')



# ##################
orders = [
    (1, 'Alice', 'Bob', 3,'Widget', 9.99, datetime.datetime.now().isoformat()),
    (3, 'Alice', 'Bruce', 1, 'Project', 99.99, datetime.datetime.now().isoformat()),
    (2, 'Charlie', 'Dana', 5,'Gadget', 19.99, datetime.datetime.now().isoformat())
]
####################

cursor.executemany('INSERT OR REPLACE INTO orders VALUES (?, ?, ?, ?, ?, ?, ?)', orders)


conn.commit()

def create_new_order(seller, buyer, product, price):
    
    order_time = datetime.datetime.now().isoformat()

    cursor.execute(
        'INSERT INTO orders (Seller, Buyer, Product, Price, Time) VALUES (?, ?, ?, ?, ?)', 
        (seller, buyer, product, price, order_time)
    )

    conn.commit()

    oder_id_updated = cursor.lastrowid

    print(f"New order created with Order ID: {oder_id_updated}")
    return oder_id_updated


def update_order(order_id, seller, new_buyer=None, new_product=None, new_price=None):
    
    cursor.execute('SELECT * FROM orders WHERE Order_id = ?', (order_id,))

    order = cursor.fetchone()

    if not order:
        print("Order not found.")
        return False
    if order[1] != seller:  
        print("Unauthorized: Seller does not match order's seller.")
        return False

    To_Update = []

    params = []

    if new_buyer is not None:
        To_Update.append("Buyer = ?")
        params.append(new_buyer)

    if new_product is not None:
        To_Update.append("Product = ?")
        params.append(new_product)

    if new_price is not None:
        To_Update.append("Price = ?")
        params.append(new_price)
        
    if not To_Update:
        print("No fields provided for update.")
        return False
    
    To_Update.append("Time = ?")
    params.append(datetime.datetime.now().isoformat())

    params.append(order_id)

    sql = f"UPDATE orders SET {', '.join(To_Update)} WHERE Order_id = ?"

    cursor.execute(sql, params)
    conn.commit()
    print(f"Order {order_id} updated successfully ")

    return True



def delete_order(order_id, seller):
    
    cursor.execute('SELECT * FROM orders WHERE Order_id = ?', (order_id,))

    order = cursor.fetchone()

    if not order:
        print("Order not found.")
        return False
    if order[1] != seller:
        print("Unauthorized - Seller does not match order's seller.")
        return False

    cursor.execute('DELETE FROM orders WHERE Order_id = ?', (order_id,))

    conn.commit()

    print(f"Order {order_id} deleted successfully.")

    return True




def request_order_by_id(order_id):
    
    cursor.execute('SELECT * FROM orders WHERE Order_id = ?', (order_id,))
    order = cursor.fetchone()
    if order:
        return {
            "order_id": order[0],
            "seller": order[1],
            "buyer": order[2],
            "product": order[3],
            "price": order[4],
            "time": order[5]
        }
    else:
        print("Order not found.")
        return None
    


def request_orders_by_seller(seller):
    
    cursor.execute('SELECT * FROM orders WHERE Seller = ?', (seller,))

    rows = cursor.fetchall()

    orders_list = []

    for row in rows:
        orders_list.append({
            "order_id": row[0],
            "seller": row[1],
            "buyer": row[2],
            "product": row[3],
            "price": row[4],
            "time": row[5]
        })

    return orders_list




# cursor.execute('SELECT * FROM orders')
# rows = cursor.fetchall()

# print("orders from the SQL database")

# for row in rows:
#   print({
#         "order_id": row[0],
#         "seller": row[1],
#         "buyer": row[2],
#         "product": row[3],
#         "price": row[4],
#         "time": row[5]
#     })
  
  
if __name__ == "__main__":
    print("Initial orders in the SQL database:")

    cursor.execute('SELECT * FROM orders')
    rows = cursor.fetchall()

    for row in rows:
        print({
            "order_id": row[0],
            "seller": row[1],
            "buyer": row[2],
            "amount":row[3],
            "product": row[4],
            "price": row[5],
            "time": row[6]
        })

        # #####################################

    # oder_id_check = create_new_order("Alice", "Eve", "NewWidget", 15.99)

    # update_order(oder_id_check, "Alice", new_product="SuperWidget", new_price=17.99)


    # order_details = request_order_by_id(oder_id_check)
    # print("\nDetails of the updated order:")
    # print(order_details)
    
    # print("\nOrders for seller Alice ")
    # seller_orders = request_orders_by_seller("Alice")
    # for order in seller_orders:
    #     print(order)
    
    
    # delete_order(oder_id_check, "Alice")
    
    # print("\nOrders for seller 'Alice' after deletion:")
    # seller_orders = request_orders_by_seller("Alice")
    # for order in seller_orders:
    #     print(order)

        # ##################################################
    




conn.close()
