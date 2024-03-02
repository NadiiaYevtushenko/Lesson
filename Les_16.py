# def bubble_sort(lst: list) -> list:
#     """сортування бульбашкою - не найкраще рішення
#     """
#     size = len(lst)
#     for i in range(size):
#         for j in range(size - 1):
#             if lst[j] > lst[j + 1]:
#                 lst[j], lst[j + 1] = lst[j + 1], lst[j]
#     return lst
# #
# # list = [1, 3, 2, 4, 6, 5, 7, 8, 9, 10]
# # print(bubble_sort(list))
# # print(len(list))
# #  Зробимо виміри часу роботи
# # import random
# # import time
# # my_list = [random.randint(0, 10000) for i in range(10000)]
# # """створює список my_list, що містить 100 випадкових цілих чисел в діапазоні від 0 до 100
# # за допомогою вбудованої функції random.randint(0, 100) та генератора списку. """
# # start = time.time()
# # """ використовується для вимірювання часу до та після виконання сортування,"""
# # bubble_sort(my_list)
# # print(time.time() - start)


def binary_search(lst: List, val: Union[int, float]):
    """    Бінарний пошук   O(log n)  """
    first = 0
    last = len(lst)-1
    index = -1
    while (first <= last) and (index == -1): # Поки є умови для пошуку
        mid = (first + last) // 2
        if lst[mid] == val: # Якщо знайшли потрібний елемент
            index = mid
        else:
            # Визначаємо в якій частині потрібно шукати
            if val < lst[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return index