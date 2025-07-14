import json
from user_crud.view import reader, product_info

def view_orders(user):
    entries = reader()
    products = product_info()

    print("\n📦============= MY ORDERS =============📦\n")

    for entry in entries:
        if entry['id'] == user['id']:
            for value in entry['orders']:
                print(f"🆔 Order ID      : {value['id']}")
                print(f"📅 Date          : {value['date']}")
                print(f"📄 Status        : {value['status']}")
                print("🛒 Items:")
                for item in value['items']:
                    print(f"   • {item['product_name']} — Qty: {item['quantity']} — "f"${item['price']} each")
                print(f"💰 Total Amount  : ${value['total_amount']}")
                print("-" * 40)
