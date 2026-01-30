class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"{self.name} is {self.age} years old.")

    def __str__(self):
        return f"{self.name} is {self.age} years old."

def main():
    dog1 = Dog("Buddy", 3)
    your_dog = Dog("Max", 5)
    print(your_dog)

if __name__ == "__main__":
    main()

class Student:
    def __init__(self, name, age, grade, Student_Id):
        self.name = name
        self.age = age
        self.grade = grade
        self.Student_Id = Student_Id

class Staff:
    def __init__(self, pid, name, age, Staff_Id):
        self.pid = pid
        self.name = name
        self.age = age
        self.Staff_Id = Staff_Id

class StudentPerson(Student):
    def __init__(self, name, age, grade, Student_Id):
        super().__init__(name, age, grade, Student_Id)

class StaffPerson(Staff):
    def __init__(self, pid, name, age, Staff_Id):
        super().__init__(pid, name, age, Staff_Id)

def main():
    Student = StudentPerson("Alice", 20, "A", "1234567890123")
    Staff = StaffPerson("9876543210987", "Bob", 35, "S1")
    print(f"Student: {Student.name}, Age: {Student.age}, Grade: {Student.grade}, ID: {Student.Student_Id}")
    print(f"Staff: {Staff.name}, Age: {Staff.age}, ID: {Staff.Staff_Id}") 

def get_person_info(person):
    

get_person_info(Student)
get_person_info(Staff)
