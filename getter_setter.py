class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
        # __ -> define o atributo salario como modificador de acesso privado
    
    def show(self):
        print(f"Nome {self.name} - Salario {self.__salary}")

    # Como acessar e modificar valores de atributos privado
    

    #Metodo para buscar dados
    def get_salary(self):
        return self.__salary
    
    #Metodo para modificar o atributo
    def set_salary(self, salary):
        self.__salary = salary

fulano = Employee("Fulano", 5000)
sicrano = Employee("Sicre", 5000)
fulano.name = "Caio Croccia"
fulano.show()




