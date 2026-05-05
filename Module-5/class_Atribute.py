# class Shop:

#     cart = []

#     def __init__(self, buyer):

#         self.buyer = buyer



#     def add_to_cart(self, product):

#         self.cart.append(product)



# Rakib = Shop("Rakib")

# Rakib.add_to_cart("shose")

# Rakib.add_to_cart("shirt")

# print("After Rakib added two products to the cart:", Rakib.cart)


# instance Atribute


class Shop:
    def __init__(self, buyer):
        self.buyer = buyer

        self. cart = []

    def add_to_cart(self, product):
        self.cart.append(product)


Rakib = Shop("Rakib")

Rakib.add_to_cart("cap")

Rakib.add_to_cart("Watch")

Rakib.add_to_cart("phone")

print("After Rakib added:", Rakib.cart)