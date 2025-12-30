# # section 1

# # 1. Create a class with property and setter

# class Square:
#     def __init__(self):
#         self.side_length = 0

#     @property
#     def area(self):
#         return self.side_length ** 2

#     @property
#     def side_length_value(self):
#         return self.side_length

#     @side_length_value.setter
#     def side_length_value(self, value):
#         self.side_length = value


# square = Square()
# square.side_length_value = 4
# print(f"Square side length: {square.side_length_value}")
# print(f"Square area: {square.area}")

# # 2. Create a class with a clean __str__ representation


# class Powerlifter:
#     def __init__(self, squat, bench_press, deadlift):
#         self.squat = squat
#         self.bench_press = bench_press
#         self.deadlift = deadlift
#         self.is_powerlifter = True

#     def __str__(self):
#         result = []
#         for key, value in self.__dict__.items():
#             result.append(f"{key}: {value}")
#         return "\n".join(result)

#     def total_lifted(self):
#         return self.squat + self.bench_press + self.deadlift


# powerlifter = Powerlifter(squat=200, bench_press=150, deadlift=265)
# print(powerlifter)

# # 3. Create a class with a meaningful __repr__


# class Powerlifter:
#     def __init__(self, squat_pr, deadlift_pr, bench_pr):
#         self.squat_pr = squat_pr
#         self.deadlift_pr = deadlift_pr
#         self.bench_pr = bench_pr

#     def __repr__(self):
#         return f"Powerlifter(squat_pr={self.squat_pr}, deadlift_pr={self.deadlift_pr}, bench_pr={self.bench_pr})"

#     def __str__(self):
#         result = []
#         for key, value in self.__dict__.items():
#             result.append(f"{key}: {value}")
#         return "\n".join(result)

#     def total_lift(self):
#         total = self.squat_pr + self.deadlift_pr + self.bench_pr
#         print(f"Total lift: {total}")
#         return total


# powerlifter1 = Powerlifter(70, 95, 50)
# powerlifter2 = Powerlifter(202.5, 265, 150)
# print(powerlifter1)
# print(powerlifter2)
# print(repr(powerlifter1))
# print(repr(powerlifter2))

# # 4. Create a class that initializes from **kwargs

# class Powerlifter:
#     def __init__(self, **kwargs):
#         for key, value in kwargs.items():
#             setattr(self, key, value)

#     def __str__(self):
#         result = []
#         for key, value in self.__dict__.items():
#             result.append(f"{key}: {value}")
#         return "\n".join(result)


# powerlifter = Powerlifter(squat=200, bench_press=150, deadlift=265)
# print(powerlifter)

# # 5. Create a class that builds its string using a comprehension


# class Powerlifter:
#     def __init__(self, **kwargs):
#         for key, value in kwargs.items():
#             setattr(self, key, value)

#     def __str__(self):

#         return f"\n".join([f"{key}: {value}" for key, value in self.__dict__.items()])


# powerlifter = Powerlifter(squat=200, bench_press=150,
#                           deadlift=265, is_powerlifter=True)
# print(powerlifter)

# # section 2

# #  6. Implement __eq__


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __eq__(self, other):
#         if isinstance(other, Person):
#             return self.name == other.name and self.age == other.age
#         return False


# person1 = Person("Alice", 30)
# person2 = Person("Alice", 30)
# person3 = Person("Bob", 25)

# print(person1 == person2)
# print(person1 == person3)

# # 7. Implement __lt__


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __lt__(self, other):
#         if isinstance(other, Person):
#             return self.age < other.age
#         return False


# person1 = Person("Alice", 30)
# person2 = Person("Bob", 25)
# print(person1.age < person2.age)
# print(person2.age < person1.age)

# # 8. Implement __add__

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __add__(self, other):
#         if isinstance(other, Person):
#             combined_name = f"{self.name} & {other.name}"
#             combined_age = self.age + other.age
#             return Person(combined_name, combined_age)
#         return NotImplemented


# person1 = Person("Alice", 30)
# person2 = Person("Bob", 25)
# combined_person = person1 + person2
# print(
#     f"Combined Person: Name={combined_person.name}, Age={combined_person.age}")

# # 9. Implement __len__


# class Author:
#     def __init__(self, name):
#         self.name = name
#         self.books = []

#     def write_book(self, book):
#         self.books.append(book)
#         print(f"{self.name} wrote a new book: {book.title}")

#     def get_books(self):
#         return self.books

#     def __len__(self):
#         return len(self.books)


# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         author.write_book(self)


