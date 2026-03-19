while True:
    nota1 = float(input("Digite a primeira nota:"))
    nota2 = float(input("Digite a segunda nota:"))
    nota3 = float(input("Digite a terceira nota:"))
    media = (nota1 + nota2 + nota3) / 3
    if media >= 7:
        print("Aprovado! Média:", media)
    elif media >= 5:
        print("Recuperação! Média:", media)
    else:
        print("Reprovado. Média:", media)
    resposta = input("Continuar? (sair para encerrar):")
    if resposta == "sair":
        break