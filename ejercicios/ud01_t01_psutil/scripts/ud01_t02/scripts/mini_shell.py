
nombre_fichero_alias = "./alias.txt"
alias = {}

with open(nombre_fichero_alias, "r") as fichero:
    #meter cosas en diccionario alias
    for linea in fichero.readlines():
        #separar la linea en dos partes y meter en el diccionario clave = valor
        k, v = linea.split("=")
        alis[k] = v


print(alias)
