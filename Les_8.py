# ###############Завдання 8.1##############

# Ваше завдання — написати функцію add_one, яка приймає список із цифр, які у свою чергу є одним числом. До нього необхідно додати 1.
# Тобто. Вам необхідно з набору цифр, що входять до списку, отримати число, скласти його з 1 і отриману суму, знову розбити на список із цифр.
# В результаті функція повертає список із цифр, що становлять значення суми.
# Так зі списку з цифрами [1, 2, 3, 4], має вийти число 1234. До нього додаємо 1, і отримуємо 1235.
# Після цього потрібно розбити отримане число на складові цифри. У результаті має бути список [1, 2, 3, 5], який повертає функція.
# Test: # def add_one(some_list): # pass
# assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
# assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
# assert add_one([0]) == [1], 'Test3'
# assert add_one([9]) == [1, 0], 'Test4'
# print("ОК")
#
# def add_one(some_list):                          # визначення функції
#     num = int(''.join(map(str, some_list)))      # Перетворюємо в рядки, потім об'єднуємо ці рядки у список як одне число
#     num += 1                                     # Додаємо 1 до числа
#     result = [int(digit) for digit in str(num)]  # Розбиваємо число на список цифр
#     return result
# some_list = [9]                                  # перевірка на прінті
# print(add_one(some_list))
# # Перевірка тестів
# assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
# assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
# assert add_one([0]) == [1], 'Test3'
# assert add_one([9]) == [1, 0], 'Test4'
# print("All is fine")
#                                                  # Варіант #2
# def add_one(some_list):                          # визначення функції
#     all_numbers = ""                             # задаємо змінну
#     for number in some_list:                     # перебираємо
#         all_numbers += str(number)               # розбиваємо на рядки
#     added_one_number = int(all_numbers) + 1      # до числа додаємо 1
#
#     result = [ int(i) for i in str (added_one_number) ]             # результат
#
#     return result
# some_list = [9, 9, 9]
# print(add_one(some_list))                        # перевірка на прінті


# ###############Завдання 8.2##############

# Завдання 2
#
# Вам необхідно написати функцію find_unique_value, яка приймає список із чисел, знаходить серед них унікальне число та повертати його.
# Унікальне число - це число, яке зустрічається в списку один раз. Випадок, коли в одному списку буде кілька унікальних чисел, перевіряти не потрібно.
# Приклад:
# def find_unique_value(some_list):
#     pass
# assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
# assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
# assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
# print("ОК")

# def find_unique_value(some_list):
#    for value in some_list:
#        if some_list.count(value) == 1:
#            return value
#
# some_list = [5, 5, 5, 2, 2, 0.5]               # вхідні дані
# print(find_unique_value(some_list))            # перевірка на прінті
#
#
# # Перевірка тестів
# assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
# assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
# assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
# print("All is fine")