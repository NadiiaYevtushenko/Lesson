# Завдання 3.1
while True:
    num_1 = float(input("Enter the number_1:"))
    operation = input("Enter action (+,-, *, /)")
    num_2 = float(input("Enter the number_2:"))
    if operation == "+":
        result = (num_1 + num_2)
    elif operation == "-":
        result =(num_1 - num_2)
    elif operation == "*":
        result =(num_1 * num_2)
    elif operation == "/" and num_2 !=0:
        result =(num_1 / num_2)
    elif operation == "/" and num_2 ==0:
        print("При діленні дільник не дорівнює 0!")
    print(result)
    break
# Завдання 3.2
#  -------------------------------1
# list_1 = [12, 3, 4, 10]
#
# if len(list_1) > 0:
#     popped_list_1 = list_1.pop()
#     last_to_first = popped_list_1
#     list_1.insert(0, last_to_first)
#
# print(list_1)
#  -------------------------------2
# list_1 = [1]
#
# if len(list_1) > 0:
#     popped_list_1 = list_1.pop()
#     last_to_first = popped_list_1
#     list_1.insert(0, last_to_first)
#
# print(list_1)
#  -------------------------------3
# list_1 = []
#
# if len(list_1) > 0:
#     popped_list_1 = list_1.pop()
#     last_to_first = popped_list_1
#     list_1.insert(0, last_to_first)
#
# print(list_1)
# -------------------------------4
list_1 = [12, 3, 4, 10, 8]

if len(list_1) > 0:
    popped_list_1 = list_1.pop()
    last_to_first = popped_list_1
    list_1.insert(0, last_to_first)

print(list_1)



