# N = int(input())
# numbers = list(map(int,input().split()))

# peven = 0

# for i, num in enumerate(numbers):
#     if num % 2 == 0:
#        peven += 1
#        numbers[i] = num / 2
#     else:
#         if peven != 0:
#             peven -= 1
#         break

# print(peven)



N = int(input())
numbers = list(map(int, input().split()))

min_count = float('inf')

for num in numbers:
    cnt = 0
    while num % 2 == 0:
        cnt += 1
        num //= 2
    min_count = min(min_count, cnt)

print(min_count)