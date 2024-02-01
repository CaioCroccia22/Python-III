class product:

    def __init__ (self, name, value):
        self.name = name
        self.value = value
        

    def __str__ (self):
        print("------------Dados do produto--------------")
        print(f"O nome do produto é {self.name}")
        print(f"O valor do produto é {self.value}")
        
    def sale(self, discount):
        percentage = self.value/100
        price = percentage*discount
        totalPrice = self.value - price
        print(f"O preço do produto é {totalPrice}")

bottle = product("garrafa", 10)
rice = product("Arroz", 40)

bottle.sale(10)
rice.sale(10)