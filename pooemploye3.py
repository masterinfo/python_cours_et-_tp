from sys import stdout
from sys import stdin


class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)

"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)

emp1.displayCount()
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % Employee.empCount)


emp1.age = 15  # Modify 'age' attribute.
print(emp1.age)
print(emp1.__dict__)
print(emp2.__dict__)
print("---------------------------------------------------------------------------")
print(hasattr(emp1, 'age'))    # Returns true if 'age' attribute exists
print(getattr(emp1, 'age') )   # Returns value of 'age' attribute
setattr(emp1, 'age', 8) # Set attribute 'age' at 8
print(emp1.age)
delattr(emp1, 'age')    # Delete attribute 'age'
print(emp1.__dict__)
"print(emp1.age)"

print(dir(emp1))