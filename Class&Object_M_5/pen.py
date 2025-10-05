# Constrctor: 

class pen:
    manufacher = 'Bangladesh'


    def __init__(self, color, brand, price):
        self.color = color
        self.brand = brand
        self.price = price




my_pen = pen('black', 'pinpoint', 6)
print(my_pen.color, my_pen.brand, my_pen.price)


read_pen = pen('read', 'High school', 6)
print(read_pen.color, read_pen.brand, read_pen.price)

jel_pen = pen('B_black', 'Jelpin', 25)
print(jel_pen.color, jel_pen.brand, jel_pen.price)
