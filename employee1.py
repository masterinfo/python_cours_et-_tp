class Employee:
    ' Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee : %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    'a static method needs no specific parameters'
    @staticmethod
    def displayCount3():
        print(" je suis une methode static  et  le nb total d'Employee %d" % Employee.empCount)

    'A class method takes cls as first parameter'
    @classmethod
    def displayCount2(cls):
        print(" je suis une methode classe  et  le nb total d'Employee %d" % Employee.empCount)

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)

"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)

emp1.displayCount()
emp1.displayEmployee()
emp2.displayEmployee()
print("****************************")
print("Total Employee %d" % Employee.empCount)
print("****************************")
Employee.displayCount2( )
Employee.displayCount3()

"""Class method vs Static Method

When to use what?

    We generally use class method to create factory methods. Factory methods return class object ( similar to a constructor ) for different use cases.
    We generally use static methods to create utility functions.
"""
print("---------------------------------")
print(dir(emp1))