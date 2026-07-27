print("===Lista de compras===")

lista = []
total = 0

while True:
   escolha = int(input(f"Escolha uma opção\n1 - Adicionar produto\n2 - Ver lista\n3 - Ver total\n4 - Remover produto\n5 - Sair\n"))
                       
   if escolha == 1:
    produto = input("Nome do produto: ")
    lista.append(produto)
    preco = float(input("Valor do produto: "))
    total = preco + total
   elif escolha == 2:
    for item in lista:
     print(item)
   elif escolha == 3:
    print(f"Total da lista de compras até agora: \n{total:.2f}")
   elif escolha == 4:
    for item in lista:
     print(item)
    produto = input("Nome do produto que deseja remover: ")
    lista.remove(produto)
   elif escolha == 5:
    print("Até mais!")
    break

  