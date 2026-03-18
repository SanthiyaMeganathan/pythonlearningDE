class mom:
    
    def car(self):
        print("red car")      

class dad:
    
    def bike(self):
        print("black bike")
    
    
"""multiple inheritance means more than one parent class and one child class."""    
    
class son1(dad,mom): 
    
    def house(self):
        print("white house")
        
s1=son1()
s1.car()
s1.bike()
s1.house()


"""

multilvel:
a
b(a)
c(b)

muliple:
a
b
c(a,b)

hybrid:
a
b(a)
c(a,b)

using two or more types of inheritance in a single program is called hybrid inheritance.
"""        