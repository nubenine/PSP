# Vamos a hacer un programa similar al anterior pero instanciando 2 threads.
# En el HiloA mostrará el mensaje NO, hasta un máximo de 30 veces
# En el HiloB mostrará el mensaje YES, hasta un máximo de 30 veces
# En el programa principal mostrará un mensaje “Ejecución en HiloA” y 
# se ejecutará el HiloA; luego mostrará un mensaje “Ejecución en HiloB”
# y se ejecutará el HiloB; y luego un mensaje “Ejecución en main”. 

import threading

def hiloA():
    print("Ejecución en HiloA: ")
    for i in range(30):
        print("NO", end="")
def hiloB():
    print("Ejecución en HiloB")
    for i in range(30):
        print("YES", end="")

if __name__ == "__main__":
    t1 = threading.Thread(target=hiloA)
    t1.start()
    t2 = threading.Thread(target=hiloB)
    t2.start()
    print("---EJECUCIÓN EN MAIN---")
    t1.join()
    t2.join()
