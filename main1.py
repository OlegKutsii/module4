from pathlib import Path

def total_salary (filename):
    with open(filename, 'r', encoding='utf-8') as text:
        data = text.readlines()
        new_text = []

        for line in data:
            _,salary = line.split(',')
            new_text.append(float(salary))

    total = sum(new_text)
    average = sum(new_text)//len(new_text)
    return total, average


def main():
    try:    
        filename = Path('salery_workers.txt')
        if filename.exists():
            total, average = total_salary(filename)
            print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}", sep='\n')
    except ValueError:
        return print('Data in file _.txt not correct')
if __name__ == "__main__":
    main()