import math
pi = 3.14

round = round(pi) 
ceil = math.ceil(pi) 
floor = math.floor(pi) 
abs = abs(pi)
pow = pow(pi, 2)
sqrt = math.sqrt(pi)
max = max(1,2,3)
min = min(1,2,3)

vals = {
    "round" : round,
    "ceil" : ceil, 
    "floor" : floor,
    "abs" : abs, 
    "pow": pow,
    "sqrt" : sqrt,
    "max" : max, 
    "min" : min,
}

print(vals)
