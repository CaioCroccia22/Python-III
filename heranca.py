# Classe Generica
class Animal:
    name = ""
    size = ""
    color = ""


    def eat(self):
        print(f"Animal {self.name} se alimentando")

# Classe especializada
class Horse(Animal):
    race = ""

    def escape(self):
        print(f"O Cavalo {self.name} está fugindo")

# Classe especializada
class Lion(Animal):
    mane = True

    def hunt(self):
        print(f"Leão {self.name} está caçando")

h = Horse()
# O atributo name não foi colocado na classe Horse, porem foi na classe Animal
h.name = "Pé de Pano"
h.race = "Branco"
h.escape()
h.eat()

l = Lion()
l.name = "Simba"
l.hunt()
l.eat()

