class Movie:
    name = ""
    yearLaunch = 0
    includedPlan = False
    note = 0
    durationMinutes = 0

#Instanciando o objeto a partir de uma classe#
#Primeiro Filme#
movie = Movie()
print(movie)
#Cria um objeto na classe movie#
movie.name = "Super Mario"
movie.yearLaunch = 2010
movie.includedPlan = False
movie.note = 5.0
print(f"Nome do filme: {movie.name}")
