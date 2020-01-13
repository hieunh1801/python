class Employee:
    # doc string => display: Employee.__doc__
    'Common base class for all employees'

    # class variable => can share among all instance
    # access by: Employee.empCount
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" + Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name,  ", Salary: ", self.salary)


print(Employee.empCount)
emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print(Employee.empCount)

hasattr(emp1, 'name')    # Returns true if 'age' attribute exists
getattr(emp1, 'name')    # Returns value of 'age' attribute
setattr(emp1, 'name', 8)  # Set attribute 'age' at 8
delattr(emp1, 'name')    # Delete attribute 'age'

print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)
