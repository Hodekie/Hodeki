numerodealunos = int(input("diga quantos alunos tem: "))
nota = 0
for x in range(numerodealunos):
    notasalunos = float(input("digite a nota do aluno"))
    nota = nota + notasalunos
media = nota / numerodealunos
print(media)

