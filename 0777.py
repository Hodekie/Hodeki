opcao = 1
while opcao !=2:
    n = int(input("digite um numero: "))
    while n <= 0:
        n = int(input("inválido, Digite um numero: "))

        n = int(input("digite um numero: "))
    for x in range(1,n+1):
        print(f"{x}", end=" ")

    opcao = int(input("você deseja continuar?\n"
                     "digite 1 para sim: \n"
                     "digite 2 para não:  "))



