from pathlib import Path

# Створення об'єкту Path для директорії
directory = Path(__file__).parent


# Виведення переліку всіх файлів та піддиректорій
def parse_folder(directory):
    for path in directory.iterdir():
        if path.is_file():
            print(f'{Fore.BLUE} [INFO] {path} - This is a file')            
        else:
            parse_folder(path)
            print(f'{Fore.GREEN} [INFO] {path} - This is a Folder')
            if path.is_file():
                print(f'{Fore.BLUE} [INFO] {path} This is a file')
                           
    return()


parse_folder(directory)
