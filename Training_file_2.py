# # # txt = "Ми є так звані \"Вікінги\" із півночі."
# # # print(txt)
# # # # gkhhhhhhhhhhhhhh
# # # print("Hello, World")
# #
# # if 5 > 2:
# #   print("\'П’ять більше ніж два!")
# # if 5 > 2:
# #   print("\\П’ять більше ніж два!")
# # if 5 > 2:
# #   print("\nП’ять більше ніж два!")
# # if 5 > 2:
# #   print("\tП’ять більше ніж два!")
# # if 5 > 2:
# #   print("\bП’ять більше ніж два!")
# # if 5 > 2:
# #     print("\fП’ять більше ніж два!")
# # if 5 > 2:
# #     print("\oooП’ять більше ніж два!")
# # import i
# #
# # number_1 = 10
# # number_2 = 3
# # number_1 += number_2
# # number_3 = 5
# # number_1 += number_3
# # print(number_1)
# # number_1 = number_1 + number_2
# #
# #
# # result_sub = number_1 - number_2
# # result_mul = number_1 * number_2
# # result_div = number_1 / number_2
# #
# # result_div_2 = number_1 // number_2   # цілочислене ділення
# # result_div_3 = number_1 % number_2      # залишок від ділення
# # result_div_4 = number_1 % number_2
# # print(result_div_3)
# # # result_div_4 = divmod(number_1, number_2) # містить в собі цілочислене ділення та залишок від ділення
# # value_str = "hello I'm"
# # name = "1.444"
# # greetings_1 = value_str + name
# # # greetings_2 = f"hello I'm {name}"
# #
# # print(greetings_1)
#
#
# # fruits = None
# #
# # if fruits is None:
# #     # print("Список фруктів ще не визначений.")
# #     fruits = ["Яблука", "Банани", "Апельсини"]
# #     print("Визначено список фруктів:", fruits)
# # else:
# #     print("Визначений список фруктів:", fruits)
#
# my_tuple = (1, "hello", 3.14)
#
# # # Доступ до елементів кортежу
# # print(my_tuple[0])  # Виведе: 1
#
# # # Зміна значення кортежу не можлива
# # my_tuple[0] = 5  # Видасть помилку
# #
# # # # Ітерація через елементи кортежу
# # for item in my_tuple:
# #     print(item)
#
# # my_dict = {"name": "John", "age": 25, "city": "New York"}
# # #
# # # # Доступ до значень за ключами
# # # print(my_dict["name"])  # Виведе: John
# # # print(my_dict["age"])   # Виведе: 25
# # #
# # # # Зміна значення за ключем
# # # my_dict["age"] = 26
# # #
# # # # Додавання нової пари ключ-значення
# # # my_dict["gender"] = "Male"
# # #
# # # # Видалення елемента за ключем
# # # del my_dict["city"]
# # #
# # # # Ітерація через ключі та значення
# # # for key, value in my_dict.items():
# # #     print(key, ":", value)
# #
# # my_set = {1, 2, 3, 4, 5}
# #
# # # Додавання елементу до множини
# # # my_set.add(6)
# # # #
# # # # # Видалення елементу з множини
# # # my_set.remove(3)
# # # #
# # # # # Перегляд елементів множини
# # for element in my_set:
# # #     print(element)
# # # # print(my_set)
# #
# # unique_numbers = {1, 2, 3, 4, 5, 2, 3, 6}
# # print("Оновлені унікальні числа:")
# # for number in unique_numbers:
# #     print(number)
# #
# # message = "One of Python's strengths\xhh is"
# # print(message)
#
# # import time
# # print i in range (5):(
# #     print (f"Залишилося {5-i} ctreyl",
# #        end = '\r'))
# # time.sleep (1)
# # print("\nГотово")
#
# # import time
# #
# # for i in range(5):
# #     print(f"Залишилося {5 - i} секунд", end='\r')
# #     time.sleep(1)
# #
# # print("\nГотово!")
#
# # import time
# #
# # for i in range(5):
# #     print(f"Прогрес: {i + 1}/5", end='\r')
# #     time.sleep(1)
# #
# # # print("\nГотово!")
# #
# # import time
# #
# # try:
# #     for i in range(10):
# #         print(f"Проходження {i + 1}", end='\r')
# #         time.sleep(1)
# # except KeyboardInterrupt:
# #     print("\nПроцес перервано користувачем.")
# # value_int = 100
# # value_float = -0.01
# # value_str = ""
# # print(bool(value_int) * 4)
# # #
# # # value_bool = True
# # # print(value_bool * 2)
# #
# # value_int = 9
# # #
# # # # and or
# # #
# # if value_int > 0 or not value_int < 10:
# # # if 0 < value_int < 10:
# #     print(f"{value_int} is bigger then 0")
# # # elif value_int > 10:# else if
# # #     print(f"{value_int} is bigger then 10")
# # # else:
# # #     print(f"{value_int} is not bigger then 0")
# # #
# # #
# # print("end")
# #
# base_list = [1, 2, 3]
# # my_new_list = base_list * 4
# # #
# # print(my_new_list)
# #
# base_list[0] = 10
#
# print(f"base_list {base_list}")
# # print(f"my_new_list {my_new_list}")
# #
# # # # ######################################
# #
# # from copy import deepcopy
# # # list_2 = [True, False]
# # base_list = [1, 2, 3, [True, False]]
# #
# # new_list = [deepcopy(base_list)] * 4
# # # new_list = [link, link, link, link]
# # print(new_list)
# # print(new_list)
# def myfunction():
#   return 3+3
#
# print(myfunction())
# a = ["apple", "banana", "cherry"]
# b = ["Ford", "BMW", "Volvo"]
# a.append(b)
# print(a)
# fruits = ['apple', 'banana', 'cherry']
# fruits.append("orange")
# # print(fruits)
# fruits = ['apple', 'banana', 'cherry', 'orange']
# fruits.clear()
# print(fruits)
# list_fruits = ['cherry', 'banana', 'apple', 'orange']
# list_fruits.remove('apple')
#
# list_fruits.count('banana')
# print(list_fruits)
# fruits = ['apple', 'banana', 'cherry']

