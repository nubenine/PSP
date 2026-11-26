# Crea un programa que calcule los factoriales del 5 al 9 
# modificando la clase Factorial del ejercicio anterior, 
# para que se visualicen los mensajes: 	

#       empieza el proceso … cálculo del factorial de: XX 	
#       acabó el proceso ….. el factorial de: XX es XXXX 	

import threading
import time

class Factorial(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        for i in range(5,10):
            print(f"Empieza el proceso... Calculo del factorial de: {i}")
            resultado = 1
            time.sleep(1)
            for j in range(1, i+1):
                resultado *= j
            
            print(f"Acabó el proceso... El factorial de {i} es: {resultado}")
            time.sleep(1)

if __name__ == "__main__":
    hilo1 = Factorial()

    hilo1.start()
    hilo1.join()