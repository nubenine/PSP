# Crea un hilo en cuyo método run() muestre los valores entre 
# 1 y 100 acompañados del identificador del hilo y su nombre. 

# Introduce una espera de 0.1 segundo antes de imprimir cada número. 

# Haz que el hilo principal espere por la finalización del hilo 
# secundario utilizando el método join(). 

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
    hilo1 = NumeroTres(1, "1")
    hilo2 = NumeroTres(2, "2")

    inicio = time.perf_counter()

    hilo1.start()
    hilo1.join()

    hilo2.start()
    hilo2.join()

    fin = time.perf_counter()

    print(f"Tiempo de ejecucion del programa: {fin - inicio:.0f} segundos")