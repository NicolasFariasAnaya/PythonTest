#Listas: Coleção ordenada, mutável e que permite valores duplicados
#Tuplas: Coleção ordenada, imutável e que permite valores duplicados
#Dicionarios: Coleção não oredenada, mutável e que não permite valores duplicados
#Sets: Coleção não ordenada, não mutavel e que não permite valores duplicados

set1 = {"item1", "item2", "item3"}
print(type(set1))
print(set1)
print(len(set1))

#Adicionar elementos
set1.add("item4")
print(set1)
set1.add(8)
set1.add(True)
print(set1)
print("-=-" * 20)

set2 = {4, 5, 7, 8, 9, 1}
set2.update(["item3", "item5", "item1"])#Adicionando uma lista
print(set2)
print("-=-" * 20)

set3 = {4, 5, 7, 8, 9, 1}
set3.update((1, 4, 7, 8, 9, 3))#Adicionando uma tupla
print(set3)
print("-=-" * 20)

#Removendo elementos
set4 = {1, 3, 4, 5, "item5", 7, 8, 9, "item6"}
print(set4)

set4.pop()#Remove items aleatorios do conjunto/set
print(set4)
print("-=-" * 20)

set5 = {1, 3, 4, 5, "item5", 7, 8, 9, "item6"}
set5.remove("item5")
set5.discard("item9")
print(set5)
set5.clear()
del set4
print("-=-" * 20)

#Gerando um conjunto novo
conjunto1 = {1, 5, 8, 9}
conjunto2 = {3, 6, 2}

conjunto3 = conjunto1.union(conjunto2)
print(conjunto3)

#Sem gerar um conjunto novo
conjunto4 = {1, 5, 8, 9}
conjunto5 = {3, 6, 2}

conjunto4.update(conjunto5)
print(conjunto4)
print("-=-" * 20)

a = {1, 5, 3, 2}
b = {3, 6, 2}

a.intersection_update(b)#Intersection só pega os valores que se repetem
print(a)

c = {1, 5, 3, 2}
d = {3, 6, 2}

c.symmetric_difference_update(d)#Valores que não se repetem 
print(c)
