
# Завдання 13. 1

# Завдання 1 Група студентів 1) Створіть клас, що описує людину (створіть метод, що виводить інформацію про людину).
# 2) На його основі створіть клас Студент (перевизначте метод виведення інформації).
# 3) Створіть клас Група, екземпляр якого складається з об'єктів класу Студент. Реалізуйте методи додавання, видалення
# студента та метод пошуку студента на прізвище.
# Метод пошуку студента повинен повертати саме екземпляр класу Студент, якщо студент є у групі, інакше - None.
# У методі видалення, використовуйте результат методу пошуку. Тобто. потрібно скомбінувати ці два методи;)
# Визначте для групи метод __str__() для повернення списку студентів у вигляді рядка.
# Нижче наведені заготовки, які необхідно доповнити.


#
#
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
#
#
# class Group:                                                             # створення класу Group
#     def __init__(self, number):                                          # атрибути класу
#         self.number = number
#         self.group = []
#
#     def add_student(self, student):                                      # функцією / методом класу
#         self.group.append(student)
#
#     def delete_student(self, last_name):                                 # функцією / методом класу
#         student = self.find_student(last_name)
#         if student:
#             self.group.remove(student)
#
#     def find_student(self, last_name):                                   # функцією / методом класу
#         for student in self.group:
#             if student.last_name == last_name:
#                 return student
#         return None
#
#     def __str__(self):                                                   # повна інфо про обєкт  класу Студент
#         all_students = '\n'.join(str(student) for student in self.group)
#         return f'Number: {self.number}\n{all_students}'
#
#                                                                          # Перевірка
#
# st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
# st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
# gr = Group('PD1')
# gr.add_student(st1)
# gr.add_student(st2)
# assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
# # print(str(gr.find_student('Jobs')))
#
# assert gr.find_student('Jobs2') is None, 'Test2'
# # print(str(gr.delete_student('Jobs2')))
# assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод пошуку має повертати екземпляр'
# # print(isinstance(gr.find_student('Jobs'), Student))
#
# gr.delete_student('Taylor')
# # print(gr)  # Only one student
#
# gr.delete_student('Taylor')  # No error!
# print(gr)

# Завдання 13. 2             "Цифровий лічильник"
#
# Створити клас цифрового лічильника. У класі реалізувати методи:
# встановлення максимального значення лічильника,
# встановлення мінімального значення лічильника
# встановлення початкового значення лічильника
# метод step_up збільшує лічильник на 1. Метод можна викликати до тих пір, поки значення досягне максимуму.
# При досягненні максимуму слід викинути (raise) виняток ValueError, з описом, що досягнуто максимуму
# метод step_down зменшує лічильник на 1. Метод можна викликати до тих пір, поки значення не досягне мінімуму.
# При досягненні мінімуму потрібно викинути (raise) виняток ValueError, з описом, що досягнутий мінімум
# повернення поточного значення лічильника
# Початкове, мінімальне та максимальне значення лічильника також можуть бути додані в метод ініціалізації екземпляра класу.
# Приблизний каркас для класу та варіанти перевірки. Вам потрібно дописати необхідне замість pass


class Counter:                                                                 # створення класу Counter

   def __init__(self, current=1, min_value=0, max_value=10):                   # атрибути класу
       self.current = current
       self.min_value = min_value
       self.max_value = max_value

   def set_current(self, start):                                              # функцією / методом класу
       self.current = start


   def set_max(self, max_max):                                              # функцією / методом класу
       self.max_value = max_max


   def set_min(self, min_min):                                               # функцією / методом класу
       self.min_value = min_min

   def step_up(self):                                                     # функцією / методом класу більшує лічильник на 1
       if self.current >= self.max_value:
           raise ValueError('This is max')
       self.current += 1

   def step_down(self):                                                    # функцією / методом класу зменшує лічильник на 1
       if self.current <= self.min_value:
           raise ValueError('This is min')
       self.current -= 1

   def get_current(self):                                                # функцією / методом класу повернення поточного значення лічильника
       return self.current

counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
assert counter.get_current() == 10, 'Test1'
try:
    counter.step_up()  # ValueError
except ValueError as e:
    print(e)                                                              # Досягнуто максимуму
assert counter.get_current() == 10, 'Test2'
# print(counter.get_current())                                             # перевірка на прінт

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7, 'Test3'
try:
    counter.step_down()  # ValueError
except ValueError as e:
    print(e)                                                                # Досягнуто мінімуму
assert counter.get_current() == 7, 'Test4'
# print(counter.get_current())                                               # перевірка на прінт