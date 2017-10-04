cod, qtd = input().split()
cod = int(cod)
qtd = int(qtd)
if cod == 1:
    valor = qtd * 4.00
elif cod == 2:
    valor = qtd * 4.50
elif cod == 3:
    valor = qtd * 5.00
elif cod == 4:
    valor = qtd * 2.00
elif cod == 5:
    valor = qtd * 1.50
print("Total: R$ {:.2f}".format(valor))