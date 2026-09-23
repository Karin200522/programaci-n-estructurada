Money, Sumatoria_del_dia = 10000, 1000
retiro, op = 0, 0

print("Bienvenido al cajero automático, su saldo es:", Money)
print(f"ustested puede retirar hasta {Sumatoria_del_dia} por día")
retiro = float(input("Ingrese la cantidad a retirar: "))

Sumatoria_del_dia += retiro

if retiro %50 != 0:
    print("El monto a retirar debe ser múltiplo de 50.")
elif retiro > Money:
    print("Fondos insuficientes.")
elif Sumatoria_del_dia > 6000:
    print("Ha excedido el límite de retiro diario.")
else:
    Money -= retiro
    print("Retiro exitoso. Su nuevo saldo es:", Money)
