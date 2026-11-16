import numpy as np


datos = np.array([
    [36.5,  72,  95],
    [38.2, 104, 140],
    [37.0,  80,  88],
    [36.8,  65, 110],
    [39.1, 112, 125],
])


minimo = datos.min(axis=0)
maximo = datos.max(axis=0)

print("Mínimo por columna:", minimo, "forma:", minimo.shape)
print("Máximo por columna:", maximo, "forma:", maximo.shape)

normalizado = (datos - minimo) / (maximo - minimo)

print("a) Datos normalizados:")
print(np.round(normalizado, 3))

min_norm = normalizado.min(axis=0)
max_norm = normalizado.max(axis=0)

print("c) Mínimo de cada columna:", min_norm)
print("   Máximo de cada columna:", max_norm)
print("   ¿Todos los mínimos son 0?", np.allclose(min_norm, 0))
print("   ¿Todos los máximos son 1?", np.allclose(max_norm, 1))