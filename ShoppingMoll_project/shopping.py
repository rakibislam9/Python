class Shopping:
    def __init__(self, name):
        self.name = name
        self.sellers = []


class Seller:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.products = []

    def seller_account(self, name, email, password):
        return Seller(name, email, password)

    def add_product(self, item_name, price, quantity):
        product = {"name": item_name, "price": price, "quantity": quantity}
        self.products.append(product)

    def find_product(self, item_name):
        for item in self.products:
            if item["name"] == item_name:
                return item
        return None

    def stock_product(self):
        return len(self.products)


class Customer:
    def __init__(self, name, email, address, password):
        self.name = name
        self.email = email
        self.address = address
        self.password = password
        self.balance = 0
        self.customers = []
        self.orders = []

    def customer_account(self, name, email, address, password):
        self.customers.append((name, email, address, password))

    def view_product(self, seller):
        print("===== Product Menu =====")
        print("Name\tPrice\tQuantity")
        for pro in seller.products:
            print(f"{pro['name']}\t{pro['price']}\t{pro['quantity']}")

    def order_place(self, seller, item_name, quantity):
        for item in seller.products:
            if item["name"] == item_name:
                total_cost = item["price"] * quantity
                if self.balance >= total_cost and item["quantity"] >= quantity:
                    self.balance -= total_cost
                    self.orders.append((item_name, quantity))
                    item["quantity"] -= quantity
                    print(f"✅ Order placed: {item_name} x{quantity}")
                else:
                    print("❌ Not enough balance or stock!")
                return
        print("❌ Product not found!")

    def stock_out(self, seller):
        print("===== Stock Status =====")
        for item in seller.products:
            print(f"{item['name']} -> In stock: {item['quantity']}")

    def add_amount(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"💰 Balance updated: {self.balance}")


# ---------- Functions ----------

def seller_account():
    print("===== Seller =====")
    name = input("Enter Your Name: ")
    email = input("Enter Your Email: ")
    password = input("Enter Your Password: ")

    seller = Seller(name, email, password)

    while True:
        print(f"\n----- {seller.name} -----")
        print("1. Create Seller Account")
        print("2. Add Product")
        print("3. Exit")

        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            name = input("Enter Your Name: ")
            email = input("Enter Your Email: ")
            password = input("Enter Your Password: ")
            new_seller = seller.seller_account(name, email, password)
            print(f"✅ Seller account created for {new_seller.name}")
        elif choice == 2:
            item_name = input("Enter Item Name: ")
            price = int(input("Enter Item Price: "))
            quantity = int(input("Enter Item Quantity: "))
            seller.add_product(item_name, price, quantity)
            print("✅ Product added successfully!")
        elif choice == 3:
            return seller
        else:
            print("❌ Invalid Input!!")


def customer_account(seller):
    print("----- Customer -------")
    name = input("Enter Your Name: ")
    email = input("Enter Your Email: ")
    address = input("Enter Your Address: ")
    password = input("Enter Your Password: ")

    customer = Customer(name, email, address, password)

    while True:
        print(f"\n===== {customer.name} =====")
        print("1. Create Customer Account")
        print("2. View Product")
        print("3. Order Place")
        print("4. Check Stock Product")
        print("5. Add Funds")
        print("6. Exit")

        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            customer.customer_account(name, email, address, password)
            print("✅ Customer account created!")
        elif choice == 2:
            customer.view_product(seller)
        elif choice == 3:
            item_name = input("Enter Product Name: ")
            quantity = int(input("Enter Quantity: "))
            customer.order_place(seller, item_name, quantity)
        elif choice == 4:
            customer.stock_out(seller)
        elif choice == 5:
            amount = int(input("Enter Your Amount: "))
            customer.add_amount(amount)
        elif choice == 6:
            break
        else:
            print("❌ Invalid Input!!")


# ---------- Main Program ----------

shopping = Shopping("Jomuna Future Park")
main_seller = None

while True:
    print("\n===== Shopping Mall =====")
    print("1. Seller Account")
    print("2. Customer Account")
    print("3. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        main_seller = seller_account()
    elif choice == 2:
        if main_seller:
            customer_account(main_seller)
        else:
            print("❌ No seller exists. Please create seller first!")
    elif choice == 3:
        break
    else:
        print("❌ Invalid Input!!")
