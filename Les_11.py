# Завдання 11. 1
# Генерація випадкових подій: Наприклад, якщо в грі є елемент випадковості,
# пов'язаний з простими числами (наприклад, генерація випадкового числа, яке повинно бути простим),
# можна використати цю функцію для отримання випадкового простого числа з заданого діапазону.


def prime_generator(end):                            #визначення функції
    """Генератор, що повертає прості числа           
    до заданої верхньої межі (включно)."""           # пояснення
    for number in range(2, end + 1):                 # починаємо з 2, кінець це заданий діапазон +1
        if_my_prime_generator = True                 # чи є поточне число простим
        for i in range(2, int(number ** 0.5) + 1):   # Якщо ділиться без остачі на i, це означає, що воно не є простим числом
            if number % i == 0:                      # Якщо 0
                if_my_prime_generator = False        # тоді False   і пропуск
                pass
        if if_my_prime_generator:                    # якщо ж число просте, то воно іде на генерацію
            yield number


from inspect import isgenerator                     # імпортує функцію з модуля

gen = prime_generator(10)
print(list(prime_generator(10)))                                       # провірка на прінт
next(prime_generator(10))
print(next(prime_generator(10)))
next(prime_generator(10))
print(next(prime_generator(10)))

assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('All fine')