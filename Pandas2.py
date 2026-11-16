

from pathlib import Path

import pandas as pd

df = pd.read_csv(Path(__file__).with_name("pacientes_mini.csv"))


fiebre = df["temperatura"] >= 38
taquicardia = df["frecuencia_cardiaca"] > 100
alerta = df[fiebre & taquicardia]


print("b) Pacientes con fiebre y taquicardia:", len(alerta))
print(alerta[["id", "temperatura", "frecuencia_cardiaca", "estudio"]])

print("c) Estudios:")
print(alerta["estudio"].value_counts())