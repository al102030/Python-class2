from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, name, family, age, email):
        self.name = name
        self.family = family
        self.age = age
        self.email = email

    @abstractmethod
    def get_position(self):
        pass


class Student(User):
    def __init__(self, name, family, age, email):
        super().__init__(name, family, age, email)
        self.position = 'Student'

    def get_position(self):
        return self.position


class Teacher(User):
    def __init__(self, name, family, age, email):
        super().__init__(name, family, age, email)
        self.position = 'Teacher'

    def get_position(self):
        return self.position
