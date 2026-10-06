import psutil


servicios_windows = psutil.win_service_iter()

#Mostrar todos:
for item in servicios_windows:
    print(f"Nome: {item.name()}||\t||PID asociado: {item.pid()}||\t||Estado: {item.status()}||\t||Tipo de inicio: {item.start_type()}" )

#Mostrar servicios filtrados:
cadena = input("Introduce una o dos palabras separadas por espacios. La primera hará referencia al estado del servicio ('running' o 'paused'), y la segunda al tipo de inicio ('manual' o 'automatic')")
filtrar = cadena.split(" ")

for nigga in filtrar:
    if nigga.lower() == "running" or nigga.lower()=="paused" or nigga.lower()=="manual" or nigga.lower()=="automatic":
        if nigga.lower()=="running" or nigga.lower()=="paused":
            for item in servicios_windows:
                print(f"Nome: {item.name()}||\t||PID asociado: {item.pid()}||\t||Estado: {item.status==nigga.lower()}||\t||Tipo de inicio: {item.start_type()}")
        elif nigga.lower()=="manual" or nigga.lower=="automatic":
            for item in servicios_windows:
                print(f"Nome: {item.name()}||\t||PID asomciado: {item.pid()}||\t||Estado: {item.status()}||\t||Tipo de inicio: {item.start_type()==nigga.lower()}")
        
# if filtrar.__sizeof__():
#     for item in servicios_windows:
#     	print(f"Nome: {item.name()}||\t||PID asociado: {item.pid()}||\t||Estado: {item.status()==filtrar[0]}||\t||Tipo de inicio: {item.start_type()}")
# elif filtrar.__sizeof__()==1:
#     for item in servicios_windows:
#         print(f"Nome: {item.name()}||\t||PID asociado: {item.pid()}||\t||Estado: {item.status(filtrar[0])}||\t||Tipo de inicio: {item.start_type(filtrar[1])}")
# elif filtrar.__sizeof__()>1:
#     while filtrar.__sizeof__()>1:
#         cadena = input("Introduce una o dos palabras separadas por espacios. La primera hará referencia al estado del servicio ('running' o 'paused'), y la segunda al tipo de inicio ('manual' o 'automatic')")
#         filtrar = cadena.split()




