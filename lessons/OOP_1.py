# Готов
# Задача №1
# (Тема: Создание класса и объекта)
#
# Создай класс Book.
# У класса должен быть конструктор (__init__), который принимает два параметра: title (название) и author (автор).
# Сохрани эти параметры как атрибуты объекта.
#
# После создания класса создай один экземпляр (объект) книги с любым названием и любым автором.
# Присвой этот объект переменной my_book.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_info(self):
        return f"Книга: {self.title}, Автор: {self.author}"
my_book = Book("Старик Хоттабыч", "Лазарь Лагин")
info = my_book.get_info()




# Задача №2
# (Тема: Общие атрибуты (атрибуты класса))
#
# Создай класс Dog.
#
# У класса должен быть:
#
# Атрибут класса species со значением "Canis familiaris".
#
# Конструктор (__init__), который принимает name и age и сохраняет их как атрибуты объекта.
#
# Создай два объекта класса Dog с разными именами и возрастами.
#
# После создания:
#
# Выведи атрибут класса species через имя класса (не через объект).
#
# Выведи атрибут класса species через один из объектов.

class Dog:
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age

Dog1 = Dog("Juan", 18)
Dog2 = Dog("Maria", 19)

print(Dog.species)
print(Dog2.species)




# Задача №3
# (Тема: Параметр self и методы экземпляра)
#
# Создай класс Counter.
#
# У класса должны быть:
#
# Конструктор (__init__), который принимает начальное значение start и сохраняет его в атрибут value.
#
# Метод increment — увеличивает value на 1.
#
# Метод decrement — уменьшает value на 1.
#
# Метод get_value — возвращает текущее значение value.
#
# Создай объект класса Counter со стартовым значением 10.
# Вызови метод increment один раз.
# Вызови метод decrement два раза.
# Выведи результат метода get_value.

class Counter:
    def __init__(self, value):
        self.value = value

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

    def get_value(self):
        return self.value

counter_start = Counter(10)
counter_start.increment()
counter_start.decrement()
counter_start.decrement()
get_value = counter_start.get_value()




# Задача №4
# (Тема: Конструктор __init__ и атрибуты по умолчанию)
#
# Создай класс Student.
#
# У класса должны быть:
#
# Конструктор (__init__), который принимает параметры name и grade (оценка).
# Сохрани их как атрибуты объекта.
#
# У конструктора должен быть третий параметр school со значением по умолчанию "Школа №1".
# Сохрани его как атрибут объекта.
#
# Создай два объекта:
#
# Первый: имя "Анна", оценка 5. Школу не указывай при создании (пусть подставится по умолчанию).
#
# Второй: имя "Иван", оценка 4, школа "Лицей №2".
#
# После создания выведи атрибут school для каждого объекта (просто print).

class Student:
    def __init__(self, name, grade, school="Школа №1"):
        self.name = name
        self.grade = grade
        self.school = school

Student1 = Student("Анна", 5)
Student2 = Student("Иван", 4, school="Лицей №2")

print(Student1.school)
print(Student2.school)




# Задача №5
# (Тема: Методы, изменяющие состояние объекта)
#
# Создай класс BankAccount.
#
# У класса должны быть:
#
# Конструктор (__init__), который принимает параметр owner (владелец) и balance (баланс) со значением по умолчанию 0.
# Сохрани их как атрибуты объекта.
#
# Метод deposit — принимает сумму и добавляет её к балансу.
#
# Метод withdraw — принимает сумму и вычитает её из баланса только если на счёте достаточно средств.
# Если средств недостаточно, метод не меняет баланс, а выводит сообщение "Недостаточно средств".
#
# Метод get_balance — возвращает текущий баланс.
#
# Создай объект счёта для "Иван" с начальным балансом 100.
#
# Внеси 50 через deposit.
#
# Сними 30 через withdraw.
#
# Попробуй снять 200 (должно появиться сообщение).
#
# Выведи итоговый баланс через get_balance.

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Недостаточно средств")

    def get_balanse(self):
        return self.balance

