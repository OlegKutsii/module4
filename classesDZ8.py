
from collections import UserDict
from datetime import datetime, timedelta, date
import pickle

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if len(value) == 10 and value.isdigit():
             
            super().__init__(value)
        else:
             raise ValueError

class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, '%d.%m.%Y').date()
            
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")       
                  
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.birthday = None
        self.phones = []
    def add_phone(self, phone):
        self.phones.append(Phone(phone))
    def add_birthday(self, value):
        self.birthday = Birthday(value)
    def find_phone(self, phone) -> Phone:
        for el in self.phones:
            if el.value == phone:
        
                return el
        return None
    def remove_phone(self, phone):
        old_phone = self.find_phone(phone)
        if old_phone is not None:
            self.phones.remove(old_phone)
        else:
            raise ValueError
    def edit_phone(self, old_phone, new_phone):
        old = self.find_phone(old_phone)
        if old:
            i = self.phones.index(old)
            self.phones[i] = Phone(new_phone)
        else:
            raise ValueError
            
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record
    def find(self, name: str):
        return self.data.get(name)
    def delete(self, name: str):
        del self.data[name]
    def __str__(self) -> str:
        return '\n'.join(str(record) for record in self.data.values())
    @staticmethod
    def find_next_weekday(start_date, weekday):
    
        days_ahead = weekday - start_date.weekday()
        if days_ahead <= 0:
            days_ahead += 7
        return start_date + timedelta(days=days_ahead)

    @staticmethod
    def adjust_for_weekend(birthday):
        if birthday.weekday() >= 5:
            return AddressBook.find_next_weekday(birthday, 0)
        return birthday #повертає обект datetime.date


    def get_upcoming_birthdays(self, days=7):
        upcoming_birthdays = []
        today = datetime.today().date()
   
        for record in self.data.values():
            if record.birthday is None:
                continue
            birthday_this_year = record.birthday.value.replace(year=today.year)
            
            if birthday_this_year < today:
                birthday_this_year = record.birthday.value.replace(year=today.year+1)
            
        
            if 0 <= (birthday_this_year - today).days <= days:
                if birthday_this_year.weekday() >= 5:
                    birthday_this_year = AddressBook.find_next_weekday(birthday_this_year, 0)
            
                # congratulation_date_str = AddressBook.date_to_string(birthday_this_year)
                upcoming_birthdays.append({"name": record.name.value, "congratulation_date": birthday_this_year.strftime('%d.%m.%Y')})
        return upcoming_birthdays

book = AddressBook()

def save_data(book, filename = "addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename = "addressbook.pkl"):
    try:
        with open(filename, "rb") as f: 
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()

