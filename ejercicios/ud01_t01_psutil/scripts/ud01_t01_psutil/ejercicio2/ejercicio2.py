import psutil


servicios_windows = list(psutil.win_service_iter())

#Mostrar todos:
for item in servicios_windows:
    print(f"Nome: {item.name()}||\t||PID asociado: {item.pid()}||\t||Estado: {item.status()}||\t||Tipo de inicio: {item.start_type()}" )


# Mostrar servicios filtrados:
cadena = input("Introduce el estado (running o stopped) y/o el tipo de inicio (manual o automatic): ")
filtrar = cadena.lower().split()

for item in servicios_windows:
    if len(filtrar) == 1:
        if filtrar[0] == "running" or filtrar[0] == "stopped":
            if item.status() == filtrar[0]:
                print(f"Nome: {item.name()}||\t||PID asociado: {item.pid()}||\t||Estado: {item.status()}||\t||Tipo de inicio: {item.start_type()}")

        elif filtrar[0] == "manual" or filtrar[0] == "automatic":
            if item.start_type() == filtrar[0]:
                print(f"Nome: {item.name()}||\t||PID asociado: {item.pid()}||\t||Estado: {item.status()}||\t||Tipo de inicio: {item.start_type()}")

    elif len(filtrar) == 2:
        if (item.status() == filtrar[0] and item.start_type() == filtrar[1]):
            print(f"Nome: {item.name()}||\t||PID asociado: {item.pid()}||\t||Estado: {item.status()}||\t||Tipo de inicio: {item.start_type()}")

#Mostrar descripción de un servicio:
import psutil

nombre = input("Introduce el nombre del servicio: ")

try:
    servicio = psutil.win_service_get(nombre)
    informacion = servicio.as_dict()

    print(f"Nome: {informacion['name']}")
    print(f"Descripcion: {informacion['description']}")

except psutil.NoSuchProcess:
    print("El servicio no existe")



