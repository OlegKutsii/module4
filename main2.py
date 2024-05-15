import re

def general_number(text):

    salaty_match = re.findall(r'\d+\.\d+', text)  
    salary = [float(salary) for salary in salaty_match]

    return sum(salary)

text = 'Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів.'

total_salary = general_number(text)

print(f'Загальний дохід: {total_salary}')
