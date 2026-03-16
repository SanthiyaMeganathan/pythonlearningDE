#which is inside the class is kknow as method and out side class its function.

class Student:

    def say_hello(self):
        print("hello")

s1=Student()
s1.say_hello()
#s1.say-hello(s1)
#thats why we put s1 inside like when we call some function 
#python dont know who is calling the function so we have to tell python that s1 is calling the function so we put s1 inside the function. but when we call the function like s1.say_hello() python automatically put s1 inside the function so we dont have to put s1 inside the function.
