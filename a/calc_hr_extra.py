#1° passo: definir quanto é o salario mensal
slr_mes = float(input("Qual o valor do salario mensal? R$:"))
vlr_hr = slr_mes/220
print (f"Seu valor por hora trabalhada é R$:{vlr_hr:.3}")

#2° passo: receber separadamente as horas extras: 50%, 100% (em horas e minutos "12:37")
hr_50prc = float(input("Quantas horas de 50% foram feitas?"))
hr_100prc = float(input("Quantas horas de 100% foram feitas?"))

vlr_hr_50prc = vlr_hr + (vlr_hr/2)
vlr_hr_100prc = vlr_hr*2

total_50prc = hr_50prc * vlr_hr_50prc
total_100prc = hr_100prc * vlr_hr_100prc

print(f"Horas de 50% ({hr_50prc}) = R${total_50prc:.2f}, Horas de 100% ({hr_100prc}) = R${total_100prc:.2f}")