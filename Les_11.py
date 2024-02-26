# Завдання 11. 1
# Генерація випадкових подій: якщо в грі є елемент випадковості,пов'язаний з простими числами
# (наприклад, генерація випадкового числа, яке повинно бути простим),
# можна використати цю функцію для отримання випадкового простого числа з заданого діапазону.
# ігри/ лотереї

#
# def prime_generator(end):                            #визначення функції
#     """Генератор, що повертає прості числа
#     до заданої верхньої межі (включно)."""           # пояснення
#     for number in range(2, end + 1):                 # починаємо з 2, кінець це заданий діапазон +1
#         if_my_prime_generator = True                 # чи є поточне число простим
#         for i in range(2, int(number ** 0.5) + 1):   # Якщо ділиться без остачі на i, це означає, що воно не є простим числом
#             if number % i == 0:                      # Якщо 0
#                 if_my_prime_generator = False        # тоді False   і пропуск
#                 pass
#         if if_my_prime_generator:                    # якщо ж число просте, то воно іде на генерацію
#             yield number
#
#
# from inspect import isgenerator                     # імпортує функцію з модуля
#
# from inspect import isgenerator
#
# gen = prime_generator(10)
# print(list(prime_generator(29)))                     # перевірка на прінт
# assert isgenerator(gen) == True, 'Test0'
# assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
# assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
# assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
# print('All is fine')

# Завдання 11. 2


# Варіант 1


# Завдання 2 Перевірка на парність.
# Завдання ускладнюється. Ваша функція is_even, як і раніше, повинна повертати True якщо число парне,
# або False якщо число непарне, але при цьому НЕ МОЖНА використовувати ділення у функції, та дії пов'язані з ним.
# Тобто. заборонено використовувати /, //, % та divmod. Складність ще полягає і в тому, щоб знайти рішення,
# яке не залежало б від розміру числа :) Вхідні дані: Ціле число. Вихідні дані: True або False

# def is_even(number):                                         #визначення функції
#     """перевіка на парність числа. Якщо вираз повертає True, це означає, що число парне, інакше воно є непарним.
#     За принципом побітності(побітового (AND) застосовується до двійкового представлення числа.
#     В залежності якій останній біт числа 1 чи 0 видається результат )"""
#     return (number & 1) == 0
#     pass
#
# print(is_even(24945638940387**3))                             # перевірка на прінт
# assert is_even(2494563894038**2) == True, 'Test1'
# assert is_even(1056897**2) == False, 'Test2'
# assert is_even(24945638940387**3) == False, 'Test3'
# print('All is fine')

# #################          Варіант 2
def is_even(number):                            #визначення функції
    return (number & 1) ^ 1 == 1                # оператор "виключне або" (^) - виключаєм всі непарні

print(is_even(2494563894038**2))                             # перевірка на прінт
assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print('All is fine')