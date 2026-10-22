
import multiprocessing


def rellenar(lista):
	for i in range(0,10):
		lista[i] = i +1
	print(f"[Proceso 1]: {list(lista)}")

def mult(lista):
	for i in range(0,10):
		lista[i] = lista[i] * 2
	print(f"[Proceso 2]: {list(lista)}")
if __name__=="__main__":
    
    mylista = multiprocessing.Array('i',10)

    p1 = multiprocessing.Process(target=rellenar, args=(mylista,))
    p2 = multiprocessing.Process(target=mult, args=(mylista,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print(f"lista desde main: {mylista[:]}")