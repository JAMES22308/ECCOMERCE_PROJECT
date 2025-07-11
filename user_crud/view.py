import json
from config import DATA_ENTRY, PRODUCTS_INFO



def reader():
    with open(DATA_ENTRY, 'r')as file:
        content = json.load(file)
    return content


def cart_items(user):
    content = reader()
    total_cost = 0


    print("="*40)  
    print(" " * 12 + "🛒 Your Shopping Cart 🛒")
    print("="*40) 
    

    for entry in content:
        if entry['id'] == user['id']:
            for key in entry['cart']:
                print("product id: ",key['order_id'])
                print("product name: ",key['product_name'])
                print("product quantity: ",key['quantity'])
                print("product price: ",key['price'])
                print("\ntotal price: ",key['total_price'])
                total_cost += key['total_price']
                print("="* 40 )

    print("="*40) 
    print(f"💸 Total Cost: ${total_cost:.2f}")
    print("="*40) 



def options():
    print()
    choices = {
        '[1]': 'edit',
        '[2]': 'delete',
        '[3]': 'place order'
    }

    for item, value in choices.items():
        print(f"{item}: {value}")
    print()



def entry_finder(user):
    content = reader()
    for acc in content:
        if acc['id'] == user['id']:
            return (acc, content)


def product_info():
    with open(PRODUCTS_INFO, 'r')as file:
        content = json.load(file)
    return content

def edit_order(user):
    increment_count = 0
    increment = False
    account = entry_finder(user)
    acc = account[0]
    acc2 = account[1]
    products = product_info()

    id = int(input('enter an id: '))
    for i in acc['cart']:
        if id == i['order_id']:
            quantity = int(input('new quantity: '))
            if quantity > i['quantity']:
                for x in range(1, quantity):
                    if x >= i['quantity']:
                        increment_count += 1
                        increment = True

            if quantity < i['quantity']:
                deducted = i['quantity'] - quantity
                print(deducted)
                for product in products:
                    if id == product['id']:
                        product['stock'] = product['stock'] + deducted
                        if id == i['order_id']:
                            i['quantity'] = quantity
                            i['total_price'] = quantity * i['price']

                            with open(DATA_ENTRY, 'w')as file:
                                json.dump(acc2, file, indent=4)
                            with open(PRODUCTS_INFO, 'w')as file:
                                json.dump(products, file, indent=4)
                            print('product deducted successfully')
                            return

    if increment:
        for product in products:
            if id == product['id']:
                current_q = product['stock'] - increment_count
                if current_q >= 0:
                    product['stock'] = current_q
                    for z in acc['cart']:
                        if id == z['order_id']:
                            z['quantity'] = quantity
                            z['total_price'] = z['price'] * quantity
                    with open(DATA_ENTRY, 'w')as file:
                        json.dump(acc2, file, indent=4)

                    with open(PRODUCTS_INFO, 'w')as file:
                        json.dump(products, file, indent=4)
                    print('updated successfully')

                if current_q < 0:
                    print('out of stock')
                    return


        

    

def view_cart(user):

    cart_items(user)

    while True:
        options()
        chosen = int(input('Select an option: '))

        if chosen == 1:
            edit_order(user)





