# Higher Order Function - 1. a fn that accepts a fn or 2. returns a fn (Functions in Py are treated as Objs)


# Function that accepts a function
def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("Hello")
    print(text)

hello(loud)
hello(quiet)

# Returns a Function 
def divisor(x):
    def dividend(y):
        return y / x
    return dividend

divide = divisor(2)
print(divide(10))