import numpy as np

sistolica = np.array(
    [118, 135, 142, 110, 128, 155, 121]
)

promedio = sistolica.mean()
desviacion = sistolica.std()  

print("a) Promedio:", round(promedio, 2), "mmHg")
print("   Desviación estándar:", round(desviacion, 2), "mmHg")

mascara = sistolica >= 130
cuantas = mascara.sum()  

print("b) Máscara:", mascara)
print("   Lecturas >= 130 mmHg:", cuantas)

posiciones = np.flatnonzero(mascara)

print("c) Posiciones:", posiciones)
print("   Valores en esas posiciones:", sistolica[posiciones])