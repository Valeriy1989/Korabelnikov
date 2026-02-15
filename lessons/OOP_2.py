# Задача 1
#
# Создай класс Animal (животное). У него должен быть метод speak, который при вызове возвращает строку "I am an Animal".
#
# Затем создай класс Dog (собака), который наследуется от Animal. Переопредели в нём метод speak так, чтобы он возвращал строку "Woof!".
#
# Напиши код для обоих классов и небольшой пример использования: создай объект класса Dog, вызови его метод speak и выведи результат на экран.

class Animal:
    def speak(self):
        return "I am an Animal"

class Dog(Animal):
    def speak(self):
        return "Woof!"

Bobik = Dog()
print(Bobik.speak())




# Задача 2
#
# Создай класс Vehicle (транспортное средство). В нём должен быть атрибут brand (марка), который задается при создании объекта, и метод honk, который возвращает строку "Beep!".
#
# Создай класс Car (машина), который наследуется от Vehicle. Добавь в класс Car новый атрибут doors (количество дверей), который также должен задаваться при создании объекта.
#
# Напиши код для обоих классов. Создай объект класса Car с маркой "Toyota" и количеством дверей 4. Выведи на экран марку машины, количество дверей и звук сигнала (метод honk).

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def honk(self):
        return "Beep!"

class Car(Vehicle):
    def __init__(self, brand, doors):
        super().__init__(brand)
        self.doors = doors

car1 = Car("Toyota", 4)
print(f"{car1.brand}, {car1.doors}", car1.honk())




# Задача 3
#
# Создай базовый класс Employee (сотрудник). При создании объекта он должен принимать два параметра: name (имя) и salary (зарплата). Добавь метод get_info, который возвращает строку вида: "Сотрудник: <имя>, зарплата: <зарплата>".
#
# Затем создай класс Manager (менеджер), который наследуется от Employee. Добавь в него новый атрибут team_size (размер команды), который также задается при создании объекта.
#
# Переопредели метод get_info в классе Manager так, чтобы он возвращал строку вида: "Менеджер: <имя>, зарплата: <зарплата>, команда: <team_size> человек".
#
# Напиши код для обоих классов и пример использования: создай менеджера с именем "Анна", зарплатой 120000 и командой из 5 человек. Выведи результат вызова метода get_info для этого менеджера.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_info(self):
        return (f"Сотрудник: {self.name}, зарплата: {self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_info(self):
        return (f"Менеджер: {self.name}, зарплата: {self.salary}, команда: {self.team_size} человек")

Manager1 = Manager("Анна", 120000, 5)
print(Manager1.get_info())




# Задача 4
#
# Создай класс Shape (фигура). У него должен быть метод area, который просто возвращает 0.
#
# Создай два дочерних класса:
#
# Rectangle (прямоугольник), который при создании принимает параметры width и height. Переопредели метод area так, чтобы он возвращал площадь прямоугольника.
#
# Circle (круг), который при создании принимает параметр radius. Переопредели метод area так, чтобы он возвращал площадь круга (используй 3.14 как значение числа Пи).
#
# Напиши код для всех трех классов. Создай по одному объекту каждого типа и выведи на экран результат вызова их метода area.

import math


class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

object1 = Shape()
object2 = Rectangle(3, 5)
object3 = Circle(7)

print(object1.area())
print(object2.area())
print(object3.area())




# Задача 5
#
# Создай класс Counter (счетчик). У него должно быть:
#
# Приватный атрибут __count, который изначально равен 0.
#
# Метод increment, который увеличивает значение счетчика на 1.
#
# Метод get_count, который возвращает текущее значение счетчика.
#
# Затем создай класс DoubleCounter (двойной счетчик), который наследуется от Counter. Переопредели в нем метод increment так, чтобы он увеличивал значение счетчика сразу на 2.
#
# Напиши код для обоих классов. Создай объект класса DoubleCounter, вызови его метод increment один раз, а затем выведи значение счетчика на экран с помощью метода get_count.

class Counter:
    def __init__(self):
        self.__count = 0

    def increment(self):
        self.__count = self.__count + 1

    def get_count(self):
        return self.__count

class DoubleCounter(Counter):

    def increment(self):
        self._Counter__count += 2

counter2 = DoubleCounter()
counter2.increment()
print(counter2.get_count())




# Задача 6
#
# Создай класс BankAccount (банковский счет). При создании он принимает параметр owner (владелец). У него должны быть:
#
# Приватный атрибут __balance (баланс), изначально равный 0.
#
# Метод deposit(amount), который добавляет сумму к балансу.
#
# Метод withdraw(amount), который вычитает сумму из баланса, но только если на счету достаточно средств. Если средств недостаточно, метод должен возвращать сообщение "Недостаточно средств", иначе выполнять операцию и ничего не возвращать.
#
# Метод get_balance, который возвращает текущий баланс.
#
# Затем создай класс SavingsAccount (сберегательный счет), который наследуется от BankAccount. Переопредели в нем метод withdraw: сделай так, чтобы снять деньги было нельзя вообще. При попытке снятия метод всегда должен возвращать строку "Снятие с накопительного счета невозможно".
#
# Напиши код для обоих классов. Покажи пример использования: создай объект SavingsAccount для "Ивана", положи на счет 1000 (метод deposit), попробуй снять 500 (метод withdraw) и выведи результат этой попытки. Затем выведи финальный баланс.

class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            return "Недостаточно средств"

    def get_balance(self):
        return self.__balance

class SavingsAccount(BankAccount):
    def __init__(self, owner):
        super().__init__(owner)

    def withdraw(self, amount):
        return "Снятие с накопительного счета невозможно"

User1 = SavingsAccount("Иван")
User1.deposit(1000)
User1.withdraw(500)
print(User1.get_balance())




# Задача 7
#
# Создай класс Player (игрок). У него должны быть:
#
# Атрибуты: name (имя) и health (здоровье), которые задаются при создании объекта.
#
# Метод attack, который возвращает строку "Наносит удар!".
#
# Создай класс Mage (маг), который наследуется от Player. При создании мага у него должен появляться новый атрибут mana (мана), который тоже задается через параметры.
# Переопредели метод attack у мага: он должен тратить 10 единиц маны и возвращать строку "Кастует заклинание!". Если маны меньше 10, метод должен возвращать строку "Недостаточно маны".
#
# Напиши код для обоих классов. Создай мага с именем "Гендальф", здоровьем 100 и маной 50. Вызови его метод attack два раза подряд, каждый раз выводя результат на экран. Затем выведи оставшееся количество маны (используй прямой доступ к атрибуту mana, он не приватный).

class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self):
        return "Наносит удар!"

