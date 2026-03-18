from OOPS.INHERIT.inherit1 import son

class grandson(son):

    def software(self):
        print("I am from grandson class")

g1=grandson()
g1.house()
g1.factory()
g1.software()

#when you get bug after creating the child object then
#and you want to fix the buy , then create parent class object and call the methods in partent class.
#dont touch the child class code to fix the bug because it may create another bug in child class.
#so create parent class object and call the method in parent class to fix the bug.