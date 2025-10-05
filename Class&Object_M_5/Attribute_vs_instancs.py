
#class attribute
class shope:
    cart = []


    def __init__(self, buyer):
        self.buyer = buyer

       
    def add_to_cart(self, product):
        self.cart.append(product) 


Rakib = shope("Rakib")
Rakib.add_to_cart('shoes')
Rakib.add_to_cart('shirt')

print("After Rakib added:",Rakib.cart)


Robin = shope("Robin")
Robin.add_to_cart('cap')
Robin.add_to_cart('watch')

print('After added Robin:',Robin.cart)



# Intranet attribute
class shope:


    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = []


    def add_to_cart(self,product):
        self.cart.append(product)


Rakib = shope("Rakib")
Rakib.add_to_cart('shose')
Rakib.add_to_cart('sunglass')
print('After added Rakib:', Rakib.cart)



Robin = shope("Robin")
Robin.add_to_cart('cap')
Robin.add_to_cart('shirt,')
print('After addded Robin:',Robin.cart)
