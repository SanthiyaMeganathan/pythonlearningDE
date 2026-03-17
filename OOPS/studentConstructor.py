#constrctor
# in constrctor we pass the arguments in the class itself instead of passing in function
#then if we passes the value in the constructor then we can access that value in the function by using self keyword 
#you will have constrctor when you want to use the same value in multiple functions in the class then you can use constructor to store that value and then you can access that value in multiple functions by using self keyword

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def say_hello(self):
        print("hello", self.name)    

s1=Student("haritha",20)
s1.say_hello()        
