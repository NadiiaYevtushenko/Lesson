# ############## Завдання 9.1 ###########################


# # Визначити популярність певних слів у тексті
# # Ще рівень розуміння ще не такий, щоб одною лінією робити ))))))))) Тому в домашній через for
# #
# text = "When I was One I had just begun When I was Two I was nearly new"
# words = ['i', "was", "tree", "near"]
# def popular_words(text_1, words_1):                   #визначення функції
#     text_lower = text_1.lower()                       # все в ловер
#     text_words = text_lower.split()                   # Розбиваємо текст на слова
#     my_dict_word_count = {}                           # Ств. словник для збер. кількості повторення кожного слова
#     for word in words_1:                              # ств. лічильник для поточного слова
#         my_dict_word_count[word] = 0                  #підрахунку кількості входжень кожного слова в тексті.
#         for text_word in text_words:
#             if text_word == word: my_dict_word_count[word]+= 1   # підрахунок
#     return my_dict_word_count                          # результат
# print(popular_words(text, words))
#
# assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
# print('All fine')


############## Завдання 9.2 ###########################


################### Варіант 1 ###################
#можна зробити читабельно і якщо потрібно буде на результат max/min числа
# def difference(*numbers_args):                         #визначення функції
#     if not numbers_args:                               # Перевірка, чи є аргументи
#         return 0                                       # результат 0, якщо немає
#     max_num = max(numbers_args)                        # Знаходимо максимум
#     min_num = min(numbers_args)                        # і мінімум
#     result = max_num - min_num                        # знаходимо різницю
#     return round(result, 2)                          # вказуємо на округлення два знаки після коми
# print(difference())
#
#
# # Перевірка тестів
# assert difference(1, 2, 3) == 2, 'Test1'
# assert difference(5, -5) == 10, 'Test2'
# assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
# assert difference() == 0, 'Test4'
# print('All fine ')

################### Варіант 2 ###################
# ще можна зробити таке, фде зрозуміло що то знущання хто не використовує

difference = lambda *numbers_args: round(max(numbers_args, default=0) - min(numbers_args, default=0), 2)

print(difference(10.2, -2.2, 0, 1.1, 0.5))
assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('All fine ')
