"""polymorphism means many forms, it is a feature of OOPS, it allows us to use the same method name in different classes and it will perform different tasks based on the class it is called from.

method overridering happens in two diffrent classes with same method name and same number of parameters but different implementation.

there is no method overloading
method overloading means same method name with different number of parameters in the same class but python does not support method overloading but we can achieve method overloading by using default arguments.

"""

class dad:
    
    def house(self):
        print("red")


class son(dad):
    
    """method overriding means same method name in two diffrent classes with same number of parameters but different implementation."""
    
    def house(self):
        print("white")  
        
s1=son()
s1.house()                