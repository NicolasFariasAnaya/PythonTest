codigovoucher = input("Digite o codigo do voucher: ")
lista = []

for x in codigovoucher:
    if x == "S":
        x = 5
        lista.append(x)
    elif x == "0":
        x = "O"
        lista.append(x)
    elif x == "I":
        x = "L"
        lista.append(x)
    elif x == "5":
        x = "S"
        lista.append(x)
    else:
        lista.append(x)

concatenada = ""
print(codigovoucher)
print(lista)
print(concatenada)