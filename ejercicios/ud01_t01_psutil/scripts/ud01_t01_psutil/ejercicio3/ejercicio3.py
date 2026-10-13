
import psutil
import time


def mostrar_procesos():
    for proceso in psutil.process_iter(['pid', 'name', 'username']):
        try:
            print(f"PID: {proceso.info['pid']} | Nombre: {proceso.info['name']} | Usuario: {proceso.info['username']}")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass


def filtrar_memoria():
    porcentaje = float(input("Introduce el porcentaje minimo de memoria: "))
    procesos = []

    for proceso in psutil.process_iter():
        try:
            memoria = proceso.memory_percent()

            if memoria > porcentaje:
                procesos.append((proceso.pid, proceso.name(), memoria))

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    procesos.sort(key=lambda proceso: proceso[2], reverse=True)

    for pid, nombre, memoria in procesos:
        print(f"PID: {pid} | Nombre: {nombre} | Memoria: {memoria:.2f}%")


def filtrar_cpu():
    porcentaje = float(input("Introduce el porcentaje minimo de CPU: "))
    procesos = list(psutil.process_iter())

    for proceso in procesos:
        try:
            proceso.cpu_percent(interval=None)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    time.sleep(0.5)

    resultados = []

    for proceso in procesos:
        try:
            cpu = proceso.cpu_percent(interval=None)

            if cpu > porcentaje:
                resultados.append((proceso.pid, proceso.name(), cpu))

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    resultados.sort(key=lambda proceso: proceso[2])

    for pid, nombre, cpu in resultados:
        print(f"PID: {pid} | Nombre: {nombre} | CPU: {cpu:.2f}%")


def mostrar_arbol(pid, indentacion=0):
    try:
        proceso = psutil.Process(pid)
        print(" " * indentacion + f"PID: {proceso.pid} | Nombre: {proceso.name()}")

        for hijo in proceso.children(recursive=False):
            mostrar_arbol(hijo.pid, indentacion + 2)

    except (psutil.NoSuchProcess, psutil.AccessDenied):
        pass


def arbol_procesos():
    try:
        pid = int(input("Introduce el PID del proceso: "))

        if psutil.pid_exists(pid):
            mostrar_arbol(pid)
        else:
            print("El proceso no existe")

    except ValueError:
        print("Debes introducir un PID numerico")


while True:
    print("\nMENU")
    print("1. Mostrar todos los procesos")
    print("2. Filtrar procesos por uso de memoria")
    print("3. Filtrar procesos por uso de CPU")
    print("4. Mostrar arbol de procesos")
    print("5. Salir")

    opcion = input("Selecciona una opcion: ")

    if opcion == "1":
        mostrar_procesos()
    elif opcion == "2":
        filtrar_memoria()
    elif opcion == "3":
        filtrar_cpu()
    elif opcion == "4":
        arbol_procesos()
    elif opcion == "5":
        break
    else:
        print("Opcion no valida")
