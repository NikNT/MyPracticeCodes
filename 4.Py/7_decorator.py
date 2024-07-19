# Decorator : Fn that extends the behavior of another function | Add to the base function without changing 

def add_sprinkles(func):
     def wrapper(*args, **kwargs):
          print("**Added Sprinkles**")
          func(*args, **kwargs)
     return wrapper

def add_fudge(func):
     def wrapper(*args, **kwargs):
          print("**Added Fudge**")
          func(*args, **kwargs)
     return wrapper

def add_oreo(func):
     def wrapper(*args, **kwargs):
          print("**Added Oreo**")
          func(*args, **kwargs)
     return wrapper

@add_sprinkles
@add_fudge
@add_oreo
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream 🍦")

get_ice_cream("vanilla")