# Завдання 1
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




