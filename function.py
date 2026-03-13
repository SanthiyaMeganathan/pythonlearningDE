#functions are reusable code.

def greet():
    print("welcome to the party")
greet()


#function with parameter

def greetName(name):
    print(f"Welcome to the party {name} come to party")
    
greetName("shalini")



#having more argument!
def add(a,b):
    print(a+b)
add(2,3)


#return , we use return when we want to give what value we get to some other function or varible 
def sum(a,b):
    return(a+b)

result=sum(5,3)
print(result)


def sub(a,b):
    print(a-b)

result2=sub(5,3)    
print(result2) #it will give none because we are not returning anything in sub function 

