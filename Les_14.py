from student import Student
from group import Group

# Завдання 14. 1 Виняток користувача
#
# # Модифікуйте клас Група (завдання минулої лекції) так, щоб при спробі додавання до групи більше 10-ти студентів,
# # було порушено виняток користувача.
# # Таким чином потрібно створити ще й виняток користувача для цієї ситуації.
# # І обробити його поза межами класу. Тобто. потрібно перехопити цей виняток, при спробі додавання 11-го студента
# #
# class Just10Student(Exception):                     # ств винятка
#     pass
# class Human:                                                            # створення класу Human
#
#     def __init__(self, gender, age, first_name, last_name):             # атрибути класу
#         self.gender = gender
#         self.age = age
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def __str__(self):                                                 # повна інфо про обєкт
#         return f"{self.first_name} {self.last_name}, {self.age} years , {self.gender}"
#
#
# class Student(Human):                                                  # створення класу Student(Human)
#
#     def __init__(self, gender, age, first_name, last_name, record_book): # атрибути класу
#         super().__init__(gender, age, first_name, last_name)
#         self.record_book = record_book                                   # атрибут екземпляру класу
#
#     def __str__(self):                                                   # повна інфо про обєкт
#         return f"{self.first_name} {self.last_name}, {self.age} years , {self.gender}"+ f", Record Book: {self.record_book}"
# class Group:
#     def __init__(self, number):                                    # атрибут екземпляру класу
#         self.number = number
#         self.group = []
#
#     def add_student(self, student):                               # метод / фун-ція при якому виловлюємо більше 10 студентів
#         if len(self.group) >= 10:
#             raise Just10Student("This max student that you have more than 10 students")
#         self.group.append(student)
#
#         def delete_student(self, last_name):             # не задіяна
#             student = self.find_student(last_name)
#             if student:
#                 self.group.remove(student)
#
#         def find_student(self, last_name):                                  # не задіяна
#             for student in self.group:
#                 if student.last_name == last_name:
#                     return student
#             return None
#
#         def __str__(self):                                                    # не задіяна
#             all_students = '\n'.join(str(student) for student in self.group)
#             return f'Number: {self.number}\n{all_students}'
#
# st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
# st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
# gr = Group('PD1')
# gr.add_student(st1)
# gr.add_student(st2)
# #
#                             # Обробка винятку поза межами класу
# gr = Group ('PD1')
# try:
#     for _ in range(11):
#         gr.add_student(Student('Male', 30, 'Nadiia', 'Mykolaivna', 'AN123'))
# except Just10Student as e:
#     print(e)





# Завдання 14. 2 Створення власних модулів

# У цьому завданні Вам необхідно зробити дві речі на підставі попереднього ДЗ.
# До класу Студента необхідно додати метод порівняння. Порівнювати можна за тими рядками, які повертає метод __str__
# Для того, щоб спрацювала коректно ось ця перевірка
# assert gr.find_student('Jobs') == st1
# Рознесіть класи, які використовували під час виконання завдання про групу студентів за модулями.
# Переконайтеся у працездатності проекту – створіть окремо файл main.py, у якому необхідно імпортувати потрібні
# класи та запустити код перевірки.
# Приблизний вміст файлу main.py для перевірки працездатності.

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)

assert gr.find_student('Jobs') == st1
assert gr.find_student('Jobs2') is None

gr.delete_student('Taylor')
print(gr) # якщо один студент