# author1 = Author("Solvej Balle")
# book1 = Book("Om uträkning av omfång 1", author1)
# book2 = Book("Om uträkning av omfång 2", author1)

# print(len(author1))

# # 10. Implement __contains__


# class Author:
#     def __init__(self, name, books):
#         self.name = name
#         self.books = books

#     def __contains__(self, item):
#         return item in self.name


# author1 = Author("Solvej Balle", [
#                  "Om uträkning av omfång 1", "Om uträkning av omfång 2"])


# print("Balle" in author1)

# #  11. Implement __getitem__

# class Author:
#     def __init__(self, name, books):
#         self.name = name
#         self.books = books

#     def __getitem__(self, index):
#         return self.books[index]


# author1 = Author("Solvej Balle", [
#                  "Om uträkning av omfång 1", "Om uträkning av omfång 2"])

# print(author1[1])


# # section 3

# # 12. Rewrite a loop using a list comprehension


# def loop_squared(list):
#     squared_list = []
#     for item in list:
#         squared_list.append(item ** 2)
#     return squared_list


# def comprehension_squared(list):
#     return [num ** 2 for num in list]


# loop_squared_list = loop_squared([1, 2, 3, 4])
# comprehension_squared_list = comprehension_squared([1, 2, 3, 4])
# print(loop_squared_list)
# print(comprehension_squared_list)

# # 13. . Create a filtered list comprehension


# def comprehension_filter(list):
#     return [num for num in list if num > 2]


# comprehension_filtered_list = comprehension_filter([1, 2, 3, 4, 5])
# print(comprehension_filtered_list)

# # 14. Create a dictionary using a dict comprehension

# keys = ['age', 'first_name', 'last_name', 'city']
# values = [12, 'Elin', 'Sson', 'Staden']

# key_value_dictionary = {k: v for (k, v) in zip(keys, values)}
# print(key_value_dictionary)

# #  15. Build a formatted string using a comprehension

# my_dict = {'age': 12,
#            'first_name': 'Elin',
#            'last_name': 'Sson',
#            'city': 'Staden',
#            }

# formatted_string = f"\n".join(
#     [f"{key}: {value}" for key, value in my_dict.items()])
# print(formatted_string)

# # 16. Create a nested comprehension

# my_list = [1, 2, 3, 4]

# nested_list = [[num for num in my_list if num > 2] for num in my_list]

# print(nested_list)

# #  Section 4

# #  17. Demonstrate LEGB with nested functions


# def outer_function():
#     name = "Outer"
#     print(f"Outer function first: {name}")

#     def middle_function():
#         nonlocal name
#         name = "Middle"
#         print(f"Middle function first: {name}")

#         def inner_function():
#             global name
#             name = "Inner"
#             print(f"Inner function: {name}")

#         inner_function()
#         print(f"Middle function second: {name}")

#     middle_function()
#     print(f"Outer function second: {name}")


# name = "Global"
# print(f"Global scope first: {name}")
# outer_function()
# print(f"Global scope second: {name}")

# #  18. Create a class that processes input using a comprehension


# class MyList():
#     def __init__(self, my_list):
#         self.my_list = my_list

#     def filter_list(self):
#         return [item for item in self.my_list if item % 2 == 0]


# my_list = MyList([1, 2, 3, 4, 5, 6, 7])
# my_filtered_list = my_list.filter_list()
# print(my_list.filter_list())
# print(my_filtered_list)

# # 19. Create a class that builds itself from a dictionary


# class MyDict():
#     def __init__(self, my_dict):
#         for key, value in my_dict.items():
#             setattr(self, key, value)

#     def __str__(self):
#         result = []
#         for key, value in self.__dict__.items():
#             result.append(f"{key}: {value}")
#         return "\n".join(result)


# my_dict = MyDict({'1': 'one', '2': 'two', '3': 'three'})

# print(my_dict)

#  20. Combine kwargs, property, and a dunder method

class Powerlifter():
    def __init__(self, **kwargs):
        self.is_powerlifter = True
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return f"\n".join([f"{key}: {value}" for key, value in self.__dict__.items()])

    def total_lift(self):
        total = self.squat + self.deadlift + self.bench_press
        print(f"Total lift: {total}")
        return total

    @property
    def is_powerlifter_value(self):
        return self.is_powerlifter

    @is_powerlifter_value.setter
    def is_powerlifter_value(self, value):
        self.is_powerlifter = value


powerlifter1 = Powerlifter(squat=200, bench_press=150, deadlift=265)
print(powerlifter1)
powerlifter1.is_powerlifter_value = False

print(powerlifter1)
powerlifter1.total_lift()
