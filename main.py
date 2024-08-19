#1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`) и методы
# (`make_sound()`, `eat()`) для всех животных.

#2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`.
# Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).

#3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных и
# вызывает метод `make_sound()` для каждого животного.

#4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.

#5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы
# (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).


class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"animal sound")

    def eat(self):
        print(f"{self.name} кушает")

class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f"{self.name} поет чирик-чирик")

    def eat(self):
        print(f"{self.name} клюет зерна")

class Mammal(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f"{self.name} мычит мууууу")

    def eat(self):
        print(f"{self.name} кушает траву")


class Reptile(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f"{self.name} шипит шшшшш")

    def eat(self):
        print(f"{self.name} кушает лягушек")


animal_bird = Bird("Чык-Чырык", 2)

animal_bird.make_sound()
animal_bird.eat()

mammal = Mammal("Буренка", 5)

mammal.make_sound()
mammal.eat()

reptile = Reptile("Крокс", 10)
reptile.make_sound()
reptile.eat()
