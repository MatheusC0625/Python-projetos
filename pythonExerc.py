def inverte(dicionario: dict) -> dict:
    retorno = {}
    for key in dicionario:
        value = dicionario[key]
        retorno[value] = key

traducao = {
    "apple": "maçã",
    "pineapple": "abacaxi",
    "orange": "laranja",
    "lime": "limão",
    "grape": "uva"
}

traducao["orange"] = "laranja"

pt = inverte(traducao)

for key in traducao:
    print(f"{key} => {traducao[key]}")