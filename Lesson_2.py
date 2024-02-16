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
fruits = ['apple', 'banana', 'cherry']

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
value_int = 0
is_true = True

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
# inner()
#
# # for i in range(pi):
# #     print(i)
is_send_second_email = True

def print_line(w, fill, is_email=True, *args):
    for i in range(w):
        print(fill, end=' ')
    if is_email:
        print('yes')

print_line(6, "*", is_send_second_email, 65, 6258)

# my_tuple = (1, 2, 3)
# val_1, *tup = my_tuple
# print(val_1)
# print(tup)