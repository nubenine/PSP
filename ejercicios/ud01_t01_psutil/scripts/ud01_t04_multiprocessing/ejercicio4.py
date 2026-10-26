# Ejercicio 4: Comunicación con multiprocessing.Pipe
# Escribe un programa que utilice multiprocessing.Pipe para la comunicación 
# entre dos procesos. El primer proceso debe enviar una cadena de texto a través del 
# tubo, y el segundo proceso debe recibirla y convertirla a mayúsculas 
# antes de imprimirla.

import multiprocessing
import subprocess

def enviarTexto(conn, msg):
 conn.send(msg)
 print("Se ha enviado el mensaje: {}".format(msg))
 conn.close()

def recibirTexto(conn):
   msg = conn.recv()
   print("Se ha recibido el mensaje: {}".format(msg.upper()))



if __name__ == '__main__':

    cadena =  "aaay"

    inicio, final = multiprocessing.Pipe()

    p1 = multiprocessing.Process(target=enviarTexto, args=(inicio, cadena))
    p2 = multiprocessing.Process(target=recibirTexto, args=(final,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    