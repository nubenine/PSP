#Ejercicio 1. Demostracion de ejecucion.

import psutil

print(f"Hola mundo soy linux? {psutil.LINUX}")
print(f"Hola mundo soy windows? {psutil.WINDOWS}")


print(f"Numero de CPUs:  {psutil.cpu_count(logical=False)}")
print(f"Frecuencias: {psutil.cpu_freq()}")
print(f"Uso: {psutil.cpu_stats()}")


print(f"Memoria total: {psutil.virtual_memory()}")


