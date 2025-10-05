class MenuItem:
    def __init__(self, name, price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


    def __str__(self):
        return f"{self.name}: {self.price}"
    

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menus = []
        self.customers = []


    def add_item(self,name, price, quantity):
        item = MenuItem(name, price, quantity)
        self.menus.append(item)


    def find_item(self,item_name):
        for item in self.menus:
            if item.name.lower() == item_name.lower():
                return item
        return None
    

    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item:
            self.menus.remove(item)
            print("Item deleted")
        else:
            print("Item not found")


    def add_customer(self, customer_id, name, email, address):
        customer = Customer(customer_id, name, email, address)
        self.customers.append(customer)

    def find_customar(self,customar_name):
        for customar in self.customers:
            if customar.name.lower() == customar_name.lower():
                return customar
                
        return None


    def remove_customar(self, customar_name):
        customar = self.find_customar(customar_name)
        if customar:
            self.menus.remove(customar)
            print("customar deleted")
        else:
            print("customar not found")


    def show_item(self):
        print("======= Menu =======")
        print("Name\tPrice\tQuantity")
        for item in self.menus:
            print(f"{item.name}\t{item.price}\t{item.quantity}")

    

class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.balance = 0
        self.orders = [] 


    def view_menu(self, restaurant):
        for item in restaurant.menus:
            print(item)


    def place_order(self, restaurant, item_name, quantity):
        for item in restaurant.menus:
            if item.name == item_name:
                total_cost = item.price * quantity
                if self.balance >= total_cost:
                    self.balance -= total_cost
                    self.orders.append((item, quantity))
                    print(f"Order placed: {quantity} x {item.name}, Total = {total_cost}")
                else:   
                    print("Insufficient balance!")
                return
        print("Item not found in menu.")


    def check_balance(self):
        print(f"Balance: {self.balance}")
        return self.balance

    def view_orders(self):
        if not self.orders:
            print("No past orders.")
        else:
            for item, qty in self.orders:
                print(f"{qty} x {item.name} = {item.price * qty}")

    def add_funds(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Added {amount}. New balance = {self.balance}")


class Admin:
    def __init__(self,name):
        self.name = name


    def add_menu_item(self, restaurant,name, price, quantity):
        restaurant.add_item(name, price, quantity)

    def remove_menu_item(self,restaurant, item_name):
        restaurant.remove_item(item_name)

    def updete_menu_item(self,restaurant, item_name, new_price):
        item = restaurant.find_item(item_name)
        if item:
            item.price = new_price
            print(f"Updete item name: {item_name} new price: {new_price}")
        else:
            print("Item not found")

    def add_customer(self, restaurant, name, email, address, balance=0):
        customer = Customer(name, email, address)
        customer.email = email
        customer.address = address
        customer.balance = balance
        restaurant.customers.append(customer)
        print(f"Customer {name} added with balance {balance}")


    def remove_customar(self,restaurant,customar_name):
        restaurant.remove_customar(customar_name)


    def view_customers(self, restaurant):
        if not restaurant.customers:
            print("No customers found.")
        else:
            print("======= Customers =======")
            for cust in restaurant.customers:
                print(f"Name: {cust.name}\n Email: {cust.email}\n Address: {cust.address}\n Balance: {cust.balance}")


MizanVai = Restaurant("Mizan Bhai's Hotel")

def login_customar():
    name = input(f"Enter Customar UserName: ")
    customar = MizanVai.find_customar(name)


    while True:
        print(f"------ {customar.name}-------")
        print("1. View Rastaurant Menu")
        print("2. View Balance")
        print("3. Add Balance")
        print("4. Place Order")
        print("5. View Order")
        print("6. Exit")


        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            customar.view_menu(MizanVai)
        elif choice == 2:
            customar.check_balance()
        elif choice == 3:
            balance = int(input("Enter Your Amount: "))
            customar.add_funds(balance)
        elif choice == 4:
            name = input("Enter Item Name: ")
            quantity = int(input("Enter Qnatity: "))
            customar.place_order(MizanVai,name, quantity)
        elif choice == 5:
            customar.view_orders()
        elif choice == 6:
            break
        else:
            print("Invalid Your input")


def admin_menu():
    admin_name = input("Enter Admin Name: ")

    admin = Admin(admin_name)


    while True:
        print(f"----- Welcom To Admin {admin.name} -----")
        print("1. Create Customer Account")
        print("2. Remove Customer Account")
        print("3. View All Customer")
        print("4. Add Restaurant Menu")
        print("5. Remove Restaurant Menu")
        print("6. Exit")

        choise = int(input("Enter Your choise: "))

        if choise == 1:
            name = input("Enter customer Name: ")
            email = input("Enter customer email: ")
            address = input("Enter customer Address: ")
            balance = int(input("Enter customer Balance: "))
            admin.add_customer(MizanVai,name,email,address,balance)
        elif choise == 2:
            name = input("Remove customer Name: ")
            admin.remove_customar(MizanVai,name)
        elif choise == 3:
            admin.view_customers(MizanVai)
        elif choise == 4:
            name = input("Enter Item Name: ")
            price = int(input("Enter Item Price: "))
            quantity = int(input("Enter item Quantity: "))
            admin.add_menu_item(MizanVai,name,price,quantity)
        elif choise == 5:
            name = input("Enter Item Name: ")
            admin.remove_menu_item(MizanVai,name)
        elif choise == 6:
            break
        else:
            print("Invalid Input")


while True:
    print("--- Restaurant Management system ---")
    print("1. Admin Login")
    print("2. Customer Login")
    print("3. Exit")


    choise = int(input("Enter Your Choise: "))

    if choise == 1:
        admin_menu()
    elif choise == 2:
        login_customar()
    elif choise == 3:
        break
    else:
        print("Invalid Input!!")
