# # Crea un hilo que en su método run() muestre un “NO” hasta un máximo de 30 veces. En el método principal, mostrará “YES” hasta un máximo de 30 veces.
# # Como salida obtendrás una serie alternativa de NOes YESes ya que una vez iniciada la ejecución del thread, el tiempo de la CPU se reparte entre todos los procesos y threads del sistema, con lo cual se intercalan instrucciones del método main() con instrucciones del método run().

# # Posible salida:
# 	    YES YES YES YES YES YES YES NO NON NO NO NO NO NO NO
#       NO NON NO NO NO NO NO NO YES YES YES YES YES YES YES

# # Ejecútalo varias veces si no te salen intercalados o aumenta el número de iteraciones en los bucles.
import threading

def yes():
    for i in range(100000):
        print("YES", end="")

def no():
    for i in range(100000):
        print("NO", end="")

if __name__ == "__main__":
    print("INICIO")

    t1 = threading.Thread(target=yes)
    t2 = threading.Thread(target=no)
    t1.start()
    t2.start()
    t1.join()
    t2.join()