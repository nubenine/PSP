import threading
import time

saldo_actual = 2000

def retirar(cantidad, nombre):
    global saldo_actual

    for i in range(5):
        if saldo_actual>=cantidad:
            saldo = saldo_actual
            time.sleep(0.5)
            saldo_actual = saldo - cantidad
    
    
        

if __name__ =="__main__":
    persona1 = threading.Thread(target=retirar, args=(300, "Persona 1"))
    persona2 = threading.Thread(target=retirar, args=(100, "Persona 2"))

    persona1.start()
    persona2.start()

    persona1.join()
    persona2.join()
    print(f"Saldo final: {saldo_actual}€")