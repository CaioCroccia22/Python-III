from decorator import my_decorator, uppercase_decorator, split_string

# Exemplo 1
@my_decorator
def my_function():
    print("Dentro da função")


my_function()

# exemplo 2
@uppercase_decorator 
def text():
    return "Hello World"

print(text())

@split_string
def exampl():
    return "Hello World"

print(exampl())

""""
Decorator não é nada mais do que a adição de um comportamento dinamico
"""