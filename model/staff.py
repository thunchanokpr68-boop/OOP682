from model.staff import staff

class Staff:
    def __init__(self, pid, name, age, Staff_Id):
        super().__init__(pid, name, age, Staff_Id)
        self.Staff_Id = Staff_Id

    def __str__(self):
        return f"Staff: {self.pid}, {self.name}, {self.age}, ID: {self.Staff_Id}"