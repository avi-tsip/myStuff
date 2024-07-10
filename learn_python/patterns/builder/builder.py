"""
Solves an issue where we are trying to build a massive object with multiple constructors and the process becomes complex
Solution: use specified constructor with specified roles to reduce complexity:
1. Director
2. Abstract builder - interface
3. Concrete builder - implements the interface
4. Product - object that will be built
"""

class Director():
    """Director"""
    def __init__(self, builder) -> None:
        self._builder = builder

    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()

    def get_car(self):
        return self._builder.car

class Builder():
    """Abstract Builder"""
    def __init__(self) -> None:
        self.car = None

    def create_new_car(self):
        self.car = Car()

class FordBuilder(Builder): # If I want to build a mustand - just add a MustandBUilder class
    """Concrete Builder"""
    def add_model(self):
        self.car.model = 'Model T'

    def add_tires(self):
        self.car.tires = 'sports tires added'

    def add_engine(self):
        self.car.engine = 'Turbo'

class Car():
    """Product"""
    def __init__(self) -> None:
        self.model = None
        self.tires = None
        self.engine = None

    def __str__(self) -> str:
        return f"The car is of model: {self.model}, with {self.tires} and an {self.engine} engine"

builder = FordBuilder()
director = Director(builder)
director.construct_car()
car = director.get_car()

print(car)
        