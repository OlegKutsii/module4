from pathlib import Path

def get_cats_info (filename):
    with open(filename, 'r', encoding = 'utf-8') as file:
       
        cats_info = [str(i.strip()).split(',') for i in file]
        new_list = []
        
        for list_in_cats_info in cats_info:
            for dict_info in list_in_cats_info:
                
                dict_info={
                    'id': list_in_cats_info[0],
                    'name': list_in_cats_info[1],
                    'age': list_in_cats_info[2]
                    }
                
            new_list.append(dict_info)
    return new_list

def main():
    try:
        filename = Path('animals.txt')
        if filename.exists():
            cats_info = get_cats_info(filename)
            print('Друге завдання:', cats_info, sep='\n')
    except IndexError:
        return print('Data in file _.txt not correct')         
       
if __name__ == '__main__':
    main()