# class Student :
#     name = "Nehal"

# s1 = Student()
# print(s1.name)
# s2 = Student()
# print(s2.name)

# class Car:
#     color = "blue"
#     brand = "mercedes"

# car1 = Car()
# print(car1.color)
# print(car1.brand)


class Student:
    #name = "Nehal"
    def __init__(self,fullname,marks):
        self.name = fullname
        self.marks = marks
        print(self)
        print("adding new student in DataBase!")

    def welcome(self):
        print("welcome student")
s1 = Student("nehal",90)
s1.welcome()

