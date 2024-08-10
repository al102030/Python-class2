def calculate_grade(*numbers):
    name = input("Please enter your name:")
    total, count = 0, 0
    message = ""
    print(numbers)
    for num in numbers:
        total += num
        count += 1
    grade = total / count
    if 18 <= grade <= 20:
        message = f"Dear {name}, your grade ({grade}) is A"
    elif 14 <= grade < 18:
        message = f"Dear {name}, your grade ({grade}) is B"
    else:
        message = f"Dear {name}, your grade ({grade}) is C"

    return message


print("Start")
print(calculate_grade(14, 18, 20, 20, 19, 20))
