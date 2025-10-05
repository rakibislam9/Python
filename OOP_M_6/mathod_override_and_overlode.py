class person:
    def __init__(self, name, age, height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        

    def helth(self):
        print("vagitabale,chiken,pakura")

    def exercis(self):
        raise NotImplementedError


class Cricketer(person):
    def __init__(self, name, age, height, weight,team):
        self.team = team
        super().__init__(name, age, height, weight)

    # Override
    def helth(self):
        print("Electrolyte Drink")

    def exercis(self):
        print("Prcur gym korte hoveve")

# Overlode:

    def __add__(self,other):
        return self.age + other.age
    
    def __mul__(self,other):
        return self.weight * other.weight
    
    def __gt__(self, other):
        return self.height > other.height


Rakib = Cricketer('Rakib', 22, 67, 65, 'BD')
Sahin = Cricketer("Shahin",23,65,58,"USA")
# Rakib.helth()
# Rakib.exercis()
print(Rakib + Sahin)
print(Rakib * Sahin)
print(Rakib > Sahin)