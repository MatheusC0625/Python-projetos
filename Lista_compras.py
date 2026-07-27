print("===Lista de compras===")

lista = []
total = 0
escolha = int(input(f"Escolha uma opção\n1 - Adicionar produto\n2 - Ver lista\n3 - Ver total\n4 - Remover produto\n5 - Sair"))

while True:
   escolha = int(input(f"Escolha uma opção\n1 - Adicionar produto\n2 - Ver lista\n3 - Ver total\n4 - Remover produto\n5 - Sair"))
   if escolha == 1:
    produto = input("Nome do produto: ")
    lista.append(produto)
    preco = float("Valor do produto: ")
    total = preco + total
   elif escolha == 2:
    print(f"Lista de compras até o momento: \n{lista}")
   elif escolha == 3:
    print(f"Total da lista de compras até agora: \n{total}")
   elif escolha == 4:
    print(f"Lista de compras ate o momento: {lista}")
    produto = input("Nome do produto que deseja remover: ")
    lista.remove(produto)
   elif escolha == 5:
    print("Até mais!")
    break

  