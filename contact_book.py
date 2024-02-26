from contact import Contact
class ContactBook:
    def __init__(self):
        self.number_dict = {}

    def addContact(self, contac):
        self.number_dict[contac.name] = contac.phone, contac.Email

    def listContact(self):
        if not self.number_dict:
            print("Lista de contato vazia")
        else:
            for contact in self.number_dict:
                print(contact)
        
    def deleteContact(self, contact):
        if contact in self.number_dict:
            del self.number_dict[contact]
            

    def getContact(self, contact):
        if contact in self.number_dict:
            print(f"{self.number_dict[contact]}")
            return contact



