#no condition and predict number of times it run

names=["don","din","jhon"]

for name in names:
    print(name)
    print("welcome to the party")

#while
correct_pin='12345'
entered_pin=''
#we dont know how many times loops and we have condition

while entered_pin != correct_pin:
    entered_pin =input("enter the pin:   ")

print("you have entered the correct pin")   

#break
#we use it to stop loop once the condition satisfies

for i in range(10):
    if i==5:
        break 
    print(i)

#continue->to skip


nums=[10,12,56,89,-1]

for n in nums:
    if n<0:
        continue
    print(n)


#placeholder for future code

for i in range(5):
    pass # future code will come here




    


