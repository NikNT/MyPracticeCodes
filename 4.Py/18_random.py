import random
random_number = random.randint(1,6)
print(random_number)

float_number = random.random()
print(float_number)

myList = ['rock', 'paper', 'scissor']
z = random.choice(myList)
print(z)

cards  = [1,2,3,4,5,6,7,8,9,"J", "Q", "K", "A"]
random.shuffle(cards)
print(cards)