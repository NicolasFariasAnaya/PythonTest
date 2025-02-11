esc_nums = int(input("Quantos números você deseja comparar? "))
contador = 1
nums = []

while contador <= esc_nums:
    num_nums = int(input(f"Digite o {contador}° número: "))
    nums.append(num_nums)
    contador += 1

def compara_maior(x):
    print(f"O maior número é: {max(x)}")

def media(x):
    print(f"A media dos números é: {sum(x)/2}")

compara_maior(nums)
media(nums)

def potencia(a, n):
    if n == 0:
        print("Seu valor é: 1")
    elif n < 0:
        print("Insira um valor maior ou igual a zero.")
    else:
        a = a ** n
        print(a)

x = int(input("Isira o 1° valor: "))
y = int(input("Isira o 2° valor: "))

potencia(x, y)