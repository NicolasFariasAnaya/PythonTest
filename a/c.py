#Joguinho de advinhação

numero = 9
advinhacao = 0

while advinhacao != numero:
    advinhacao = int(input("Tente advinhar o número de 1 a 10: "))
    if advinhacao == numero:
        break
    print("Número errado, tente novamente")
print("Parabéns, você acertou.")

#Fatorial

fatorial = 1
num = int(input("Qual o numero a ser calculado o fatorial? "))

if num < 0:
    print(f"Não existe fatorial deste numero: {num}")
elif num == 0:
    print("O valor do fatorial é: 0")
else:
    for x in range(1, num+1):
        fatorial *= x
    print(f"O fatorial de {num} é: {fatorial}")

#Descobrir se o numero é primo

numero = int(input("Isira um número para descobrir se ele é primo: "))

if numero > 1:
    for x in range(2,numero):
        if (numero % x) == 0:
            print("Este número não é primo.")
            break
    else:
        print("Este número é primo.")
else: 
    print("Este número não é primo: número menor ou igual a 1.")
