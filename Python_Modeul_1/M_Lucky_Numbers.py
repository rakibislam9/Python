
line = input().split()
A = int(line[0])
B = int(line[1])

found = False

for i in range(A, B+1):
    ok = True
    for ch in str(i):
        if ch != '4' and ch != '7':
            ok = False
            break
    if ok:
        print(i, end=" ")   # print directly with space
        found = True

if not found:
    print(-1)



