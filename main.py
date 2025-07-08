from auth.register_page import register
from auth.login_page import login
from crud.add import add_product
from crud.search import search_product
from crud.edit import edit_product
from crud.delete import delete_product
from crud.products import view_all_products

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

def main():
    auth = authentication()
    if auth == 'admin':
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
    
    if auth == 'user':
        print('user account dashboard')




if __name__ == '__main__':
    main()