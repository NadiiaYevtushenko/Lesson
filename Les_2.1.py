
# my_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
# second_list = []        # create new list
# zero = my_list.count(0)  # count how many zero we have in our list
# for index in range(len(my_list)): # for пробігаємося і якщо це не 0 то додаємо до 2-го листа
#     if my_list[index] != 0:
#         second_list.append(my_list[index])
# second_list.extend([0]* zero) # метод extend використовується для додавання всіх елементів і іншого списку
# # в нашому випадку ми просто добавляємо метод каунт і аппенд
# print(second_list)


# my_list = [1, 0, 13, 0, 0, 0, 5, 9, 9, 9, 9, 0, 0, 4, 3]
# for i in range(len(my_list)):   # перебераємо цифри
#     if my_list[0] == 0:         # якщо елемент в листі
#         my_list.remove(0)       # ремувимо
#         my_list.append()        # додаємо в кінець
# print(my_list)


# ##############3#####################
# my_list = [1, 0, 13, 0, 0, 0, 5, 9, 9, 9, 9, 0, 0, 4, 3]
# my_list.sort(key=bool, reverse=True) # 0 це False, bool це True. Ми сортуємо - на початку True потім False
# print(my_list)


##############5#####################
# list = [0, 3, 5, 0, 4, 0, 7, 9]
# index = 0
# for i in range(len(list)):         # перебрати лист
#     if list[i] != 0:                 # якщо елемент не дорівнює нулю
#         list[i], list[index] = list[index], list[i]   # ми змінємо їх місцями оцей індекс в оце значення
#         # значення 0 рухаються в кінець, а цифри вперед
#         index = index + 1
# print(list)

# № 2 завдання


# my_list = [0, 1, 7, 2, 4, 8]
# result = 0
#
# for i in range(0,len(my_list),2):
#     result += my_list[i]
#
# if my_list != []:
#     result = result * my_list[-1]
#
# print(result)


# some_list = [0, 4, 5, 2, 6, 7, 4, 2, 1, 7]
# result = sum(some_list[::2]) * some_list[-1]
# print(result)

# # Заняття 6
# some_list = [ i for i in range(5)]
# print(some_list)