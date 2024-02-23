"""
Agenda de contatos
Desenvolva uma agenda de contatos utilizando POO

1 - Ter uma classe Contact contend os atributos name, phone, E-mail

2 - Ter uma class ContactBook contendo quatro metodos
 a. Um metodo para adiciona contato
 b. Um metodo para listar os contatos
 c. Um metodo para buscar contatos
 d. Um metodo para remover contatos

3 - Criar um arquivo principal para a aplicação que deve instanciar 
as duas classes criadas anteriormente e desenvolver e chamar cada um dos metodos
dos metodos desenvolvidos de acordo com a opção escolhida
"""

class Contact:

    def __init__(self, name, phone, Email):
        self.name = name
        self.phone = phone
        self.Email = Email

class ContactBook:
    def __init__(self):
        self.number_dict = {}

    def addContact(self, contac):
        self.number_dict[contac.name] = contac.phone

    def listContact(self):
        for name, phone in self.number_dict.items():
            print(f"{name} -- {phone}")
        

contact_book = ContactBook()
Caio = Contact("Trabalho", "2233", "dds@dsd")
contact_book.addContact(Caio)
contact_book.listContact()