from functools import reduce
letters = ["H", "E", "L", "L", "O"]
word = reduce(lambda x,y : x+y, letters)
print(word)

factorial = [1,2,3,4,5,6]
res = reduce(lambda x,y : x*y, factorial)
print(res)