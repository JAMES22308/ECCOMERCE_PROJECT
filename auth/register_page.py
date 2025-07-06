import json
from config import COUNTER_ID, DATA_ENTRY

def get_email(m="Email: "):
    admin = False
    database = handling_empty_file()
    with open(database, 'r') as file:
        content = json.load(file)
    if content:
        for data in content:
            if 'admin' in data['role']:
                admin = True

    email = input(m).strip()

    if '@' in email and '.' in email:
        if admin and 'admin' in email:
            print('⚠️ Admin account already exists. Only one admin is allowed.')
            return 
        else:
            if content:
                if email == data['email']:
                    print('⚠️ Email already exists. Please use a different one.')
                    return
            return email
    else:
        print('❌ Invalid email format. Please include "@" and "."')
        return


def get_password(p="Password: "):
    password = input(p).strip()
    return password if len(password) > 5 else None
 

def handling_empty_file():
    database = DATA_ENTRY
    with open(database, 'r') as file:
        content = file.read()
        if content == '':
            with open(database, 'w') as file:
                json.dump([], file)
    return database
               


def unique_id():
    counter_id = COUNTER_ID
    with open(counter_id, 'r') as file:
        content = file.read()
    if content == "":
        current_id = 1
    else:
        last_id = json.loads(content)
        current_id = last_id['id'] + 1
    with open(counter_id, 'w') as file:
        json.dump({'id': current_id}, file, indent=4)
    return current_id



def sort_account():
    with open(DATA_ENTRY, 'r') as file:
        content = json.load(file)
        data_id = [data['id'] for data in content]
    if len(content) == 1 and 1 in data_id:
        print("\n🎉 First account has been created successfully!")
    else:
        print("\n✅ New account has been added to the system.")

def display_info(content):
    print("\n" + "-"*35)
    print("✅ Account successfully registered!")
    print(f"🆔 ID: {content['id']}")
    print(f"📧 Email: {content['email']}")
    print(f"👤 Role: {content['role'].capitalize()}")
    print("-"*35 + "\n")


def register():
    print("\n" + "="*30)
    print("        🔐 REGISTER PAGE        ")
    print("="*30 + "\n")
    database = handling_empty_file()

    email = get_email()
    if not email:
        return 
    password = get_password()
    if not password:
        print("❌ Password must be at least 5 characters long.")
        return 
    
    credentials = {
        'id': unique_id(),
        'email': email,
        'password': password,
        'role': 'admin' if 'admin' in email else 'user'
    }
    with open(database, 'r') as file:
        content = json.load(file)

    content.append(credentials)
    with open(database, 'w') as file:
        json.dump(content, file, indent=4)
    sort_account()
    display_info(credentials)

if __name__ == "__main__":
    print("WARNING: This file is a module and should not be executed directly.")