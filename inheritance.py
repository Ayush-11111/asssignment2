class Person:

    def __init__(self, name):
        self.name = name

    def show(self):
        print("Name :", self.name)

class Student(Person):

    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll

    def display(self):
        self.show()
        print("Roll No :", self.roll)

s = Student("Ram", 35)

s.display()