class shopping:
    def __init__(self,name):
        self.name = name
        self.cart = []


    def add_to_cart(self,item,price,quantity):
        product = {'item': item, 'price': price, 'quantity' : quantity}
        self.cart.append(product)



    def remove_item(self, item):
        for product in self.cart:
            if product['item'] == item:
                self.cart.remove(product)
                print(f'{item} remove from cart')
                return
        print(f'{item} not found in card')



    def checkout(self, amount):
        Total = 0
        for item in self.cart:
            Total += item['price'] * item['quantity']

        print('Total item price: ', Total)
        if amount < Total:
            print(f'pleces provide the {amount - Total} more')
        else:
            extra = amount - Total
            print(f'Here is your item extra money: {extra}')


Rakib = shopping("Rakib")
Rakib.add_to_cart('Alu', 25, 5)  
Rakib.add_to_cart('shobji', 30, 6)  
Rakib.add_to_cart('dim', 10, 36) 
Rakib.add_to_cart('rice', 25, 65) 


print(Rakib.cart)
Rakib.remove_item('ajgobi')
# Rakib.checkout(400)
Rakib.checkout(1400)

        