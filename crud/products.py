import json
from crud.add import dic_reader



def view_all_products():
    products = dic_reader()

    if not products:
        print("\n🚫 No products available.\n")
        return

    print("\n📦========= ALL PRODUCTS =========📦\n")
    
    for index, product in enumerate(products, start=1):
        print(f"🛒 Product {index}")
        print("-" * 30)
        for key, value in product.items():
            print(f"🔹 {key.capitalize():<12}: {value}")
        print("-" * 30 + "\n")
