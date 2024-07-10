"""
The borg pattern allows many instances, but they all share, can update and use the same attributes
"""

class Borg:
    _shared_data = {}
    
    def __init__(self):
        self.__dict__ = self._shared_data  

class Singelton(Borg):
    def __init__(self, **kwargs):
        Borg.__init__(self)
        self._shared_data.update(kwargs)

    def __str__(self) -> str:
        return str(self._shared_data)
    
singelton = Singelton(HTTP = 'Hyper Text Transfer Protocol')
second_singelton = Singelton(SNMP = 'Simple Network Management Protocol')
print(singelton)