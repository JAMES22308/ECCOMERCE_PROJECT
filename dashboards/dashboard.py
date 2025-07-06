import datetime

def date():
    x = datetime.datetime.now()
    return x

def get_option():
    not_valid = True
    while not_valid:
        option = input('choose an option: ')
        if option.replace(" ", "").isalpha():
            if not len(option) > 6:
                not_valid = False
                return option
            else:
                print('not more than 6 characters')
        else:
            print('must be an alpha')

def dictionary():
    options = {
        'a': 'add',
        'r': 'read',
        'e': 'edit',
        's': 'search',
        'd': 'delete'
    }
    print()
    for key, value in options.items():
        print(f"{key}: {value}")
    print()

def get_name(name="name: "):
    not_valid = True
    while not_valid:
        name = input(name)
        if name.replace(' ', '').isalpha():
            not_valid = False
            return name
        else:
            print('must be an alpha')  

def get_age(age='age: '):
    not_valid = True
    while not_valid:
        age = input(age)
        if age.replace(' ', '').isdigit():
            converted = int(age)
            if not converted > 50:
                not_valid = False
                return converted
            else:
                print('invalid age')
        else:
            print('must be a digit')
       
    

def add_data(id):
    dt = date()
    name = get_name()
    age = get_age()

    data = {
        'datetime': dt,
        'id': id,
        'name': name,
        'age': age
    }
    print('successfully added')
    return data
    
def read_data(database):
    print("\n----Database----")
    if not database:
        print('no data yet')
    else:
        for data in database:
            for key, value in data.items():
                print(f"{key}: {value}")
            print()



def edit_data(database):
    if not database:
        print('no data yet')
        return ''
    
    not_found_id = True
    while not_found_id:
        id = input('search by id: ')
        if id.replace(' ', '').isdigit():
            converted = int(id)
            for data in database:
                if data['id'] == converted:
                    name = get_name(name='new name: ')
                    age = get_age(age='new age: ')
                    data['name'] = name
                    data['age'] = age
                    print('updated successfully')
                    not_found_id = False
                    break
                else:
                    print('id not found')
                    return ''
    
    


def delete_data(database):
    if not database:
        print('no data yet!')
        return ''
    
    not_found = True
    while not_found:
        id = input('search by id: ')
        if id.replace(' ', '').isdigit():
            converted = int(id)
            for data in database:
                if data['id'] == converted:
                    not_found = False
                else:
                    print('id not found')
                    return ''
        else:
            print('must be a digit')
    if not not_found:
        database.remove(data)
        print('deleted successfully')
  
def search_data(database):
    if not database:
        print('no data yet')
        return ''
    
    not_found = True
    count = 0
    while not_found:
        person = input('search by id or name: ')
        print('\n---results---')
        for data in database:
            print()
            if data['name'] == person or data['id'] == int(person):
                for key, value in data.items():
                    print(key, value)
                count += 1
                not_found = False
            elif data['name'] != person and data['id'] != int(person):
                print('entry is not found')
                return ''
    if count == 0:
        print('')
    else:
        print(f'\nentries count: {count}')
                    
                
                    
def main():
    database = []
    current_id = 1
    wrong_key = True
    while wrong_key:
        print(f'\n=====CRUD PROJECT====')
        dictionary()
        option = get_option()
        if option == 'a' or option == 'add':
            data = add_data(current_id)
            database.append(data)
            current_id += 1
        elif option == 'r' or option == 'read':
            read_data(database)
        elif option == 'e' or option == 'edit':
            edit_data(database)
        elif option == 'd' or option == 'delete':
            delete_data(database)
        elif option == 's' or option == 'search':
            search_data(database)
        elif option == 'exit':
            print('Exit!')
            wrong_key = False
        else:
            print('wrong key')


if __name__ == "__main__":
    print("WARNING: This file is a module and should not be executed directly.")


