class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def show(self):
        print(f"Nome {self.name} - Salario {self.salary}")
    