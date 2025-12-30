# # lab1

# s = 'Python'
# o = s[4]
# pyth = s[0:4]
# yth = s[1:4]
# reversed_s = s[::-1]

# print(f"o: {o}, pyth: {pyth}, yth: {yth}, reversed_s: {reversed_s}")

# # lab2

# l = [3, 7, [1, 4, 'hello']]

# l[2][2] = 'goodbye'

# print(l)

# # lab3

# d1 = {'simple_key': 'hello'}
# d2 = {'k1': {'k2': 'hello'}}
# d3 = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}

# hello1 = d1['simple_key']
# hello2 = d2['k1']['k2']
# hello3 = d3['k1'][0]['nest_key'][1][0]

# print(f"hello1: {hello1}, hello2: {hello2}, hello3: {hello3}")

# # lab4
# my_list = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
# unique_list = list(set(my_list))

# print(f"Unique List: {unique_list}")

# # lab5

# age = 4
# name = 'Sammy'

# print(f"Hello my dog's name is {name} and he is {age} years old.")
# print("Hello my dog's name is {name} and he is {age} years old.".format(
#     name=name, age=age))

# # lab6

# base = int(input("Enter the base: "))
# exponent = int(input("Enter the exponent: "))

# for i in range(exponent):
#     result = base ** i
#     print(f"{base}^{i} = {result}")

# lab7

my_tuple = (1, 2, 3, 4, 5)
sum_of_elements = sum(my_tuple)

sum_of_elements_loop = 0
for num in my_tuple:
    sum_of_elements_loop += num

print(f"Sum of elements: {sum_of_elements}")
print(f"Sum of elements (loop): {sum_of_elements_loop}")

# lab8

my_tuple = (1, 2, 3, 4, 5)
my_even_tuple = tuple(num for num in my_tuple if num % 2 == 0)

print(f"My even tuple: {my_even_tuple}")

# lab9

dict1 = {'a': 1, 'b': 2}
dict2 = {'a': 1, 'b': 3, 'c': 4}
dict1.update(dict2)

print(f"Merged Dictionary: {dict1}")

dict12 = {'a': 1, 'b': 2}
dict22 = {'a': 1, 'b': 3, 'c': 4}

dict3 = dict12.copy()
for key, value in dict22.items():
    dict3[key] = value
print(f"Merged Dictionary (loop): {dict3}")

# lab10


def get_even_numbers(input_list):
    even_list = [num for num in input_list if num % 2 == 0]

    return even_list


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = get_even_numbers(list)

print(f"Even numbers: {even_numbers}")

# lab11


def reverse_string(string):
    return string[::-1]


input_string = "Hello, World!"
reversed_string = reverse_string(input_string)

print(f"Reversed string: {reversed_string}")
