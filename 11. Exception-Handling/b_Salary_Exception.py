"""
Create a custom exception named SalaryNotInRange if salary is less than 10,000 and greater than 50,000

     _____________________
     |                   |
     |     Rectangle     |
     |___________________|
     |                   |
     |+ name             |
     |+ salary           |
     |___________________|
     |                   |
     |+ displaySalary()  |
     |___________________|

"""

class SalaryNotInRange(Exception):
    def __init__(self, salary):
        super().__init__(f"Salary {salary} is not in the range of 10,000 to 50,000")


class Rectangle:
    def __init__(self, name, salary):
        self.name = name
        if not (10000 <= salary <= 50000):
            raise SalaryNotInRange(salary)
        self.salary = salary

    def displaySalary(self):
        print(f"Name: {self.name}, Salary: {self.salary}")


try:
    emp = Rectangle("John", 60000)  # Will raise exception
    emp.displaySalary()
except SalaryNotInRange as e:
    print(e)
