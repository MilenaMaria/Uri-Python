from math import sqrt
a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

if a != 0:
    delta = b * b - (4 * a * c)
    if delta > 0:
        r1 = (-b + sqrt(delta)) / (2 * a)
        r2 = (-b - sqrt(delta)) / (2 * a)
        print("R1 = {:.5f}".format(r1))
        print("R2 = {:.5f}".format(r2))
    elif delta < 0:
        print("Impossivel calcular")
else:
    print("Impossivel calcular")