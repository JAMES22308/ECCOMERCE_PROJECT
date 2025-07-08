import json
from config import PRODUCTS_INFO
from crud.add import product_name, product_price, product_stock, product_category, dic_reader
from crud.search import current_products


def edit_product():

    try:
        products = dic_reader()
        current_products(products)

        product_id = input('search by id: ').strip()

        product_id = int(product_id) if product_id and product_id.replace(' ', '').isdigit() else None

        found = False

        if product_id is None:
            print('invalid id')
            return
        
        for product in products:
            if product['id'] == product_id:
                print(f"\n========PRODUCT INFORMATION=======\nId: {product['id']}\nproduct name: {product['name']}\nproduct price: {product['price']}\nproduct stock: {product['stock']}\nproduct category: {product['category']}\n")

                product['name'] = product_name(n="new name: ")
                product['price'] = product_price(p="new price: ")
                product['stock'] = product_stock(s="new stock: ")
                product['category'] = product_category(c="new category: ")
                found = True
        
        if found:
            with open(PRODUCTS_INFO, 'w')as file:
                json.dump(products, file, indent=4)
            print('\nsuccessfully updated\n')
        else:
            print('\nid not found\n')
    
    except json.decoder.JSONDecodeError:
        print('no data in the system yet')

        
   