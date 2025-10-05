N = int(input())
digits = input().split()

revd = digits[::-1]

if digits == revd :
    print("YES")
else:
    print("NO")