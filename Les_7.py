
###################### 7.1 ###################
# добавила до функції умови
#
# def say_hi(name, age, city):
#     return f"Hi. My name is {name} and I'm {age} years old. I'm from {city}"
# input_name = input('Enter your name: ')
# if input_name.islower():
#     input_name = input_name.upper()
# input_age = input('Enter your age: ')
# if input_age is not input_age.isdigit():
#     input_age = input_age
# input_city = input('Enter your city: ')
# if input_city.islower():
#     input_city = input_city.upper()
# result = say_hi(input_name, int(input_age), input_city)
# print(result)
#
# assert say_hi(name = "Alex",age=32, city="London") == 'Hi. My name is Alex and I\'m 32 years old. I\'m from London'
# assert say_hi("Frank",age="32", city="London") == 'Hi. My name is Frank and I\'m 32 years old. I\'m from London'
# print('All is fine')
#
# ###################### 7.2 ###################
def correct_sentence(text):

    if text[0].islower():
        text = text[0].upper() + text[1:]         # Заголовна літера + крапка

    if not text.endswith('.'):
        text += '.'
    return text

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
# print ("All tests passed.")
my_greetings = input ("Write your greetings: ")
print ( correct_sentence(my_greetings) )
