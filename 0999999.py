n = 1
soma = 0
qtd = int(input("digite a quantidade de alunos: "))
while n < qtd + 1:
    print(f"estamos no passo {n} e a soma é {soma}")
    nota = float(input("digite a nota"))
    soma = soma + nota
    n = n + 1
    media = nota / qtd
    print(media)
