lista1 = [1, 2, 3, 4, 5]
lista2 = [1.1, 2.2, 3.3, 4.4, 5.5]
lista3 = ["Cayque Pereira Ceccon", "Nicolas Farias Anaya", "Matheus Romeike Kauva"]

lista1 += lista2

print(lista1)
#"LEN" conta quantos itens tem dentro da lista. "LEN" vem do length que significa COMPRIMENTO em ingles
print(len(lista1))
print(sum(lista2))# Soma todos os elementos da lista
print(max(lista2))# Pega o maior valor da lista e retorna
print(min(lista2))# Pega o menor valor da lista e retorna

frase = list(lista3[2])

print(frase)

espaco = 0
letras = 0

for letra in frase:
    if letra == " ":
        espaco += 1
    elif letra != " ":
        letras += 1

print("Quantidade de letras:", letras)
print("Quantidade de espaços:", espaco)

for x in range(len(lista3)):
    print(x, lista3[x])

texto = "A paciencia não é uma virtude, ela é A virtude"
lista4 = list(texto)
print(lista4)

texto = texto.split(",")
print(texto)
