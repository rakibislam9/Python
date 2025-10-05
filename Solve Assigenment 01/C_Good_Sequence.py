
N = int(input())
a = input().split()   

a = [int(x) for x in a]

freq = {}
for x in a:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

removals = 0
for x in freq:
    count = freq[x]
    if count == x:
        continue
    elif count > x:
        removals += count - x
    else:  
        removals += count

print(removals)
