class  jipp:
    def __init__(self,name, licens, salary):
        self.name = name
        self.licens = licens
        self.salary = salary
        

    @classmethod
    def driver(self,distanation):
        print("Ami kuthai jacchi", distanation)

    @staticmethod
    def pacentjer(tiket, price):
        print(tiket * price)



jipp.driver('mymenshing')

jipp.pacentjer(2,320)