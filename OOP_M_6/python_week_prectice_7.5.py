class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

class Cricketer(Person):
    def __init__(self, name, age, height, weight) -> None:
        super().__init__(name, age, height, weight)

    @property
    def getter(self):
        return self.age



    @getter.setter
    def getter(self, value):
        if value > 41:
            self.age = value
        else:
            raise ValueError("Plyeer no retaiyar time")


    # def __gt__(self,other):
    #     return self.age > other.age
    

    # def __ls__(self,other):
    #     return self.age < other.age
    

    # def __str__(self):
    #     return f"Name: {self.name}  Age {self.age}" 


sakib = Cricketer('Sakib', 38, 68, 91)
musfiq = Cricketer('Rahim', 36, 68, 88)
kamal = Cricketer('Kamal', 39, 68, 94)
jack = Cricketer('Jack', 38, 68, 91)
kalam = Cricketer('Kalam', 37, 68, 95)
 

plyears =[sakib,musfiq,kalam,jack,kamal]
# olled = max(plyears)
kamal.getter = 41
# print(olled)
print(f"team hight age plyeer name: {kamal.getter}")


