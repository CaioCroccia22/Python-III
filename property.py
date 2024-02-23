class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age


    #get 
    @property
    def name(self):
        return self._name
    # set
    @name.setter
    def name(self,value):
        if not isinstance(value, str):
            raise TypeError("Nome deve ser uma string")
        self._name = value


Caio = Person("Caio", 14)
print(vars(Caio))
print(Caio.name)
