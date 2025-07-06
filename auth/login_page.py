import json
from config import DATA_ENTRY
from dashboards.dashboard import main
from .logout import logout_user

def dict_reader():
    with open(DATA_ENTRY, 'r') as file:
        content = json.load(file)
    return content
        
def get_email(m="email: "):
    email = input(m).strip()
    if '@' in email and '.' in email:
        return email
    
def get_password(p="password: "):
    password = input(p).strip()
    return password


def login():
    print("\n" + "=" * 40)
    print("           🔐 LOGIN PAGE")
    print("=" * 40 + "\n")
    database = dict_reader()
    email = get_email()
    if not email:
        print("\n[❌] Invalid email. Please try again.\n")
        return
    account = None
    for data in database:
        if data['email'] == email:
            account = data
            break
    
    if not account:
        print("\n[⚠️] Email doesn't exist in our system.\n")
        return
    
    attempts = 0
    while attempts < 3:
        password = get_password()
        if account['password'] == password:
            return 'admin' if account['role'] == 'admin' else 'user'
        else:
            attempts += 1
            print(f"[🔐] Wrong password: Attempt {attempts}/3")

    print("\n" + "-" * 45)
    print("🚫 Account has been temporarily locked due to")
    print("   multiple failed login attempts.")
    print("-" * 45 + "\n")

   
if __name__ == '__main__':
    print("WARNING: This file is a module and should not be executed directly.")