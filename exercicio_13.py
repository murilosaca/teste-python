# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

h = float(input("digite sua altura:"))
pesom = (72.7 * h) -58
pesof = (62.1*h) - 44.7

print(f"caso seja homem seu peso ideal é de: {pesom} kg")
print(f"caso seja mulher seu peso ideal é de: {pesof} kg")
