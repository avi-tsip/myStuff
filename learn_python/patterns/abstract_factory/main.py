"""When the program expects to get a family of related objects but doesn't need to now what are they"""

class Dog:
    """concrete object"""
    def speak(self):
        return ("woof!")
    
    def __str__(self):
        return "Dog"
    
class DogFactory:
    """concrete factory"""
    def get_pet(self):
        """returns the dog object"""
        return Dog()
    
    def get_food(self):
        """returns a dog food obejct"""
        return ("dog food bag received")
    
class PetStore:
    """abstract factory"""

    def __init__(self, pet_factory) -> None:
        self._pet_factory = pet_factory

    def show_pet(self):
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print(f"our pet is a {pet}")
        print(f"out pet says {pet.speak()}")
        print(f"it's time for some {pet_food}")

factory = DogFactory()

store = PetStore(factory)
store.show_pet()
