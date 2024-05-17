import re

text = 'Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів.'

def generator_numbers(text):

    salary_match = re.findall(r'\d+\.\d+', text)
    
    for salary in salary_match:
        salary = float(salary)
        yield salary

def sum_profit(text, generator_numbers):
    return sum(generator_numbers(text))

total_salary = sum_profit(text, generator_numbers)   

print(f'Загальний дохід: {total_salary}')