diccionario = {
    "nombre" : "Miguel",
    "apellido" : "Glez",
    "edad" : 18
}

claves = diccionario.keys()
get = diccionario.get("nombre")

print(claves)
print(get)

#Elimina todo el diccionario
diccionario.clear()
print(diccionario)