balance = 3000

def buy_thinks(item, price):
    global balance
    print(f'previous balance value ', balance)
    balance = balance - price
    print(f'after balance vuying {item} ', balance)
    print(f'balance after buying', balance)

buy_thinks(f'sunglass',1000)
