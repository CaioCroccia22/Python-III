"""
1 -  O metodo de classe utiliza o parametro referente a classe

2 - O metodo de classe pode acessar ou modificar o estado da classe

3 - Usamos o decorator @classmethod para criar um metodo de classe

"""

import re

class Console:
    def  __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def from_text(cls, string):
        import re
        item = re.findall(" é \w*", string)
        name = item[0][2:]
        price = item[1][2:]
        return cls(name, int(price))
    
WiiU = Console.from_text("Meu video game é WiiU e o preço é 1000 reais")
print(WiiU.__dict__)
