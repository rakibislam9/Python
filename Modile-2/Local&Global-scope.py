# Global scope

def func():
    print(balance)

func()
print(balance)



def chk():
    balance = balance -5

def chk():
    global balance
    balance = balance - 5

chk()

# local scope

# def func():
#     balance = 500
#     print(balance)

# func()