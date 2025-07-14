import json
from config import DATA_ENTRY, PRODUCTS_INFO



def reader():
    with open(DATA_ENTRY, 'r')as file:
        content = json.load(file)
    return content


def cart_items(user):
    content = reader()
    total_cost = 0

    print("\n🛒 ============= YOUR CART ============= 🛒\n")

    for entry in content:
        if entry['id'] == user['id']:
            for item in entry['cart']:
                print(f"🆔  Product ID   : {item['order_id']}")
                print(f"🏷️   Name         : {item['product_name']}")
                print(f"🔢  Quantity     : {item['quantity']}")
                print(f"💲  Price/Unit   : {item['price']}")
                print(f"💰  Subtotal     : {item['total_price']}")
                print("-" * 40 + "\n")
                total_cost += item['total_price']

    
    print(f"🧾  Total Amount : {total_cost:.2f}")
    print("\n" + "\n")



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

# def edit_order(user):
#     increment_count = 0
#     increment = False
#     account = entry_finder(user)
#     acc = account[0]
#     acc2 = account[1]
#     products = product_info()
#     id_not_found = False
#     id = int(input('enter an id: '))
#     for i in acc['cart']:
#         if id == i['order_id']:
#             id_not_found = True
#             quantity = int(input('new quantity: '))
#             if quantity > i['quantity']:
#                 for x in range(1, quantity):
#                     if x >= i['quantity']:
#                         increment_count += 1
#                         increment = True

#             elif quantity <= i['quantity']:
#                 # deducted = i['quantity'] - quantity
#                 # print(deducted)
#                 # for product in products:
#                 #     if id == product['id']:
#                 #         product['stock'] = product['stock'] + deducted
#                 #         if id == i['order_id']:
#                 #             i['quantity'] = quantity
#                 #             i['total_price'] = quantity * i['price']

#                 with open(DATA_ENTRY, 'w')as file:
#                     json.dump(acc2, file, indent=4)
#                 with open(PRODUCTS_INFO, 'w')as file:
#                     json.dump(products, file, indent=4)
#                 print('product deducted successfully')
#                 return
#     if not id_not_found:
#         print('id not found')
#         return

#     if increment:
#         for product in products:
#             if id == product['id']:
#                 current_q = product['stock'] - increment_count
#                 if current_q >= 0:
#                     product['stock'] = current_q
#                     for z in acc['cart']:
#                         if id == z['order_id']:
#                             z['quantity'] = quantity
#                             z['total_price'] = z['price'] * quantity
#                     with open(DATA_ENTRY, 'w')as file:
#                         json.dump(acc2, file, indent=4)

#                     with open(PRODUCTS_INFO, 'w')as file:
#                         json.dump(products, file, indent=4)
#                     print('updated successfully')

#                 if current_q < 0:
#                     print('out of stock')
#                     return

def edit_order(user):

    entry_order = reader()
    products = product_info()
    id = int(input('enter the id: '))
    for entry in entry_order:
        if entry['id'] == user['id']:
            if entry['cart']:
                for item in entry['cart']:
                    if id == item['order_id']:
                        quantity = int(input('new quantity: '))
                        for product in products:
                            if product['id'] == id:
                                if quantity > item['quantity']:
                                    if quantity > product['stock']:
                                        print('out of stock')
                                        return
                                    if quantity <= product['stock']:
                                        item['quantity'] = quantity
                                        
                                        print(f'increased by {quantity} successfully')
                                
                                if quantity < item['quantity']:
                                    item['quantity'] = quantity
                                    print(f'decreased by {quantity} successfully')

                                with open(DATA_ENTRY, 'w')as file:
                                    json.dump(entry_order, file, indent=4)

                                    
        





def delete_order(user):
    entries = reader()
    id_not_found = False
    data = None

    print("\n🗑️ ===== DELETE ORDER ITEM ===== 🗑️")
    id = int(input('🔢 Enter Order ID to delete: '))

    for entry in entries:
        if entry['id'] == user['id']:
            for i in entry['cart']:
                if id == i['order_id']:
                    id_not_found = True
                    data = i
                    entry['cart'].remove(i)

                    with open(DATA_ENTRY, 'w') as file:
                        json.dump(entries, file, indent=4)

                    print(f"\n✅ Order ID {id} has been successfully removed.\n")

    if not id_not_found:
        print('\n❌ Order ID not found.\n')
        return

    # if data is not None:
    #     products = product_info()
    #     for product in products:
    #         if product['id'] == data['order_id']:
    #             product['stock'] = product['stock'] + data['quantity']
    #             with open(PRODUCTS_INFO, 'w') as file:
    #                 json.dump(products, file, indent=4)

    #     print("📦 Product stock has been updated.\n")


    
       
def place_order(user):
    print("\nProceed with payment and place order?\n")
    option = input("[y] Yes   [n] No   →  ").strip()
    items = []
    order_place = False
    if option == 'y' or option == 'yes':
        entries = reader()
        for entry in entries:
            if entry['id'] == user['id']:
                for item in entry['cart']:
                    products = product_info()
                    for product in products:
                        if item['order_id'] == product['id']:
                            if item['quantity'] <= product['stock']:
                                items.append(item)

                                product['stock'] = product['stock'] - item['quantity']

                                with open(PRODUCTS_INFO, 'w')as file:
                                    json.dump(products, file, indent=4)
                                order_place = True
                            
                            elif item['quantity'] > product['stock']:
                                
                                print(f'we got only {product['stock']} available, pls reduce the quantity, we are out of stock atm, thanks!')
                                return
                    
    if order_place:
        print('successfully placed order')
        hold = False
        hold_items = []
        total = 0
        entries = reader()
        for entry in entries:
            if entry['id'] == user['id']:
                for i in entry['cart']:
                    total += i['total_price']
                    hold_items.append(i)
                    hold = True
        
        if hold:

            ordered_items = {
                'id': '001',
                'items': hold_items,
                'total_amount': total,
                'status': 'processing',
                'date': 'test'
            }
            
            accounts = reader()
            for entry in accounts:
                if entry['id'] == user['id']:
                    entry['orders'].append(ordered_items)

                    

            for items_placed in accounts:
                if items_placed['id'] == user['id']:
                    items_placed['cart'].clear()

            with open(DATA_ENTRY, 'w')as file:
                        json.dump(accounts, file, indent=4)
            
            # with open(PRODUCTS_INFO, 'w')as file:
            #     json.dump(products, file, indent=4)


                                
                            
    

def view_cart(user):

    cart_items(user)
    

    while True:
        options()
        chosen = input('Select an option: ').strip()

        if chosen == '1':
            cart_items(user)
            edit_order(user)
            return
        elif chosen == '2':
            cart_items(user)
            delete_order(user)
            return
        elif chosen == '3':
            cart_items(user)
            place_order(user)
        else:
            print('returned back')
            return





