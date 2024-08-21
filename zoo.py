#4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.

#5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы
# (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).

class Animal():
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def animal_info(self):
        return f"{self.name} - {self.species}"

    def __str__(self):
        return self.animal_info()

class Employee():
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def employee_info(self):
        return f"{self.name} - {self.position}"

    def __str__(self):
        return self.employee_info()

class Zoo():
    def __init__(self):
        self.animals = []
        self.employee = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Добавлено животное {animal}")

    def add_employee(self, employee):
        self.employee.append(employee)
        print(f"Добавлен новый сотрудник {employee}")

    def __str__(self):
        animal_info = ', '.join([str(animal) for animal in self.animals])
        employee_info = ', '.join([str(employee) for employee in self.employee])
        return f"Zoo with animals: {animal_info} and employees: {employee_info}"


zoo = Zoo()

lion = Animal("Симба","Лев")
fox = Animal("Патрикеевна", "Лиса")

keeper = Employee("Виктор", "Смотритель")
manager = Employee("Василий", "Управляющий")

zoo.add_animal(lion)
zoo.add_animal(fox)

zoo.add_employee(keeper)
zoo.add_employee(manager)

print(zoo)





