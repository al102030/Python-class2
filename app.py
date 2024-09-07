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

# =================================================================
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

# def calculate_square(number):
#     return [item**2 for item in range(1, number+1) if item % 2 == 0]


# print(calculate_square(14))
# ========================================================================

# my_text = "This is a common interview question"


# def char_frequency(text):
#     my_dict = {}
#     for char in text:
#         if char in my_dict:
#             my_dict[char] += 1
#         else:
#             my_dict[char] = 1
#     my_dict_sorted = sorted(my_dict.items(),
#                             key=lambda kv: kv[1],
#                             reverse=True)
#     return my_dict_sorted[0]


# print(char_frequency(my_text))

# ==================================================

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass

    def info(self):
        return f"I am an animal, and my name is {self.name}"


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        return "HOOP!"

    def info(self):
        return f"I am a Dog, my name is {self.name}, and I am a {self.breed}"


class Puppy(Dog):
    def __init__(self, name, breed, age):
        super().__init__(name, breed)
        self.age = age

    def info(self):
        return f"I am a Puppy, my name is {self.name}, I am a {self.breed}, and I am {self.age} months old"


class Pet(ABC):
    def __init__(self, owner):
        self.owner = owner

    def pet_info(self):
        return f"My owner is {self.owner}"


class Cat(Animal, Pet):
    def __init__(self, name, owner, color):
        Animal.__init__(self, name)
        Pet.__init__(self, owner)
        self.color = color

    def sound(self):
        return "Meow!"

    def info(self):
        return f"I am a Cat, my name is {self.name}, my color is {self.color}, and my owner is {self.owner}"


dog = Dog("Zombe", "German")
puppy = Puppy("Max", "Husky", 6)
cat = Cat("Garfield", "Ali", "Black")

print(dog.sound())  # Output: HOOP!
print(dog.info())  # Output: I am a Dog, my name is Zombe, and I am a German
print(puppy.sound())  # Output: HOOP!
# Output: I am a Puppy, my name is Max, I am a Husky, and I am 6 months old
print(puppy.info())
print(cat.sound())  # Output: Meow!
# Output: I am a Cat, my name is Garfield, my color is Black, and my owner is Ali
print(cat.info())
