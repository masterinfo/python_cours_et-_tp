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

    @classmethod
    def displayCount2(cls):
        print(" je suis une methode classe  et le nb total d'Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)

"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)

emp1.displayCount()
emp1.displayEmployee()
emp2.displayEmployee()
print("**************************************************")
print( emp1.empCount)
emp1.empCount=3    #"?????"
print( emp1.empCount)
print("**************************************************")
Employee.displayCount2()

print("Total Employee %d" % Employee.empCount)