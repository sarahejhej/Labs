import functools
import time
import timeit
from functools import lru_cache

# # lab 1: Execution-time decorator


# def execution_time_decorator_time(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         execution_time = (end_time - start_time) * 1e3
#         print(
#             f'The execution of {func.__name__} took {round(execution_time, 5)} ms (measured with time())')

#         return result

#     return wrapper


# def execution_time_decorator_timeit(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         def run():
#             return func(*args, **kwargs)

#         execution_time = timeit.timeit(run, number=1) * 1e3
#         print(
#             f'The execution of {func.__name__} took {round(execution_time, 5)} ms (measured with timeit())')

#         return run()

#     return wrapper


# @execution_time_decorator_time
# def calculate_sum_list(numbers):
#     return sum(numbers)


# calculate_sum_list([1, 2, 3, 4, 5, 6])

# sum_of_list = calculate_sum_list([1, 2, 3, 4, 5, 6])
# print(sum_of_list)


# @execution_time_decorator_timeit
# def calculate_sum_list(numbers):
#     return sum(numbers)


# sum_of_list = calculate_sum_list([1, 2, 3, 4, 5, 6])
# print(sum_of_list)

# #  lab 2: Functional list transformation

# initial_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# altered_list = list(map(lambda x: x + x, initial_list))

# filtered_list = list(filter(lambda x: x % 2 == 0, altered_list))

# print(filtered_list)


# # lab 3: Closure-based configuration

# def factory_function(value):

#     def inner_function(x):

#         return x * value

#     return inner_function


# double = factory_function(2)
# triple = factory_function(3)

# print(double(5))  # -> 5 * 2 = 10
# print(triple(5))  # -> 5 * 3 = 15

# # lab 4: Decorator that modifies return values


# def double_result_decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")

#         result = func(*args, **kwargs)

#         return result

#     return wrapper


# @double_result_decorator
# def sum_list(numbers):
#     return sum(numbers)


# @double_result_decorator
# def multiply(a, b):
#     return a * b


# sum_result = sum_list([1, 2, 3, 4])
# print(sum_result)  # -> sum 10 * 2 = 20

# product_result = multiply(3, 5)
# print(product_result)  # product 15 * 20 = 30

# # lab 5: Static utility methods

# class MathHelper:
#     """Utility class for simple math operations."""

#     @staticmethod
#     def add_numbers(a, b):
#         return a + b

#     @staticmethod
#     def is_even(x):
#         return x % 2 == 0

#     @staticmethod
#     def is_odd(x):
#         return not MathHelper.is_even(x)


# print(MathHelper.add_numbers(2, 56))
# print(MathHelper.is_even(53))
# print(MathHelper.is_odd(53))
# print(MathHelper.__doc__)

# # Task 6: Higher-order function pipeline


# def apply_function(value, func):
#     """Apply the function arg to the value and return the result."""
#     return func(value)


# def square(a):
#     return a * a


# def double(a):
#     return a * 2


# value = 24
# pipeline = [double, lambda x: x + 24, square]

# for func in pipeline:
#     value = apply_function(value, func)
#     print(value)

# value = 24

# value = apply_function(value, double)
# print(value)

# value = apply_function(value, lambda x: x + 24)
# print(value)

# value = apply_function(value, square)
# print(value)

# # lab 7: Preserving function metadata

# def logging_decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print(
#             f"Before calling function {func.__name__}\n  args={args}\n  kwargs={kwargs}\n  docs={func.__doc__}")

#         result = func(*args, **kwargs)

#         print(
#             f"After calling function {func.__name__}\n  args={args}\n  kwargs={kwargs}\n  docs={func.__doc__}")
#         return result

#     return wrapper


# @logging_decorator
# def sum_list(numbers):
#     """Return the sum of a list of numbers."""
#     return sum(numbers)


# sum_result = sum_list([1, 2, 3, 4])

# # lab 8: Flexible decorator with arguments


# def log_with_prefix(prefix):
#     """Decorator that prints a message before running a function and adds a custom prefix'."""
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             print(
#                 f'{prefix}: Calling function {func.__name__}\n  args={args}\n  kwargs={kwargs}\n  docs={func.__doc__}')

#             result = func(*args, **kwargs)
#             print(f"{prefix}: Function {func.__name__} returned {result}")
#             return result

#         return wrapper

#     return decorator


# @log_with_prefix("DEBUG")
# def add(a, b):
#     """Function to return sum of two values."""
#     return a + b


# @log_with_prefix("INFO")
# def multiply(a, b):
#     """Function to return product of two values."""
#     return a * b


# print(add(3, 7))
# print(multiply(3, 7))

# # lab 9: Recursive problem design

# def execution_time_decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time.perf_counter()
#         result = func(*args, **kwargs)
#         end = time.perf_counter()
#         execution_time = (end - start) * 1e3
#         print(f"The execution of {func.__name__} took {execution_time:.2f} ms")
#         return result

#     return wrapper


# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)


# @lru_cache(maxsize=None)
# def fibonacci_memo(n):
#     if n <= 1:
#         return n
#     return fibonacci_memo(n-1) + fibonacci_memo(n-2)


# @execution_time_decorator
# def run_fibonacci(n):
#     print(fibonacci(n))


# @execution_time_decorator
# def run_fibonacci_memo(n):
#     print(fibonacci_memo(n))


# run_fibonacci(30)  # -> 71.61 ms
# run_fibonacci_memo(30)  # -> 0.02 ms

# lab 10: Decorators + recursion interaction

def log_function_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}")
        return func(*args, **kwargs)

    return wrapper


@lru_cache(maxsize=None)
@log_function_calls
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


print(factorial(5))
