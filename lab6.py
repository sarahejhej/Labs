# #  lab 1 Constructor Execution Order

# class Powerlifter:
#     def __init__(self):
#         self.is_powerlifter = True
#         print("I am a powerlifter")


# class Benchpresser(Powerlifter):
#     def __init__(self):
#         print("I am a benchpresser")
#         super().__init__()


# class BenchPressChamp(Benchpresser):
#     def __init__(self):
#         print("I am a benchpress champ")
#         super().__init__()


# benchpress_champ1 = BenchPressChamp()

# # lab 2. Modifying State Through super()

# class BaseValue:
#     def __init__(self, value):
#         print(f'This is base value: {value}')
#         self.value = value
#         print(f'This is base value2: {self.value}')


# class AddValue(BaseValue):
#     def __init__(self, value):
#         print(f'This is add value: {value}')
#         super().__init__(value)
#         self.value += value
#         print(f'This is add value2: {self.value}')


# class MultiplyValue(AddValue):
#     def __init__(self, value):
#         print(f'This is multiply value: {value}')
#         super().__init__(value)
#         self.value *= value
#         print(f'This is multiply value: {self.value}')


# multiplied = MultiplyValue(7)
# print(multiplied.value)

# # lab 3. Multiple Inheritance and MRO

# class GrandParent:
#     def __init__(self, age):
#         super().__init__()
#         self.age = age
#         print(f'Hello from grandparent, age: {self.age}')


# class ParentA(GrandParent):
#     def __init__(self, age):
#         super().__init__(age)
#         self.age -= 30
#         print(f'Hello from parent A, age: {self.age}')


# class ParentB(GrandParent):
#     def __init__(self, age):
#         super().__init__(age)
#         self.age += 10
#         print(f'Hello from parent B, age: {self.age}')


# class Child(ParentB, ParentA):
#     def __init__(self, age):
#         super().__init__(age)
#         self.age += age
#         print(f'Hello from child, age: {age}')


# child1 = Child(5)

# print(f'Age: {child1.age}')
# print(f'MRO: {Child.__mro__}')

# #  The final value depends on the MRO, i.e. the order in which constructors are called

# # 4. Predict and Verify MRO


# class Workplace:
#     def __init__(self):
#         super().__init__()
#         print('This is the workplace')


# class Remote(Workplace):
#     def __init__(self):
#         super().__init__()
#         print('This is the remote workplace')


# class OnSite(Workplace):
#     def __init__(self):
#         super().__init__()
#         print('This is the on-siteworkplace')


# class Hybrid(Remote, OnSite):
#     def __init__(self):
#         super().__init__()
#         print('This is the hybrid workplace')

# # Prediction order: Hybrid -> Remote -> OnSite -> Workplace


# work = Hybrid()

# print(f'MRO: {Hybrid.mro()}')
# #  MRO: [<class '__main__.Hybrid'>, <class '__main__.Remote'>, <class '__main__.OnSite'>, <class '__main__.Workplace'>, <class 'object'>]

# # lab 5. Overriding a Method and Calling the Parent

# class Base:
#     def __init__(self):
#         self.class_name = 'Base'

#     def print_message(self):
#         print(f'This is the message from class {self.class_name}')


# class Override(Base):
#     def __init__(self):
#         super().__init__()
#         self.class_name = 'Override'

#     def print_message(self):
#         print(f'This is the message from class {self.class_name}')
#         super().__init__()
#         print(
#             f'This is the message from class {self.class_name} after calling super()')


# class1 = Override()
# class1.print_message()

# # lab 6. Class Variables Across Inheritance


# class Base:
#     class_variable = 'Class variable'

#     def __init__(self):
#         print(f'Class variable from Base: {self.class_variable}')


# class Sub1(Base):
#     def __init__(self):
#         super().__init__()
#         self.class_variable = 'Sub1 overridden class variable'
#         super().__init__()
#         print(f'Class variable from Sub1: {self.class_variable}')


# class Sub2(Base):
#     def __init__(self):
#         self.class_variable = self.class_variable
#         super().__init__()
#         print(f'Class variable from Sub2: {self.class_variable}')


# base = Base()
# sub1 = Sub1()
# sub2 = Sub2()

# # lab 7. Protected Attributes

# class Base:
#     _score = 10

#     def __init__(self):
#         print(f'This is the score in Base: {self._score}')


# class SubClass(Base):
#     def __init__(self):
#         super().__init__()
#         print(f'This is the score in Subclass: {self._score}')

#     def score(self):
#         super().__init__()
#         print(f'Getting the score in Subclass: {self._score}')
#         return self._score

#     def reset(self):
#         self._score = 0
#         super().__init__()
#         print(f'Score has been reset: {self._score}')


# base = Base()
# print(f'Score: {base._score}')
# sub_class1 = SubClass()
# score = sub_class1.score()
# sub_class1.reset()
# score1 = sub_class1.score()
# sub_class2 = SubClass()
# score2 = sub_class2.score()


# # class variables are shared between all instances but modifying it
# # through an instance creates a new instance of the variable. The class
# # variables remains unchanged for other instances
# # The idea of class variables is to share data between all class instances.
# # Modifying class variables through instances can lead to confusion

# # lab 8. Private Attributes and Name Mangling


# class Base:
#     __score = 10

#     def __init__(self):
#         print(f'This is the score in Base: {self.__score}')


# base = Base()
# # print(f'Score: {base.__score}')
# print(f'Score: {base._Base__score}')

# # Name mangling changes the names of attributes starting with double underscore to include the class name.
# # This is to prevent accidental overtiding in subclasses

# # 9. Overriding __str__ in a Subclass

# class Plant:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return f'Plant: {self.name}'


# class Tree(Plant):
#     def __init__(self, name, tree, is_evergreen):
#         super().__init__(name)
#         self.type = tree
#         self.is_evergreen = is_evergreen

#     def __str__(self):
#         base_string = super().__str__()
#         return f'{base_string}, Type: {self.type}, Evergreen: {self.is_evergreen}'


# plant = Plant('Birch')
# tree = Tree('Pine', 'tree', True)

# print(plant)
# print(tree)

# 10. Design Task – Controlled Inheritance

class Animal:
    kingdom = 'Animalia'
    needs_food = True
    _energy_level = 10

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Kingdom: {self.kingdom}, Needs food: {self.needs_food}, Name: {self.name}. Energy level: {self._energy_level}'

    def eat(self):
        self._energy_level += 2

    def get_food(self):
        self._energy_level -= 2

    def sleep(self):
        self._energy_level = 10


class Mammal(Animal):
    has_fur = True

    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        super().eat()
        self._energy_level += 1


class Dog(Mammal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def __str__(self):
        base_string = super().__str__()
        return f'{base_string}, Breed: {self.breed}'

    def bark(self):
        print('Woof')


class Reptile(Animal):
    is_cold_blooded = True

    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        super().eat()
        self._energy_level -= 1


class Snake(Reptile):
    def __init__(self, name, length):
        super().__init__(name)
        self.length = length

    def hiss(self):
        print('Sssss')


animal = Animal('Elephant')
print(animal)

mammal = Mammal('Elephant')
mammal.eat()
print(mammal)

dog = Dog('Dog', 'Dachshund')
print(dog)
dog.bark()
dog.get_food()
dog.sleep()
print(dog)

reptile = Reptile('Crocodile')
reptile.eat()
print(reptile)

snake = Snake('Mamba', 12)
print(snake)
snake.hiss()
