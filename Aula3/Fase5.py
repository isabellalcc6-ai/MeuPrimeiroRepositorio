tem_ingresso = (input("Você tem ingresso? (sim/não): "))
aniversariante = (input("Você é aniversariante? (sim/não): "))

if tem_ingresso == "sim" or aniversariante == "sim":
    print("Entrada liberada!")
else:
    print("Precisa comprar ingresso!")