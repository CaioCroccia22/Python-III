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

class SmartPhone(Phone):
    def __init__(self, brand, model_name, price, ram, internal_memory, back_camera):
        # Metodo super invoca os valores da classe pai
        super().__init__(brand, model_name, price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.back_camera = back_camera

Moto = Phone('Moto', '17', 1000)
print(Moto.__str__)
Moto.make_a_call(13997447473)
print(f"Valor do {Moto._brand} {Moto._model_name} é {Moto._price}")
print(vars(Moto))

Iphone = SmartPhone('Iphone', '14', 4800, '4GB', '128GB', '25MP')
print(Iphone)
Iphone.make_a_call(139981447473)
print(f"Valor do iphone {Iphone._brand} {Iphone._model_name} {Iphone._price}")
print(vars(Iphone))