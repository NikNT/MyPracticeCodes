friends = [
    ("Rachel", 19),
    ("Monica", 18),
    ("Phoebe", 17),
    ("Joey", 16),
    ("Chandler", 21),
    ("Ross", 20)
]

age = lambda data:data[1] >= 18
drinking_friends = filter(age, friends)
print(drinking_friends)

for friend in drinking_friends:
    print(friend)