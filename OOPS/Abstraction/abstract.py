from abc import ABC,abstractmethod

"""
abstract class is a class which contains one or more abstract methods.
when a class is derived from an abstract class, then it is mandatory to override the abstract method in child class.
if we are not overriding the abstract method in child class then we will get an error.
"""

class manager(ABC):
    
#abstract class can also have non abstract methods.
#you should not create object for the abstract class , but you create object for the child class to access the abstract method and normal method in abstract class.    
    
    @abstractmethod
    def salary(self):
        print("we can implement the code in abstract method but we cant create object for abstract method to call the method because its an abstract method.")
        pass
    
    @abstractmethod
    def bonus(self):
        pass
    

    def leave(self):
        print("hi")
        pass
""" leave is a normal method and salary and bonus are abstract method.
we can create object for normal method but we cant create object for abstract method.
its not mandatory to override the normal method in child class but its mandatory to override the abstract method in child class."""    
    
class employee(manager):
    
    def salary(self):
        print("salary is 50000")
    
    def bonus(self):
        print("bonus is 5000")
"""If we are not overriding the all abstract method in child class then we will get an error. So we have to override all the abstract method in child class."""     

emp1 = employee()
emp1.salary()
emp1.bonus()
emp1.leave()