# def sum(a,b):
#     return a+b

# result = sum(5, 23)
# print(result)


# difult parameter args

# def sum (a, b, c = 0):
#     return a + b + c

# result = sum(5, 6, 7)
# print(result)

# result2 = sum(2,4) # c = 0 by default
# print(result2)



# *args

# def sum(*args):
#     sum = 0
#     for num in args:
#         sum = sum + num

# result = sum(5, 4)
# print(result)


# **kwargs

def func(**kwargs):
    print(f"apple: {kwargs['apple']}")
    for key, value in kwargs.items():
        print(f"{key} : {value}")

    result = func(apple=5, orange= 4)