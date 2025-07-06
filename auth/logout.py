

def logout_user():

    prompt = input('do you want to log out?: ').lower()
    if prompt == 'yes' or prompt == 'y':
        print('logged out')

    else:
        print('stayed login')
        
    return

if __name__ == '__main__':
    print("WARNING: This file is a module and should not be executed directly.")
    


