#Elabora un programa en Python que permita consultar la información del sistema. El programa mostrará un menú con dos opciones:
Mostrar información del sistema:
Deberán mostrarse por pantalla los siguientes datos:
Plataforma sobre la que se ejecuta el script: Windows o Linux
Información de CPUs
Número de CPUs
Frecuencia de cada CPU
Uso de CPU por CPUs
Información de memoria
Memoria total
Memoria disponible
Porcentaje de memoria usada
Información de discos
Listado de particiones
Uso de disco para cada unidad o partición
Número de operaciones de lectura
Número de operaciones de escritura
Número de bytes leídos
Número de bytes escritos
Estadísticas de red
Bytes enviados
Bytes recibidos
Paquetes enviados
Paquetes recibidos
Guardar información del sistema:
Realizará un volcado de la información del sistema que se muestra por pantalla a un fichero JSON en la ruta que se proporcione, siendo el nombre del fichero el siguiente: yyyyMMddhhmmss-system-info.json

Elabora un programa en Python que permita consultar la información de los servicios en Windows. El programa mostrará un menú con dos opciones:
Mostrar todos los servicios:
Para cada servicio se mostrará su nombre, PID asociado, estado y tipo de inicio
Mostrar servicios filtrados:
El filtro será una cadena de texto formada por una o dos palabras separadas por un espacio. La primera de ellas hará referencia al estado del servicio: iniciado o parado; y la segunda al tipo de inicio: manual o automático
Mostrar descripción de un servicio:
Se proporcionará el nombre del servicio y mostrará la descripción del mismo

Elabora un programa en Python que recopile información de los procesos del sistema. El programa deberá mostrar el siguiente menú:
Mostrar información de todos los procesos:
Se mostrará por defecto PID, nombre y usuario
Filtrar procesos por uso de memoria:
Se preguntará al usuario un porcentaje de uso de memoria y sólo se mostrarán los procesos que tengan un valor mayor. Los procesos se mostrarán de mayor a menor uso de memoria.
Filtrar procesos por uso de CPU:
Se preguntará al usuario un porcentaje de uso de CPU (se realizará un sondeo con intervalo de 0.5) y solo se mostrarán los procesos que tengan un valor mayor. Los procesos se mostrarán de menor a mayor uso de CPU.
Mostrar árbol de procesos
Se preguntará al usuario por un PID, se debe comprobar que el proceso existe, y a continuación se mostrará de manera recursiva el árbol de procesos. De estos procesos solo se mostrará PID y nombre. Gráficamente se representarán los hijos de un proceso imprimiendo estos con dos espacios de indentado respecto a su padre.