User1 = BankAccount(owner="Иван", balance=100)
User1.deposit(50)
User1.withdraw(30)
User1.withdraw(200)
print(User1.get_balanse())




# Задача №6
# (Тема: Комбинация всего пройденного — атрибуты класса, конструктор, методы)
#
# Создай класс Employee (сотрудник).
#
# У класса должны быть:
#
# Атрибут класса company со значением "ООО Ромашка".
#
# Конструктор (__init__), который принимает name (имя) и salary (зарплата). Сохрани их как атрибуты объекта.
#
# Метод give_raise — увеличивает зарплату сотрудника на переданную сумму.
#
# Метод get_info — возвращает строку вида:
# "Сотрудник: <имя>, зарплата: <сумма>, компания: <название компании>"
# (название компании бери из атрибута класса).
#
# Создай один объект сотрудника с именем "Алексей" и зарплатой 50000.
#
# Вызови метод give_raise с суммой 10000.
#
# Вызови метод get_info и сохрани результат в переменную info.
#
# Выведи info.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    company = "ООО Ромашка"

    def give_raise(self, amount):
        self.salary += amount

    def get_info(self):
        return(f"Сотрудник: {self.name}, зарплата: {self.salary}, компания: {self.company}")

sotrudnik1 = Employee(name="Алексей", salary=50000)

sotrudnik1.give_raise(10000)
info = sotrudnik1.get_info()
print(info)




# Задача №7
# (Тема: Взаимодействие методов и изменение атрибутов)
#
# Создай класс Rectangle (прямоугольник).
#
# У класса должны быть:
#
# Конструктор (__init__), который принимает width (ширина) и height (высота). Сохрани их как атрибуты объекта.
#
# Метод area — возвращает площадь прямоугольника (width * height).
#
# Метод perimeter — возвращает периметр (2 * (width + height)).
#
# Метод scale — принимает коэффициент factor и изменяет и ширину, и высоту, умножая каждую на этот коэффициент.
#
# Создай объект прямоугольника со сторонами 5 и 3.
#
# Выведи его площадь и периметр (просто print).
#
# Примени метод scale с коэффициентом 2.
#
# Снова выведи площадь и периметр (убедись, что они изменились).

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return (self.width * self.height)

    def perimeter(self):
        return (2 * (self.width + self.height))

    def scale(self, factor):
        self.width *= factor
        self.height *= factor

pryamoygolnik = Rectangle(5, 3)

print(pryamoygolnik.area())
print(pryamoygolnik.perimeter())

pryamoygolnik.scale(2)
print(pryamoygolnik.area())
print(pryamoygolnik.perimeter())




# Задача №8
# (Тема: Атрибуты класса и методы класса)
#
# Создай класс Car.
#
# У класса должны быть:
#
# Атрибут класса total_cars со значением 0 (счётчик созданных автомобилей).
#
# Конструктор (__init__), который принимает brand (марка) и model (модель).
# Сохрани их как атрибуты объекта.
# При создании каждого нового объекта атрибут класса total_cars должен увеличиваться на 1.
#
# Метод класса get_total_cars, который возвращает текущее значение total_cars.
# (Подсказка: для метода класса используй декоратор @classmethod и параметр cls).
#
# Создай три объекта класса Car с разными марками и моделями.
# После создания каждого объекта выводи общее количество машин, используя метод get_total_cars.

class Car:
    total_cars = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_cars += 1
        print(f"Создана машина: {brand} {model}")

    @classmethod
    def get_total_cars(cls):
        return cls.total_cars


car1 = Car("Toyota", "Camry")
print(f"Всего машин: {Car.get_total_cars()}\n")

car2 = Car("BMW", "X5")
print(f"Всего машин: {Car.get_total_cars()}\n")

car3 = Car("Lada", "Granta")
print(f"Всего машин: {Car.get_total_cars()}")