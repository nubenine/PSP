#Ejercicio 1. Demostracion de ejecucion.
import json
import psutil
from datetime import datetime


frecuencia = psutil.cpu_freq()
estadisticas_cpu = psutil.cpu_stats()
memoria = psutil.virtual_memory()
particiones = psutil.disk_partitions(all=True)
disco = psutil.disk_usage('/')
operaciones_disco = psutil.disk_io_counters(perdisk=False, nowrap=True)
red = psutil.net_io_counters(pernic=False, nowrap=True)

print(f"Hola mundo soy linux? {psutil.LINUX}")
print(f"Hola mundo soy windows? {psutil.WINDOWS}")

print(f"Numero de CPUs:  {psutil.cpu_count(logical=False)}")
print(f"Frecuencias: {frecuencia}")
print(f"Uso: {estadisticas_cpu}")

print(f"Memoria total: {memoria.total} bytes")
print(f"Memoria disponible: {memoria.available} bytes")
print(f"Porcentaje de memoria usada: {memoria.percent}%")

print(f"Listado de particiones: {particiones}")
print(f"Uso de disco para cada unidad o particion: {disco}")
print(f"Numero de operaciones de lectura: {operaciones_disco.read_count}")
print(f"Numero de operaciones de escritura: {operaciones_disco.write_count}")
print(f"Numero de bytes leidos: {operaciones_disco.read_bytes}")
print(f"Numero de bytes escritos: {operaciones_disco.write_bytes}")

print(f"Bytes enviados: {red.bytes_sent}")
print(f"Bytes recibidos: {red.bytes_recv}")
print(f"Paquetes enviados: {red.packets_sent}")
print(f"Paquetes enviados: {red.bytes_recv}")

datos = {
    "sistema": {
        "linux": psutil.LINUX,
        "windows": psutil.WINDOWS
    },

    "cpu": {
        "numero_cpus": psutil.cpu_count(logical=False),
        "frecuencia": {
            "actual": frecuencia.current,
            "minima": frecuencia.min,
            "maxima": frecuencia.max
        },
        "estadisticas": {
            "context_switches": estadisticas_cpu.ctx_switches,
            "interrupciones": estadisticas_cpu.interrupts,
            "soft_interrupts": estadisticas_cpu.soft_interrupts,
            "syscalls": estadisticas_cpu.syscalls
        }
    },

    "memoria": {
        "total": memoria.total,
        "disponible": memoria.available,
        "porcentaje_usada": memoria.percent
    },

    "disco": {
        "particiones": [
            {
                "dispositivo": particion.device,
                "punto_montaje": particion.mountpoint,
                "sistema_archivos": particion.fstype
            }
            for particion in particiones
        ],
        "uso": {
            "total": disco.total,
            "usado": disco.used,
            "libre": disco.free,
            "porcentaje": disco.percent
        },
        "operaciones": {
            "lecturas": operaciones_disco.read_count,
            "escrituras": operaciones_disco.write_count,
            "bytes_leidos": operaciones_disco.read_bytes,
            "bytes_escritos": operaciones_disco.write_bytes
        }
    },

    "red": {
        "bytes_enviados": red.bytes_sent,
        "bytes_recibidos": red.bytes_recv,
        "paquetes_enviados": red.packets_sent,
        "paquetes_recibidos": red.packets_recv
    }
}
fecha = datetime.now().strftime("%Y%m%d%H%M%S")
nombre_archivo = f"{fecha}-system-info.json"

with open(nombre_archivo,'w') as file:
    json.dump(datos, file, indent=4)

