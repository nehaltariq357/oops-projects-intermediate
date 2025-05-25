#create student class that takes name and marks of 3 subjects as arguments in constructor.
#then create a method to print the average.


class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks


    def average(self):
        sum = 0
        for val in self.marks:
            sum +=val
        print(f"hi {self.name} your avg score is {sum/3}")
    @staticmethod
    def hello():
        print("hello")


s1 = student("Nehal",[95,90,92])
s1.average()
s1.hello()