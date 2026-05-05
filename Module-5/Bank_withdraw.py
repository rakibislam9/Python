class Bank:
    def __init__(self, balance):
        self.balance = balance

        self.min_withdraw = 100
        self.max_withdraw = 1000000


    def get_balance(self):
        return self.balance
    

    def deposit(self, amount):

        if amount > 0:
            self.balance += amount


    def withdraw(self, amount):

        if amount < self.min_withdraw:
            print(f"Minimun withdraw amount is {self.min_withdraw}")
        elif amount > self.max_withdraw:
            print(f"Maximum withdraw amount is {self.max_withdraw}")
        else:
            self.balance -= amount
            print(f'your balance is after withdraw: {self.get_balance()}')

    
      

brack = Bank(15000000)

brack.withdraw(500000)