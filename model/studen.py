from model.studen import Student

class Student:
    def __init__(self, name, age, grade, Student_Id):
        super().__init__(name, age, grade, Student_Id)
        self.Student_Id = Student_Id

    def __str__(self):
        return f"Student: {self.name}, {self.age},  {self.grade}, {self.Student_Id}"