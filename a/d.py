#01 . Organizador de Números. Faça com que ele separe e atualize 5 variaveis em ordem numerica.

num1 = int(input("Insira o primeiro valor: "))
num2 = int(input("Insira o segundo valor: "))
num3 = int(input("Insira o terceiro valor: "))
num4 = int(input("Insira o quarto valor: "))
num5 = int(input("Insira o quinto valor: "))
backup = 0

while num4 > num5:
    backup = num5
    num5 = num4
    num4 = backup
while num3 > num4:
    backup = num4
    num4 = num3
    num3 = backup
while num2 > num3:
    backup = num3
    num3 = num2
    num2 = backup
while num1 > num2:
    backup = num2
    num2 = num1
    num1 = backup
#-=-=-
while num4 > num5:
    backup = num5
    num5 = num4
    num4 = backup
while num3 > num4:
    backup = num4
    num4 = num3
    num3 = backup
while num2 > num3:
    backup = num3
    num3 = num2
    num2 = backup
#-=-=-
while num4 > num5:
    backup = num5
    num5 = num4
    num4 = backup
while num3 > num4:
    backup = num4
    num4 = num3
    num3 = backup
#-=-=-
while num4 > num5:
    backup = num5
    num5 = num4
    num4 = backup

print(num1, num2, num3, num4, num5)

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

num1 = int(input("Insira o primeiro valor: "))
num2 = int(input("Insira o segundo valor: "))
num3 = int(input("Insira o terceiro valor: "))
num4 = int(input("Insira o quarto valor: "))
num5 = int(input("Insira o quinto valor: "))

while num4 > num5:
    num4, num5 = num5, num4
while num3 > num4:
    num3, num4 = num4, num3
while num2 > num3:
    num2, num3 = num3, num2
while num1 > num2:
    num1, num2 = num2, num1

#-=-=-

while num4 > num5:
    num4, num5 = num5, num4
while num3 > num4:
    num3, num4 = num4, num3
while num2 > num3:
    num2, num3 = num3, num2

#-=-=-

while num4 > num5:
    num4, num5 = num5, num4
while num3 > num4:
    num3, num4 = num4, num3

#-=-=-

while num4 > num5:
    num4, num5 = num5, num4

#-=-=-

print(num1, num2, num3, num4, num5)