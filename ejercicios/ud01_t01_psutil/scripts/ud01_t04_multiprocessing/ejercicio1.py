
import multiprocessing


def rellenar(lista):
	for num in range(11):
		lista[num] = num +1
	print("Lista llena:", list.lista)

def mult(lista):
	for num in lista:
		print("Multiplicado: {}".format(num*2))
if __name__=="__main__":
    
    lista = multiprocessing.Array('i',10)

    p1 = multiprocessing.Process(target=rellenar, args=(lista,))
    p2 = multiprocessing.Process(target=mult, args=(lista,))

    p1.start()
    p1.join()
    p2.start()
    p2.join()