N = input().strip()

rev = str(int(N[::-1]))

print(rev)

if N == N[::-1]:
    print("YES")
else:
    print("NO")
