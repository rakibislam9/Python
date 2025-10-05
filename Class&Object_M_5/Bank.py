class bank:
    def __init__(self,balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 25000

    def get_balance(self):  
        return self.balance
    

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        

    def withdraw(self, amount):
        if amount < self.min_withdraw:
            print(f'Your balance is low places minimum withdraw {self.min_withdraw} taka')
        elif amount > self.max_withdraw:
            print(f'places you maximum withdraw {self.max_withdraw}')
        else:
            self.balance -= amount
            print(f'Here is your money {amount}')
            print(f'Your current money {self.balance}')



barck_bank = bank(40000)
barck_bank.withdraw(99.99)
barck_bank.withdraw(50000)
barck_bank.withdraw(13000)

    