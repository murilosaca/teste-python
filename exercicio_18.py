# Faça um programa que peça o tamanho de um arquivo para download (em MB) e
# a velocidade de um link de Internet (em Mbps), calcule e informe o tempo 
# aproximado de download do arquivo usando este link (em minutos).


aq = int(input("insira o tamanho do arquivo:"))
velo = int(input("insira a velocidade de um link da internet:"))
td = aq/velo
resposta = td/60

print(f"seu arquivo demorará {resposta} minutos")
