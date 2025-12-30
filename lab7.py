from abc import ABC, abstractmethod

# # lab 1 — Discover Duck Typing

# from abc import ABC, abstractmethod


# def make_lower(obj):
#     print(obj.lower())


# class Whispering:
#     def __init__(self, text):
#         self.text = text

#     def lower(self):
#         return self.text.lower()


# m = Whispering("HELLO WORLD")
# make_lower('Hello WORLD!')
# make_lower(m)

# # lab 2 — Break Duck Typing on Purpose


# def make_lower(obj):
#     print(obj.lower())


# class Whispering:
#     def __init__(self, text):
#         self.text = text

#     # def lower(self):
#     #     return self.text.lower()


# m = Whispering('HELLO WORLD')
# make_lower('Hello WORLD!')
# make_lower(m)

# # An AttributeError is thrown at runtime when the make_lower() function attempts
# # to call the lower() method on the object

# # lab 3 — EAFP vs LBYL

# def get_area(length, width):
#     try:
#         return (length * width)
#     except TypeError:
#         return (int(length) * int(width))


# print(get_area(2, 3))
# print(get_area('1', '3'))
# print(get_area('1', 0))

# # LAB 4 — Build Polymorphism with Inheritance


# class Animal:
#     def __init__(self):
#         pass

#     def sound(self):
#         raise NotImplementedError


# class Dog(Animal):
#     def __init__(self):
#         super().__init__()

#     def sound(self):
#         print('Woof')


# class Cat(Animal):
#     def __init__(self):
#         super().__init__()

#     def sound(self):
#         print('Meow')


# class Snake(Animal):
#     def __init__(self):
#         super().__init__()

#     def sound(self):
#         print('Ssss')


# def animal_sound(animal):
#     animal.sound()


# dog = Dog()
# cat = Cat()
# snake = Snake()

# animal_sound(dog)
# animal_sound(cat)
# animal_sound(snake)

# # lab 5 — Feel the Pain of isinstance

# class Dog:
#     pass


# class Cat:
#     pass


# class Snake:
#     pass


# def animal_sound(animal):
#     if isinstance(animal, Dog):
#         print('Woof')
#     elif isinstance(animal, Cat):
#         print('Meow')
#     # will have to add an elif here to chech if animal is snake

#     animal.sound()


# class Animal:
#     def __init__(self):
#         pass

#     def sound(self):
#         raise NotImplementedError


# class Dog(Animal):
#     def __init__(self):
#         super().__init__()

#     def sound(self):
#         print('Woof')


# class Cat(Animal):
#     def __init__(self):
#         super().__init__()

#     def sound(self):
#         print('Meow')


# class Snake(Animal):
#     def __init__(self):
#         super().__init__()

#     def sound(self):
#         print('Ssss')


# def animal_sound(animal):
#     animal.sound()

# # LAB 6 — Abstract Base Class Enforcement


# class Animal(ABC):
#     @abstractmethod
#     def sound(self, string):
#         pass


# class Dog(Animal):
#     def sound(self):
#         print('Woof')


# class Cat(Animal):
#     def sound(self):
#         print('Meow')


# class Snake(Animal):
#     def sound(self):
#         print('Ssss')


# dog = Dog()
# cat = Cat()
# snake = Snake()

# dog.sound()
# # Trying to instantiate the Dog class gives me this error
# # TypeError: Can't instantiate abstract class Dog without
# # an implementation for abstract method 'sound'
# # because the required method was not defined


# def animal_sound(animal):
#     animal.sound()


# animal_sound(dog)
# animal_sound(cat)
# animal_sound(snake)


# class Animal(ABC):
#     @abstractmethod
#     def sound(self, string):
#         pass


# class Dog(Animal):
#     def sound(self):
#         print('Woof')


# class Cat(Animal):
#     def sound(self):
#         print('Meow')


# class Snake(Animal):
#     def sound(self):
#         print('Ssss')


# dog = Dog()
# cat = Cat()
# snake = Snake()

# dog.sound()

# # LAB 7 — Duck Typing vs ABCs (Comparison Lab)

# #  Abstract


# class Animal(ABC):
#     @abstractmethod
#     def sound(self, string):
#         pass


# class Dog(Animal):
#     pass


# class Cat(Animal):
#     def sound(self):
#         print('Meow')


# class Snake(Animal):
#     def sound(self):
#         print('Ssss')


# dog = Dog()
# cat = Cat()
# snake = Snake()

# dog.sound()

# # Throws a TypeError. Error occurs when trying to instantiate the Dog object

# #  Duck type


# class Dog:
#     pass


# class Cat:
#     def sound(self):
#         print('Meow')


# class Snake:
#     def sound(self):
#         print('Ssss')


# dog = Dog()
# cat = Cat()
# snake = Snake()

# dog.sound()

# # Throws an AttributeError when the method is called

# # Coming from TypeScript I prefer the less flexible and more safe approach
