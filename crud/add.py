import json
from config import PRODUCTS_INFO, PRODUCT_ID

def dic_reader():
    with open(PRODUCTS_INFO, 'r')as file:
        content = json.load(file)
    return content


def empty_list():
    with open(PRODUCTS_INFO, 'r')as file:
        content = file.read()
    if content == "":
        with open(PRODUCTS_INFO, 'w')as file:
            json.dump([], file)

def product_name(n="name: "):
    while True:
        name = input(n)
        if name.replace(' ', '').isalpha():
            return name
        else:
            print('must be an alpha')
    
def product_price(p="price: "):
    while True:
        price = input(p)
        if price.replace(' ', '').isdigit():
            converted = float(price)
            return converted
        else:
            print('must be a digit')
    

def product_stock(s="stock: "):
    while True:
        stock = input(s)
        if stock.replace(' ', '').isdigit():
            converted = int(stock)
            return converted
        else:
            print('must be a digit')
    

def product_category(c="category: "):
    while True:
        category = input(c)
        if category.replace(' ', '').isalpha():
            return category
        else:
            print('must be an alpha')


def unique_id():
    with open(PRODUCT_ID, 'r')as file:
        content = file.read()
    if content == '':
        current_id = 1
    else:
        previous_id = json.loads(content)
        current_id = previous_id['id'] + 1
    with open(PRODUCT_ID, 'w')as file:
        json.dump({'id': current_id}, file, indent=4)
    return current_id


def add_product():
    empty_list()
    content = dic_reader()
    name = product_name()
    price = product_price()
    stock = product_stock()
    category = product_category()

    product = {
        'id': unique_id(),
        'name': name,
        'price': price,
        'stock': stock,
        'category': category
    }

    content.append(product)
    with open(PRODUCTS_INFO, 'w')as file:
        json.dump(content, file, indent=4)
    print('product has been added')

    

