import csv 


def leer_archivo_csv(pacientes_mini):
    datos=[]
    with open(pacientes_mini, mode='r', newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            datos.append(fila)
    return datos


def escribir_archivo_csv(pacientes_mini, datos):
    with open(pacientes_mini, mode='w', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(datos)

if __name__ == "__main__":
    nombre_archivo = "pacientes_mini.csv"
    datos = leer_archivo_csv(nombre_archivo)
    print("Datos leídos del archivo CSV:")
    for fila in datos:
        print(fila)
