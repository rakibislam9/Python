# inner function 

def dobble_decar():
    print("inner Function niya kaj korci")

    def inner_fun():
        print("print hocce inner function")
        return 'RAKIB '
    return inner_fun
    # print(inner_fun())

# print(dobble_decar()())


# WRAPPER FUNCTION

def do_somtime(work):
    print("work strat")
    work()
    print("work end")


def decode():
    print("Argument with inner function")

def Tallha():
    print("Tallha windos rebot korte jane na bule")
    


# do_somtime(decode)
do_somtime(Tallha)


