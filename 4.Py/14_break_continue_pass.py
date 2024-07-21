'''
1. break : used to terminate the loop
2. continue : skip to the next iteration
3. pass : do nothing, acts as placeholder
'''

while True:
    name = input('Enter your name here: ')
    if name != "":
        break

phone_number = "123-456-8950"
for i in phone_number:
    if i == "-":
        continue
    print(i,end="")

for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)