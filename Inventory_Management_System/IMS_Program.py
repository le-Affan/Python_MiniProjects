# Objective : Build a console-based inventory system to manage products in stock using Python OOP.

# Features to Implement:
# Add new product (name, price, quantity)
# Update stock quantity
# Remove product
# View product details
# Show total products
# Exit


class InventoryManagement:
    product_count=0
    PID_seed=1000
    def __init__(self,name,price,quantity):
        InventoryManagement.product_count+=1
        InventoryManagement.PID_seed=InventoryManagement.PID_seed+1
        self.PID=InventoryManagement.PID_seed

        self.name=name
        self.price=price
        self.quantity=quantity
    def update_quantity(self,updated_quantity):
        self.quantity=updated_quantity
        print("Quantity successfully updated")

    def details(self):
        print(f"Product ID : {self.PID}\n"
              f"Product Name: {self.name}\n"
              f"Product Quantity : {self.quantity}\n"
              f"Product Price : {self.price}\n")

    @classmethod
    def prod_count(cls):
        print(f"There are a total of {InventoryManagement.product_count} products in the inventory")

products=[]

def PID_finder():
    while True:
        user_PID=int(input("Enter the Product ID of your product: "))
        found_PID=None
        for i in products:
            if i.PID==user_PID:
                print("Product Found")
                found_PID=i.PID
                return found_PID

        print(f"Product with ID {user_PID} not found. Please check the product ID and try again")



while True:
    print("\nWelcome to your inventory.\n"
          "What would you like to do today?\n"
          " \n"
          "1.Add new product\n"
          "2.Update stock quantity\n"
          "3.Remove product\n"
          "4.View product details\n"
          "5.Show total products\n"
          "6.Exit\n")
    try:
        choice = int(input("Enter Your Choice: "))
    except ValueError:
        print("please enter a valid choice")
        break

    if choice in [2,3,4] and len(products)==0:
        print("There are no products in the inventory")
        continue

    if choice==1:
        name=input("Enter Product Name: ")
        price=int(input("Enter Product Price: "))
        quantity=int(input("Enter Product Quantity: "))

        prod=InventoryManagement(name,price,quantity)
        products.append(prod)

    if choice==2:
        obj_PID=PID_finder()
        for i in products:
            if i.PID==obj_PID:
                updated_quantity = int(input("Enter new product quantity: "))
                i.update_quantity(updated_quantity)

    if choice==3:
        obj_PID=PID_finder()
        for i in products:
            if i.PID==obj_PID:
                products.remove(i)

    if choice==4:
        obj_PID=PID_finder()
        for i in products:
            if i.PID==obj_PID:
                i.details()

    if choice==5:
        InventoryManagement.prod_count()

    if choice==6:
        print("Have a great day!")
        break



