# fruits.pop(2)
# print(fruits)
# fruits.pop(0)
# print(fruits)
# fruits.insert(1,'apple')
# print(fruits)
#
# # a,b, *left_1 = (1, 2, 3, 0)
# # print(a)
# # print(b)
# # print(left_1)
# value_list = ('apple', 'banana', 'cherry')
# value_list.__reversed__()
# print(value_list)
# # value_list.sort(reverse=False, key=len)
# # value_list_1 = sorted(value_list, reverse=True)
# # print(value_list_1)

#
# number_1 = float
#
# if not number_1.isdigit or not action not in ('+', '-', '/', '*') or not number_2.isdigit():
#         print('Undefined number! Try again.')
#         continue
#
#
#     # if action not in ('+', '-', '/', '*'):
#     #     print('Unavailable operator! Try again.')
#     #     continue
#     #
#     # if not number_2.isdigit():
#     #     print('Undefined number! Try again.')
# #     #     continue
# value_list = [1, 3, 9]   #88 bytes
# value_list = ["apple", "red", "true", "aapple"]
#
# value_list.append("Hello")
#
# print(value_list)
#
# some_value = value_list.pop()                  # зробило нову змінну з Hello
#
# print(some_value)                              # Hello
# print(value_list)                              # ['apple', 'red', 'true', 'aapple']
#
# value_list.reverse()                            # перевернуло
# print(value_list)                                # ['apple', 'red', 'true', 'aapple']
# # value_list.sort(reverse=False, key=len)                    # ['apple', 'red', 'true', 'aapple']
# # value_list_1 = sorted(value_list, reverse=True)            # ['aapple', 'true', 'red', 'apple']
# # print(value_list_1)
# #
# value_list.insert(5, "oooo")
# # print(value_list)
# # print(len(value_list))
# print(value_list)
# #
# #
# # value_list = [1, 3, 9]   #88 bytes
# # value_list.append(2)  #88 bytes

# while  for
# value_int = 0
# is_true = True

# while True:
#     value_int += +1
#     print(value_int)
#     if value_int > 10:
#         break
# else:
#     print("dddddd")

# # while value_int < 10:
# #     value_int += 1
# #     print(value_int)
# #
# while is_true:
#     value_int += 1
#     print(value_int)
#     if value_int > 10:
# #         is_true = False
# # else:
# #     print("dddddd")
# # #
# # # print("end")
#
# # continue
# # while is_true:
# #     value_int += 1
# #
# #     if value_int == 5:
# #         continue
# #
# #     print(value_int)
# #     if value_int > 10:
# #         is_true = False
# # else:
# #     print("dddddd")
#
# num = input("Data: ")
# index = 0
#
# while index < len(num):
#     print(num[index])
#     index += 1
#
# # print("end")
#
#
# # # for, for - else, range()
#
# # some_str = "hello"
#
# # [1,2,3,4]
# # (1,2,3,4)
# # "hello"
# # index = 0
# # for letter in some_str:
# #     print(letter)


