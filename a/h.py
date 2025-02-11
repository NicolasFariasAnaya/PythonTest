#Listas: Coleção ordenada, mutável e que permite valores duplicados
#Tuplas: Coleção ordenada, imutável e que permite valores duplicados
#Dicionarios: Coleção não oredenada, mutável e que não permite valores duplicados

#index     0        1       2  
lista = ["item", "item2", "item"]
tupla = ("item1", "item2", "item1")

dicio = {"chave" : "Cayque", "chave2" : 2003, "chave3" : True}
print(dicio)
dicio["chave"] = "Pedro"
print(dicio)
dicio.update({"chave" : "Cayo"})
print(dicio)
dicio.update({"Estado" : "Paraná"})
print(dicio)
print("-=-" * 20)

dicionario = {
    "Nome" : "Cayque",
    "Idade" : 20,
    "Nascionalidade" : "Brasileiro"
}

print(dicionario)
print(dicionario["Idade"])
print(dicionario.get("Idade"))
print(dicionario.keys())
print(len(dicionario))
print(dicionario.values())
print(dicionario.items())
print("-=-" * 20)

dados = {"Nome" : "Cayque", "Ano" : 2003, "valor_logico" : True}
print(dados)
dados.update({"Estado" : "Paraná"})
print(dados)
#Elimina o ultimo item
dados.popitem()
print(dados)
dados.pop("Nome")
print(dados)
del dados["Ano"]
print(dados)
dados.clear()
print(dados)
dados.update({"Nome" : "Cayque", "Estado" : "Paraná", "Ano" : 2003, "Nacionalidade" : "Brasileiro"})

for x in dados:
    print(x, dados[x])
print("-=-" * 20)

for x in dados.keys():
    print(x)

for x in dados.values():
    print(x)
print("-=-" * 20)

for x, y in dados.items():
    print(x, y)
print("-=-" * 20)

dicionar = dicio.copy()
print(dicionar)

dicionar2 = dict(dicio)
print(dicionar2)
print("-=-" * 20)

#index      0        1        2
tupla = ("item1", "item2", "item3")
x = 0
dita = dict.fromkeys(tupla, x)
print(dita)