valor = float(input(''))

print("NOTAS:")

notas_cem = valor // 100
valor = valor % 100
print("{:.0f} nota(s) de R$ 100.00".format(notas_cem))

notas_cinquenta = valor // 50
valor = valor % 50
print("{:.0f} nota(s) de R$ 50.00".format(notas_cinquenta))

notas_vinte = valor // 20
valor = valor % 20
print("{:.0f} nota(s) de R$ 20.00".format(notas_vinte))

notas_dez = valor // 10
valor = valor % 10
print("{:.0f} nota(s) de R$ 10.00".format(notas_dez))

notas_cinco = valor // 5
valor = valor % 5
print("{:.0f} nota(s) de R$ 5.00".format(notas_cinco))

notas_dois = valor // 2
valor = valor % 2
print("{:.0f} nota(s) de R$ 2.00".format(notas_dois))
print("MOEDAS:")

moeda_umr = valor // 1
valor = valor % 1
print("{:.0f} moeda(s) de R$ 1.00".format(moeda_umr))

moeda_cinquenta = valor // 0.50
valor = valor % 0.50
print("{:.0f} moeda(s) de R$ 0.50".format(moeda_cinquenta))

moeda_vinte_cinco = valor // 0.25
valor = valor % 0.25
print("{:.0f} moeda(s) de R$ 0.25".format(moeda_vinte_cinco))

moeda_dez = valor // 0.10
valor = valor % 0.10
print("{:.0f} moeda(s) de R$ 0.10".format(moeda_dez))

moeda_cinco = valor // 0.05
valor = valor % 0.05
print("{:.0f} moeda(s) de R$ 0.05".format(moeda_cinco))

moeda_um = valor / 0.01
valor = valor % 0.01
print("{:.0f} moeda(s) de R$ 0.01".format(moeda_um))