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


class Employee:
    # class property
    company = "HP"

    def __init__(self, name, salary):
        # instance property
        self.name = name
        self.salary = salary

    # instance method
    def info(self):
        print(f"{self.name} get {self.salary} from {self.company}.")

    # class method
    @classmethod
    def change_company_for_all(cls, company):
        cls.company = company

    # static method
    @staticmethod
    def add(sal1, sal2):
        return sal1 + sal2

    # Magic or Dunder (double underscore) methods
    def __str__(self):
        return f"The name is {self.name} and the salary he get from {self.company} is {self.salary}"

    def __repr__(self):
        return f"name: {self.name}\nsalary: {self.salary}"

    def __len__(self):
        return len(self.name)

    # operator overloading
    def __add__(self, other):
        return self.salary + other.salary


e1 = Employee("Pallab", 48372)
e2 = Employee("Rahul", 23473)

e1.info()
e2.info()

Employee.change_company_for_all("Acer")

e1.info()
e2.info()

print(Employee.add(e1.salary, e2.salary))


print(str(e1))
print(len(e1))
print(repr(e1))

# operator overloading
print(e1 + e2)
