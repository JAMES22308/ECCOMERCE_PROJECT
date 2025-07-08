import json

from config import PRODUCTS_INFO
from crud.add import dic_reader




def delete_product():
    products = dic_reader()
    
    print("\n🗂️ ===== CURRENT PRODUCT LIST ===== 🗂️\n")
    for product in products:
        print("🆔 ID          :", product['id'])
        print("🔤 Name        :", product['name'])
        print("💵 Price       :", product['price'])
        print("📦 Category    :", product['category'])
        print("-" * 40)
    
    print("\n🗑️ ===== DELETE PRODUCT ===== 🗑️")
    product_id = input("🔎 Enter Product ID to delete: ").strip()
    
    product_id = int(product_id) if product_id and product_id.isdigit() else None

    if product_id is None:
        print("\n❌ Invalid ID. Please enter a valid numeric Product ID.\n")
        return
    
    found = False
    for product in products:
        if product['id'] == product_id:
            products.remove(product)
            found = True

    if found:
        with open(PRODUCTS_INFO, 'w') as file:
            json.dump(products, file, indent=4)
        print(f"\n✅ Product with ID {product_id} was successfully deleted.\n")
    else:
        print(f"\n⚠️ Product with ID {product_id} not found.\n")
