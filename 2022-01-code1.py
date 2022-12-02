with open("2022-01-input.txt") as arquivo:
    lista_elfos = arquivo.read().split("\n\n")

lista_total_cal_por_elfo = []
print(lista_elfos)


for elfo in lista_elfos:
    elfo.split("\n")
    soma_cal = 0
    print(elfo)
#    for suprimento in elfo:
#        print(suprimento)
#        soma_cal=+ int(suprimento)
#    lista_total_cal_por_elfo.append(soma_cal)

#print(lista_elfos)
#print(lista_total_cal_por_elfo)
