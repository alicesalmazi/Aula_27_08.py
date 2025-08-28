# Aula 27.08 - Revisão
import os

# For
familia = {"Pai": "Fábio",
           "Mãe" : "Cristiene",
           "Filhos": ["Alice", "Lucas", "Sofia", "João Vitor"]}

for key, valor in familia.items():
    if type(valor) == list:
        print("Filhos:")
        for i, nome in enumerate(valor):
            if i == (len(valor) - 1):
                print(f"- {nome}.\n")
            else:
                print(f"- {nome};")
    else:
        print(f"{key}: {valor};")

os.system('pause')
os.system('cls')

# While
import random

lista = []
for _ in range(10):
    lista.append(random.randint(1, 10))

indice = 0
print("Lista Aleatória (8 itens):")
while indice < 8:
    if indice == 7:
        print(f"- {lista[indice]}.")
    else:
        print(f"- {lista[indice]};")
    indice += 1