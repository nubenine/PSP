
nombre_fichero_alias = "scripts/ud01_t02/scripts/alias.txt"
alias = {}

with open(nombre_fichero_alias, "r") as fichero:
    #meter cosas en diccionario alias
    for linea in fichero.readlines():
        #separar la linea en dos partes y meter en el diccionario clave = valor
        k, v = linea.split("=")
        alias[k] = v




print(alias)
