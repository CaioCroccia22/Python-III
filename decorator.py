"""
Decorator - É um padrão de projeto que permite
adicionar um comportamento a um objeto já existente em tempo
de execução
Ex: @staticmehod e @staticmethod
Oferecem uma alternativa flexível ao uso de herança
para estender uma funcionalidade -> Adiociona um responsabilidade ao objeto e não a classe

Aplicabilidade :

Acrescentar responsabilidades a um objeto dinamicamente

Pode usar um ou mais decoradores para englobar um objeto

Muito utilizado  em frameworks Web como Flask e Django

"""

# Criando Decorators

def my_decorator(func):
    # wrapper - boa pratica
    def wrapper():
        print("Antes de executar a função")
        func()
        print("Depois de executar a função")
    return wrapper


def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

def split_string(function):
    def wrapper():
        func = function()
        split_string = func.split()
        return split_string
    return wrapper