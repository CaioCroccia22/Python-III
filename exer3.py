from exe3 import Travel

trip0 = Travel("Campos do Jordão")
trip1 = Travel("Gramado")

print("Temos ofertas para você")
traveler = input("Digite seu nome para começar: ")
print(f"{traveler}, temos destinos para você\n"
      "[0] - Campos do Jordão\n"
      "[1] - Gramado")

choice = input("Digite a opção que você deseja: ")
list_trip = [trip0,trip1]
if int(choice) >= 2:
    print("Esta opção não está incluída nos destinos")
else:
    print(f"{traveler}, sua viagem para {list_trip[int(choice)].destiny} está marcada")
