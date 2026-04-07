class order:
    
    def __init__(self,customer_name, items, tot_amount, discount):
        
        self.customer_name = customer_name
        self.items=items
        self.__tot_amount=tot_amount
        self.__discount=discount
        
    def __calculate_final_amount(self): #private
        return self.__tot_amount- self.__discount
    
    def _get_admin_view(self): #protected
        return{
            "customer_name": self.customer_name,
            "items": self.items,
            "total_amount": self.__tot_amount,
            "discount": self.__discount,
            "final_amount": self.__calculate_final_amount()
            
        }
    
    def get_customer_view(self):
        return{
            
            "customer_name":self.customer_name,
            "items": self.items,
            "final_amount":self.__calculate_final_amount()
        } 
            
#creating an seperate class:

class AdminPortal:
    
    def show_order(self, order):
        admin_view = order._get_admin_view()
        print("Admin View")
        print(admin_view)
        return admin_view
    
class CustomerPortal:
    
    def show_order(self,order):
        return order.get_customer_view()   
    
    
order = order("John Doe", ["item1", "item2"], 100, 10)


admin = AdminPortal()
customer = CustomerPortal()

print("Admin Portal:")
print(admin.show_order(order))

print("\nCustomer Portal:")
print(customer.show_order(order))     