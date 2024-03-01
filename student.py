class Student:
    def __init__(self, gender, age, first_name, last_name, record_book):    # визначення функції (попередні дані )
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.record_book = record_book

    def __str__(self):                                                      # визначення функції (попередні дані )
        return f"{self.first_name} {self.last_name}, {self.age} years, {self.gender}, Record Book: {self.record_book}"

    def __eq__(self, other):           # визначення функції (виключення)
        if isinstance(other, Student):
            return str(self) == str(other)
        return False

    def __hash__(self):                 # визначає хеш-код; перетворює його у рядок
        return hash(str(self))