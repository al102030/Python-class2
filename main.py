# import xml.dom.minidom

# domtree = xml.dom.minidom.parse('people.xml')

# group = domtree.documentElement

# people = group.getElementsByTagName("person")

# for person in people:
#     print(f"-- Person {person.getAttribute('id')} --")

#     name = person.getElementsByTagName('name')[0].childNodes[0].nodeValue
#     age = person.getElementsByTagName('age')[0].childNodes[0].nodeValue
#     weight = person.getElementsByTagName('weight')[0].childNodes[0].nodeValue
#     height = person.getElementsByTagName('height')[0].childNodes[0].nodeValue

#     print(f"Name: {name}")
#     print(f"Age: {age}")
#     print(f"Weight: {weight}")
#     print(f"Height: {height}")

#     people[0].getElementsByTagName('name')[0].childNodes[0].nodeValue
#     people.setAttribute("id", "200")
#     people.setAttribute("newAttr", "Hello")

#     domtree.writexml(open('people.xml', 'w'))


import xml.sax


class PeopleHandler(xml.sax.ContentHandler):

    def startElement(self, name, attrs):
        self.current = name
        if name == "person":
            print(f"-- Person {attrs['id']} --")

    def characters(self, content):
        if self.current == "name":
            self.name = content
        elif self.current == "age":
            self.age = content
        elif self.current == "weight":
            self.weight = content
        elif self.current == "height":
            self.height = content

    def endElement(self, name):
        if self.current == "name":
            print(f"Name: {self.name}")
        elif self.current == "age":
            print(f"Age: {self.age}")
        elif self.current == "weight":
            print(f"Weight: {self.weight}")
        elif self.current == "height":
            print(f"Height: {self.height}")
        self.current = ""


handler = PeopleHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('people.xml')

# import zipfile
# import csv
# import json
# import requests

# response = requests.get("https://www.google.com/")
# print(response)

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

# from abc import ABC, abstractmethod


# class Animal(ABC):
#     def __init__(self, name):
#         self.name = name

#     @abstractmethod
#     def sound(self):
#         pass

#     def info(self):
#         return f"I am an animal, and my name is {self.name}"


# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed

#     def sound(self):
#         return "HOOP!"

#     def info(self):
#         return f"I am a Dog, my name is {self.name}, and I am a {self.breed}"


# class Puppy(Dog):
#     def __init__(self, name, breed, age):
#         super().__init__(name, breed)
#         self.age = age

#     def info(self):
#         return f"I am a Puppy, my name is {self.name}, I am a {self.breed}, and I am {self.age} months old"


# class Pet(ABC):
#     def __init__(self, owner):
#         self.owner = owner

#     def pet_info(self):
#         return f"My owner is {self.owner}"


# class Cat(Animal, Pet):
#     def __init__(self, name, owner, color):
#         Animal.__init__(self, name)
#         Pet.__init__(self, owner)
#         self.color = color

#     def sound(self):
#         return "Meow!"

#     def info(self):
#         return f"I am a Cat, my name is {self.name}, my color is {self.color}, and my owner is {self.owner}"


# dog = Dog("Zombe", "German")
# puppy = Puppy("Max", "Husky", 6)
# cat = Cat("Garfield", "Ali", "Black")

# print(dog.sound())  # Output: HOOP!
# print(dog.info())  # Output: I am a Dog, my name is Zombe, and I am a German
# print(puppy.sound())  # Output: HOOP!
# # Output: I am a Puppy, my name is Max, I am a Husky, and I am 6 months old
# print(puppy.info())
# print(cat.sound())  # Output: Meow!
# # Output: I am a Cat, my name is Garfield, my color is Black, and my owner is Ali
# print(cat.info())


# class Solution:
#     def __init__(self, olst=[]):
#         self.olst = olst

#     def generate(self, numRows: int):
#         if len(self.olst) < numRows:
#             if len(self.olst) == 0:
#                 self.olst.append([1])
#             if numRows == 1:
#                 pass
#             else:
#                 self.olst.append([self.olst[-1][i] + self.olst[-1][i+1]
#                                   for i in range((len(self.olst))-1)])
#                 self.olst[-1].insert(0, 1)
#                 self.olst[-1].append(1)
#                 self.generate(numRows)
#         return self.olst


# solution = Solution()
# print(solution.generate(4))


# json_data = "YOUR_JSON_TEXT"

# data = json.loads(json_data)

# json_filename = 'data.json'
# with open(json_filename, 'w', encoding='utf-8') as json_file:
#     json.dump(data, json_file, indent=4)

# csv_filename = 'data.csv'
# with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
#     csv_writer = csv.writer(csv_file)
#     csv_writer.writerows(data)

# zip_filename = 'data_files.zip'
# with zipfile.ZipFile(zip_filename, 'w') as zip_file:
#     zip_file.write(json_filename)
#     zip_file.write(csv_filename)
