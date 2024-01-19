"""
Avaliação e nota media do filme 
Desenvolva novas funcionalidades para complemnetar o nosso gereciamento da classe filmes 
Segue o escopo das funcionalidades

1- Uma das funcionalidades requeridas é que o usuario posso realizar a avaliação de um filme passando uma nota 
com parametro e que essa nota seja salva no atributo especifico da classe

2- Assim que uma avalição for realizada, deve ser incrementado o total de avaliadores daquele filme passando uma
nota com parametro e que essa nota seja salva no atributo especifico da classe 

3- Para cada filme ter uma nota de avaliação media que consiste na divisão do total de avaliação pelo total de avaliadores



"""

class Movie():
    def __init__(self, name):
        self.name = name
    
    
    def getRate(self):
        note = input("Digite a nota do filme:")
        print(note)



mario = Movie("Mario Bros")
mario.getRate()
    