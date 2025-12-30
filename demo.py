from functools import lru_cache
import functools


def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__}')
        return func(*args, **kwargs)

    return wrapper


# def say(name):
#     print(f'Hello, {name}!')


# def call_with_name(fn, name):
#     # pass a function as an argument and invoke it
#     fn(name)


# def get_greeter(prefix):
#     # return a new function (higher-order function)
#     def greeter(name):
#         print(f'{prefix} {name}')
#     return greeter


# @my_decorator
# def excited(name):
#     print(f'YAY {name.upper()}!!!')


# # examples
# call_with_name(say, 'Alice')
# call_with_name(get_greeter('Welcome,'), 'Bob')
# call_with_name(excited, 'Carol')

# #  higher-order functiontion


def apply_function(func, value):
    return func(value)


# def square(x):
#     return x * x


# def cube(x):
#     return x * x * x

# # pass functions as arguments


# print(apply_function(square, 3))
# print(apply_function(cube, 3))

# def square(x):
#     return x * x


# def square_lambda(x): return x * x


# print(square(5))
# print(square_lambda(5))

# print(apply_function(lambda x: x + 10, 5))

# # Recursion and memoization

# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)


# print(factorial(5))


@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(10))
print(fibonacci.cache_info())
