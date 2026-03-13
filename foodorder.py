order_amount=int(input("Enter the order amount: "))
day_of_week=input("Enter the day of the week: ")
membership=input("Are you a member?(yes/no):  ")


if(order_amount>=1000 and day_of_week in['sat','sun']) or membership.lower()=='yes':
    print("you are eligible for discount")
else:
    print("you are not eligible for the discount")    
