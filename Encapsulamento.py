class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
        # __ -> define o atributo salario como modificador de acesso privado
    
    def show(self):
        print(f"Nome {self.name} - Salario {self.__salary}")

fulano = Employee("Fulano", 5000)
sicrano = Employee("Sicre", 5000)
fulano.show()
sicrano.show()
fulano.__salary = 400000
fulano.show()


