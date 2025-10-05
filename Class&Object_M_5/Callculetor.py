class callculetor:
    breand = 'casio Ms990'

    def add(self, num1, num2):
        result = num1 + num2
        return result
    
    def deduct(self, num1, num2):
        result = num1 - num2
        return result
    

    def multiply(self, num1, num2):
        result = num1 * num2
        return result
    

    def divide(self, num1, num2):
        result = num1 // num2
        return result


my_callculetor = callculetor()
print(my_callculetor.add(10, 20))
print(my_callculetor.deduct(10, 20))
print(my_callculetor.multiply(10, 20))
print(my_callculetor.divide(10, 3))