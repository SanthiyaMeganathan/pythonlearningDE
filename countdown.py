count=5

while(count>0):
    print(f"countdown is {count}")
    count -=1

print("Time is up! ")

#cart funtionality of the e-commerce website

items=[]

while True:
    item=input("Enter the item to put in cart and if done enter done ." )
    if item.lower()=='done':
        break
    items.append(item)
print("your cart items are: ", items)    
