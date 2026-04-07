class Parent:
    
    def public(self):
        print("This is a public method")
    
    def _protected(self):
        print("This is a protected method")
    
    def __private(self):
        print("This is a private method")
    
    def access_from_same_class(self):
        self.public()
        self._protected()
        self.__private()
        
class Child(Parent):
    
    def access_from_child_class(self):
        self.public()
        self._protected()
        # self.__private()  # This will raise an AttributeError


parent = Parent()
parent.public()  # This will work
parent._protected()  # This will work, but it's not recommended
parent.__private()  # This will raise an AttributeError   

c = Child()
c.access_from_child_class()  # This will call the public and protected methods, but not the private method
                         