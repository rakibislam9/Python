numbers = [1, 2, 3, 4, 5]
odds = []
for num in numbers:
    if num % 2 == 1 and num % 5 == 0:
        odds.append(num)

print(odds)



players = ['sakib', 'musfik', 'liton']
ages = [38, 37, 32]

age_comb = []
for player in players:
    for age in ages:
        age_comb.append([player, age])
        
print(age_comb)

players = ['sakib', 'musfik', 'liton']
ages = [38, 37, 32]

age_comb = [[player, age] for player in players for age in ages]
print(age_comb)
