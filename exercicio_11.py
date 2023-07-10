# código que peça 2 números inteiros e um número real. Calcule e mostre:
# a = o produto do dobro do primeiro com metade do segundo .
# b= a soma do triplo do primeiro com o terceiro.
# c = terceiro elevado ao cubo.

a = int(input("Insira um número inteiro:"))
b = int(input("Insira outro número inteiro:"))
c = int(input("Insira um número natural:"))

if c < 0:
    print("Não é válido")
else:
    print(a*2*(b/2),
    3*a + c,
    c**3)
