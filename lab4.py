# #  lab 1

# global_variable = "This is a global variable"


# def demonstrate_variable_scope():
#     local_variable = "This is a local variable"
#     print(local_variable)
#     print(global_variable)


# demonstrate_variable_scope()
# print(global_variable)

# # lab 2

# global_variable = 'This is a global variable'


# def read_global_variable():
#     print(global_variable)


# read_global_variable()
# print(global_variable)

# # lab 3

# global_variable = 'This is a global variable'


# def modify_global_variable():
#     global global_variable
#     global_variable = 'Modified global variable'


# print(f"Before calling modify_global_variable(): {global_variable}")
# modify_global_variable()
# print(f"After calling modify_global_variable(): {global_variable}")

# # lab 4

# global_variable = 'This is a global variable'


# def demonstrate_variable_shadowing():
#     global_variable = 'This is a local variable'
#     print(f"Inside function: {global_variable}")


# demonstrate_variable_shadowing()
# print(f"Outside function: {global_variable}")

# # lab 5

# name = "Global Name"


# def outer_function():
#     name = "Enclosing Name"

#     def inner_function():
#         name = "Local Name"
#         print(f"Inside inner_function: {name}")

#     inner_function()
#     print(f"Inside outer_function: {name}")


# print(f"Outside all functions: {name}")
# outer_function()
# print(f"Outside all functions after calling outer_function: {name}")

# # lab 6


# def outer_function():
#     name = "Enclosing Name"

#     def inner_function():
#         nonlocal name
#         name = "Modified Enclosing Name"
#         print(f"Inside inner_function: {name}")

#     print(f"Inside outer_function before calling inner_function: {name}")
#     inner_function()
#     print(f"Inside outer_function after calling inner_function: {name}")


# outer_function()

# # lab 7

# class Powerlifter:
#     def __init__(self, squat_pr, deadlift_pr, bench_pr):
#         self.squat_pr = squat_pr
#         self.deadlift_pr = deadlift_pr
#         self.bench_pr = bench_pr

#     def get_personal_records(self):
#         print(
#             f"Squat: {self.squat_pr}, Deadlift: {self.deadlift_pr}, Bench: {self.bench_pr}.")

#     def total_lift(self):
#         total = self.squat_pr + self.deadlift_pr + self.bench_pr
#         print(f"Total Lift: {total}")
#         return total


# powerlifter1 = Powerlifter(70, 95, 50)
# powerlifter2 = Powerlifter(202.5, 265, 150)

# powerlifter1.get_personal_records()
# powerlifter2.get_personal_records()
# powerlifter1.total_lift()
# powerlifter2.total_lift()

# # lab 8


# class Powerlifter:
#     is_powerlifter = True

#     def __init__(self, squat_pr, deadlift_pr, bench_pr):
#         self.squat_pr = squat_pr
#         self.deadlift_pr = deadlift_pr
#         self.bench_pr = bench_pr

#     def get_powerlifting_status(self):
#         print(f"Is Powerlifter: {self.is_powerlifter}")


# powerlifter1 = Powerlifter(70, 95, 50)
# powerlifter2 = Powerlifter(202.5, 265, 150)

# powerlifter1.get_powerlifting_status()
# powerlifter2.get_powerlifting_status()
# powerlifter1.is_powerlifter = False
# powerlifter1.get_powerlifting_status()
# powerlifter2.get_powerlifting_status()

# # lab 9

# class Walk:
#     def __init__(self, morning_walk_distance, evening_walk_distance):
#         self.morning_walk_distance = morning_walk_distance
#         self.evening_walk_distance = evening_walk_distance

#     def get_walking_distance(self):
#         total_distance = self.morning_walk_distance + self.evening_walk_distance
#         print(
#             f"Total walk distance: {total_distance}")
#         return total_distance


# walk1 = Walk(3, 5)
# walk2 = Walk(7, 2)

# walk1.get_walking_distance()
# walk2.get_walking_distance()


# # lab 10

# class Walk:
#     def __init__(self, morning_walk_distance, evening_walk_distance):
#         self.morning_walk_distance = morning_walk_distance
#         self.evening_walk_distance = evening_walk_distance

#     def get_walking_distance(self):
#         total_distance = self.morning_walk_distance + self.evening_walk_distance
#         print(
#             f"Total walk distance: {total_distance}")
#         return total_distance

#     def set_morning_walk(self, new_distance):
#         self.morning_walk_distance = new_distance
#         print(f"Updated morning walk distance: {self.morning_walk_distance}")


# walk1 = Walk(3, 5)

# walk1.get_walking_distance()
# walk1.set_morning_walk(6)
# walk1.get_walking_distance()

# #  Challenge 1

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

# # Challenge 2

# class BenchPresser:
#     is_bench_presser = True

#     def __init__(self, pr, weight, reps):
#         self.pr = pr
#         self.weight = weight
#         self.reps = reps

#     def one_rep_max(self):
#         if self.is_bench_presser:
#             orm = self.weight * (1 + self.reps / 30)
#             print(f"One Rep Max: {orm}")
#             return orm
#         else:
#             print("Not a bench presser.")
#             return 0

#     def set_bench_presser_pr(self, new_pr):
#         self.pr = new_pr
#         print(f"Updated  bench press PR: {self.pr}")


# bench_presser1 = BenchPresser(100, 80, 10)
# bench_presser2 = BenchPresser(150, 120, 5)
# bench_presser1.one_rep_max()
# bench_presser2.one_rep_max()
# bench_presser1.set_bench_presser_pr(110)

# bench_presser1.is_bench_presser = False
# bench_presser1.one_rep_max()
# bench_presser3 = BenchPresser(200, 150, 3)
# bench_presser3.one_rep_max()
# bench_presser2.one_rep_max()

# BenchPresser.is_bench_presser = False
# bench_presser1.one_rep_max()
# bench_presser2.one_rep_max()
# bench_presser3.one_rep_max()

# # Challenge 3

# class Author:
#     def __init__(self, name):
#         self.name = name
#         self.books = []

#     def write_book(self, book):
#         self.books.append(book)
#         print(f"{self.name} wrote a new book: {book.title}")

#     def get_books(self):
#         return self.books


# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         author.write_book(self)


# author1 = Author("Solvej Balle")
# book1 = Book("Om uträkning av omfång 1", author1)
# book2 = Book("Om uträkning av omfång 2", author1)
# print(
#     f"Books written by {author1.name}: {[book.title for book in author1.get_books()]}")
# print(f"Author of '{book1.title}': {book1.author.name}")
# print(f"Author of '{book2.title}': {book2.author.name}")
