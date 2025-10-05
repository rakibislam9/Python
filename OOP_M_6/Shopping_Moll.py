class Product:
    def __init__(self, name,price):
        self.name = name 
        self.price = price
        
              
class Shope:
    def __init__(self, Shope_name):
        self.Shope_name = Shope_name
        self.menu = []
        
    def add_product(self,item):
        self.menu.append(item)
        print(f'{item.name} add_to {self.Shope_name}')


    def buy_product(self,product_name):
        for prod in self.menu:
            if prod.name == product_name:
                self.menu.remove(prod)
                print(f"Congaatulation! you purchess {prod.price} TK")
                return
        print("Sorry! Your product is not available")



# -------------------------
# Example usage
# -------------------------
p1 = Product("Laptop", 50000)
p2 = Product("Mobile", 15000)
p3 = Product("Headphone", 2000)

shop = Shope("Rakib's Tech Store")

shop.add_product(p1)
shop.add_product(p2)
shop.add_product(p3)

# Trying to buy products
shop.buy_product("Mobile")      # Available
shop.buy_product("Camera")      # Not Available
shop.buy_product("Headphone")   # Available