""""
Polismorfismo - Poder invocar metodos com mesma assinatura
porém metodos que tenham comportamento diferente

"""

class Phone:

    def __init__(self, brand, model_name, price):
        self._brand = brand
        self._model_name = model_name
        self._price = price

    def __str__(self):
        return f"Telefone de marca:  {self._brand} e modelo: {self._model_name}"

    @staticmethod
    def make_a_call(phone_num):
        print(f"Ligando para {phone_num}")
    
    def discount(self):
        return self._price * 0.10


class SmartPhone(Phone):
    def __init__(self, brand, model_name, price, ram, internal_memory, back_camera):
        # Metodo super invoca os valores da classe pai
        super().__init__(brand, model_name, price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.back_camera = back_camera
 
    # Na classe SmartPhone vai incovar o mesmo metodo discount, porem com diferença de valor
    def discount(self):
        return self._price * 0.15

    

Moto = Phone('Moto', '17', 1000)
print(Moto.__str__)
Moto.make_a_call(13997447473)
print(f"Valor do {Moto._brand} {Moto._model_name} é {Moto._price}")
print(vars(Moto))
print(Moto.discount())


Iphone = SmartPhone('Iphone', '14', 4800, '4GB', '128GB', '25MP')
print(Iphone)
Iphone.make_a_call(139981447473)
print(f"Valor do iphone {Iphone._brand} {Iphone._model_name} {Iphone._price}")
print(vars(Iphone))
print(Iphone.discount())
#Senao tivesse o Polismorfismo o desconto seria de 10%

