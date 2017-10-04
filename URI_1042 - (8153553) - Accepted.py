a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

if (a < b) and (a < c):
    print(a)
    if b < c:
        print(b)
        print(c)
    else:
        print(c)
        print(b)

elif (b < a) and (b < c):
    print(b)
    if a < c:
        print(a)
        print(c)
    else:
        print(c)
        print(a)

if (c < a) and (c < b):
    print(c)
    if b < a:
        print(b)
        print(a)
    else:
        print(a)
        print(b)

print()
print(a)
print(b)
print(c)
