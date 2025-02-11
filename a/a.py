'''Exercicio para aprendizado 1° 
01 - Calcule a area de um retangulo
02 - Calcule a area de um quadrado
03 - Se o produto que voce quer avaliar custa (???) reais
qual será o valor dele com um desconto de (???)%?
04 - Area de um triangulo
05 - Conversão de Dolar pra Real
06 - Conversão de Real pra Dolar
'''

#01 - Area de um Retangulo.
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("Calculo para a area de um retangulo.")
base = float(input("Qual a base do retangulo? "))
altura = float(input("Qual a altura do retangulo? "))
retanguloarea = base * altura

print(f"O seu retangulo possui a area igual {retanguloarea}" )

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

#02 - Area de um Quadrado
print("Calculo para a area de um Quadrado")
lado = float(input("Qual o valor do lado do quadrado? "))
quadradoarea = lado ** 2

print(f"A area do quadrado é {quadradoarea}")

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

#03 - Calculo de desconto em porcentagem
total = float(input("O valor total sem desconto do produto: "))
desconto = float(input("O desconto oferecido em porcentagem: "))
valor = total * (100 - desconto) / 100

print(f"O valor final que terá que ser pago com o desconto é: {valor}")

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

#04 - Area de um Triangulo
bbase = float(input("A base do triangulo: "))
aaltura = float(input("A altura do triangulo: "))
area = bbase * aaltura / 2

print(f"A area do triangulo é {area}")

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

#05 - Conversão de Dolar para Real
dolar = float(input("Quantos dolares você tem? "))
Dolar = 4.85
compra = dolar * Dolar

print(f"Você tem {compra} reais.")

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

#06 - Conversão de Real para Dolar
real = float(input("Quantos reais você tem? "))
compra2 = real / Dolar

print(f"Você tem {compra2} dolares.")