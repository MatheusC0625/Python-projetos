alimentos = [  #uma list de dict é uma lista onde cada item é um dicionario
    {"Nome": "Uva", "Cor": "Roxa", "Tipo": "Fruta"},
    {"Nome": "Maçã", "Cor": "Vermelho", "Tipo": "Fruta"},
    {"Nome": "Abacaxi", "Cor": "Amarela (predominantemente)", "Tipo": "Fruta"}
    ]

for fruta in alimentos:
    print(f"Fruta:", fruta["Nome"], "Cor:", fruta["Cor"])