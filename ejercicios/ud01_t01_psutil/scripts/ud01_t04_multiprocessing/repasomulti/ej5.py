import multiprocessing

def cuadrado(numero): 
    return numero ** 2

if __name__ == '__main__':
    numeros = [1,2,3,4,5]

    with multiprocessing.Pool() as pool:
        resultados = pool.map(cuadrado, numeros)

    print(f"Resultados: {resultados}")