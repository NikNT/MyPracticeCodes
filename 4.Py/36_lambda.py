# lambda parameters:expression

square = lambda x : x * x
res = square(2)
print(res)

multi = lambda x,y : x * y
res2 = multi(2,4)
print(res2)

add = lambda x,y,z : x + y + z
res3 = add(1,2,3)
print(res3)

full_name = lambda first_name, last_name : first_name + " " + last_name
res4 = full_name('Nik', 'Tan')
print(res4)