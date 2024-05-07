from module4 import get_cats_info, total_salary, parse_input, add_contact, change_contact, show_phone, show_all
from pathlib import Path


def main():
    filename = Path('salery_workers.txt')
    if filename.exists():
        total, average = total_salary(filename)
        print('Перше завдання:', f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}", sep='\n')

if __name__ == "__main__":
    main()


def main():
    filename = Path('animals.txt')
    if filename.exists():
        cats_info = get_cats_info(filename)
        print('Друге завдання:', cats_info, sep='\n')
       
if __name__ == '__main__':
    main()

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
