class phone:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
        
    
    def call(self):
        pass




samsung = phone('samsung', 15000)

iphone = phone('iphone', 15000000)


print(samsung.brand)

print(iphone.brand)
print(iphone.price)