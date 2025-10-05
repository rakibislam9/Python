import math
def timer(func):
    def inner(*args, **kwarges):
        print("start inner")
        func(*args, **kwarges)
        print("end inner")
    return inner 
@timer
def factoriyal(n):
    print("factoriyal starting")
    result = math.factorial(n)
    print(f"factorial of {n} is {result}")

factoriyal(110 == 5)
