amount =1200
#gst 18%
tax = 0.18*amount
total_amount = amount + tax

print(total_amount)

if total_amount > 1000:
    discount = total_amount *0.10
    total_amount -=discount

print(total_amount)