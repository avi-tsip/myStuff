"""
Here, in the __new__ method, we will check whether an instance is created or not. 
If created, it will return the instance; otherwise, it will create a new instance. 
You can notice that singleton and new_singleton return the same instance and have the same variable.
"""
class SingletonClass(object):
  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(SingletonClass, cls).__new__(cls)
    return cls.instance
   
singleton = SingletonClass()
new_singleton = SingletonClass()
 
print(singleton is new_singleton)
 
singleton.singl_variable = "Singleton Variable"
print(new_singleton.singl_variable)