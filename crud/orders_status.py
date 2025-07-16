import json
from config import DATA_ENTRY

def status_options():
    stat = ['processing', 'shipped', 'cancelled', 'failed', 'delivered']
    return stat


def reader():
    with open(DATA_ENTRY, 'r')as file:
        content = json.load(file)
    return content


def display_user():
    entries = reader() 

    for entry in entries:
        if entry["role"] == "admin":
            continue  
        print("\n" + "=" * 40)
        print(f"👤  USER: {entry['email'].replace('@gmail.com', '')}  "
              f"(ID: {entry['id']})")
        print("=" * 40)


        if not entry['orders']:
            print('This account has no order yet')


        for idx, order in enumerate(entry['orders'], start=1):
            print(f"\n  🧾  ORDER {idx}")
            print("  " + "-" * 40)
            print(f"  🆔 Order ID     : {order['id']}")
            print(f"  📅 Date         : {order['date']}")
            print(f"  📄 Status       : {order['status'].capitalize()}")
            print("  🛒 Items        :")

            for item in order['items']:
                print(f"     • {item['product_name']} — Qty: {item['quantity']} — "
                    f"${item['price']} each")

            print(f"  💰 Total Amount : ${order['total_amount']}")
            print("  " + "-" * 40)

        print()  


def order_status():
    display_user()
    entries = reader()
    status_result = status_options()  # Assumed to return dict like {0: 'processing', 1: 'shipped', ...}

    print("\n" + "=" * 50)
    id = input("🔎 Select the user ID: ")
    id = int(id) if id and id.replace(' ', '').isdigit() else None

    if id is None:
        print("❌ Cancelled: Invalid or no ID provided.")
        return

    for entry in entries:
        if id == entry['id']:
            print("\n" + "=" * 50)
            print(f"📦 Orders for: {entry['email'].replace('@gmail.com', '')}")
            print("=" * 50)

            for order in entry['orders']:
                print(f"\n🆔 Order ID     : {order['id']}")
                print(f"📅 Date         : {order['date']}")
                print(f"📄 Status       : {order['status'].capitalize()}")
                print("🛒 Items        :")
                for item in order['items']:
                    print(f"   • {item['product_name']} — Qty: {item['quantity']} — "
                          f"${item['price']} each")
                print(f"💰 Total Amount : ${order['total_amount']}")
                print("-" * 50)

            print("\n" + "=" * 50)
            order_id = input("✏️  Enter the Order ID to update: ")

            for order in entry['orders']:
                if order_id == order['id']:
                    print("\n🔄 Choose new status:")
                    print(" [0] Processing")
                    print(" [1] Shipped")
                    print(" [2] Cancelled")
                    print(" [3] Failed")
                    print(" [4] Delivered\n")

                    status_input = input("👉 Enter status number (0–4): ")

                    if status_input in ['0', '1', '2', '3', '4']:
                        status_code = int(status_input)
                        new_status = status_result[status_code]
                        order['status'] = new_status

                        with open(DATA_ENTRY, 'w') as file:
                            json.dump(entries, file, indent=4)
                        
                        print(f"\n✅ Status successfully updated to **{new_status.upper()}**.")
                        return
                    else:
                        print("❌ Cancelled: Invalid status input.")
                        return




    
