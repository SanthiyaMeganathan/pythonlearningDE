age=12

if age >= 30:
    print("you are eligible for the discount")
else:
    print("you are not eligible for the discount")    


mark = int(input("enter your mark:  "))

if mark>=90:
    print("garde o")
if mark>=80:
    print("garde a")
else:
    print("grade b")    

#nested if else:

age = int(input("Enter your age: "))
has_license = input("DO YOU HAVE LICENSE(yes/no):  ")

if age>=18:
    print("hi")
    if has_license.lower()=="yes":
        print("you can drive")
    else:
        print("Go and take license")    
else:
    print("you are under age") 

#logical operator: and, or, not

your_mark= int(input("enter your mark:   "))
your_attendance = int(input("enter you attendance "))

if your_mark>=50 or your_attendance >=50:
    print("you are eligible for exam")
else:
    print("you are not eligible for the exam")    
              

