import json
from config import DATA_ENTRY
from crud.add import dic_reader
from crud.search import current_products




def account_cart(account, product_info, quantity):
    count = 0
    found = False
    for i, x in account.items():
        if i == 'cart':
            for n in x:
                if n['order_id'] == product_info['id']:
                    found = True
                    break
                else:
                    count += 1
    
    return (count, found)


def product_quantity(products, item_order, user):
    found = False
    id_found = False
    product_info = None
    for product in products:
        if product['id'] == item_order:
            id_found = True
            quantity = int(input('quantity: '))
            if quantity <= product['stock']:
                # current_quantity = product['stock'] - quantity
                # product['stock'] = current_quantity
                product_info = product
                found = True
            if product['stock'] == 0:
                print(f"❌ Sorry! {product['name']} is out of stock.")
                return
            
            if quantity > product['stock']:
                print(f'{product['stock']} pcs available atm, thanks!')
                return
    if not id_found:
        print('id not found')
        return
    

    if found:
        #dont save it till not place order
        # with open(PRODUCTS_INFO, 'w')as file:
        #     json.dump(products, file, indent=4)

        with open(DATA_ENTRY, 'r')as file:
            content = json.load(file)
            for account in content:
                if account['email'] == user['email'] and account['password'] == user['password']:

                    cart = account_cart(account, product_info, quantity)
                    index = cart[0]
                    same_id = cart[1]

                    if same_id:
                        account['cart'][index]['quantity'] = account['cart'][index]['quantity'] + quantity
                        account['cart'][index]['total_price'] = account['cart'][index]['quantity'] * product_info['price']

                        print(f'📈 Quantity increased by {quantity}')



                    if not same_id:
                        account['cart'].append({
                            'order_id': product_info['id'],
                            'product_name': product_info['name'],
                            'quantity': quantity,
                            'price': product_info['price'],
                            'total_price': product_info['price'] * quantity
                        })
                        print('🛒 Item successfully added to cart!')

                    with open(DATA_ENTRY, 'w')as file:
                        json.dump(content, file, indent=4)
                    


def add_user_product(user):
    try:
        products = dic_reader()
        current_products(products)

        item_order = input('Enter Product ID to add to cart or press Enter to return: ').strip()

        item_order = int(item_order) if item_order and item_order.replace(' ', '').isdigit() else None

        if item_order is None:
            print('enter an id pls')
            return 
        
        product_quantity(products, item_order, user)
    except json.decoder.JSONDecodeError:
        print('no product at the moment')

    


