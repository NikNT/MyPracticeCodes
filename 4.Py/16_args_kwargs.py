def hello(first, middle, last):
    print(f"Hello {first} {middle} {last}!")

hello(last='C', first='A', middle='B')

def add(*args):
    sum = 0
    for i in args:
        sum += i 
    return sum

print(add(1,2,3,4))

def greet(**kwargs):
    # print(f"Hello {kwargs['first']} {kwargs['middle']} {kwargs['last']}")
    print("Hello",end=" ")
    for key, val in kwargs.items():
        print(val,end=" ")

greet(title="Mr", first="Bro", second="Dude", last="Code")

# args - tuples
# kwargs - dict