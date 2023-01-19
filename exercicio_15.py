valor = int(input("insira quanto ganha por hr trabalhada: "))
horas = int(input("insira quantas horas trabalhou no mes: "))
slb = valor* horas
inss = valor * horas * 0.08
sind = valor * horas * 0.05
renda = valor * horas * 0.11
liq = slb - (inss + sind + renda)

print(f"salario bruto igual: {slb}")
print(f"inss igual: {inss}")
print(f"sindicato igual: {sind}")
print(f"imposto de renda igual: {renda}")
print(f"salario liquido igual: {liq}")
