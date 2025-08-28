# Aula 27.08

familia = {"Pai": "Fábio",
           "Mãe" : "Cristiene",
           "Filhos": ["Alice", "Lucas", "Sofia", "João Vitor"]}

for key, valor in familia.items():
    if type(valor) == list:
        print("Filhos:")
        for i, nome in enumerate(valor):
            if i == (len(valor) - 1):
                print(f"- {nome}.")
            else:
                print(f"- {nome};")
    else:
        print(f"{key}: {valor};")