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

def add_contact(args, contacts):
    
    name = args[0]
    if not name in contacts:
        name, phone = args
        contacts[name] = phone
    else:
        return 'This name already exists' 
    return 'Contact added'
     
@input_error

def change_contact(args, contacts):
    name = args[0]

    if not name in contacts:
        return 'Name is not find!'
    else:
        name, phone = args
        contacts[name] = phone
    return 'Contact update'
   
@input_error

def show_phone(args, contacts):
    
    phone = args[0]
    if not phone in contacts:
        return 'Name is not find!'
    else:
        return contacts[phone]
    
def show_all(contacts):
    return (contacts)

def main ():
    contacts = {}
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
        else:
            print(f'Invalid command. Please Enter command:', '1) hello', '2) add', '3) change', '4) phone', '5) all', '6) exit or close', sep ='\n')
    
if __name__== '__main__':
    main()

