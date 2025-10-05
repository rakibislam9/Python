from abc import ABC
from order import Order
class User(ABC):
    def __init__(self, name, email, phone, addrese):
        self.name = name
        self.email = email
        self.phone = phone
        self.addrese = addrese



class Customer(User):
    def __init__(self, name, email, phone, addrese):
        super().__init__(name, email, phone, addrese)

        self.cart = Order()

    def view_menu(self, restaurent):
        restaurent.menu.show_menu()

    def add_to_cart(self, restaurent, item_name, quantity):
        item = restaurent.menu.find_item(item_name)
        # print(item.name)
        if item:
            if quantity > item.quantity:
                print("Item quantity exceeded")
            else:
                item.quantuty = quantity
                self.cart.add_item(item)
                print("Added item")
        else:
            print("item not found")

    def view_cart(self):
        print("** view cart **")
        print("Name\tprice\tQuantity")
        for item,quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
        print(f"Total Price: {self.cart.total_price}")

    def Pay_Bill(self):
        print(f"Toata {self.cart.total_price} Paid successful")
        self.cart.Clear()


class Employee(User):
    def __init__(self, name, email, phone, addrese, age, degination, salary):
        super().__init__(name, email, phone, addrese)
        self.age = age
        self.degination = degination
        self.salary = salary


class Admin(User):
    def __init__(self, name, email, phone, addrese):
        super().__init__(name, email, phone, addrese)
        

    def add_employees(self, restaurent, employee):
        restaurent.add_employee(employee)


    def view_employee(self, restaurent):
        restaurent.view_employee()

    
    def add_item(self,restaurent,item):
        restaurent.menu.add_menu(item)


    def item_remove(self,restaurent, item):
        restaurent.menu.item_remove(item)


    def view_manu(self, restaurent):
        restaurent.menu.show_manu()


