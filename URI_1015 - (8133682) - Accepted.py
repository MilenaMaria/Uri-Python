from math import sqrt

lista_01 = input().split()
lista_02 = input().split()

x1,y1 = lista_01
x2,y2 = lista_02

dist = sqrt((float(x2)-float(x1))**2 +(float(y2)-float(y1))**2)

print("{:.4f}".format(dist))
