

#Criando uma classe#
#Primeiro Filme#
class Movie:
    name = ""
    yearLaunch = 0
    includedPlan = False
    note = 0
    durationMinutes = 0

#Referenciando a classe fora dela#
movie = Movie()
print(movie)

#Instanciando o objeto a partir de uma classe#
#Cria um objeto na classe movie#
movie.name = "Super Mario"
movie.yearLaunch = 2010
movie.includedPlan = False
movie.note = 5.0
print(f"Nome do filme: {movie.name}")