# while index < len(some_str):
#     print(some_str[index])
#     index += 1
# # # # first_symbol = float(input("1st num:  "))
# # # # operator = input("operator:  ")
# # # # second_symbol = float(input("2nd num:  "))
# # # #
# # # # # result = 0
# # # #
# # # # # if operator not in "+-*/" or len(operator) != 1:
# # # # if operator not in ["+", "-", "*", "/"]:
# # # #     result = "ERROR - something goes wrong"
# # # # elif operator == "+":
# # # #     result = first_symbol + second_symbol
# # # # elif operator == "-":
# # # #     result = first_symbol - second_symbol
# # # # elif operator == "*":
# # # #     result = first_symbol * second_symbol
# # # # elif operator == "/" and second_symbol == 0:
# # # #     result = "ERROR - can't divide by zero"
# # # # elif operator == "/":
# # # #     result = first_symbol / second_symbol
# # # # else:
# # # #     result = "hhhhhh"
# # # # #
# # # # # print(result)
# # #
# # # first_symbol = float(input("1th number: "))
# # # operator = input("operator: ")
# # # second_symbol = float(input("2nd number:"))
# # # if operator not in ["+", "-", "*", "/"] or len(operator) != 1:
# # #     print("invalid operator")
# # # elif operator == "+":
# # #     result = first_symbol + second_symbol
# # # elif operator == "-":
# # #     result = first_symbol - second_symbol
# # # elif operator == "*":
# # #     result = first_symbol * second_symbol
# # # elif operator == "/" and second_symbol == 0:
# # #     result = "Error"
# # # elif operator == "/":
# # #     result = first_symbol / second_symbol
# # # else:
# # #     print("Invalid operator2")
# # # print(result)
# #
# # # value_str = 'Hello'
# # # # for letter in value_str:
# # # #     print
# # # # for i in range(len(value_str)):
# # # #     print(i, value_str[i])
# # # # for index, letter in enumerate (value_str):
# # # #     print(index, letter)
# # # value_list = [1, 2, 3, 4, 5]
# # # value_str = str(value_list)
# # # print(value_str, type(value_str))
# # value_str = 'Hello'
# # print(value_str.lower())
# #
# # value_float = "heeeeeeeeeeeeeeello"
# # # value = ""
# # # # value_is_digit = value_float.isdigit()
# # # # print(value_float, value_is_digit)
# # # for letter in value_float:
# # #     # if letter.isdigit():
# # #     #     value += letter
# # #     if letter.isalpha():
# # #         value += letter
# # # print(value)
# # method = value_float.index("l")
# # print(method)
# value_float ="/Documents/kkk.png"
# # some_method = value_float.split(".")
# # print(some_method)
# # some_method[-1] = "jpeg"
# # print(some_method)
# # result = ".".join(some_method)
# # print(result)
# # print(value_float)
# # result = value_float.replace(".pnj",".jpeg",4)
# # print(result)
# import this
# print(dir(this))




# collections OrderedDict (popitem, move_to_end)
#
# from collections import defaultdict
#
# for i in range(5):
#     defdict[i].append(i * 5)
#
# print(defdict)
#
# dict_one = {}
#
# for i in range(5):
#     dict_one.setdefault(i, [])
#     dict_one[i].append(i * 5)
# print(dict_one)
#


# from collections import namedtuple
# fields = ('color', 'engine')
# car = namedtuple('Car', fields)
# car1 = car('red', 2000)
# car1._asdict()
# # color1, engine1 = car1
# # print(color1, engine1)
# print(car1._asdict())



# max(), min(), sum()

from collections import OrderedDict, defaultdict

# value_dict = {
#     "name": "Nick",
#     "age": 18,
#     "country": "Ukraine",
# }
# print(value_dict)
#
# my_order_dict = OrderedDict(value_dict)   # [("name", "Nick"), ("age", 18), ("country", "Ukraine")]
# print(my_order_dict.popitem())


# this_dict = dict.fromkeys(('name', 'age', 'key_3'), [])
#
# print(this_dict)
# this_dict["name"].append(2)
#
# print(this_dict)





# from collections import namedtuple
#
# fields = ('color', 'engine')
#
# car = namedtuple('Car', fields)
#
# car_1 = car('red', 2000)
#
# # print(car_1)
#
# color_1, engine_1 = car_1
#
# # print(color_1, engine_1)
#
# # print(car_1.color)
# # print(car_1.engine)
# print(car_1._asdict())
#
# def inner():
#     global pi
#     pi += 10
#     # pi = pi + "!!!"
#     # print(pi)
#
#     return "Hello"
#
#
# pi = 5
#
# # inner()
# #
# # # for i in range(pi):
# # #     print(i)
# is_send_second_email = True
#
# def print_line(w, fill, is_email=True, *args):
#     for i in range(w):
#         print(fill, end=' ')
#     if is_email:
#         print('yes')
#
# print_line(6, "*", is_send_second_email, 65, 6258)
#
# # my_tuple = (1, 2, 3)
# # val_1, *tup = my_tuple
# # print(val_1)
# # # print(tup)
# import requests
#
# def make_request(url, **kwargs):
#     response = requests.get(url, **kwargs)
#     print(response.text)
#
# # Виклик функції make_request з аргументами, які будуть передані в requests.get
# make_request("https://www.example.com", headers={"User-Agent": "Mozilla/5.0"})

