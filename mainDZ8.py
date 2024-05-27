from classesDZ8 import AddressBook, Record, load_data, save_data

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter the arguments name and phone for the command"
        except IndexError:
            return "Enter the arguments name and phone for the command"
        except KeyError:
            return "Enter the arguments name and phone for the command"   

    return inner

@input_error

def add_contact(args, contacts: AddressBook):
    name, phone = args
    record = contacts.find(name)
    if record is None:
        record = Record(name)
        contacts.add_record(record)
    record.add_phone(phone)    
     
    return 'Contact added'
     
@input_error

def change_contact(args, contacts):
    name, old_phone, new_phone = args
    record:Record = contacts.find(name)
    if record is None:
        return 'Name is not find!'
    else:
        record.edit_phone(old_phone, new_phone)
        
    return 'Contact update'
   
@input_error

def show_phone(args, contacts):
    
    name = args[0]
    record = contacts.find(name)
    if record is None:
        return 'Name is not find!'
    else:

        return record
    
def show_all(contacts):
    return contacts

@input_error

def add_birthday(args, contacts):
    name, birthday = args
    record = contacts.find(name)
    if record is None:
        return 'User not found'
    else:
        record.add_birthday(birthday)

@input_error

def show_birthday(args, contacts):
    name = args[0]
    record = contacts.find(name)
    if record is None:
        return 'User not found'
    else:
        return record.birthday

@input_error

def birthdays(contacts):
    return contacts.get_upcoming_birthdays()

def main ():
     
    contacts = load_data()
    
    print('Welcome to assistant bot!')
    while True:
         
        user_input = input('Enter a command:').strip().lower()

        command, args = parse_input(user_input)
        
        if command in ['close', 'exit']:                  
            print('Good bye!')
            break
        elif command == 'hello':
            print('How can I help you?')
        elif command == 'add':
            print(add_contact(args, contacts))            
        elif command == 'change':
            print(change_contact(args, contacts))         
        elif command == 'phone':
            print(show_phone(args, contacts))
        elif command == 'all':
            print(show_all(contacts))

        elif command == 'add-birthday':
            print(add_birthday(args, contacts))
        elif command == 'show-birthday':
            print(show_birthday(args, contacts))
        elif command == 'birthdays':
            print(birthdays(contacts))
        else:
            print(f'Invalid command. Please Enter command:', '1) hello', '2) add', '3) change', '4) phone', '5) all', '6) exit or close', sep ='\n')
    save_data(contacts)

if __name__== '__main__':
    
    main()

