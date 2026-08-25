Tem_ingresso = (input("Você tem ingresso? (sim/não): "))

aniversariante = (input("Você é aniversariante? (sim/não): "))

if Tem_ingresso == "sim":
    Tem_ingresso = True
else:
    Tem_ingresso = False

if aniversariante == "sim":
    aniversariante = True
else:
    aniversariante = False

if Tem_ingresso or aniversariante:
    print("Entrada liberada!")
else:
    print("Precisa comprar ingresso!")