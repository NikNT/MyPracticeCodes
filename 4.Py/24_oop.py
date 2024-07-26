class Car:

    def __init__(self, make, model, year, color) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print(f'This {self.model} is driving!')

    def stop(self):
        print(f'This {self.model} is stopped!')

car1 = Car(make="Chevy",model="Corvette",year=2021,color="Blue")
car2 = Car(make="Ford", model="Mustang", year=2022, color="Red")

car1.drive()