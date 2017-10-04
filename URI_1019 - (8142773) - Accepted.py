tempo = int(input())

hora = tempo//3600
tempo = tempo % 3600
minutos = tempo//60
tempo = tempo % 60

print("{:.0f}:{:.0f}:{:.0f}".format(hora,minutos,tempo))
