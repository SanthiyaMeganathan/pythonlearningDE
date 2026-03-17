class Employee:
    def __init__(self,AadharNo,AadharName,AadharAddress):
        self.AadharNo=AadharNo
        self.AadharName=AadharName
        self.AadharAddress=AadharAddress


    def displayName(self):
        print(f"Aadhar name is {self.AadharName}") 

    def displayAddress(self):
        print(f"Aadhar address is {self.AadharAddress}")  

    def displayAadharNo(self):
        print(f"Aadhar number is {self.AadharNo}")


emp1 = Employee("12344e5678","shalini","ambur")
emp1.displayName()
emp1.displayAddress()
emp1.displayAadharNo()