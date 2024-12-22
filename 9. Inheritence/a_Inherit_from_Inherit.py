"""

Design the following code:

     _____________________
     |                   |
     |      Person       |                                                                   _____________________
     |___________________|                                                                   |                   |
     |                   |                                                                   |       Admin       |
     |-- firstName       |<------------------------------------------------------------------|___________________|
     |-- lastName        |                                                                   |                   |
     |___________________|                                                                   |-- joiningYear     |
     |                   |                                                                   |___________________|
     |+ display()        |                                                                   |                   |
     |___________________|<----------------------------------------                          |+ display()        |
               ^                                                  |                          |___________________|
               |                                                  |                                     ^
     __________|__________                               _________|___________                          |
     |                   |                               |                   |                          |
     |      Student      |                               |      Teacher      |                          |
     |___________________|                               |___________________|                          |
     |                   |                               |                   |                          |
     |-- graduationYear  |                               |-- joiningYear     |               _____________________
     |___________________|                               |___________________|               |                   |
     |                   |                               |                   |               |     Employee      |
     |+ display()        |                               |+ display()        |<--------------|___________________|
     |___________________|<-------------------           |___________________|               |                   |
               ^                             |                                               |-- id              |
               |                             |                                               |___________________|
     __________|__________         __________|__________                                     |                   |
     |                   |         |                   |                                     |+ display()        |
     |     Alumni        |         | CurrentStudent    |                                     |___________________|
     |___________________|         |___________________|
     |                   |         |                   |
     |-- passingYear     |         |-- currentSemester |
     |___________________|         |___________________|
     |                   |         |                   |
     |+ display()        |         |+ display()        |
     |___________________|         |___________________|

"""

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def display(self):
        return f"Name: {self.first_name} {self.last_name}"


class Student(Person):
    def __init__(self, first_name, last_name, graduation_year):
        super().__init__(first_name, last_name)
        self.graduation_year = graduation_year

    def display(self):
        return f"{super().display()}, Graduation Year: {self.graduation_year}"


class Alumni(Student):
    def __init__(self, first_name, last_name, graduation_year, passing_year):
        super().__init__(first_name, last_name, graduation_year)
        self.passing_year = passing_year

    def display(self):
        return f"{super().display()}, Passing Year: {self.passing_year}"


class CurrentStudent(Student):
    def __init__(self, first_name, last_name, graduation_year, current_semester):
        super().__init__(first_name, last_name, graduation_year)
        self.current_semester = current_semester

    def display(self):
        return f"{super().display()}, Current Semester: {self.current_semester}"


class Employee(Person):
    def __init__(self, first_name, last_name, emp_id):
        super().__init__(first_name, last_name)
        self.emp_id = emp_id

    def display(self):
        return f"{super().display()}, Employee ID: {self.emp_id}"


class Teacher(Employee):
    def __init__(self, first_name, last_name, emp_id, joining_year):
        super().__init__(first_name, last_name, emp_id)
        self.joining_year = joining_year

    def display(self):
        return f"{super().display()}, Joining Year: {self.joining_year}"


class Admin(Employee):
    def __init__(self, first_name, last_name, emp_id, joining_year):
        super().__init__(first_name, last_name, emp_id)
        self.joining_year = joining_year

    def display(self):
        return f"{super().display()}, Joining Year: {self.joining_year}"


# Example Usage
person = Person("John", "Doe")
student = Student("Alice", "Smith", 2024)
alumni = Alumni("Bob", "Brown", 2020, 2021)
current_student = CurrentStudent("Cathy", "Davis", 2025, "6th")
teacher = Teacher("David", "Evans", 1234, 2018)
admin = Admin("Emily", "Clark", 5678, 2015)

print(person.display())
print(student.display())
print(alumni.display())
print(current_student.display())
print(teacher.display())
print(admin.display())
