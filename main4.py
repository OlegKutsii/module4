
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    name = args[0]
    try:
        if not name in contacts:
            name, phone = args
            contacts[name] = phone
        else:
            return 'This name already exists' 
        return 'Contact added'
    except ValueError:
        return 'Invalid command. Please enter name und number'  

def change_contact(args, contacts):
    name = args[0]
    try:
        if not name in contacts:
            return 'Name is not find!'
        else:
            name, phone = args
            contacts[name] = phone
        return 'Contact update'
    except ValueError: 
        return 'Invalid command. Please enter name und number' 
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
            print('Invalid command.')
    
if __name__== '__main__':
    main()

