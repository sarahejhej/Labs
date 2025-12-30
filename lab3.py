# # lab 1

# def print_odd_numbers(input_list):
#     for num in input_list:
#         if num % 2 != 0:
#             print(num)


# numbers = list(range(1, 21))

# print_odd_numbers(numbers)


# def calc_sum(input_list):
#     total = 0
#     for num in input_list:
#         total += num
#     return total


# numbers = list(range(1, 101))
# sum_of_numbers = calc_sum(numbers)
# sum_of_numbers_short = sum(range(1, 101))

# print(f"Sum of numbers from 1 to 100: {sum_of_numbers}")
# print(f"Sum of numbers from 1 to 100 (short): {sum_of_numbers_short}")


# def print_times_table(input_number):
#     for i in range(1, 11):
#         result = input_number * i
#         print(f"{input_number} x {i} = {result}")


# input_number = int(input("Enter a number to print its times table: "))
# print_times_table(input_number)

# # lab 2

# def square_numbers(input_list):
#     squared_list_loop = []
#     for num in input_list:
#         squared_list_loop.append(num ** 2)

#     squared_list_comprehension = [num ** 2 for num in input_list]

#     print(f'squared_list_loop: {squared_list_loop}')
#     print(f'squared_list_comprehension: {squared_list_comprehension}')


# def positive_numbers(input_list):
#     positive_list = [num for num in input_list if num > 0]
#     print(f'positive_list: {positive_list}')


# numbers = list(range(-5, 6))
# square_numbers(numbers)
# positive_numbers(numbers)

# # lab 3


# def greet_user(name="Default User"):
#     return f"Hello, {name}!"


# user_name = input("Enter your name: ")
# greeting = greet_user(user_name)
# default_greeting = greet_user()
# print(greeting)
# print(default_greeting)


# def check_even_numbers(number):
#     if number % 2 == 0:
#         return True
#     return False


# input_number = int(input("Enter a number to check if it's even: "))
# is_even = check_even_numbers(input_number)
# print(f"{input_number} is {'even' if is_even else 'odd'}")


# def calculate_sum_even_numbers(num1, num2):
#     if num1 % 2 == 0 and num2 % 2 == 0:
#         return num1 + num2
#     return 0


# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# sum_even = calculate_sum_even_numbers(number1, number2)
# print(f"{'Sum of even numbers: ' if sum_even else 'No even numbers to sum.'} {sum_even if sum_even else ''}")

# # lab 4

# def is_even_number(number):
#     return number % 2 == 0


# result_function = filter(is_even_number, range(1, 21))
# result_lambda = filter(lambda x: x % 2 == 0, range(1, 21))
# print(f"Even numbers (function): {list(result_function)}")
# print(f"Even numbers (lambda): {list(result_lambda)}")


# def long_names(name):
#     return len(name) > 3


# names = ["Anna", "Sara", "Maria", "Ko", "Heijkenskjöld"]

# long_names_result = filter(long_names, names)
# print(f"Names longer than 3 characters: {list(long_names_result)}")


# def names_with_a(name):
#     return 'a' in name.lower()


# names_with_a_result = filter(names_with_a, names)
# print(f"Names containing 'a': {list(names_with_a_result)}")

# lab 5

def calculate_sum(*args):
    return sum(args)


total_sum = calculate_sum(1, 2, 3, 4, 5)
print(f"Total sum: {total_sum}")


def get_maximum_value(*args):
    return max(args)


max_value = get_maximum_value(10, 20, 5, 30, 15)
print(f"Maximum value: {max_value}")


def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(name="Sara", age=30, city="Mörby")


def print_combined_args_kwargs(number, *args, **kwargs):
    print(f"Number: {number}")

    print("Positional arguments:")
    for arg in args:
        print(arg)

    print("Keyword arguments:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_combined_args_kwargs(10, 'apple', 'banana', name='John', age=25)

# lab 6

input_list = input("Enter numbers separated by spaces: ").split()
input_list = [int(num) for num in input_list]

even_numbers = list(filter(lambda x: x % 2 == 0, input_list))

print(f"Even numbers: {even_numbers}")
print(f"Even number count: {len(even_numbers)}")
