# Utilizando la clase creada en el ejercicio anterior, 
# crea 5 hilos a partir de esta, almacénalos en una lista, 
# cambiales su nombre por miHilo-n, lánzalos y finalmente 
# espera por ellos desde el hilo principal utilizando el método join().

# Mide el tiempo total de ejecución del programa.

import threading
import time

class NumeroTres(threading.Thread):
    def __init__(self, id, nombre):
        super().__init__(name=nombre)
        self.id = id

    def run(self):
        print(f"Ejecutando el hilo{self.name}...")
        for i in range(1, 100):
            print(f"Valor: {i}")
            time.sleep(0.1)

if __name__ == "__main__":
    inicio = time.perf_counter()
    
    hilos = []

    for i in range(5):
        hilos.append(NumeroTres(i+1, f"miHilo{i+1}"))
        hilos[i].start()

    for hilo in hilos:
        hilo.join()

    fin = time.perf_counter()
    
    print(f"Tiempo de ejecucion del programa: {fin - inicio:.2f} segundos")