import random

aprobadas = 0
rechazadas = 0
sospechoso = 0

cantidadNumeros = int(input("Ingrese cuántos números aleatorios quiere generar:  "))
for i in range (cantidadNumeros):
    numerosAleatorios = random.randint(000000, 999999)

    if numerosAleatorios %10 == 5:
        print(f" {numerosAleatorios} - Sospechoso")
        sospechoso += 1
    elif numerosAleatorios %2 == 0:
        print(f" {numerosAleatorios} - Aprobado")
        aprobadas += 1
    else:
        print(f" {numerosAleatorios} - Rechazado")
        rechazadas += 1


print("\n")
#Resumen numeros aleatorios
print("Resumen de Números Aleatorios")
print(f"Total Aprobadas:  {aprobadas}")
print(f"Total Rechazadas: {rechazadas}")
print(f"Total Sospechosos:  {sospechoso}")