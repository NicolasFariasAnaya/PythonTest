#             0        1        2       3         4         5         6
lista1 = ["AnoNovo", "Amor", "Jogo", "Moscou", "Cayque", "Lisboa", "Tomou"]
print(lista1)
print(10 * "-=-=-=-")
lista2 = [2, 3, 4, 5, 6]
print(lista2)
print(10 * "-=-=-=-")
lista3 = [1.1, 2.2, 3.3, 4.4]
print(lista3)
print(10 * "-=-=-=-")
lista4 = [True, False]
print(lista4)
print(10 * "-=-=-=-")
# index =  0       1       2     3    4   5  6  --> 7 elementos
lista5 = [True, "Cayque", 2.5, False, 12, 4, 8]
print(lista5)
print(10 * "-=-=-=-")

print(type(lista1))
print(10 * "-=-=-=-")
print(type(lista2))
print(10 * "-=-=-=-")
print(type(lista3))
print(10 * "-=-=-=-")
print(type(lista4))
print(10 * "-=-=-=-")
print(type(lista5))
print(10 * "-=-=-=-")
print(" ")
print(10 * "-=-=-=-")

#Slicing
#Aqui temos que entender que o primeiro valor é por onde vai começar
print("  0       1       2     3    4   5  6  --> 7 elementos")
print(lista5[::]) # Retorna toda a lista
print(lista5[1:]) # Retorna o valor/posição que destacamos até o fim da lista
print(lista5[2:]) # Retorna o valor/posição que destacamos até o fim da lista
print(lista5[:3]) # Retorna o inicio da lista até o valor/posição que destacamos
print(lista5[:4]) # Retorna o inicio da lista até o valor/posição que destacamos
print(lista5[2:4]) # Retorna o valor que destacamos até o valor que foi destacado
print(lista5[1:4]) # Retorna o valor que destacamos até o valor que foi destacado
#obs: o ultimo valor nos 2 exemplos a cima não são classificados pois precisa ser lembrada a regra do -1 neste caso
print(lista5[0:7:2]) # Começa no index "0" e vai até o "7" (que na vdd é "6" pq é -1) pulando de 2 em 2
print(10 * "-=-=-=-")

nome = "Cayque"

print(nome[2:5])