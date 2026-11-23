# Diseña un programa que escriba dos sucesiones ascendentes de 
# números de forma simultánea. Es decir, un programa con dos hilos 
# en ejecución concurrente.

# El hilo tendrá:
# 2 atributos de tipo entero que marcarán el comienzo y fin de 
# la secuencia que queremos que se muestre (por ejemplo, desde el 
# 18 hasta el 45), una cadena para el nombre del hilo.
# El constructor, al que se le pasará el comienzo y fin de 
# la secuencia y el nombre del hilo. Es decir, cuando se instancia 
# un objeto hilo se le pasarán el intervalo de valores a mostrar 
# y cómo se llamará.
# El método run(), mostrará el nombre del hilo indicando que 
# comienza, luego la secuencia de valores y cuando haya finalizado 
# indicará que terminó.

# En el programa principal:
# crear dos objetos de tu hilo, pasándoles el inicio, 
# fin y nombre del hilo. Por ejemplo:
# Un ThreadA que comenzará en 1 y terminará en 10
# Un ThreadB que empezará en 20 y terminará en 30
# Un mensaje indicando que “Vamos a iniciar los dos threads”
# Un mensaje indicando que los hilos se han inicializado
# Lanzas los dos hilos
# Y un mensaje de que el programa principal ha terminado.

# Ejecuta varias veces tu aplicación para ver que obtienes diferentes salidas dependiendo de los tiempos que asigne la CPU a cada hilo.

import threading

class NumeroCuatro(threading.Thread):
    def __init__(self, nombre, inicio, fin ):
        super().__init__(name=nombre)
        self.inicio = inicio
        self.fin = fin

    def run(self):
        print(f"Thread{self.name} empieza...")
        for i in range(self.inicio, self.fin):
            print(f"Thread{self.name} dice: {i}.")
        print(f"Thread{self.name} acaba...")

if __name__ == "__main__":
    hiloA = NumeroCuatro("A", 1, 10)
    hiloB = NumeroCuatro("B", 20, 30)

    print("Vamos a iniciar los dos threads...")

    hiloA.start()
    hiloB.start()
    hiloA.join()
    hiloB.join()
