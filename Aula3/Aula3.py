nota = float(input("Digite a primeira nota do estudante: "))

nota2 = float(input("Digite a segunda nota do estudante: "))

nota3 = float(input("Digite a terceira nota do estudante: "))

nota4 = float(input("Digite a quarta nota do estudante: "))


media = (nota + nota2 + nota3 + nota4) /4

print("A media do aluno é: ", media)

if media >= 7:
    print("O aluno está aprovado!")
elif media < 7 and media >= 5:
    print("O aluno está em recuperação!")
else:
    print("O aluno está reprovado!")