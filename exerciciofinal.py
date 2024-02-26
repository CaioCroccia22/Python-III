from contact_book import ContactBook, Contact

agenda_de_contato = ContactBook()

while True:
    print("\n------Opções agenda de contato------")
    print("1. Adicionar contato")
    print("2. Remover contato")
    print("3. Listar contato")
    print("4. Buscar contato")
    print("5. Sair")

    choice = input("Digite a opção que deseja:\n")

    if choice == "1":
        name = input("Digite o nome:\n")
        phone = input("Digite o telefone:\n")
        Email = input("Digite o e-mail:\n")

        contact = Contact(name, phone, Email)
        agenda_de_contato.addContact(contact)
        print("O contato foi adicionado com sucesso")

    elif choice == "2":
        name = input("Informe o nome para remover:\n")
        contact = agenda_de_contato.getContact(name)
        if contact:
            agenda_de_contato.deleteContact(contact)
            print("Contato removido com sucesso")
    elif choice == "3":
        contact = agenda_de_contato.listContact()
    elif choice == "4":
        name = input("Informe o nome para buscar contato:\n")
        contact = agenda_de_contato.getContact(name)
    elif choice == "5":
        break
    else:
        print("Opção inválida!")