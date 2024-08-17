# def calculate_grade(*numbers):
#     name = input("Please enter your name:")
#     total, count = 0, 0
#     message = ""
#     print(numbers)
#     for num in numbers:
#         total += num
#         count += 1
#     grade = total / count
#     if 18 <= grade <= 20:
#         message = f"Dear {name}, your grade ({grade}) is A"
#     elif 14 <= grade < 18:
#         message = f"Dear {name}, your grade ({grade}) is B"
#     else:
#         message = f"Dear {name}, your grade ({grade}) is C"

#     return message


# print("Start")
# print(calculate_grade(14, 18, 20, 20, 19, 20))

# def fizz_buzz():
#     for i in range(1, 101):
#         if i == 3 or i == 5:
#             print("Prime")
#         elif i % 2 == 0:
#             print("Even")
#         elif i % 15 == 0:
#             print("FizzBuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print("Prime")


# fizz_buzz()

def calculate_square(number):
    return [item**2 for item in range(1, number+1) if item % 2 == 0]


print(calculate_square(14))
