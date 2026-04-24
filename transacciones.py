import random #para los valores aleatorios

#Pedir al usuario cantidad de transacciones
numeroTransacciones = int(input("Ingrese cantidad de transacciones a realizar:   "))
#lista de nombres
listaNombres = ["Sophie Karlic", "Jose Gutierrez", "Ana Romero", "Luis Gallardo"]

#Para resumen transacciones
aprobadas = 0
rechazadas = 0

#Motivo Rechazos
RechazadoInactivo = 0
RechazadoMontoInvalido = 0
RechazadoSuperaLimite = 0
RechazadoSaldoInsuficiente = 0

#Montos aprobados
MontosAprobados = []

#Rechazos por usuario
RechazosPorUsuario = {}

#generar datos aleatorios
for i in range(numeroTransacciones):
    numeroTransaccion = random.randint (10000000, 99999999)
    nombreUsuario = random.choice(listaNombres)
    saldoDisponible = random.randint(100000, 5000000)
    montoTransferir = random.randint(10000, 3000000)
    usuario = random.choice ([True, False]) #activo o inactivo

    print(f"\n  Transacción  {i + 1}  ")
    print(f"número de Transacción:  {numeroTransaccion}")
    print(f"usuario:    {nombreUsuario}")
    print(f"Saldo Disponible:  ${saldoDisponible}")
    print(f"Monto a transferir: ${montoTransferir}")

    if usuario == False:
        print("Inactivo")
        rechazadas += 1
        RechazadoInactivo += 1
        if nombreUsuario in RechazosPorUsuario:
            RechazosPorUsuario[nombreUsuario] += 1
        else:
            RechazosPorUsuario[nombreUsuario] = 1
    elif montoTransferir <= 0:
        print("Monto inválido")
        rechazadas += 1
        RechazadoMontoInvalido += 1
        if nombreUsuario in RechazosPorUsuario:
            RechazosPorUsuario[nombreUsuario] += 1
        else:
            RechazosPorUsuario[nombreUsuario] = 1
    elif montoTransferir > 2000000:
        print("Monto supera el límite permitido")
        rechazadas += 1
        RechazadoSuperaLimite += 1
        if nombreUsuario in RechazosPorUsuario:
            RechazosPorUsuario[nombreUsuario] += 1
        else:
            RechazosPorUsuario[nombreUsuario] = 1
    elif saldoDisponible < montoTransferir:
        print("Saldo Insuficiente")
        rechazadas += 1
        RechazadoSaldoInsuficiente += 1
        if nombreUsuario in RechazosPorUsuario:
            RechazosPorUsuario[nombreUsuario] += 1
        else:
            RechazosPorUsuario[nombreUsuario] = 1
    else:
        print("Transferencia exitosa")
        aprobadas += 1
        MontosAprobados.append(montoTransferir)

print("\n")
#Resumen Final
print("Resumen de Transacciones Realizadas")
print(f"Total Aprobadas:  {aprobadas}")
print(f"Total Rechazadas: {rechazadas}")
print(f"Rechazadas por Usuario Inactivo:  {RechazadoInactivo}")
print(f"Rechazadas por Monto Invalido:   {RechazadoMontoInvalido}")
print(f"Rechazadas por Monto Superado:   {RechazadoSuperaLimite}")
print(f"Rechazadas por Saldo Insuficiente:   {RechazadoSaldoInsuficiente}")

if MontosAprobados:
    print(f"Transaccion Mayor Monto:   ${max(MontosAprobados):,}")
    print(f"Transaccion Menor Monto:   ${min(MontosAprobados):,}")
    print(f"Promedio de Montos:    ${sum(MontosAprobados) / len(MontosAprobados):,.2f}")
else:
    print("No se encontraron transacciones aprobadas.")

print("Usuarios con más de una transacción rechazada:  ")
for usuario, cantidad in RechazosPorUsuario.items():
    if cantidad > 1:        
        print(f"   {usuario}: {cantidad} rechazos")   



    




