'''
Lambda Function

Throw away function, one-time use 
Helps in keeping namespace clear
n arguments but 1 expression
'''

double = lambda x: x * 2
print('double', double(2))

add = lambda x,y: x+y
print('add', add(1,2))

max = lambda x,y: x if x > y else y
print('max', max(5,6))

min = lambda x,y: x if x < y else y
print('min', min(6,5))

full_name = lambda first_name, last_name : first_name + last_name
print('full_name', full_name('Sponge', 'Bob'))

is_even = lambda x: 'Even' if x % 2 == 0 else 'Odd'
print(is_even(11))

age_check = lambda age: True if age >= 18 else False
print(age_check(20))