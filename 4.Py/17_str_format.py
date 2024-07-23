animal = "cow"
item = "moon"

print(f"The {animal} jumped over the {item}")
print("The {} jumped over the {}".format(animal, item))
print("The {0} jumped over the {1}".format(animal, item))
print("The {ani} jumped over the {ite}".format(ani="cow", ite="moon"))

text = "The {} jumped over the {}"
print(text.format(animal, item))

name="Bro"
print("Hello my name is {:10}. Nice to meet you.".format(name))
print("Hello my name is {:<10}. Nice to meet you.".format(name))
print("Hello my name is {:>10}. Nice to meet you.".format(name))
print("Hello my name is {:^10}. Nice to meet you.".format(name))

num = 3.14159
num2 = 1000
print("The number pi is {:.3f}".format(num))
print("The number pi is {:,}".format(num))
print("The number in binary {:b}".format(num2))
print("The number in binary {:o}".format(num2))
print("The number in binary {:X}".format(num2))
print("The number in binary {:e}".format(num2))