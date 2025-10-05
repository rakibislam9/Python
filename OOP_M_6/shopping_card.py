# class Shopping_Mol:
#     def __init__(self,shoroom):
#         self.shoroom = shoroom

# class ledis_item:
#     def __init__(self, thripis, hanpass, lipstic):
#         self.thripis = thripis
#         self.hanpass = hanpass
#         self.lipstic = lipstic 


# class jems_item:
#     def __init__(self,pant, shart, cap):
#         self.pant = pant
#         self.shart = shart
#         self.cap = cap

# class shopping_cart:
#     def __init__(self,shorooom,thripis, hanpass, lipstic,pant, shart, cap ):
#         self.shop = Shopping_Mol(shorooom)
#         self.femal = ledis_item(thripis, hanpass, lipstic)
#         self.mail = jems_item(pant, shart, cap)




# Shope = shopping_cart('Moshomi','Pakhi','Gucci','Diro','Boss','Esy','adidas')

# print(Shope)





class Shopping_Mol:
    def __init__(self, shoroom):
        self.shoroom = shoroom

class ledis_item:
    def __init__(self, thripis, hanpass, lipstic):
        self.thripis = thripis
        self.hanpass = hanpass
        self.lipstic = lipstic 

class jems_item:
    def __init__(self, pant, shart, cap):
        self.pant = pant
        self.shart = shart
        self.cap = cap

class shopping_cart:
    def __init__(self, shorooom, thripis, hanpass, lipstic, pant, shart, cap):
        self.shop = Shopping_Mol(shorooom)
        self.femal = ledis_item(thripis, hanpass, lipstic)
        self.mail = jems_item(pant, shart, cap)

    def __str__(self):
        return f"""
Shopping Mall: {self.shop.shoroom}
--- Ladies Item ---
Thripis: {self.femal.thripis}
Hanpass: {self.femal.hanpass}
Lipstic: {self.femal.lipstic}
--- Gents Item ---
Pant: {self.mail.pant}
Shart: {self.mail.shart}
Cap: {self.mail.cap}
"""

Shope = shopping_cart('Moshomi','Pakhi','Gucci','Diro','Boss','Esy','adidas')
print(Shope)

