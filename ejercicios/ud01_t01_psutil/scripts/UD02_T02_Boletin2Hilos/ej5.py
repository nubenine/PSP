# Crea un programa que calcule el factorial y un número de la sucesión
# de  Fibonacci. 	
# 
# Cada uno de los cálculos tiene que ser realizado por un hilo 
# independiente. 
# 
# Las clases que implementen cada hilo tienen que llamarse Factorial
# y Fibonacci. 
# 
# Implementar la solución heredando de threading.Thread y creando 
# métodos target:
#               -Recuerda que factorial(0)=1 y para todo n>0, 
#                   factorial(n)=n*factorial(n-1).
#               -Recuerda que fib(0)=0, fib(1)=1 y para todo n>1, 
#                   fib(n)=fib(n-1)+fib(n-2).

import threading

class Factorial(threading.Thread):
    def __init__(self, num):
        super().__init__()
        self.num = num
    def run(self):
        if self.num==0:
            resultado = 1
            print(f"Factorial de {self.num}: {resultado}")
        else :
            resultado = 0
            for i in range(1,self.num):
                resultado += self.num*(self.num-i)
            print(f"Factorial de {self.num}: {resultado}")

class Fibonacci(threading.Thread):
    def __init__(self, num):
        super().__init__()
        self.num = num
    def run(self):
        if self.num==0:
            resultado = 0
            print(f"Fibonacci de {self.num}: {resultado}")
        elif self.num==1:
            resultado=1
            print(f"Fibonacci de {self.num}: {resultado}")
        else:
            resultado = 0
            for i in range(1,self.num):
                resultado += (self.num-i) + (self.num-(i+1))
            print(f"Fibonacci de {self.num}: {resultado}")

if __name__=="__main__":
    hilo1 = Factorial(8)
    hilo2 = Fibonacci(13)

    hilo1.start()
    hilo1.join()

    hilo2.start()
    hilo2.join()
