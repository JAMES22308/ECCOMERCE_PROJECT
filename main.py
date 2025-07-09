from auth.register_page import register
from auth.login_page import login
from crud.add import add_product, dic_reader
from crud.search import search_product
from crud.edit import edit_product
from crud.delete import delete_product
from crud.products import view_all_products
from user_crud.add import add_user_product


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
        '5': 'all products'
    }
    print()
    for key, value in options.items():
        print(f"{key}: {value}")



def user_get_options():
    options = {
        '1': '🛍️ View All Products',
        '2': '🧺 View My Cart',
        '3': '📦 View My Orders',
        '4': '🔓 Logout'
    }
    print('\n' + '='*45)
    print("📋 What would you like to do today?")
    print('-'*45)
    for key, value in options.items():
        print(f" [{key}] {value}")
    print('='*45 + '\n')

def main():
    auth = authentication()
    if auth[0] == 'admin':
        print('admin account dashboard')
        while True:
            get_options()
            prompt = int(input('\nChoose an option: '))
            if prompt == 1:
                add_product()
            elif prompt == 2:
                search_product()
            elif prompt == 3:
                edit_product()
            elif prompt == 4:
                delete_product()
            elif prompt == 5:
                view_all_products()
    
    if auth[0] == 'user':
        user = auth[1]
        print('\n' + '='*50)
        print(f"👋 Welcome, {user['email'].replace("@gmail.com", "")}!")
        print("🧾 USER ACCOUNT DASHBOARD")
        print('='*50)

        while True:
            user_get_options()
            option = int(input('\nChoose an option: '))
            if option == 1:
                add_user_product(user)
            else:
                print('wrong key')
            

        




if __name__ == '__main__':
    main()