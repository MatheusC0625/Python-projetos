import random

jogarNovamente = "sim"

while jogarNovamente == "sim":
    print("===Bem-vindo ao jogo da adivinhação===")
    nome = input("Para começar digite seu nome: ")
    print(f"Certo {nome}, aqui estão as regras:\n1- O sistema irá sortear um número inteiro de 1 a 10, 1 a 50 ou 1 a 100\n2- Quando o jogo acabar (independente do resultado), você pode escolher continuar ou parar")

    escolhaMargem = int(input("Escolha qual a margem de números que você quer\n1- 1 a 10\n2- 1 a 50\n3- 1 a 100\nEscolha: "))

    if escolhaMargem == 1:
        numero_secreto = random.randint(1, 10)
    elif escolhaMargem == 2:
        numero_secreto = random.randint(1, 50)
    elif escolhaMargem == 3:
        numero_secreto = random.randint(1, 100)
    else:
        print("Opção inválida!")
        continue

    chute = int(input("Chute: "))

    while chute != numero_secreto:
        if chute < numero_secreto:
            print("O número secreto é maior!")
        else:
            print("O número secreto é menor!")
        chute = int(input("Tente novamente: "))

    print(f"Parabéns {nome}, você acertou! O número era {numero_secreto}.")

    jogarNovamente = input("Deseja jogar novamente? (sim/nao): ")

print("Obrigado por jogar, até mais!")