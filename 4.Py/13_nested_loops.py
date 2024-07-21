rows = int(input('Enter number of rows: '))
cols = int(input('Enter number of cols: '))
symb = input('Enter a symbol: ')

for i in range(rows):
    for j in range(cols):
        print(symb, end=" ")
    print()