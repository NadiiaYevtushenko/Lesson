
# # Завдання 4.1
# # Здаю з запізненням бо довго розбирала. Запропонувала ще один варіант (варіант 2).
# # В Варіанті 3 не розумію 29 рядок.
# my_list_1 = [0, 1, 0, 12, 3]
# my_list_2 = [0]
# my_list_3 = [1, 0, 13, 0, 0, 0, 5]
# my_list_4= [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
#
# for i in range(len(my_list_1)):                  # значення в діапазоні
#     if my_list_1[i] == 0:                        # якщо  значення і =0
#         my_list_1.remove(0)                      # вийняти з списку і з спец. значенням
#         my_list_1.append(0)                      # перемістити значення в кінець списку
#
# print(my_list_1)                                 # друк
#
# # Варіан №2
# def move_0 (my_list_3):                      # визначення функції
#     non_zeros = [num for num in my_list_3 if num != 0]  # значення в діапазоні і = 0
#     zeros = [0] * (len(my_list_3) - len(non_zeros))      # видалення нулів
#     result = non_zeros + zeros                           # переміщення нулів в кінець
#     return result                                        #  результат функції
# print(move_0 (my_list_3))                                 # друк
#
# # Варіан №3
# my_in = 0                                             # надаємо мінній значення
# for i in range(len(my_list_1)):                       # значення в діапазоні
#     if my_list_1 [i] != 0:                            # якщо знаяення = 0
#         my_list_1[i], my_list_1 [my_in] = my_list_1 [my_in], my_list_1 [i]  #
#         my_in += 1
# print(my_list_1)
#
# # Варіан №4
# for нуль in range(len(my_list_1)):                       # значення в діапазоні
#     if my_list_1[нуль] == 0:                             # якщо знаяення = 0
#         my_list_1.append(my_list_1.pop(нуль))  # видалення нулів з списку та переміщення в кінець
#
# print(my_list_1

# Завдання 4.2

my_list = [0, 1, 7, 2, 4, 8]
def sum_multiply (my_list):         # визначення функції
    some_1 = sum(my_list[::2])          # Сума елементів з парними індексами
    if my_list != []:                     # якщо не пусте значення
       result = some_1 * my_list[-1]       # Перемноження суми на останній елемент
    return result                        #  результат функції
print(sum_multiply ([0, 1, 7, 2, 4, 8]))

