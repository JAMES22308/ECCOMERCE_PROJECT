from config import PRODUCTS_INFO
import json

def dic_reader():
    with open(PRODUCTS_INFO, 'r')as file:
        content = json.load(file)
    return content



def display_products(product_info_id, product_name, product_list):
    if product_info_id:
        print('\n🆔========= PRODUCT ID MATCH =========🆔\n')
        for i in product_info_id:
            for x, y in i.items():
                print(f"🔹 {x.capitalize():<12}: {y}")
            print('-' * 40)

    if product_name:
        
        print('\n🔤========= PRODUCT NAME MATCH =========🔤\n')
        for a in product_name:
            for b, c in a.items():
                print(f"🔹 {b.capitalize():<12}: {c}")
            print('-' * 40)

    if product_list:
        print('\n📦========= PRODUCT CATEGORY MATCH =========📦\n')
        for f in product_list:
            for t, y in f.items():
                print(f"🔹 {t.capitalize():<12}: {y}")
            print('-' * 40)



def sort_product(products, product_id, product_name, category):
    

    product_list = []
    product_info_id = []
    name_of_product = []

    for product in products:
        if product_id is not None and product['id'] == product_id:
            product_info_id.append(product)

        if category is not None and product['category'] == category:
            product_list.append(product) 

        if name_of_product is not None and product['name'] == product_name:
            name_of_product.append(product)
        
        

    return (product_info_id, name_of_product, product_list)
        


def search_product():

    products = dic_reader()

    product_id = input("Enter Product ID (press Enter to skip): ").strip()
    product_name = input("Enter Product Name (press Enter to skip): ").strip()
    category = input("Enter Category (press Enter to skip): ").strip()
    

    product_id = int(product_id) if product_id and product_id.replace(' ', '').isdigit() else None  
    product_name = product_name if product_name else None

    category = category if category else None

    results = sort_product(products, product_id, product_name, category)

    product_info_id = results[0]
    product_name = results[1]
    product_list = results[2]

    display_products(product_info_id, product_name, product_list)

   

  





    








