print("===Tabuadas===")

numero = int(input("Digite o número que deseja saber a tabuada: "))
for i in range(1, 11): #range e logo depois, dentro do parenteses, temos o limite e o minimo
   print(f"{numero} x {i} = {numero * i}")