lista = ["carro", "moto", "aviao", "barco"]
print(lista)

#Remove um index/posicao expecifica
lista.pop()
print(lista)

#Remove um elemento especifico
lista.remove("moto")
print(lista)


for x in range(len(lista)):
    print(x, lista[x])