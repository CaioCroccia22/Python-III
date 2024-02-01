class Movie:
    #Variavel de classe é uma caracteristica geral de todo objeto#
    plataform = "Netflix"
    def __init__(self, name, yearLaunch, includedPlan, note, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.note = note
        self.durationMinutes = durationMinutes
    
    def __str__(self):
        return f"Filme: {self.name}"
    
    def techinal_sheet(self):
        print("#Dados do filme")
        print(f"Plataforma: {Movie.plataform}")
        print(f"Nome do filme: {self.name}")
        print(f"Avaliação do filme: {self.note}")

mario = Movie("Super Mario", 2023, False 
              , 5, 100)

mario.techinal_sheet()
#Modificando a variavel de classe#
Movie.plataform = "Amazon"