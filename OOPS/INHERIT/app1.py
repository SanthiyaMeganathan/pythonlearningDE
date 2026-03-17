class app1:
    def v1(self):
        print("orders")

class app2(app1):

    def v2(self):
        print("refund")  

    #over ridig

    def v1(self):
        print("cart")

#always create the child class object to access the parent class method and child class method
#override means same method name in two diffrent class..


a2=app2()
a2.v1()
a2.v2()              

