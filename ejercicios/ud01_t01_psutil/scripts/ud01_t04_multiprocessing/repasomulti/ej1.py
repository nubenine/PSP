import multiprocessing
import random

def rellenar(lista):
    for i in range(0,10):
        lista[i] = random.randint(1,10)
    print(f"Proceso1: {list(lista)}")

def mult(lista):
    for i in range(0,10):
        lista[i] = lista[i] * 2
    print(f"Proceso 2: {list(lista)}")

if __name__ =='__main__':
    mylist = multiprocessing.Array('i', 10)

    p1 = multiprocessing.Process(target=rellenar, args=(mylist, ))
    p2 = multiprocessing.Process(target=mult, args=(mylist, ))

    p1.start()
    p1.join()

    p2.start()
    p2.join()

    print(f"Lista: {mylist[:]}")