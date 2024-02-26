
# Завдання 12. 1
#Корзина для покупок 1) Створіть клас для опису товару (припустимо, це заділ для інтернет-магазину).
# Як поля товару можете використовувати значення ціни, опис, габарити товару.
# Створіть пару екземплярів вашого класу та протестуйте їхню роботу.
# 2) Створіть клас "Покупець". Як поля можна використовувати прізвище, ім'я, по батькові, мобільний телефон і т.д.
# 3) Створіть клас "Замовлення".
# Замовлення може містити кілька товарів, причому кількість кожного з товарів може бути різною.
# Замовлення має бути "підв'язане" до користувача, який його здійснив.
# Реалізуйте метод обчислення сумарної вартості замовлення.
# Визначте метод __str__() для коректного виведення інформації про це замовлення.

class Item:                                                         # клас опису товару
    def __init__(self, name, price, description, dimensions):       # визначення функції клас опису товару
        """Клас опису товару"""
        self.name = name                                             # назва товару
        self.price = price                                           # ціна
        self.description = description                               # опис
        self.dimensions = dimensions                                 # габарити товару

    def __str__(self):                                               # виведення інформації про це замовлення
        return f"{self.name}, price: {self.price}"

class User:                                                             # клас "Покупець"
    def __init__(self, name, surname, numberphone):         # визначення функції клас "Покупець"
        """Клас Покупець"""
        self.name = name                                             # імя Покупця
        self.surname = surname                                       # Прізвище
        self.numberphone = numberphone                               # Номер телефону

    def __str__(self):
        return f"{self.name} {self.surname}"

class Purchase:                                    # клас "Замовлення".
    def __init__(self, user):                      # визначення функції клас "Замовлення"
        """Клас Замовлення"""
        self.user = user
        self.products = {}
        self.total = 0

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def __str__(self):
        output = f"User: {self.user}\nItems:\n"
        for item, cnt in self.products.items():
            output += f"{item.name}: {cnt} pcs.\n"
        return output

    def get_total(self):
        self.total = sum(item.price * cnt for item, cnt in self.products.items())
        return self.total

# Створюємо товари
lemon = Item('lemon', 5, "yellow", "small")
apple = Item('apple', 2, "red", "middle")

# Створюємо користувача
buyer = User("Ivan", "Ivanov", "02628162")

# Створюємо корзину та додаємо товари до неї
cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)

# Виводимо корзину та обчислюємо її загальну вартість
print(cart)
print(f"Total: {cart.get_total()}")

# Перевірка
assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
cart.add_item(apple, 10)
print(cart)
print(f"Total: {cart.get_total()}")
assert cart.get_total() == 40