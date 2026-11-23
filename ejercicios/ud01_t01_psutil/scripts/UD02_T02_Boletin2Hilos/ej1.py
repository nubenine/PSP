# Crear un hilo cuyo método run() deberá dormirlo durante unos 
# 2000 milisegundos (el cuerpo del método irá encerrado en un 
# bloque try… catch (una excepción).

# Luego en el programa principal quiero que me muestres el 
# estado del hilo antes de ejecutarse (indicará false) y 
# durante su ejecución (indicará que está vivo, true). 

# Luego con el método join() esperaremos a que el hilo 
# muera y se mostrará su estado (deberá estar muerto, false).

# El método hilo.is_alive() me dice cuál es el estado del hilo.

import threading
import time

class NumeroUno(threading.Thread):
    def __init__(self, delay):
        super().__init__()
        self.delay = delay

    def run(self):
        try:
            time.sleep(self.delay)
        except:
            print("Aqui saldria un error")

if __name__ == "__main__":
    hilo = NumeroUno(2)

    print("run: ")
    print(f"Estado antes de iniciarse: {hilo.is_alive()}")
    hilo.start()
    print(f"Estado durante su ejecución: {hilo.is_alive()}")
    hilo.join()
    print(f"Estado después de su ejecución: {hilo.is_alive()}")