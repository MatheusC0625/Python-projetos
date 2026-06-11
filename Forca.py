import random

chutes = ""
tentativas = 6
acertou = False

palavras = ["abacaxi", "banana", "melancia", "morango", "uva", "manga", "laranja", "limao", "pera", "maca",
            "cachorro", "gato", "elefante", "girafa", "leao", "tigre", "cobra", "macaco", "cavalo", "peixe",
            "futebol", "basquete", "tenis", "natacao", "volei", "boxe", "ciclismo", "golfe", "surfe", "karate",
            "computador", "teclado", "mouse", "monitor", "impressora", "celular", "tablet", "camera", "televisao",
            "brasil", "argentina", "franca", "alemanha", "japao", "china", "italia", "portugal", "mexico", "canada"]

palavra = random.choice(palavras)

while tentativas > 0 and not acertou:
    for x in palavra:
        if x in chutes:
            print(x, end=" ")
        else:
            print("_", end=" ")
    print()

    letra = input("Digite uma letra: ").lower()
    chutes = chutes + letra

    if letra not in palavra:
        tentativas = tentativas - 1
        print(f"Errou! Tentativas restantes: {tentativas}")

    acertou = True
    for x in palavra:
        if x not in chutes:
            acertou = False

if acertou:
    print(f"Parabéns, você acertou a palavra: {palavra}!")
else:
    print(f"Você perdeu! A palavra era: {palavra}")