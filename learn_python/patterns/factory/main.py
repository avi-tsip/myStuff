"""Factory is an object spacializes in creating other objects
It solves an issue where you don't know which type should be each object.
When needing to decide what kind of class to create at run time"""

class Dog:

    def __init__(self, name) -> None:
        self.name = name

    def speak(self):
        return ('Woof')

class Cat:

    def __init__(self, name) -> None:
        self.name = name

    def speak(self):
        return ('Meow')

def get_pet(pet):
    pets = dict(dog=Dog('Henry'), cat=Cat('Wiskers'))
    return pets[pet]

d = get_pet('dog')
print(d.speak())

c = get_pet('cat')
print(c.speak())