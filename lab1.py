#  lab1
# first_number = int(input())
# second_number = int(input())

# sum = first_number + second_number
# difference = first_number - second_number
# product = first_number * second_number
# division = first_number / second_number
# power = first_number ** second_number

# print(f"Sum: {sum}\nDifference: {difference}\nProduct: {product}\nDivision: {division:.2f}\nPower: {power}")

# # lab2
# salary = 12000
# bonus = 5000
# tax_rate = 0.4

# total_income = salary + bonus
# taxes = int((salary + bonus) * tax_rate)
# net_income = (salary + bonus) - taxes

# print(
#     f"Total Income: {total_income}\nTaxes: {taxes}\nNet Income: {net_income}")

# # lab3
# s = "ProgrammingIsFun"
# first_letter = s[0]
# last_three_letters = s[-3:]
# every_second_letter = s[::2]
# programming = s[:11]
# fun = s[13:]
# reversed = s[::-1]

# print(f"First Letter: {first_letter}\nLast Three Letters: {last_three_letters}\nEvery Second Letter: {every_second_letter}\nProgramming: {programming}\nFun: {fun}\nReversed: {reversed}")

# # lab4
# input_string = input("Enter a string: ")
# uppercase_string = input_string.upper()
# lowercase_string = input_string.lower()
# length_of_string = len(input_string)
# string_list = input_string.split(' ')
# replaced_string = input_string.replace(string_list[0], 'Else')

# print(
#     f"Uppercase: {uppercase_string}\nLowercase: {lowercase_string}\nLength: {length_of_string} List: {string_list}\nReplaced: {replaced_string}")

# lab5
# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# birth_year = int(input("Enter your birth year: "))
# username = first_name.lower()[:3] + \
#     last_name.lower()[-3:] + str(birth_year)[-2:]

# print(f"Username: {username}")

# # lab6
# mixed_list = [1, 'hello', True, [1, 2, 3], {'key': 'value'}]
# mixed_list.append(3.14)
# mixed_list.append(False)
# mixed_list.pop()
# mixed_list.reverse()
# # mixed_list.sort()
# print(mixed_list)

# # lab7
# cart = []

# for i in range(5):
#     item = input("Enter an item to add to the cart: ")
#     cart.append(item)

# print("Items in your cart:")
# for item in cart:
#     print(f"- {item}")

# removed_item = cart.pop()

# print(f"Removed item: {removed_item}")
# print(f"You now have {len(cart)} items in your cart.")
# print(f"First item: {cart[0]}, Last item: {cart[-1]}")

# # lab8

# first_list = [1, 2, 3,]
# second_list = [4, 5, 6]
# third_list = [7, 8, 9]
# matrix = [first_list, second_list, third_list]
# second_column_in_first_row = matrix[0][1]
# second_row = matrix[1]
# diagonal = [matrix[i][i] for i in range(len(matrix))]
# first_column_elements_indexing = []
# for row in matrix:
#     first_column_elements_indexing.append(row[0])
# first_column_elements_comprehension = [row[0] for row in matrix]

# print(f"Second column in first row: {second_column_in_first_row}")
# print(f"Second row: {second_row}")
# print(f"Diagonal: {diagonal}")
# print(f"First column elements (indexing): {first_column_elements_indexing}")
# print(
#     f"First column elements (comprehension): {first_column_elements_comprehension}")

# # lab9
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# squared_numbers = [num ** 2 for num in numbers]
# even_numbers = [num for num in numbers if num % 2 == 0]
# doubled_numbers = [num * 2 for num in numbers]
# numbers_greater_than_five = [num for num in numbers if num > 5]
# numbers_as_strings = ['Number: ' + str(num) for num in numbers]

# print(f"Squared Numbers: {squared_numbers}")
# print(f"Even Numbers: {even_numbers}")
# print(f"Doubled Numbers: {doubled_numbers}")
# print(f"Numbers Greater Than Five: {numbers_greater_than_five}")
# print(f"Numbers as Strings: {numbers_as_strings}")

# # lab10

# name = input("Enter your name: ").strip()
# first_name = name.split(' ')[0].capitalize()
# last_name = name.split(' ')[-1].capitalize()
# full_name = first_name + ' ' + last_name
# age = int(input("Enter your age: ").strip())
# favourite_subject = input("Enter your favourite subject: ").strip()
# favourite_quote = input("Enter your favourite quote: ").strip()
# name_list = full_name.split()


# introduction = f"Hello, my name is {full_name}. I am {age} years old. My favourite subject is {favourite_subject}. My favourite quote is: \"{favourite_quote}\""
# print(introduction)
# print(f"First letter: {name[0]} and last letter: {name[-1]}")

students = []
for _ in range(int(input())):
    name = input("Enter student name: ").strip()
    score = float(input("Enter student score: ").strip())

    students.append((name, score))

scores = [s[1] for s in students]
sorted_students = sorted(students, key=lambda x: x[0])
min_score = min(scores)

second_lowest_scores = min([score for score in scores if score > min_score])

for student in students:
    if student[1] == second_lowest_scores:
        print(student[0])

# sorted_students = sorted(students, key=lambda x: x[1])

# for student in sorted_students:
#     print(f"Name: {student[0]}, Score: {student[1]}")
