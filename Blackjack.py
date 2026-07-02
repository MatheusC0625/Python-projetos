cartas = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4

mao_jogador = []
mao_dealer = []

import random
random.shuffle(cartas)

mao_jogador.append(cartas.pop())
mao_dealer.append(cartas.pop())

mao_jogador.append(cartas.pop())
mao_dealer.append(cartas.pop())

print("===Blackjack===")
print("Sua mão:", sum(mao_jogador))
print("Mão do dealer:", mao_dealer[0], "e uma carta escondida.")

while sum(mao_jogador) < 21:
    pergunta = input("Pegar uma carta ou parar? (pegar/parar)")
    if pergunta == "pegar":
        mao_jogador.append(cartas.pop())
        print("Sua mão:", sum(mao_jogador))
    elif pergunta == "parar":
        print("Você parou, sua mão:", sum(mao_jogador))
        break
    else:
        print("Comando inválido!")

if sum(mao_jogador) > 21:
    print("Você perdeu!")
else:
    while sum(mao_dealer) < 17:
        mao_dealer.append(cartas.pop())

    if sum(mao_dealer) > 21:
        print(f"Você ganhou com a mão de {sum(mao_jogador)} e o dealer perdeu com a mão de {sum(mao_dealer)}. Parabéns!")
    elif sum(mao_dealer) < sum(mao_jogador):
        print(f"Você ganhou com a mão de {sum(mao_jogador)} e o dealer perdeu com a mão de {sum(mao_dealer)}. Parabéns!")
    elif sum(mao_dealer) > sum(mao_jogador):
        print(f"O dealer ganhou com a mão de {sum(mao_dealer)} em cima da sua mão de {sum(mao_jogador)}")
    else:
        print("Empate!")