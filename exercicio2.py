class product:

    def __init__ (self, name, value):
        self.name = name
        self.value = value
        

    def __str__ (self):
        print("------------Dados do produto--------------")
        print(f"O nome do produto é {self.name}")
        print(f"O valor do produto é {self.value}")
        
    def sale(self, discount):
        percentage = discount/100
        price = percentage*self.value
        print(f"O preço do produto é {price}")

