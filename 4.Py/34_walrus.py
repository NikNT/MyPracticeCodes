happy = True
print(happy)
print(happy := False)

# foods = list()
# while True:
#     food = input("What food do you like?: ")
#     if food == "quit":
#         break
#     foods.append(food)

foods_2 = list()
while food := input("What food do you like?: ") != "quit":
    foods_2.append(food)
print('Food ', foods_2)

say = print
say("Whoa! I can't believe this works! :O")