class Animals:
    num_animals = 0

    def __init__(self, name):
        self.name = name
        Animals.num_animals += 1

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animals):

    def speak(self):
        print("WOOF!")

class Cat(Animals):
    def speak(self):
        print("MEOW!")

dog = Dog("Max")
cat = Cat("Tom")

print(f"Number of animals: {Animals.num_animals}")
print(dog.name)
print(cat.name)

dog.speak()
cat.speak()