# def my_code(w, h, fill, *args):
#     for i in range(w):
#         for j in range(h):
#             print(fill, end=' ')
#     return None
# # my_code(7,5,"*")
#
# my_args = 7, 5, "*"
# my_code(*my_args)
# print(my_args)
# #
# def my_add(number_1):
#     return number_1 + 2
# # #
# # # my_math_adding = my_add(10, 20)
# # # print(my_math_adding)
# #
# # def my_mul(number_1, number_2):
# #     return number_1 * number_2
# #
# # func_list = [my_add, my_mul]
# # print(func_list)
# #
# # for func in func_list:
# #     print(func(1,2), end=',')
# def my_mul(number_1, *args):
#     return number_1 * 2
# # print(my_mul(5))
#
# def map_func(num_list, func):
#     for num in num_list:
#         print(func(num), end=" ")
# map_func([1,5,10], my_add)


# # функція пишиться на льоту в залежності від вибору клієнта пишеться
# choice = 0
# if choice == 1:
#     def my_func(n):
#         if n > 0:
#             return 1
#         else: return 0
# # else:
# #     def my_func(n):
# #         if n < 0:
# #             return 1
# #         else:
# #             return 0
# # print(my_func(10))
#
# ############# __main__############
#
# def my_func():
#     """"This func doing stuff with"""
#     return 10
# print(my_func.__name__)
# print(my_func.__module__)
#
# if __name__ == "__main__":
#     print("fruits")
#
# def my_add(numb_1: int, numb_2: int) -> int:
#     return numb_1 + numb_2
# print(my_add("2","5"))


###########Рекурсія##############

# функція яка викликає сама себе
# def fibo(n):
#     a = 0
#     b = 1
#     for i in range(2, n + 1):
#         a, b = b, a + b
#     return b
# print(fibo(10))
# def fibo(n):
#     a = 0
#     b = 1
#     print(a,b)
#     for i in range(2, n + 1):
#         a, b = b, a + b           #  a стало б, б стало а, 0, 1 = 1  0+1
#     return b

# print(fibo(6))
# def fibo(n):
#     print(n)
#     if n in (1, 2):
#         return 1
#     return fibo(n-1) + fibo(n-2)
# print(fibo(3))
# def my_filter(seq, predicate):
#     result = []
#     for element in seq:
#         if predicate(element):
#             result.append(element)
#     return result
# sequence = [8, 9, 8, - 4, 2]
# res = my_filter(sequence, lambda x: x > 0)
# print (res)

# value_str = "1234"
# int_nums = []
# for i in value_str:
#     int_nums.append(int(i))
# int_nums = map(int, "1234")
# print(int_nums)
# print(list(int_nums))

# def power(n):
#     return n**2
# numbers = [1,2,3,4,5]
# power_numbers = map(power, numbers)
# print(numbers)
# print(list(power_numbers))
#
# def power (n):
#     return n*2
# numbers = [1,2,3,4,5,6,7,8,9]
# power_numbers = map(power, numbers)
# print(list(power_numbers))

# write
# writelines

# filename = "test.txt"

# my_file = open(filename, "w")   # "r", "w", "a"

# my_file.write("Hello World!\n")
# my_file.write("Hello World!\n")
# my_file.write("Hello World!\n")
#
# my_file.close()


# val_list = ["Hello World!", "Apple", "Red", "green"]
# my_file = open(filename, "w")
# for i in val_list:
#
#     my_file.writelines(i + "\n")
#
# my_file.close()
#
# filename = "test.txt"
#
# with open(filename, "w") as my_file:
#     my_file.write("Hello World!\n")
#     my_file.write("Hello World!\n")
#     my_file.write("Hello World!\n")

filename = "test.txt"
#
# with open(filename, "w") as my_file:
#     for i in val_list:
#         my_file.writelines(i + "\n")
#
# filename = "test.txt"
# filename = "C:/doc/desktop/test.txt"

# my_file = open(filename, "r")
# data = my_file.read()
# print(data, type(data))
# my_file.close()

# with open(filename, "r") as my_file:
#     data = my_file.read()
#
#
# print(data, type(data))


# with open(filename, "r") as my_file:
#     data = my_file.readlines()
#
# print(data)

def simple_num(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_generator(end):
    number = 1
    while number <= end:
        if simple_num(number):
            yield number
        number += 1


from inspect import isgenerator

gen = prime_generator(10)
print(list(prime_generator(29)))
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')