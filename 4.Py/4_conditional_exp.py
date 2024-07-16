# Conditional exp =

num = 5

isPositive = "Positive" if num > 0 else "Negative"
isOdd = 'Even' if num % 2 == 0 else "Odd"
print(isPositive)
print(isOdd)

a = 6
b = 7
max_num = a if a > b else b
min_num = a if a < b else b
print(max_num, min_num)