"""
1 - O metodo estático não utiliza o parametro referente a classe

2 - O metódo estático pode acessar mas não pode modificar o estado da classe

3 - Usamos o decorator @staticmethod para criar um método estático

"""


class Course:
    def __init__(self, name, trail):
        self.name = name
        self.trail = trail

    @staticmethod
    def courses_trail(trail):
        if trail == "Python Fundamentos":
            courses = ["Dominando o Python", "Modulos e PIP", "Orientação a Objeto"]
        elif trail == "Automação com o python":
            courses = ["Automação de Tarefas", "Web Scraping", "Assistente Virtual"
                       ]
        else:
            courses = ["A definir"]
        return courses

print(Course.courses_trail("Python Fundamentos"))