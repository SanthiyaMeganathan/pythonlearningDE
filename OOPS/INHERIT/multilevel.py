class garndpa:
    
    def car(self):
        print("red car")      

class dad(garndpa):
    
    def bike(self):
        print("black bike")
    
    
class son1(dad): 
    
    def house(self):
        print("white house")
        
"""heirarchy inheritance means one parent class and more than one child class."""        
        
class son2(dad):
    
    def market(self):
        print("i have orange market")            


s1=son1()
s1.car()
s1.bike()
s1.house()

s2=son2()
s2.car()
s2.bike()
s2.market()


