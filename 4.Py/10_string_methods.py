name = "Bro"
small_case = "bro code"
all_caps = "BRO CODE"
digits = "123"

len = len(name)
find = name.find("o")
capitalize = small_case.capitalize()
upper = small_case.upper()
lower = all_caps.lower()
isDigit = digits.isdigit()
isAlpha = name.isalpha()
count = name.count("o")
replace = name.replace("o", "0")

vals = {
    "len" : len,
    "find" : find,
    "capitalize" : capitalize, 
    "upper" : upper,
    "lower" : lower,
    "isDigit" : isDigit, 
    "isAlpha" : isAlpha,
    "count" : count,
    "replace" : replace, 
}

print(vals)
