###############Завдання 6.1##############
#Даний список словників людей у форматі [{"name": "John", "age": 15}, ..., {"name": "Jack", "age": 45}]
# а) Створити список і помістити туди ім'я наймолодшої людини. Якщо вік збігається – помістити всі імена наймолодших.
# б) Створити список та помістити туди найдовше ім'я. Якщо довжина імені збігається - помістити такі імена.
# в) Порахувати середню вік усіх людей із початкового списку.
#
# people_list = [
#     {"name": "Nadiia", "age": 33},
#     {"name": "Vika", "age": 30},
#     {"name": "Valia", "age": 27},
#     {"name": "Albina", "age": 24},
#     {"name": "Igor", "age": 36},
# ]
# min_age = min(person["age"]for person in people_list)
# youngest_name = [person["name"] for person in people_list if person["age"]== min_age]
# print(("A)youngest_name:"), youngest_name)
#
# max_name_len = max(len(person['name']) for person in people_list)
# longest_name = [person['name'] for person in people_list if len(person['name'])==max_name_len]
# print(("B)longest_name:"), longest_name)
#
# midle_age = sum(person['age'] for person in people_list)/len(people_list)
# print("C)midle_age:", midle_age)
#
# #########Через функцію ##################
#
# def find_min_age(people_list):
#     min_age = min(person["age"] for person in people_list)
#     youngest_names = [person["name"] for person in people_list if person["age"] == min_age]
#     return youngest_names
# def find_max_name_len(people_list):
#     max_name_len = max(len(person["name"]) for person in people_list)
#     longest_names = [person["name"] for person in people_list if len(person["name"]) == max_name_len]
#     return longest_names
# def find_middle_age(people_list):
#     total_age = sum(person["age"] for person in people_list)
#     middle_age = total_age / len(people_list)
#     return middle_age
#
# people_list = [
#     {"name": "Nadiia", "age": 33},
#     {"name": "Vika", "age": 30},
#     {"name": "Valia", "age": 27},
#     {"name": "Albina", "age": 24},
#     {"name": "Igor", "age": 36}
# ]
#
# youngest_names_result = find_min_age(people_list)
# print("A) youngest names:", youngest_names_result)
#
# longest_names_result = find_max_name_len(people_list)
# print("B) longest names:", longest_names_result)
#
# middle_age_result = find_middle_age(people_list)
# print("C) middle_age:", middle_age_result)

################6.2#############
# Завдання 2
# Дано два словники my_dict_1 і my_dict_2.
# а) Створити список із ключів, які є в обох словниках.
# б) Створити список із ключів, які є у першому, але немає у другому словнику.
# в) Створити новий словник з пар {ключ:значення} для ключів, які є в першому, але немає в другому словнику.
# г) Об'єднати ці два словники у новий словник за правилом:
# якщо ключ є тільки в одному з двох словників - помістити пару ключ: значення,
# якщо ключ є у двох словниках - помістити пару {ключ: [значення_з_першого_словника, значення_з_другого_словника]},
# {1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}


# def result_home_work(my_dict_1, my_dict_2):
#     result_1 = list(set(my_dict_1.keys()).intersection(set(my_dict_2.keys()))) # Ств. список із ключів, які є в обох словниках.
#     result_2 = list(set(my_dict_1.keys()).difference(set(my_dict_2))) # Ств. список із ключів, які є у першому, але немає у другому словнику.
#     result_3 = {key:my_dict_1[key] for key in result_2} #  Ств. новий словник з пар {ключ:значення} для ключів, які є в першому, але немає в другому словнику.
#     result_4 = my_dict_1.copy()
# # Об'єднати ці два словники у новий словник за правилом:
# # якщо ключ є тільки в одному з двох словників - помістити пару ключ: значення,
# # якщо ключ є у двох словниках - помістити пару {ключ: [значення_з_першого_словника, значення_з_другого_словника]}
#     for key in my_dict_2:
#         if key in result_4:
#             result_4[key] = [result_4[key], my_dict_2[key]]
#         else:
#             result_4[key] = my_dict_2[key]
#     return result_1, result_2, result_3, result_4
# my_dict_1 = {1:1, 2:2}
# my_dict_2 = {11:11, 2:22}
# print(result_home_work(my_dict_1, my_dict_2))


##############################    Варіан 2  до задачі 6.2  ####################

def my_home_work_6 (dict1, dict2):                             # визначення функції
    variant_1_both = list(set(dict1.keys()) & set(dict2.keys())) # Ств. список  є в обох словниках
    variant_2_unique_dict1 = list(set(dict1.keys()) - set(dict2.keys()))  # Ств. список  є у dict1, але немає в другому
    unique_dict1 = {key: dict1[key] for key in variant_2_unique_dict1}    # Ств. new_dict  є в dict1 але немає в другому
    variant_4 = {}                                                 # Об'єднуємо г)
    for key in dict1.keys():                                         # для ключів в dict1
        if key in dict2.keys():                                      # якщо ключ в dict2
            variant_4[key] = [dict1[key], dict2[key]]              # г) =
        else:
            variant_4[key] = dict1[key]                             # в іншому випадку ключ з dict1
    for key in dict2.keys():                                  # для ключів в dict2
        if key not in dict1.keys():                        # якщо ключ не dict1
            variant_4[key] = dict2[key]                          # г) = ключ з dict2

    return variant_1_both, variant_2_unique_dict1, unique_dict1, variant_4  # результат

# Вхідні дані
dict1 = {1: 1, 2: 2}
dict2 = {11: 11, 2: 22}

result = my_home_work_6(dict1, dict2)
print("variant_1_both:", result[0])
print("variant_2_unique_dict1:", result[1])
print("unique_dict1:", result[2])
print("variant_4:", result[3])