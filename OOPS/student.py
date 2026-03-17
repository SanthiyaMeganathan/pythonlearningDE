#which is inside the class is kknow as method and out side class its function.

class Student:
    

    def say_hello(self, name):
        print("hello" , name)

s1=Student()
s1.say_hello("haritha")

#this is normal function , here we pass the argument in function
#but when we create the constructor in the class , we will pass the arguements in the class itself.
#s1.say-hello(s1)
#thats why we put s1 inside like when we call some function 
#python dont know who is calling the function so we have to tell python that s1 is calling the function so we put s1 inside the function. but when we call the function like s1.say_hello() python automatically put s1 inside the function so we dont have to put s1 inside the function.
#when you dont have self there , it will show error like , its sending one positional argument but it is expecting 0 positional argument because we are not telling python that s1 is calling the function. so we have to put self inside the function to tell python that s1 is calling the function.


s2=Student()
s3=Student()
