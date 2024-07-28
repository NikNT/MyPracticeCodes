class Car:
    color = None

class Motorcyle:
    color = None

def change_color(vehicle, color):
    vehicle.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()

change_color(vehicle=car_1, color="red")
change_color(vehicle=car_2, color="white")
change_color(vehicle=car_3, color="blue")

bike_1 = Motorcyle()
bike_2 = Motorcyle()
bike_3 = Motorcyle()

change_color(vehicle=bike_1, color="red")
change_color(vehicle=bike_2, color="white")
change_color(vehicle=bike_3, color="blue")

print(car_1.color)
print(car_2.color)
print(car_3.color)

print("------------------------------------")

print(bike_1.color)
print(bike_2.color)
print(bike_3.color)