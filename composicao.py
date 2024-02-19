"""
Composição - Tecnico de programação orientada ao Objetos
para estabelecer relação entre classes e objetos
ex: Leao faz parte de um zoologico
POde ser usada de forma complementar com a herança
"""

class Animal:
    def __init__(self, name, category):
        self.name = name
        self.category = category


class Fish(Animal):
    race = ""

class Parrots(Animal):
    color = ""

class Zoo:
    def __init__(self):
        self.animals_dict = {}

    def add_animal(self, animal):
        self.animals_dict[animal.name] = animal.category

    def total_of_category(self, category):
        result = 0
        for animal in self.animals_dict.values():
            if animal == category:
                result += 1
        return f"No nosso zoologico temos {result} quantidade de categorias {category}"


zoo = Zoo()
peixe = Fish("Nemo", "mamiferos")
print(vars(peixe))
papagaio = Parrots("Louro", "aves")
zoo.add_animal(peixe)
zoo.add_animal(papagaio)
print(zoo.total_of_category("aves"))
print(zoo.total_of_category("mamiferos"))
