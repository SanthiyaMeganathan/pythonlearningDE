"""
we can have access specifiers in python like public, private and protected but we dont have any keyword to declare the access specifier in python but we can use some symbols to declare the access specifier in python.

class->class
class->subclass
class->stranger class

public 
private ->_classname__methodname
protected ->__methodname

one underscore means protected and 
two underscore means private 
but we can access the private variable and method in python
by using _classname__methodname and _classname__variablename
but we cant access the private variable and method in other 
class because its a private variable and method.
"""

class Parent:
    
    def __init__(self):
        
        self.public="i am public"
        self._protected="i am protected"
        self.__private="i am private"
        
    def access_from_same_class(self):
        print("Accessing the public variable from same class:",self.public)
        print("Accessing the protected varibale from same class:" , self._protected)  
        print("Accessing the private varibale from same class:" ,self.__private) 
        
p = Parent()
p.access_from_same_class() 

print("*******************************************************************************************")       
        
        
class Child(Parent):
    
    def access_from_subclass(self):
        print("Accessing the public varauble from subclass:" ,self.public)
        print("Accessing the protected from the subclass:" ,self._protected)
        print("Accessing the private varible from subclass using the name mangling: ", self._Parent__private)
        # print("Accessing the private variable from subclass:" ,self.__private) 
        # # This will raise an AttributeError
        try:
            #we can access the private variable and methods in python
            # by using the _classname__mathodname its a name mangling 
            # but thats not recommended to access the private variable 
            # and method because its a private variable and method and 
            # it may create a bug in the code if we are accessing 
            # the private variable and method in other class because its a private variable and method.
            
            
            
            print("trying to access private varible from subclass:" , self.__private)
        except AttributeError:
            print("Cannot access private variable from subclass because it is private(attribute error)") 
            
c = Child()
c.access_from_subclass()

print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")


class Stranger:
    
    def access_from_stranger_class(self, obj):
        
        print("Accessing the public varibal from strangerclass" ,obj.public)
        print("Accessing the protected variable from stranger class: " , obj._protected) # but this is not recommended to
        #access the protected variable
        
        #accessing the private variable using name mangling in the stranger class
        """Not recommended to access the private variable and method in other class because its a private variable and method and it may create a bug in the code if we are accessing the private variable and method in other class because its a private variable and method."""
        
        print("Accessing the private variable using the name managling in the stranger class : ", obj._Parent__private)
        
        try:
            print("Accessing the private variable from stranger class: ", obj.__private)
            
        except AttributeError:
            print('Cannot access private variable from stranger class because it is private(attribute error)')    
        
        
s = Stranger()
s.access_from_stranger_class(p)
        
               
