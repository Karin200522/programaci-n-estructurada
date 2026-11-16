
from pathlib import Path

import pandas as pd

df = pd.read_csv(Path(__file__).with_name("pacientes.csv"))


df["imc"] = df["peso_kg"] / df["estatura_m"] ** 2


bins = [0, 18.5, 25, 30, 100]
labels = ["Bajo peso", "Normal",
          "Sobrepeso", "Obesidad"]


df["categoria"] = pd.cut(df["imc"], bins=bins, labels=labels, right=False)

print("b) Primeros pacientes con su IMC y categoría:")
print(df[["id", "peso_kg", "estatura_m", "imc", "categoria"]].round({"imc": 1}).head(10))


print("c) Pacientes por categoría:")
print(df["categoria"].value_counts())

sin_imc = df[df["imc"].isna()]
print("   Pacientes sin IMC:", len(sin_imc))
print(sin_imc[["id", "peso_kg", "estatura_m"]])
print("   Quedaron sin IMC porque les falta el peso (peso_kg vacío),")
print("   y cualquier operación con un dato faltante (NaN) da NaN.")