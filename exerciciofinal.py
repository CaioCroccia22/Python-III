from contact import Contact
class ContactBook:
    def __init__(self):
        self.number_dict = {}

    def addContact(self, contac):
        self.number_dict[contac.name] = contac.phone

    def listContact(self):
        if not self.number_dict:
            print("Lista de contato vazia")
        else:
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