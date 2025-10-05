from menu import Menu

class Restaurent:
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.menu = Menu() 


    def add_employee(self, employee):
        self.employees.append(employee)

    def view_employee(self):
        print("\nView All Employee")
        for emp in self.employees:
            print(f"\nName: {emp.name}\nEmail: {emp.email}\nPhone: {emp.phone}\nAddrese: {emp.addrese}\nAge: {emp.age}\nDegination: {emp.degination}\nSalary: {emp.salary}")


