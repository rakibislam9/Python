S = input().strip()

balance = 0
part = []
current = ""


for ch in S:
    current += ch
    if ch == 'L':
        balance -= 1
    else:
        balance += 1


    if balance == 0:
        part.append(current)
        current = ""
    

print(len(part))
for p in part:
    print(p)
