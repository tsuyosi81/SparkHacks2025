from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def root_path():
    return "<h1>root</h1>"

@app.route('/home')
def home():
    return "<h1>home</h1>"

@app.route('/login')
def login():
    return "<h1>login</h1>"

@app.route('/buyer')
def buyer():
    return "<h1>buyer</h1>"

@app.route('/seller')
def seller():
    return "<h1>seller</h1>"

@app.route('/seller/table')
def seller_table():
    return "<h1>seller table</h1>"
    
@app.route('/seller/table/<number>')
def seller_table_number(number):
    return render_template("hello.html",order=number)
