n1, n2, n3, n4 = input().split()

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media = ((n1*2) + (n2*3) + (n3*4) + (n4*1)) / 10

print("Media: {:.1f}".format(media))

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
elif (media >= 5.0) and (media <= 6.9):
    print("Aluno em exame.")

    exame = float(input())

    print("Nota do exame: {:.1f}".format(exame))

    nota_exame = (media + exame) / 2

    if nota_exame >= 5.0:
        print("Aluno aprovado.")
    elif nota_exame <= 4.9:
        print("Aluno reprovado.")
    print("Media final: {:.1f}".format(nota_exame))
