#Metodo para configuração inicial da classe#
#Metodo construtor#
#Os atributos são passados todos no metodo construtor#
#inicializar#
class Movie:
    def __init__(self, name, yearLaunch, includedPlan, note, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.note = note
        self.durationMinutes = durationMinutes
    #A palavras self se refere aos atributos da classe#
        
    #Metodo especial que sobrescreve o que quer retornar ao inves de uma informação técnica#
    def __str__(self):
        return f"Filme: {self.name}"
        

Movie = Movie("Game of thrones", 2011, False, 4.5, 3)
Movie2 = Movie("Mario", 2013, True, 3, 5)
print(Movie.note)
print(Movie.name)

print(Movie)#Antes do metodo str >> <__main__.Movie object at 0x000001EEB771A1E0>
print(Movie2)


