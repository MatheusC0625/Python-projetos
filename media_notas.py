print("===Média de Notas===")

while True:
 escolha = int(input(f"1 - Calcular média da turma\n2 - Calcular minha média\n"))

 if escolha == 1:
    soma = 0
    contador = 0
    alunos = int(input("Alunos presentes na sala: "))
    while contador != alunos:
        contador = contador + 1
        nota = float(input(f"Nota do aluno {contador}: "))
        soma = soma + nota
    media = soma / alunos
    print(f"Média da classe: {media:.2f}")
