import json

def read_products():
    with open("products.json",'r') as f:
        return json.load(f)



def update_product(seller, product, price):

    data = read_products()
    
    for i in data[seller]['products']:
        if i['name'] == product:
            i['price'] = price
            

    with open("products.json",'w') as f:
        json.dump(data,f)

def update_stock(seller, product, stock):

    data = read_products()
    
    for i in data[seller]['products']:
        if i['name'] == product:
            i['stock'] = stock
            

    with open("products.json",'w') as f:
        json.dump(data,f)

def create_product(seller, product, price, stock):

    data = read_products()

    if seller in data.keys():
        data[seller]['products'].append({"name":product, "price":price, "stock":stock})
    else:
        data[seller] = {'products':[]}
        data[seller]['products'].append({"name":product, "price":price, "stock":stock})

    with open("products.json",'w') as f:
        json.dump(data,f)

def delete_product(seller,product):
    
    data = read_products()

    item = {}
    for i in data[seller]["products"]:
        print(i)
        if i["name"] == product:
            item = i
    if item != {}:
        data[seller]['products'].remove(item)

    with open("products.json",'w') as f:
        json.dump(data,f)

            


    

print(read_products())
update_product('company1','generic phone',40000)
update_stock('company1','generic phone', 200)
# create_product('company2','apple',300,1)
delete_product('company2','apple')
print(read_products())