class Mage(Player):
    def __init__(self, name, health, mana):
        super().__init__(name, health)
        self.mana = mana

    def attack(self):
        if self.mana >= 10:
            self.mana -= 10
            return "Кастует заклинание!"
        else:
            return "Недостаточно маны"

mag_gendalf = Mage("Гендальф", 100, 50)

mag_gendalf.attack()
print(mag_gendalf.attack())

mag_gendalf.attack()
print(mag_gendalf.attack())

print(mag_gendalf.mana)




# Задача 8
#
# Создай класс Product (товар). При создании он принимает два параметра: name (название) и price (цена). У него должен быть метод get_price, который возвращает цену товара.
#
# Создай класс DiscountedProduct (товар со скидкой), который наследуется от Product. При создании он принимает ещё один параметр — discount (скидка в процентах, например, 15 означает скидку 15%).
#
# Переопредели метод get_price в классе DiscountedProduct так, чтобы он возвращал цену с учетом скидки (округленную до двух знаков после запятой).
#
# Напиши код для обоих классов. Создай объект класса DiscountedProduct с названием "Ноутбук", ценой 1000 и скидкой 10. Выведи на экран его итоговую цену, вызвав метод get_price.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

class DiscountedProduct(Product):
    def __init__(self, name, price, discount):
        super().__init__(name, price)  # Родитель сам сохранит name и price
        self.discount = discount

    def get_price(self):
        return round((self.price - ((self.price / 100) * self.discount)), 2)

product1 = DiscountedProduct("Ноутбук", 1000, 10)
print (product1.get_price())