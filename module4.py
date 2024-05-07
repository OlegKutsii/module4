def total_salary (filename):
    with open(filename, 'r', encoding='utf-8') as text:
        data = text.read()
        n = ''
        new_text = []    
        for word in data:
            if '0' <= word <= '9':
                n += word
            else:
                if n != '':
                    new_text.append(int(n))
                    n = ''        
        if n !='':
            new_text.append(int(n))
    total = sum(new_text)
    average = sum(new_text)//len(new_text)
    return total, average

def get_cats_info (filename):
    with open(filename, 'r', encoding = 'utf-8') as file:
       
        cats_info = [str(i.strip()).split(',') for i in file]
        new_list = []
        
        for list_in_cats_info in cats_info:
            for dict_info in list_in_cats_info:
                dict_info= {}
                count = 0
                dict_info.update({'id': list_in_cats_info[count], 'name': list_in_cats_info[count+1], 'age': list_in_cats_info[count+2]})
            new_list.append(dict_info)
    return new_list

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

