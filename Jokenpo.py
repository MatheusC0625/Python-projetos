import random
print("Bem-vindo ao pedra,papel ou tesoura!")
opcoes = ["pedra", "papel", "tesoura"]

escolhaUser = input("Escolha entre pedra, papel e tesoura: ") #lembrar que essa é a linha para o jogo continuar


while escolhaUser not in opcoes:
    print("Opção inválida!")
    escolhaUser = input("Escolha entre pedra, papel e tesoura: ")


escolhaBot = random.choice(opcoes)

if escolhaUser == "tesoura" and escolhaBot == "tesoura":
    print("Escolha do bot:", escolhaBot)
    print("Sua escolha:", escolhaUser)
    print("Empate! Os dois escolheram a mesma opção.")

elif escolhaUser == "papel" and escolhaBot == "papel":
    print("Escolha do bot:", escolhaBot)
    print("Sua escolha:", escolhaUser)
    print("Empate! Os dois escolheram a mesma opção.")

elif escolhaUser == "pedra" and escolhaBot == "pedra":
    print("Escolha do bot:", escolhaBot)
    print("Sua escolha:", escolhaUser)
    print("Empate! Os dois escolheram a mesma opção.")

elif escolhaUser == "papel" and escolhaBot == "tesoura":
    print("Escolha do bot:", escolhaBot)
    print("Sua escolha:", escolhaUser)
    print("O bot ganhou! Tesoura corta o papel.")

elif escolhaUser == "tesoura" and escolhaBot == "pedra":
    print("Escolha do bot:", escolhaBot)
    print("Sua escolha:", escolhaUser)
    print("O bot ganhou! Pedra esmaga a tesoura.")

elif escolhaUser == "pedra" and escolhaBot == "papel":
    print("Escolha do bot:", escolhaBot)
    print("Sua escolha:", escolhaUser)
    print("O bot ganhou! Papel engole a pedra.")

elif escolhaBot == "papel" and escolhaUser == "tesoura":
    print("Escolha do bot:", escolhaBot)
    print("Sua escolha:", escolhaUser)
    print("O user ganhou! Tesoura corta o papel.")

elif escolhaBot == "tesoura" and escolhaUser == "pedra":
    print("Escolha do bot:", escolhaBot)
    print("Sua escolha:", escolhaUser)
    print("O user ganhou! Pedra esmaga a tesoura.")

elif escolhaBot == "pedra" and escolhaUser == "papel":
    print("Escolha do bot:", escolhaBot)
    print("Sua escolha:", escolhaUser)
    print("O user ganhou! Papel engole a pedra.")
else:
    print("Você quebrou o jogo, parabéns.")
    