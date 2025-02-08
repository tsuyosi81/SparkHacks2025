from flask import Flask, render_template, request, redirect, url_for
from flask import g
import sqlite3
from datetime import datetime
# import storage

conn = sqlite3.connect("orders.db")
cursor = conn.cursor()

app = Flask(__name__)

DATABASE = "orders.db"#C:\Users\crime\SparkHacks2025\orders.db orders.db

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

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


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def root_path():
    return "<h1>root</h1>"

@app.route('/home')
def home():
    return "<h1>home</h1>"

@app.route('/seller/<name>/product')
def seller_product(name):
    return "<h1>"

@app.route('/seller/<name>/table') #:)
def seller_table(name):
    cursor = get_db().cursor()
    cursor.execute('SELECT * FROM orders WHERE Seller = ?', (name,))

    rows = cursor.fetchall()

    orders_list = []

    for row in rows:
        orders_list.append({
            "order_id": row[0],
            "seller": row[1],
            "buyer": row[2],
            "amount":row[3],
            "product": row[4],
            "price": row[5],
            "time": row[6]
        })
    return render_template("table.html",orders=orders_list)
    
@app.get('/seller/<name>/table/<number>')       #:|
def seller_table_number(number,name):
    cursor = get_db().cursor()
    cursor.execute('SELECT * FROM orders WHERE Order_id = ?', (number,))
    idorder = cursor.fetchone()
    print(idorder)
    if idorder:
        return render_template("hello.html",order=idorder)
    else:
        print("Order not found.")
        return render_template("notfound.html")
    
@app.post('/seller/<name>/table/<number>')
def update_order(name, number):
    cursor = get_db().cursor()
    cursor.execute('SELECT * FROM orders WHERE Order_id = ?', (number,))
    print('got post')
    print(request.form.to_dict())
    order = cursor.fetchone()
    To_Update = []

    params = []

    if request.form['new_buyer']:
        print("there is a new buyer")
        To_Update.append("Buyer = ?")
        params.append(request.form['new_buyer'])
        
    if not To_Update:
        print("No fields provided for update.")
        return False
    
    To_Update.append("Time = ?")
    params.append(datetime.now().isoformat())

    params.append(number)
    print(To_Update)
    print(params)
    sql = f"UPDATE orders SET {', '.join(To_Update)} WHERE Order_id = ?"

    cursor.execute(sql, params)
    
    target = f'/seller/{name}/table/{number}'
    return redirect(target)

@app.route('/seller/<name>/products/')
def edit_products(name):
    pass


conn.close()

