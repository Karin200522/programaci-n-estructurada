import time
lista = [100, 200, 400, 800, 1600]


def suma_objetivo(lista, objetivo):
    n = len(lista)
    for i in range(n):
        for j in range(i + 1, n):
            if lista[i] + lista[j] == objetivo:
                return True 
    return False

if __name__== "__main__":
    lista = [1, 2, 3, 4, 5]

    lista = [i for i in range(10000)]

    objetivo = 9 
    resultado = suma_objetivo(lista, objetivo)

    inicio = time.perf_counter()
    wait = suma_objetivo(lista, objetivo)
    final = time.perf_counter()
    print(f"Tiempo de ejecución: {final - inicio:.6f} segundos")



