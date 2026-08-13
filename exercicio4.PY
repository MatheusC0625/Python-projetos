lista = [2, 5, -7, 9, 3, 10, 15, 6] #percorrer apenas o indice e não a lista

x = 11

for num in lista: #for in esta percorrendo os indices e não a lista
 for num2 in lista:
  if num + num2 == x:
   print(f"soma: {num}, {num2}")
   print("Achou!")