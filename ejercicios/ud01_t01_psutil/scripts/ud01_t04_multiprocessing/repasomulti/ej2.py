import random
import multiprocessing

def agregar(diccionario, clave):
    diccionario[clave] = random.randint(1,100)

if __name__ == "__main__":
    with multiprocessing.Manager() as manager:
        diccionario = manager.dict()

        procesos = []

        for i in range(5):
            p = multiprocessing.Process(target=agregar, args=(diccionario, f"Proceso{i}"))
            procesos.append(p)
            p.start()

        for p in procesos:
            p.join()

        print(diccionario)