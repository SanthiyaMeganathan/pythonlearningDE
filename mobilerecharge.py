recharge_amount=int(input("Enter the recharge amount: "))
data_balance=int(input("Enter the data balance in GB: "))

if recharge_amount >=399 or data_balance >=1.5:
    print("You are eligible unlimited data")
else:
    print("your not eligible ")    
