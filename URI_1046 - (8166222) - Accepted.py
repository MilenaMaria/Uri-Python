inicial, final = input().split()

inicial = int(inicial)
final = int(final)

if inicial > final:
    hora = (24 - inicial) + final
elif final > inicial:
    hora = final - inicial
elif inicial == final:
    hora = 24

print("O JOGO DUROU {} HORA(S)".format(hora))