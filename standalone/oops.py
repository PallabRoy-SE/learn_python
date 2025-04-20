class Animal:
    def sound(self):
        print("Animal sound.")


class Dog(Animal):
    def sound(self):
        print("Bow!")


class Cat(Animal):
    def sound(self):
        print("Meow!")


animal = Animal()
dog = Dog()
cat = Cat()

animal.sound()
dog.sound()
cat.sound()
