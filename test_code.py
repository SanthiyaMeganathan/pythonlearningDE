delivery_partner ="swiggy" #global variable

def hotel():

    item = "pizza" #enclosed variable

    def order_now():
        quantity =2 #local variable
        print(f"ordering {quantity} {item} from {delivery_partner}")
    order_now()

hotel() 


