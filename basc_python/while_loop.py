# print numbers form 1 to 5 using while loop 
i = 1
while i <= 5:
    print(i)
    i += 1

# print numbers from 1 to 10 using while loop

num = 1
while num <= 10:
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")
    num += 1

# Example : print numbers from 1 to 5 skipping even numbers while loop

num = 1

while num <= 5:
    if num % 2 == 0:
        num += 1 
        continue
    print(num)
    num += 1


# Example : print numbers from 1 onwards until reachibg a number greater than 5 using a while loop

num = 1
while True:
    print(num)
    if num > 5:
        break
    num += 1