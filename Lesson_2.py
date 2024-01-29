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