# Ejercicio 3: Comunicación con multiprocessing.Queue
# Implementa un programa que utilice multiprocessing.Queue para que dos procesos 
# se comuniquen. El primer proceso debe generar una serie de números aleatorios y 
# enviarlos a través de la cola. El segundo proceso debe recibir estos números y 
# calcular su suma.
import multiprocessing
import random

def generarNumeros(cantidad, q):  #recibe la cantidad (primer arg), y la cola (segundo arg)
    for ay in range(0,cantidad + int(cantidad/2)):
        ay = random.randint(0,10)
        q.put(ay) #lo pone en la cola del paro fuck nigga

def recibirNumeros(q):
    print("Elementos de la cola: ")
    suma = 0
    while not q.empty():
        suma += q.get()
        print(q.get())
    print(f"Suma total: {suma}")
        
	
if __name__ == '__main__':

    cantidad = 6
    q = multiprocessing.Queue() #Se crea la cola (que goloso)
    p1 = multiprocessing.Process(target=generarNumeros, args=(cantidad, q))
    p2 = multiprocessing.Process(target=recibirNumeros, args=(q,))

    p1.start()
    p1.join()

    p2.start()
    
    

    p2.join()
  