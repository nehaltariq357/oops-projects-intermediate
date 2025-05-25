
class Student:
    def __init__(self,name,roll,marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def average(self):
        avg = sum(self.marks)/ len(self.marks)
        return avg
    
    def grade(self,avg):
        if avg >= 90:
            return "Grade A+"
        elif avg >= 80:
            return "Grade A"
        elif avg >= 70:
            return "Grade B"
        elif avg >= 60:
            return "Grade C"
        elif avg >= 50:
            return "Grade D"
        else:
            return "F"
    def show_report(self):
        avg = self.average()
        grade = self.grade(avg)
        print(f"Hello, {self.name} (Roll No: {self.roll}), your average is {avg:.2f}, so your grade is {grade}")



s1 = Student("Nehal",1,[80,90,78])
s1.show_report()
