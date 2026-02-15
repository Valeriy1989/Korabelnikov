class Bird:

    def fly(self):
        return "Летает"

class Penguin(Bird):

    def fly(self):
        return "Не летает"

class Eagle(Bird):
    pass


class Duck(Bird):

    def quack(self):
        return "Кря!"

Bird_1 = Penguin()
Bird_2 = Eagle()
Bird_3 = Duck()
print(Bird_1.fly())
print(Bird_2.fly())
print(Bird_3.fly())
print(Bird_3.quack())


