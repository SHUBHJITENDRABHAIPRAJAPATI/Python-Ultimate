"""
Object-Oriented Programming in Python
======================================
This file demonstrates classes, objects, and OOP concepts.
"""

# Simple class
print("=== Simple Class ===")

class Dog:
    """A simple Dog class."""
    
    def __init__(self, name, age):
        """Initialize dog attributes."""
        self.name = name
        self.age = age
    
    def bark(self):
        """Make the dog bark."""
        print(f"{self.name} says Woof!")
    
    def description(self):
        """Return a description of the dog."""
        return f"{self.name} is {self.age} years old"

# Creating objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1.description())
dog1.bark()

print(dog2.description())
dog2.bark()

# Class with class variables
print("\n=== Class Variables ===")

class Car:
    """A Car class with class variables."""
    
    # Class variable (shared by all instances)
    wheels = 4
    
    def __init__(self, brand, model, year):
        """Initialize car attributes."""
        # Instance variables (unique to each instance)
        self.brand = brand
        self.model = model
        self.year = year
    
    def description(self):
        """Return car description."""
        return f"{self.year} {self.brand} {self.model}"

car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2021)

print(f"{car1.description()} has {car1.wheels} wheels")
print(f"{car2.description()} has {car2.wheels} wheels")

# Inheritance
print("\n=== Inheritance ===")

class Animal:
    """Base class for animals."""
    
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        """Method to be overridden by subclasses."""
        pass

class Cat(Animal):
    """Cat class inheriting from Animal."""
    
    def speak(self):
        return f"{self.name} says Meow!"

class Cow(Animal):
    """Cow class inheriting from Animal."""
    
    def speak(self):
        return f"{self.name} says Moo!"

cat = Cat("Whiskers")
cow = Cow("Bessie")

print(cat.speak())
print(cow.speak())

# Method overriding and super()
print("\n=== Method Overriding ===")

class Person:
    """Base Person class."""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old"

class Student(Person):
    """Student class inheriting from Person."""
    
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Call parent constructor
        self.student_id = student_id
    
    def introduce(self):
        """Override parent method."""
        parent_intro = super().introduce()
        return f"{parent_intro}. My student ID is {self.student_id}"

student = Student("Alice", 20, "S12345")
print(student.introduce())

# Encapsulation
print("\n=== Encapsulation ===")

class BankAccount:
    """Bank account with private attributes."""
    
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute
    
    def deposit(self, amount):
        """Deposit money."""
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount")
    
    def withdraw(self, amount):
        """Withdraw money."""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn ${amount}. New balance: ${self.__balance}")
        else:
            print("Insufficient funds or invalid amount")
    
    def get_balance(self):
        """Get current balance."""
        return self.__balance

account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(200)
print(f"Current balance: ${account.get_balance()}")

# Class methods and static methods
print("\n=== Class Methods and Static Methods ===")

class MathOperations:
    """Class demonstrating class and static methods."""
    
    pi = 3.14159
    
    @classmethod
    def circle_area(cls, radius):
        """Class method to calculate circle area."""
        return cls.pi * radius ** 2
    
    @staticmethod
    def add(a, b):
        """Static method to add numbers."""
        return a + b

print(f"Circle area (radius 5): {MathOperations.circle_area(5)}")
print(f"Addition 10 + 20: {MathOperations.add(10, 20)}")

print("\n✅ Object-Oriented Programming demonstration complete!")
