class User:
    def __init__(self,name, salary):
        self._name = name
        self._salary = salary
        

    @property
    def acel(self):
        return Rakib._salary
    
    @acel.setter
    def acel(self, value):
        if value > 0:
            self._salary = value
        else:
            raise ValueError("salary must be a positibe number")
        
    @acel.deleter
    def acel(self):
        del Rakib._salary




Rakib = User("Rakib", 36000)
del Rakib.acel
print(f"Employee salary {Rakib.acel}")


Rakib.acel = 40000
print(f"Employee updete salary {Rakib.acel}")
