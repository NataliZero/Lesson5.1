# Базовый класс Animal
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Этот метод должен быть переопределен в подклассе")

    def eat(self):
        print(f"{self.name} is eating.")

# Пример подкласса Dog, который наследуется от Animal
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def make_sound(self):
        print(f"{self.name} barks.")

# Пример подкласса Cat, который наследуется от Animal
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def make_sound(self):
        print(f"{self.name} meows.")

# Создание объектов
dog = Dog("Rex", 5, "Labrador")
cat = Cat("Whiskers", 3, "Black")

# Использование методов
dog.make_sound()  # Выведет: Rex barks.
dog.eat()         # Выведет: Rex is eating.
cat.make_sound()  # Выведет: Whiskers meows.
cat.eat()         # Выведет: Whiskers is eating.
