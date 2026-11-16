from pathlib import Path

import pandas as pd

df = pd.read_csv(Path(__file__).with_name("pacientes_mini.csv"))

filas, columnas = df.shape
print("a) Pacientes:", filas)
print("   Columnas:", columnas)

faltantes = df.isna().sum()

faltantes = faltantes[faltantes > 0]
print("b) Columnas con faltantes:")
print(faltantes)


print("c) Tipo de dato de cada columna:")
print(df.dtypes)