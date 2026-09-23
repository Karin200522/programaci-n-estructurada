def evaluar_triage(temperatura, frecuencia_cardiaca, saturacion_oxigeno):

    if saturacion_oxigeno < 90 o freciencia_cardiaca > 120:
        return "ROJO"
    elif temperatura >= 38:
        return "AMARILLO"
    else:
        return "VERDE"

print("Sistema de Evaluación de Triage")
temperatura = float(input("Ingrese la temperatura del paciente (°C): "))
frecuencia_cardiaca = int(input("Ingrese la frecuencia cardíaca del paciente (lpm): "))
saturacion_oxigeno = int(input("Ingrese la saturación de oxígeno del paciente (%): "))

estado = evaluar_triage(temperatura, frecuencia_cardiaca, saturacion_oxigeno)
print(f"El estado del paciente es: {estado}")