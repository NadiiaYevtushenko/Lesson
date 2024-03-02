# Завдання 15.1  Клас «Прямокутник»
# Створіть клас «Прямокутник», у якого необхідно реалізувати два поля (ширина та висота) та кілька обов'язкових методів:
#     Метод порівняння прямокутників за площею.
#     Метод складання прямокутників (площа сумарного прямокутника повинна дорівнювати сумі площ прямокутників, які
#     ви складаєте).
#     Методи множення прямокутника на число n (це має збільшити площу базового прямокутника в n разів).
# У класі можуть бути створені додаткові (допоміжні методи)
# Декілька уточнень:
# 1. Методи складання, множення, поділу тощо. обов'язково маємо повертати новий екземпляр класу Прямокутник!
# 2. Для множення, додавання, порівняння, обов'язково потрібно перевизначати "магічні" методи. Для множення є
# вбудований метод __mul__
# 3. Коли в результаті мат. дій створюєте новий екземпляр класу Прямокутник, то у цього екземпляру, перемноження
# сторін, має давати необхідну площу. Це теж важливо
import math


class Rectangle:                                                     # клас "Прямокутник"

    def __init__(self, width, height):                               # визначення функції класу "Прямокутник"
        self.width = width                                           # ширина
        self.height = height                                         # висота

    def get_square(self):                                            # визначення функції: отримання площі
        return math.ceil(self.width * self.height)

    def __eq__(self, other):                                         # визначення функції: порівняння (площа)
        if isinstance(other, Rectangle):
            return self.get_square() == other.get_square()
        return NotImplemented

    def __add__(self, other):
        """Метод складання прямокутників (площа сумарного прямокутника повинна
        дорівнювати сумі площ прямокутників, які ви складаєте)."""
        if isinstance(other, Rectangle):                      # чи є даний об'єкт екземпляром певного класу або підкласу.
            square = self.get_square() + other.get_square()
            x = square ** 0.5
            return Rectangle(x, x)
            return NotImplemented


    def __mul__(self, n):
        """Метод множення прямокутника на число n (це має збільшити площу базового прямокутника в n разів)."""
        my_width = self.width * (n ** 0.5)
        my_height = self.height * (n ** 0.5)
        return Rectangle(my_width, my_height)


    def __str__(self):
        return f"Rectangle (width={self.width}, height={self.height})"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
print(r1)
assert r2.get_square() == 18, 'Test2'
print(r2)

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'
print(r3)

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'
print(r4)
print("All tests passed")