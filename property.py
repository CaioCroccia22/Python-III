class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age


        #get 
        @property
        def name(self):
            return self.name
        # set
        @name.setter
        def name(self,value):
            if not isinstance(value, str):
                raise TypeError("Nome deve ser uma string")
            self.name = value