from OOPS.INHERIT.inherit1 import son

class grandson(son):

    def software(self):
        print("I am from grandson class")

g1=grandson()
g1.house()
g1.factory()
g1.software()