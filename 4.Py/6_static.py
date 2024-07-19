# Static Methods - Best for utlity functions that do not need access to class data

class Employee:
    def __init__(self, name, position) -> None:
        self.name = name
        self.position = position

    # Instance method 
    def get_info(self):
        return f"{self.name} is a {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        positions = ["Manager", "Cashier", "Cook", "Janitor", "Developer"]
        return position in positions

employee1 = Employee("Nikhil", "Developer")

if employee1.is_valid_position(employee1.position):
    print(employee1.get_info())
else:
    print('Out of bounds!')

print(Employee.is_valid_position("Rocket Scientist"))        