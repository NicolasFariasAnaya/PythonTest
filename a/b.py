'''Exercicio para aprendizado 1° 
01 - Implemente um programa que receba a idade de uma pessoa e imprima mensagem de
acordo com os critérios:
● Menor de 16 anos: MENOR
● Entre 16 e 18 anos: EMANCIPADO
● Maior de 18 anos: MAIOR

02 - Implemente um programa que receba a idade de um nadador e imprima a sua
categoria seguindo as regras:
● Infantil A | 5 ~ 7 anos
● Infantil B | 8 ~ 10 anos
● Juvenil A  | 11 ~ 13 anos
● Juvenil B  | 14 ~ 17 anos
'''

#01 Idade
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
idade = int(input("Insira sua idade: "))

if idade < 16:
    print("MENOR DE IDADE.")
elif 16 <= idade <= 18:
    print("EMANCIPADO.")
else:
    print("MAIOR DE IDADE.")

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

#02 Nadadores
idadenadador = int(input("Insira sua idade: "))

if 5 <= idadenadador <= 7:
    print("Sua categoria é: INFANTIL A")
elif 8 <= idadenadador <= 10:
    print("Sua categoria é: INFANTIL B")
elif 11 <= idadenadador <= 13:
    print("Sua categoria é: JUVENIL A")
elif 14 <= idadenadador <= 17:
    print("Sua categoria é: JUVENIL B")
else:
    print("Você não se encaixa em nenhuma das categorias.")