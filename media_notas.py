print("===Média de Notas===")

while True:
 escolha = int(input(f"1 - Calcular média da turma\n2 - Calcular minha média\n3- Sair\n"))

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

 elif escolha == 2:
    soma = 0
    contador = 0
    quantidade_notas = int(input("Quantida de notas: "))
    while contador != quantidade_notas:
        contador = contador + 1
        nota = float(input(f"Nota {contador}: "))
        soma = soma + nota
    media = soma / quantidade_notas
    print(f"Média: {media}")
    if media >= 6.0:
       print("Aprovado!")
    else:
       print("Reprovado!")
 elif escolha == 3:
    print("Encerrando o programa.")
    break
    
 else:
   print("Opção inválida!")