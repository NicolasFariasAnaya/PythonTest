listados = open("matriculas.txt", "r")
desligados = open("Desligados.txt", "r")
lista = []
lista2 = []

for x in listados:
    lista.append(x)

for i, elemento in enumerate(lista):
    if elemento in lista[i+1:]:
        print(f'Elemento repetido: {elemento}')

for x in desligados:
    lista2.append(x)

for i, elemento in enumerate(lista2):
    if elemento in lista2[i+1:]:
        print(f'Elemento repetido: {elemento}')

print(len(lista))
print(len(lista2))

def instersection(lista, lista2):
    return set(lista).intersection(lista2)

print("-="*20)

for x in instersection(lista, lista2):
    print(x)

listados.close()
desligados.close()