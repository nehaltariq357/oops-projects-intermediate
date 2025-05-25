

class Student:
    student_count = 0

    def __init__(self,name,roll):
        self.name = name
        self.roll = roll

        Student.student_count +=1

    def show_info(self):
        print(f"Name: {self.name}, Roll No: {self.roll}")

    @staticmethod
    def show_total_student():
        print(f"Total Registered Students: {Student.student_count}")



s1 = Student("Nehal", 1)
s2 = Student("Ali", 2)
s3 = Student("hamza", 3)

Student.show_total_student()