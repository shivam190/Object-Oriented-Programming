# Print Person detail using inheritance
class Person:
    def __init__(self,first,last):
        self.firstname = first
        self.lastname = last

    def name(self):
        return self.firstname + " " + self.lastname

class Employee(Person):
    def __init__(self,first,last,staffnum):
        Person.__init__(self,first,last)
        self.staffnumber = staffnum

    def getEmployee(self):
        return self.name() + ", " + self.staffnumber

x = Person("shivam", "singh")
y = Employee("shivam", "singh", "101")

print(x.name())
print(y.getEmployee())
        
