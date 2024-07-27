class Organism:
    alive = True

class Animal(Organism):
    def eat(self):
        print('This animal is eating.')

class Dog(Animal):
    def bark(self):
        print('This dog is barking.')

dog = Dog()
alive = dog.alive
print(alive)
dog.eat()
dog.bark()