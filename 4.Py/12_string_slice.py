name = "Spongebob Squarepants"

# Indexing
first_name = name[0:9]
last_name = name[10:22]
step_name = name[0:8:2]
just_step = name[::2]
rev_name = name[ : :-1]

vals = [
    {'first_name' : first_name},
    {'last_name': last_name},
    {"step_name", step_name},
    {"just_step", just_step},
    {"rev_name" : rev_name}]

for val in vals:
    print(val)

# Slicing 
google = "http://google.com"
wiki = "http://wikipedia.com"
slice = slice(7,-4)
print(google[slice], wiki[slice])