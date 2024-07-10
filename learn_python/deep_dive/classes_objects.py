class Person:
    race = 'Human'
    walking = 'two legs'     

    def say_hello():
        print(f'say hello {Person.race}')                         

print(type(Person)) # type of type

print(type(type)) # but type is also of type type

print(Person.__name__) # Perons

p = Person()

print(p.__dict__) # {} 

# vs the class dict as you can see below     

print(p.__class__) # __main__.Person             

print(type(p)) # __main__.Person

print(p.__class__) # __main__.Person
  
print(isinstance(p, Person)) # True

print(Person.race) # Human
print(Person.walking) # two legs

Person.race = 'alien'
print(Person.race) # alien

print(getattr(Person, 'race')) # alien

setattr(Person, 'race', 'Human')

print(Person.race) # Human

print(getattr(Person, 'name', 'avi')) # The third value is the default value in case the attrribute does not exist   

print(Person.__dict__)                                                                   
"""
    {'__module__': '__main__',
    'race': 'Human',
    'walking': 'two legs',
    '__dict__': <attribute '__dict__' of 'Person' objects>,
    '__weakref__': <attribute '__weakref__' of 'Person' objects>,
    __doc__': None} 
"""

Person.x = 100

print(Person.__dict__)  
"""
    {'__module__': '__main__',
      'race': 'Human',
        'walking': 'two legs',
          '__dict__': <attribute '__dict__' of 'Person' objects>,
            '__weakref__': <attribute '__weakref__' of 'Person' objects>,
              '__doc__': None,
                 'x': 100} => x attribute is added 
"""

delattr(Person, 'x')

print(Person.__dict__)  
"""
    {'__module__': '__main__',
      'race': 'Human',
        'walking': 'two legs',
          '__dict__': <attribute '__dict__' of 'Person' objects>,
            '__weakref__': <attribute '__weakref__' of 'Person' objects>,
              '__doc__': None,
"""
Person.say_hello() # say hello human

getattr(Person, 'say_hello')() # say hello human

print(getattr(Person, 'say_hello') ) # <function Person.say_hello at 0x000001F291396CA0>

print(Person.say_hello) # <function Person.say_hello at 0x000001F291396CA0>

# do not user __class__ instead of type:

class MyClass:
    __class__ = str

m = MyClass ()

print (m.__class__, type(m)) # hey are not the same

# now lets see the isinstance behavior:

isinstance(m, MyClass)  # true

isinstance(m, str) # true

isinstance(m, int) # false