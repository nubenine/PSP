# Crea 3 hilos que se dormirán un tiempo comprendido 
# entre 0 y 10 segundos (tiempo calculado aleatoriamente).

# El método run() mostrará un mensaje similar a:
# El hiloX va a estar dormido durante 7675 milisegundos.

# luego lo dormiremos (esto deberá estar incluido en un bloque 
# try {} catch, atrapar una excepción)

# Y finalmente indicaremos: hiloX1 ha despertado

# El tiempo que estará dormido el hilo lo calcularemos en el 
# constructor.

# Cuando lo ejecutes comprueba que los hilos van despertando 
# poco a poco
import random
import threading
import time

class NumeroDos(threading.Thread):
    def __init__(self, nombre, dormir):
        super().__init__(name=nombre)
        self.dormir = dormir

    def run(self):
        print(f"El hilo{self.name} va a estar dormido durante {self.dormir*1000} milisegundos")
        try:
            time.sleep(self.dormir)
            print(f"El hilo{self.name} ha despertado")
        except:
            print("Ou shi")

if __name__ == "__main__":
    
    hilo1 = NumeroDos("1", random.randint(0,10))
    hilo2 = NumeroDos("2", random.randint(0,10))
    hilo3 = NumeroDos("3", random.randint(0,10))

    print("run: ")
    print("Iniciando subprocesos...")

    hilo1.start()
    hilo2.start()
    hilo3.start()

    print("Subprocesos iniciados, termina main")
