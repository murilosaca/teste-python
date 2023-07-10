# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# a = salário bruto.
# b = quanto pagou ao INSS.
# c = quanto pagou ao sindicato.
# d = o salário líquido.
# e = calcule os descontos e o salário líquido, conforme a tabela abaixo:

# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$

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
