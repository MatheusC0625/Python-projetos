print("===Conversor de Temperatura===")

escolha = int(input(f"1 - Celsius para Fahrenheit\n2 - Celsius para Kelvin\n3 - Fahrenheit para Celsius\n4 - Fahrenheit para Kelvin\n5 - Kelvin para Celsius\n6 - Kelvin para Fahrenheit\n"))

if escolha == 1:
    c = float(input("Celsius: "))
    x = (c * 9/ 5) + 32
    print(f"Convertendo: {x:.2f}")
elif escolha == 2:
    c = float(input("Celsius: "))
    x = c + 273.15
    print(f"Convertendo: {x:.2f}")
elif escolha == 3:
    f = float(input("Fahrenheit: "))
    x = (f - 32) * 5/9
    print(f"Convertendo: {x:.2f}")
elif escolha == 4:
    f = float(input("Fahrenheit: "))
    x = (f - 32) * 5/9 + 273.15
    print(f"Convertendo: {x:.2f}")
elif escolha == 5:
    k = float(input("Kelvin: "))
    x = k - 273.15
    print(f"Convertendo: {x:.2f}")
elif escolha == 6:
    k = float(input("Kelvin: "))
    x = (k - 273.15) * 9/5 + 32
    print(f"Convertendo: {x:.2f}") #APRENDI COM O CLAUDE COMO DEIXAR AS CASAS DECIMAIS CERTINHAS, tentar lembrar daqui 
else:
    print("Opção inválida! Tente novamente.")
