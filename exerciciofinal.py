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
        
    def deleteContact(self, name):
        if name in self.number_dict:
            del self.number_dict[name]
            print(f"O contato {name} foi removido com sucesso!")

    def getContact(self, name):
        if name in self.number_dict:
            print(f"{name} -- {self.number_dict[name]}")




contact_book = ContactBook()
Caio = Contact("Caio", "2233", "dds@dsd")
Trabalho = Contact("Trabalho", "2233", "dds@dsd")
Faculdade = Contact("Faculdade", "223232", "wqewed@wewew")
contact_book.addContact(Caio)
contact_book.addContact(Trabalho)
contact_book.addContact(Faculdade)
contact_book.listContact()

contact_book.deleteContact("Caio")
contact_book.listContact

contact_book.getContact("Faculdade")