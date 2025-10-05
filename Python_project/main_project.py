from food_item import Fooditem
from menu import Menu
from restaurent import Restaurent
from Restsurent_Manegement_system import Customer, Employee, Admin
from order import Order


Hati_mamar = Restaurent("Hati Mamar Restaurent")

def customer_menu():
    name = input("Enter Your Name: ")
    email = input("Enter Your Email: ")
    phone = input("Enter Your Phone: ")
    addrese = input("Enter Your Addrese: ")
    
    customer = Customer(name=name, email=email, phone=phone,addrese=addrese)


    while True:
        print(f"Welcome To {customer.name}")
        print("1. View Menu")
        print("2. Add Item To cart")
        print("3. view cart")
        print("4. PayBill")
        print("5. Exit")

        Choice = int(input("Enter Your choice: "))

        if Choice == 1:
            customer.view_menu(Hati_mamar)
        elif Choice == 2:
            item_name = input("Enter Item Namw: ")
            item_quantity = int(input("Enter Item Quantity: "))

            customer.add_to_cart(Hati_mamar, item_name, item_quantity)
        elif Choice == 3:
            customer.view_cart()
        elif Choice == 4:
            customer.Pay_Bill()
        elif Choice == 5:
            break
        else:
            print("Invalid Input!")



def admin_menu():
    name = input("Enter Your Name: ")
    email = input("Enter Your Email: ")
    phone = input("Enter Your Phone: ")
    addrese = input("Enter Your Addrese: ")
    
    admin = Admin(name=name, email=email, phone=phone,addrese=addrese)

    while True:
            print(f"Welcome To {admin.name}")
            print("1. Add new item")
            print("2. Add New Employee")
            print("3. view Employee")
            print("4. View Item")
            print("5. Delete Item")
            print("6. Exit")

            Choice = int(input("Enter Your choice: "))

            if Choice == 1:
                item_name = input("Enter Item Name: ")
                item_price = int(input("Enter Item Price: "))
                item_quantity = int(input("Enter item quantity: "))
                item = Fooditem(item_name, item_price, item_quantity)
                admin.add_item(Hati_mamar, item)
            elif Choice == 2:
                name = input("Enter Employee Name: ")
                email = input("Enter Employee Email: ")
                phone = input("Enter Employee Phone: ")
                age = input("Enter Employee AGE: ")
                addrese = input("Enter Employee Addrese: ")
                degination = input("Enter Employee Degination: ")
                salary = input("Enter Employee Salary: ")
                employee = Employee(name, email, phone, addrese, age, degination, salary)
                admin.add_employees(Hati_mamar,employee)

            elif Choice == 3:
                admin.view_employee(Hati_mamar)
            elif Choice == 4:
                admin.view_manu(Hati_mamar)
            elif Choice == 5:
                item_name = input("Enter item Name: ")
                admin.item_remove(Hati_mamar,item_name)
            elif Choice == 6:
                break
            else:
                print("Invalid Input!")



while True:
    print("Welcome!!")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")

    Choice = int(input("Enter Your Choice: "))

    if Choice == 1:
        customer_menu()
    elif Choice == 2:
        admin_menu()
    elif Choice == 3:
        break
    else:
        print("Invalid Input!!")