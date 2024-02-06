###############Завдання 5.1######################################################
#
# # import string             # множина допустимих символів
# # import keyword           # провіряємо чи слово не є ключовою ф-цією чи інше - тобто лише допустимі імена
# import string, keyword
# can_be_named = input("Введіть свої значення: ")
# def can_be_named(variant_for_input):               # визначення функції
#     if not variant_for_input or variant_for_input[0].isdigit() or variant_for_input.isnumeric():
#         # не може починатися з цифри,не може складатися лише з цифр
#         return False        # визначення не правильного варіанту
#
#     allowed_1 = set("_")      # дозволяєм нижнє підкреслення
#     allowed_1.update(string.ascii_letters, string.digits)
#     # може включати string.ascii_letters- всі літери, всі цифри string.digits
#
#     if any(char not in allowed_1 for char in variant_for_input): якщо не виконується дозволені параметри
#         return False                                    # визначення не правильного варіанту
#
#     if variant_for_input.lower() in keyword.kwlist:     # якщо введення значення (перевірка на lower) входить в keyword.kwlist
#         return False                                    # визначення не правильного варіанту
#
#     return True                                         # в інших варыантах правильно
#

# перевірка
# print(can_be_named("_"))  # True
# print(can_be_named("x"))  # True
# print(can_be_named("get_value"))  # True
# print(can_be_named("get value"))  # False
# print(can_be_named("get!value"))  # False
# print(can_be_named("some_super_puper_value"))  # True
# print(can_be_named("Get_value"))  # False
# print(can_be_named("get_Value"))  # False
# print(can_be_named("getValue"))  # False
# print(can_be_named("3m"))  # False
# print(can_be_named("m3"))  # True

###############Завдання 5.2######################################################
# беру попередній калькулятор

# while True:
#     num_1 = input("Enter the number_1:")
#     operation = input("Enter action (+,-, *, /): ")
#     num_2 = input("Enter the number_2:")
#     if not num_1.isdigit() or operation not in ('+', '-', '/', '*') and not num_2.isdigit():
#         print("Invalid input. Try again.")
#         continue
#     num_1 = float(num_1)
#     num_2 = float(num_2)
#     result = 0
#     if operation == "+":
#         result = num_1 + num_2
#         print(result)
#     elif operation == "-":
#         result = num_1 - num_2
#         print(result)
#     elif operation == "*":
#         result = num_1 * num_2
#         print(result)
#     elif operation == "/" and num_2 == 0:
#         result = str("При діленні дільник не може дорівнювати 0!")
#         print(result)
#     else:
#         operation = num_1 / num_2
#         print(result)
#
#     user_variant = input("Чи бажаєте продовжити (y/n): ")
#     if user_variant.lower() != 'y':
#         print('Goodbye')
#         break
