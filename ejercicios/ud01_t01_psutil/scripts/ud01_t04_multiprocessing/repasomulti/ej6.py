import multiprocessing

def incrementar(contador, lock):
    for i in range(100):
        with lock:
            contador.value += 1

if __name__ == '__main__':
    contador = multiprocessing.Value('i',0)
    lock = multiprocessing.Lock()

    procesos = []

    for i in range(5):
        p = multiprocessing.Process(target=incrementar, args=(contador, lock))

        procesos.append(p)
        p.start()

    for p in procesos: 
        p.join()

    print(f"Contadir final: {contador.value}")