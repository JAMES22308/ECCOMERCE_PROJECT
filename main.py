import os
from auth.register_page import register
from auth.login_page import login
from crud.add import add_product
from crud.search import search_product
from crud.edit import edit_product
from crud.delete import delete_product
from crud.products import view_all_products
from crud.orders_status import order_status
from user_crud.add import add_user_product
from user_crud.view import view_cart
from user_crud.orders import view_orders
from tqdm import tqdm
import time


def load_project(total_steps=20, delay=0.2):
    print("Loading Project:")
    for _ in tqdm(range(total_steps)):
        time.sleep(delay)
    print("Loading Complete!\n")

def directory():
    folder = 'database'
    if os.path.exists(folder):
        print('')
    else:
        os.mkdir(folder)
        files = ['counter_id.json', 'data_entries.json', 'product_id.json', 'products.json']
        for file in files:
            file_path = os.path.join(folder, file)
            with open(file_path, 'w')as file:
                file.write('')
        


def option():
    print("\n" + "=" * 40)
    print("        🔐 AUTHENTICATION MENU        ")
    print("=" * 40 + "\n")

    
    print("Please choose an option:")
    print("  [1] 📝 Register")
    print("  [2] 🔓 Login")


def prompt():
    opt = input('Select an option: ')
    if opt.replace(' ', ''). isdigit():
        converted = int(opt)
        return converted



def authentication():
    while True:
        option()
        user_option = prompt()
        if user_option == 1:
            register()
        elif user_option == 2:
            result = login()
            return result
        elif user_option == 0:
            break
        else:
            print('invalid key')


def get_options():
    options = {
        '1': 'add',
        '2': 'search',
        '3': 'edit',
        '4': 'delete',
        '5': 'all products',
        '6': 'orders status',
        '0': 'logout'
    }
    print()
    for key, value in options.items():
        print(f"{key}: {value}")



def user_get_options():
    options = {
        '1': '🛍️ View All Products',
        '2': '🧺 View My Cart',
        '3': '📦 View My Orders',
        '0': '🔓 Logout'
    }
    print('\n' + '='*45)
    print("📋 What would you like to do today?")
    print('-'*45)
    for key, value in options.items():
        print(f" [{key}] {value}")
    print('='*45 + '\n')

def main():
    load_project()
    directory()

    while True:
        auth = authentication()

        if not auth:
            return
        if auth[0] == 'admin':
            print('admin account dashboard')
            while True:
                get_options()
                prompt = input('\nChoose an option: ')
                if prompt == '1':
                    add_product()
                elif prompt == '2':
                    search_product()
                elif prompt == '3':
                    edit_product()
                elif prompt == '4':
                    delete_product()
                elif prompt == '5':
                    view_all_products()
                elif prompt == '6':
                    order_status()
                elif prompt == '0':
                    print('logging out')
                    break
                else:
                    print('wrong key')
        
        if auth[0] == 'user':
            user = auth[1]
            print('\n' + '='*50)
            print(f"👋 Welcome, {user['email'].replace("@gmail.com", "")}!")
            print("🧾 USER ACCOUNT DASHBOARD")
            print('='*50)

            while True:
                user_get_options()
                option = input('\nChoose an option: ').strip()
                if option == '1':
                    add_user_product(user)
                elif option == '2':
                    view_cart(user)
                elif option == '3':
                    view_orders(user)
                elif option == '0':
                    print('logging out')
                    break
                else:
                    print('wrong key')

def browser():
    print("Welcome to James Browser!")
    while True:
        url = input("\nEnter a URL (or type 'exit' to quit): ").strip()
        
        if url.lower() == "exit":
            print("Exiting browser. Goodbye!")
            break
        elif url.lower() == "www.ecommerce.com":
            main()  
        else:
            print(f"URL '{url}' not recognized. Try again or type 'exit' to quit.")
            


if __name__ == '__main__':
    browser()