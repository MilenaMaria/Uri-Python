lista = input().split()

a, b,c, d = lista

if int(b) > int(c) and int(d) > int(a) and (int(c) + int(d)) > (int(a) + int(b)):
        print("Valores aceitos")
else:
    print("Valores nao aceitos")