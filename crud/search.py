from config import PRODUCTS_INFO
import json

def dic_reader():
    with open(PRODUCTS_INFO, 'r')as file:
        content = json.load(file)
    return content


def products_list(products, product_id=None, category=None):
    result = []
    if product_id is not None and product_id.replace(' ', '').isdigit():
        int(product_id)

    for product in products:
        if product_id is not None and product['id'] != product_id:
            continue
        elif category and product['category'] != category:
            continue
        else:
            result.append(product)

    return result




def search_product():

    products = dic_reader()
    product_id = input("Enter Product ID (press Enter to skip): ").strip()
    category = input("Enter Category (press Enter to skip): ").strip()

    product_id = product_id if product_id else None
    category = category if category else None

    products = products_list(products, product_id, category)
    

    if products:
        for product in products:
            print(product)









